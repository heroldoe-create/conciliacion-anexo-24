# Entrada completa del ejemplo (FICTICIO — Andén Norte)

Pega todo este archivo en el chat con la frase: «Concilia mi Anexo 24 al corte. Dame hallazgos, saldos, plazos y mensajes.»

## empresa.md

### Datos de la empresa y del corte (FICTICIOS — Andén Norte)

| Dato | Valor |
|---|---|
| Razón social | Andén Norte Manufactura, S.A. de C.V. (FICTICIA) |
| RFC | AAA010101AAA (RFC de prueba, FICTICIO) |
| Programa IMMEX | 9999-2026 (FICTICIO), modalidad industrial |
| ¿Tiene Registro en el Esquema de Certificación de Empresas (IVA e IEPS)? | Sí |
| Periodo que se concilia | 2026-10-01 00:00 a 2026-10-15 18:00 |
| Fecha y hora de corte | 2026-10-15 18:00 |
| Saldos de apertura | reporte de saldos del Anexo 24 al 2026-09-30 |
| Activo fijo (vence con la vigencia del programa) | AF-01 (molde) |
| Aviso de «por vencer» | 60 días naturales |
| Fracciones en Anexos I BIS, I TER, II o III del Decreto IMMEX | ninguna (y la empresa está certificada) |

## pedimentos.csv

```csv
pedimento,clave,tipo,fecha_pedimento,despacho_concluido,codigo,descripcion,fraccion,cantidad,um
240-9901-6000210,IN,ENTRADA,2026-10-06,2026-10-06 16:00,MP-03,Etiqueta impresa autoadherible,4821.10.99,5000,pza
240-9901-6000210,IN,ENTRADA,2026-10-06,2026-10-06 16:00,AF-01,Molde de inyección para carcasa,8480.71.01,1,pza
240-9901-6000233,IN,ENTRADA,2026-10-13,2026-10-13 10:00,MP-02,Tornillo de acero M4,7318.15.99,8000,pza
240-9901-6000198,RT,SALIDA,2026-10-09,2026-10-09 15:00,PT-01,Carcasa de polipropileno ensamblada,8538.90.99,2000,pza
```

## movimientos-erp-wms.csv

```csv
folio,fecha,tipo,codigo,cantidad,um,pedimento_ref
REC-7781,2026-10-06,RECIBO,MP-03,5000,pza,240-9901-6000210
REC-7782,2026-10-06,RECIBO,AF-01,1,pza,240-9901-6000210
EMB-3302,2026-10-09,EMBARQUE,PT-01,2000,pza,240-9901-6000198
REC-7790,2026-10-13,RECIBO,MP-02,7600,pza,240-9901-6000233
REC-7795,2026-10-14,RECIBO,MP-01,500,kg,
EMB-3310,2026-10-14,EMBARQUE,PT-01,500,pza,
```

## anexo24-registro.csv

```csv
modulo,pedimento,clave,fecha_registro,codigo,fraccion,cantidad,um,pedimento_origen_descargo
ENTRADA,240-9901-6000210,IN,2026-10-09 10:00,MP-03,4821.10.01,5000,pza,
ENTRADA,240-9901-6000210,IN,2026-10-09 10:00,AF-01,8480.71.01,1,pza,
SALIDA,240-9901-6000198,RT,2026-10-10 09:00,MP-01,3902.10.01,600,kg,240-9901-5000101
SALIDA,240-9901-6000198,RT,2026-10-10 09:00,MP-01,3902.10.01,1100,kg,240-9901-6000045
SALIDA,240-9901-6000198,RT,2026-10-10 09:00,MP-02,7318.15.99,8000,pza,240-9901-6000045
SALIDA,240-9901-6000198,RT,2026-10-10 09:00,MP-03,4821.10.01,2000,pza,240-9901-6000210
```

## anexo24-saldos.csv

```csv
fecha_saldo,pedimento,fecha_entrada,codigo,fraccion,saldo,um
2026-09-30,240-9901-5000101,2025-03-10,MP-01,3902.10.01,600,kg
2026-09-30,240-9901-6000045,2026-04-20,MP-01,3902.10.01,1500,kg
2026-09-30,240-9901-6000045,2026-04-20,MP-02,7318.15.99,9000,pza
2026-10-15,240-9901-5000101,2025-03-10,MP-01,3902.10.01,0,kg
2026-10-15,240-9901-6000045,2026-04-20,MP-01,3902.10.01,400,kg
2026-10-15,240-9901-6000045,2026-04-20,MP-02,7318.15.99,1000,pza
2026-10-15,240-9901-6000210,2026-10-06,MP-03,4821.10.01,3000,pza
2026-10-15,240-9901-6000210,2026-10-06,AF-01,8480.71.01,1,pza
```

## lista-de-materiales.csv

```csv
producto,material,cantidad_por_unidad,um
PT-01,MP-01,0.9,kg
PT-01,MP-02,4,pza
PT-01,MP-03,1,pza
```
