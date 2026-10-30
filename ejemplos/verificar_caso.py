#!/usr/bin/env python3
"""Recalcula el caso de ejemplo desde los CSV y lo compara con salida-esperada.md.

NO hace falta para usar la skill (la skill trabaja en el chat). Existe para que cualquiera
compruebe que las cifras de salida-esperada.md salen de la entrada y no de la memoria de
quien la escribió. Solo biblioteca estándar.

  python3 ejemplos/verificar_caso.py          imprime el recálculo; rc 0 si todo cuadra
"""
import csv, os, re, sys
from datetime import datetime, date
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
CASO = os.path.join(AQUI, "caso-01-anden-norte-octubre")
ENT = os.path.join(CASO, "entrada")
CORTE = datetime(2026, 10, 15, 18, 0)
LIMITE_H = 48
ACTIVO_FIJO = {"AF-01"}


def leer(n):
    with open(os.path.join(ENT, n), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def dt(s):
    return datetime.strptime(s.strip(), "%Y-%m-%d %H:%M")


def mas_meses(d, n):
    m = d.month - 1 + n
    a, m = d.year + m // 12, m % 12 + 1
    for dia in (d.day, 30, 29, 28):
        try:
            return date(a, m, dia)
        except ValueError:
            continue


ped = leer("pedimentos.csv")
bom = leer("lista-de-materiales.csv")
wms = leer("movimientos-erp-wms.csv")
reg = leer("anexo24-registro.csv")
sal = leer("anexo24-saldos.csv")

# saldos: (pedimento, codigo) -> dict
fila = {}
for s in sal:
    k = (s["pedimento"], s["codigo"])
    r = fila.setdefault(k, {"entrada": s["fecha_entrada"], "apertura": 0.0, "entradas": 0.0,
                            "descargos": 0.0, "a24": None})
    if s["fecha_saldo"] == "2026-09-30":
        r["apertura"] = float(s["saldo"])
    else:
        r["a24"] = float(s["saldo"])
for p in ped:
    if p["tipo"] == "ENTRADA":
        k = (p["pedimento"], p["codigo"])
        r = fila.setdefault(k, {"entrada": p["fecha_pedimento"], "apertura": 0.0, "entradas": 0.0,
                                "descargos": 0.0, "a24": None})
        r["entradas"] += float(p["cantidad"])

# PEPS de las salidas
receta = defaultdict(list)
for b in bom:
    receta[b["producto"]].append((b["material"], float(b["cantidad_por_unidad"])))
esperado_desc = defaultdict(float)  # (salida, material) -> cantidad
peps = []  # (salida, material, pedimento origen, cantidad, fecha salida)
for p in sorted([p for p in ped if p["tipo"] == "SALIDA"], key=lambda p: p["despacho_concluido"]):
    for mat, q in receta[p["codigo"]]:
        falta = float(p["cantidad"]) * q
        esperado_desc[(p["pedimento"], mat)] += falta
        fuentes = sorted([k for k in fila if k[1] == mat and fila[k]["entrada"] <= p["fecha_pedimento"]],
                         key=lambda k: (fila[k]["entrada"], k[0]))
        for k in fuentes:
            r = fila[k]
            disp = r["apertura"] + r["entradas"] - r["descargos"]
            toma = min(disp, falta)
            if toma > 0:
                r["descargos"] += toma
                falta -= toma
                peps.append((p["pedimento"], mat, k[0], toma, p["fecha_pedimento"]))
        if falta > 1e-9:
            print(f"DESCARGO-SIN-SALDO {p['pedimento']} {mat} {falta}")

a24_desc = defaultdict(float)
for r in reg:
    if r["modulo"] == "SALIDA":
        a24_desc[(r["pedimento"], r["codigo"])] += float(r["cantidad"])

hall = []
fped = {p["pedimento"]: p["fecha_pedimento"] for p in ped}
# C8 vencidos / C6-C7
print("Tabla 2 · saldos")
for k in sorted(fila, key=lambda k: (fila[k]["entrada"], k[0], k[1])):
    r = fila[k]
    esp = r["apertura"] + r["entradas"] - r["descargos"]
    ent = datetime.strptime(r["entrada"], "%Y-%m-%d").date()
    vence = "vigencia del programa" if k[1] in ACTIVO_FIJO else mas_meses(ent, 18).isoformat()
    a24 = "—" if r["a24"] is None else r["a24"]
    dif = "—" if r["a24"] is None else r["a24"] - esp
    print(f"  {k[0]} {r['entrada']} {k[1]} ap={r['apertura']:g} +{r['entradas']:g} -{r['descargos']:g} "
          f"esp={esp:g} a24={a24} dif={dif} vence={vence}")
    if vence != "vigencia del programa" and r["apertura"] > 0 and CORTE.date().isoformat() > vence:
        tard = [x for x in peps if x[2] == k[0] and x[1] == k[1] and x[4] > vence]
        if tard:
            dias = (datetime.strptime(tard[0][4], "%Y-%m-%d").date() - date.fromisoformat(vence)).days
            hall.append(("CRÍTICO", "VENCIDO", k[0], k[1], f"{tard[0][3]:g} descargado {dias} días después de vencer", r["entrada"], k[0]))
    if r["a24"] is None and (r["entradas"] > 0):
        pass  # lo cubre C1

for (s, mat), q in sorted(esperado_desc.items()):
    if abs(a24_desc[(s, mat)] - q) > 1e-9:
        hall.append(("ALTO", "DIF-DESCARGO", s, mat, f"esperado {q:g} vs A24 {a24_desc[(s, mat)]:g}", fped[s], s))

# C1/C2 plazo de registro
print("Tabla 3 · plazo de registro")
hreg = {}
for r in reg:
    hreg.setdefault(r["pedimento"], dt(r["fecha_registro"]))
vistos = set()
for p in sorted(ped, key=lambda p: p["despacho_concluido"]):
    if p["pedimento"] in vistos:
        continue
    vistos.add(p["pedimento"])
    d = dt(p["despacho_concluido"])
    if p["pedimento"] in hreg:
        h = (hreg[p["pedimento"]] - d).total_seconds() / 3600
        est = "FUERA" if h > LIMITE_H else "EN PLAZO"
        if est == "FUERA":
            hall.append(("ALTO", "REGISTRO-FUERA-DE-PLAZO", p["pedimento"], "", f"{h:g} h", p["fecha_pedimento"], p["pedimento"]))
    else:
        h = (CORTE - d).total_seconds() / 3600
        est = "SIN REGISTRO, FUERA" if h > LIMITE_H else "SIN REGISTRO, EN PLAZO"
        hall.append(("CRÍTICO" if h > LIMITE_H else "MEDIO", "SIN-REGISTRO-A24", p["pedimento"], p["codigo"],
                     f"{h:g} h al corte", p["fecha_pedimento"], p["pedimento"]))
    print(f"  {p['pedimento']} {p['clave']} {d} -> {hreg.get(p['pedimento'], '—')} {h:g} h {est}")

# C3 cantidades WMS vs pedimento, C5 sin pedimento
for w in wms:
    if not w["pedimento_ref"].strip():
        extra = ""
        if w["tipo"] == "EMBARQUE":
            extra = "; descargo pendiente " + ", ".join(f"{m} {float(w['cantidad']) * q:g}" for m, q in receta[w["codigo"]])
        hall.append(("ALTO", "SIN-PEDIMENTO", "—", w["codigo"], f"{w['folio']} {float(w['cantidad']):g}{extra}", w["fecha"], w["folio"]))
        continue
    pp = [p for p in ped if p["pedimento"] == w["pedimento_ref"] and p["codigo"] == w["codigo"]]
    if pp and float(pp[0]["cantidad"]) != float(w["cantidad"]):
        hall.append(("ALTO", "DIF-CANTIDAD", w["pedimento_ref"], w["codigo"],
                     f"pedimento {float(pp[0]['cantidad']):g} vs {w['folio']} {float(w['cantidad']):g}", pp[0]["fecha_pedimento"], w["pedimento_ref"]))

# C4 catálogo
for p in ped:
    for r in reg:
        if r["pedimento"] == p["pedimento"] and r["codigo"] == p["codigo"] and r["fraccion"] != p["fraccion"]:
            hall.append(("MEDIO", "DIF-CATALOGO", p["pedimento"], p["codigo"], f"{p['fraccion']} vs {r['fraccion']}", p["fecha_pedimento"], p["pedimento"]))

orden = {"CRÍTICO": 0, "ALTO": 1, "MEDIO": 2, "INFO": 3}
hall.sort(key=lambda h: (orden[h[0]], h[5], h[6], h[3]))
print("Tabla 1 · hallazgos")
for i, h in enumerate(hall, 1):
    print(f"  H{i:02d} {h[0]:<8} {h[1]:<24} {h[2]:<18} {h[3]:<6} {h[4]}")
cuenta = {s: sum(1 for h in hall if h[0] == s) for s in orden}
print("conteo:", cuenta, "total", len(hall))

# comparación con la salida esperada
esp = open(os.path.join(CASO, "salida-esperada.md"), encoding="utf-8").read()
m = re.search(r"(\d+) hallazgos \((\d+) CRÍTICO, (\d+) ALTO, (\d+) MEDIO, (\d+) INFO\)", esp)
ok = bool(m) and [int(x) for x in m.groups()] == [len(hall), cuenta["CRÍTICO"], cuenta["ALTO"], cuenta["MEDIO"], cuenta["INFO"]]
ids = re.findall(r"^\| (H\d\d) \| (CRÍTICO|ALTO|MEDIO|INFO) \| ([A-Z0-9-]+) \|", esp, re.M)
ok = ok and [(s, t) for _, s, t in ids] == [(h[0], h[1]) for h in hall]
print("CUADRA con salida-esperada.md" if ok else "NO CUADRA con salida-esperada.md")
sys.exit(0 if ok else 1)
