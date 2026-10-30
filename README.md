# Conciliación IMMEX / Anexo 24

Movimientos del ERP/WMS + pedimentos + registro y saldos del Anexo 24 → hallazgos con su cifra,
saldos por pedimento con PEPS, plazos de registro de 48 horas, vencimientos de 18 meses y los
mensajes listos para el agente aduanal, el responsable del Anexo 24 y el almacén.
**Licencia para empresa: USD 20.** Autor: Heroldo Escobedo — heroldo.org.

## Uso en 3 pasos

1. Conecta la skill con el conector de Agensi en claude.ai, o sube **conciliacion-anexo-24.zip**
   desde la opción de cargar skills de tu cuenta. No hay que instalar, configurar ni editar nada.
2. Adjunta o pega lo que tengas: pedimentos del periodo, movimientos del ERP/WMS, registro y
   saldos de tu Anexo 24 y lista de materiales (Excel, CSV, PDF o texto; tus columnas sirven
   como están). Di si tu empresa está certificada en IVA e IEPS y la fecha y hora de corte.
3. Pide: **«Concilia mi Anexo 24 al corte. Dame hallazgos, saldos, plazos y mensajes.»**
   Recibes las tablas y los mensajes listos para copiar; si falta un dato, sale lo que sí se
   pudo cruzar y una tabla corta de lo que falta y quién lo tiene.

Sin terminal, scripts, API ni acceso a tu sistema. No adjuntes contraseñas, e.firma ni el
usuario de acceso en línea de tu Anexo 24.

## Qué recibes

- **Hallazgos** (CRÍTICO, ALTO, MEDIO, INFO), cada uno con lo que dice cada documento, la
  diferencia, la regla oficial que lo sostiene, el responsable y el siguiente paso:
  pedimentos sin registrar, registros fuera de las 48 horas, saldos vencidos o por vencer,
  descargos que no cuadran con la lista de materiales o que no siguen PEPS, diferencias entre
  pedimento y almacén, recibos y embarques sin pedimento, fracciones distintas entre pedimento y
  catálogo.
- **Saldos por pedimento al corte**: apertura + entradas − descargos PEPS = esperado, contra lo
  que dice tu Anexo 24, con su fecha de vencimiento.
- **Plazo de registro** de cada pedimento: horas entre el despacho concluido y el registro.
- **Un mensaje por responsable**, con sus hallazgos y su fecha, listo para pegar.
- **Evidencia**: de qué archivo y renglón sale cada cifra.

**No sustituye al contador, al agente aduanal ni al SAT, ni es tu sistema de control de
inventarios:** pre-revisa, cruza y arma evidencia. No registra ni corrige tu Anexo 24, no hace
el descargo oficial, no clasifica fracciones, no calcula contribuciones ni multas y no decide
rectificaciones o cambios de régimen: los pregunta a quien le toca.

## Reglas que usa (fuente oficial, consultada el 2026-10-29)

Ley Aduanera arts. 59 fr. I, 108 y 109 (última reforma DOF 19-11-2025) · RGCE 2026 regla 4.3.1 y
7.1.1 fr. XIV (DOF 27-12-2025, vigentes hasta el 31-12-2026) · Anexo 24 apartados A y C y Anexo 22
de las RGCE 2026 (DOF 15-01-2026) · Decreto IMMEX arts. 4 y 24 fr. IX. Texto citado y URL de cada
una en `references/fuentes.md`. **El plazo de 48 horas es para empresas certificadas** (Anexo 24
apartado C); si tu empresa no lo está, la skill usa un umbral interno y lo rotula así.

## Prueba sin datos propios

Escribe: **«Corre el ejemplo incluido de la skill conciliacion-anexo-24»**. Si tu forma de
instalación no trae los archivos, pega el contenido de `ejemplos/entrada-completa.md` con la
frase del paso 3. Debe salir lo mismo que `ejemplos/caso-01-anden-norte-octubre/salida-esperada.md`:
**8 hallazgos (2 CRÍTICO, 5 ALTO, 1 MEDIO)**; 600 kg vencidos el 2026-09-10 y descargados 29 días
después; un pedimento sin registrar a las 56 h; otro registrado a las 66 h; y el saldo de MP-01
en 300 kg esperado contra 400 kg del Anexo 24 (2,000 piezas × 0.9 kg = 1,800 kg, no 1,700).
Todo es **FICTICIO de Andén Norte**: empresa, RFC, programa, pedimentos, patente y fracciones
(las fracciones son ilustrativas, no una clasificación).

`ejemplos/verificar_caso.py` recalcula el ejemplo desde los CSV para quien quiera comprobar las
cuentas con Python; **no hace falta para usar la skill**.

## Contenido

`skills/conciliacion-anexo-24/SKILL.md` contiene las instrucciones; `references/fuentes.md`, las
fuentes oficiales con fecha de consulta; `ejemplos/`, el caso de entrada, su salida esperada y la
entrada en un solo archivo para pegar; `LICENSE`, la licencia completa.
`conciliacion-anexo-24.zip` lleva una carpeta `conciliacion-anexo-24/` con SKILL.md en su raíz,
más referencias, ejemplos, README y LICENSE, para cargarla sin reorganizar archivos.

---

## Licencia

**Propiedad intelectual de Heroldo Escobedo**, con el código a la vista ([Licencia de uso de Heroldo 1.0](LICENSE)):

- **Uso personal: gratis.** Léelo, pruébalo y adáptalo para aprender o en tus propios datos.
- **Uso en una empresa o con fines de lucro: solo con compra.** Cómpralo en [Agensi](https://agensi.io/skills/conciliacion-anexo-24)
  o escribe a heroldo@lolo-enterprises.com. La compra cubre a tu empresa.
- **Siempre se cita la fuente:** «Basado en una skill de Heroldo Escobedo — heroldo.org».
- No se revende ni se vuelve a publicar.

> **In English:** Source-available, not open source. Free for personal use. Business use requires purchase on
> [Agensi](https://agensi.io/skills/conciliacion-anexo-24). Attribution to Heroldo Escobedo — heroldo.org is always required.
