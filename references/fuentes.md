# Fuentes oficiales de la skill `conciliacion-anexo-24`

Regla del paquete: toda regla que la skill usa para marcar un hallazgo sale de este archivo, con
su fuente oficial, URL y fecha de consulta. Lo que no está aquí no se usa para marcar.

**Fecha de consulta de todas las fuentes: 2026-10-29.** Los textos se descargaron ese día de
los sitios oficiales y las citas entre comillas son literales.

## F1 · Ley Aduanera (texto vigente, última reforma publicada DOF 19-11-2025)

- **URL:** https://www.diputados.gob.mx/LeyesBiblio/pdf/LAdua.pdf (Cámara de Diputados).
  SHA-256 del PDF consultado: `43927095d22ff7bc7780e78132d2160b5050b5f76026b539daec32be09d7341d`
  (el archivo cambia con cada reforma; el encabezado dice «Última reforma publicada DOF 19-11-2025»).
- **Art. 59, fr. I** — «Llevar los sistemas de control de inventarios en forma automatizada y
  permanente, que mantengan en todo momento el registro actualizado de los datos de control de
  las mercancías de comercio exterior, mismos que deberán estar a disposición de la autoridad
  aduanera.» (párrafo reformado DOF 30-12-2002, 19-11-2025). Segundo párrafo: quienes
  introduzcan mercancías en importación temporal para elaboración, transformación o reparación
  en programas de maquila o de exportación «deberán llevar, en forma automatizada, el sistema
  de control de inventarios». Tercer párrafo: si se incumple, «se presumirá que las mercancías
  […] análogas o iguales a las importadas, son de procedencia extranjera».
  *Uso en la skill:* fundamento del registro actualizado (paso 1, empresa no certificada) y de
  los hallazgos DIF-CANTIDAD y SIN-REGISTRO-A24.
- **Art. 108, plazos de permanencia** — «podrán permanecer en el territorio nacional por los
  siguientes plazos. I. Hasta por dieciocho meses, en los siguientes casos: a) Lubricantes y
  otros materiales que se vayan a consumir durante el proceso productivo […] b) Materias primas,
  partes y componentes que se vayan a destinar totalmente a integrar mercancías de exportación.
  c) Envases y empaques. d) Etiquetas y folletos. II. Hasta por dos años, tratándose de
  contenedores y cajas de trailers. III. Por la vigencia del programa de maquila o de
  exportación, en los siguientes casos: a) Maquinaria, equipo, herramientas, instrumentos,
  moldes y refacciones destinados al proceso productivo. […] c) Equipo para el desarrollo
  administrativo.»
  Mismo artículo: «Las mercancías que hubieran sido importadas temporalmente de conformidad con
  este artículo deberán retornar al extranjero o destinarse a otro régimen aduanero en los
  plazos previstos. En caso contrario, se entenderá que las mismas se encuentran ilegalmente en
  el país, por haber concluido el régimen de importación temporal al que fueron destinadas.»
  *Uso en la skill:* paso 2 y hallazgos VENCIDO / POR-VENCER.
- **Art. 109** — declaración de retornos, mermas y desperdicios, y cambio de régimen a
  definitiva. *Uso en la skill:* solo para nombrar las salidas que descargan (paso 3.2); no
  calcula contribuciones.
- **Lo que la skill supone y lo dice:** el plazo de permanencia se cuenta desde la «fecha de
  entrada declarada en el pedimento» (campo del Anexo 24, F3). El artículo dice «podrán
  permanecer […] hasta por»; el punto exacto de inicio lo confirma el agente aduanal.

## F2 · Reglas Generales de Comercio Exterior para 2026 (RGCE 2026)

- **Publicación:** DOF 27-12-2025, «Reglas Generales de Comercio Exterior para 2026 y Anexo 13»,
  nota 5777199.
- **URL:** https://dof.gob.mx/nota_detalle.php?codigo=5777199&fecha=27/12/2025
- **Vigencia** (Transitorio Primero): «La presente Resolución entrará en vigor el 1o. de enero de
  2026 y estará vigente hasta el 31 de diciembre de 2026.»
- **Regla 4.3.1** «Información mínima del control de inventarios (Anexo 24)»: «Para los efectos
  de los artículos 59, fracción I, 108, 109 y 112 de la Ley y 24, fracción IX del Decreto IMMEX,
  las empresas con Programa IMMEX que importen temporalmente mercancías al amparo de su
  respectivo programa y las ECEX, deberán llevar un control de inventarios en forma automatizada
  y permanente, que contenga al menos los catálogos y módulos establecidos en el Anexo 24,
  apartado A.»
- **Regla 7.1.1, fr. XIV** (requisito del Registro en el Esquema de Certificación de Empresas):
  «Llevar el control de inventarios de conformidad con el artículo 59, fracción I de la Ley, en
  términos del Anexo 24, apartado C.»
- *Uso en la skill:* quién está obligado y qué apartado le aplica (paso 1); regla dura 7 (vigencia).

## F3 · Anexo 24 de las RGCE 2026 — «Información mínima que debe contener el sistema automatizado de control de inventarios»

- **Publicación:** DOF 15-01-2026, «Anexos 21, 22, 23, 24, 25, 26, 27, 28, 29 y 30 de las Reglas
  Generales de Comercio Exterior para 2026, publicadas el 27 de diciembre de 2025», nota 5778300.
- **URL:** https://dof.gob.mx/nota_detalle.php?codigo=5778300&fecha=15/01/2026
- **Apartado A** (regla 4.3.1), lo que la skill usa:
  - I. Catálogos: a) datos generales del contribuyente; b) materiales: «1. Fracción arancelaria
    […] 2. Descripción del material […] 3. Unidad de medida de la TIGIE»; c) productos.
  - II, a) Módulo de entradas: «1. Número de pedimento (clave de la aduana/sección de despacho,
    patente y número de documento). 2. Clave del pedimento. 3. Fecha de entrada declarada en el
    pedimento.»
  - II, b) Materiales utilizados: debe «relacionar las cantidades del producto elaborado con el
    consumo real de componentes utilizados en su producción, para un periodo específico; así
    como las cantidades de mermas y desperdicios».
  - II, c) Salidas: «se deberá descargar (descontar) de manera automática, la cantidad de cada
    mercancía determinada o calculada conforme al inciso b) […] utilizando para tales efectos el
    método de control de inventarios PEPS, descargando dichas mercancías del pedimento que ampara
    la importación temporal más antigua que contenga la mercancía a descargar»; si la cantidad es
    mayor que el saldo de ese pedimento, «se descargará el saldo […] y la diferencia se
    descargará del siguiente pedimento que ampare la importación temporal que corresponda en
    orden cronológico».
  - II, d) Activo fijo; III) Reportes de entradas, salidas, saldos por fracción y materiales utilizados.
- **Apartado C** (empresas con Registro en el Esquema de Certificación de Empresas): «El sistema
  automatizado de control de inventarios conforme al presente apartado, deberá actualizarse en un
  plazo que no exceda de 48 horas contadas a partir de que concluyan los actos y formalidades
  relacionados con el despacho aduanero en términos de la Ley. Asimismo, se deberá permitir el
  acceso en línea a la autoridad aduanera».
- *Uso en la skill:* pasos 1–3, reglas C1, C2, C4, C6–C9. **El plazo de 48 horas es del apartado C;
  el apartado A no fija horas**, por eso para empresas no certificadas la skill usa un umbral
  interno rotulado como tal. La skill cuenta horas corridas y toma como inicio la hora de
  «despacho concluido» que da el usuario; si solo hay fecha, usa 00:00 y lo marca `PROXY`.

## F4 · Anexo 22 de las RGCE 2026 — Apéndice 2, claves de pedimento

- **Publicación y URL:** las mismas de F3 (DOF 15-01-2026, nota 5778300).
- Claves que la skill reconoce: «IN - Importación temporal de bienes que serán sujetos a
  transformación, elaboración o reparación (IMMEX)»; «RT - Retorno de mercancías (IMMEX)»;
  «V1 - Transferencias de mercancías (importación temporal virtual; […] retorno virtual […])»;
  «F4 - Cambio de régimen de insumos o de mercancía exportada temporalmente»; «H1 - Retorno de
  mercancías en su mismo estado».
- Número de pedimento: patente o autorización (4 dígitos) y «siete dígitos […] numeración
  progresiva […] antecedido por el último dígito del año»; el Anexo 24 lo registra con la clave
  de la aduana/sección de despacho al frente.
- *Uso en la skill:* clasificar entradas y salidas (paso 3) y validar la forma del número.

## F5 · Decreto para el Fomento de la Industria Manufacturera, Maquiladora y de Servicios de Exportación (Decreto IMMEX)

- **Publicación original:** DOF 01-11-2006. Texto de la publicación en el sitio del SAT:
  http://m.sat.gob.mx/informacion_fiscal/normatividad/Documents/maquila20061101.doc
- **Reforma que se cita:** DOF 24-12-2010, nota 5172388,
  https://dof.gob.mx/nota_detalle.php?codigo=5172388&fecha=24/12/2010
  - Art. 24, fr. IX (texto reformado): «Llevar el control de inventarios en forma automatizada,
    observando lo dispuesto en el artículo 10 del presente Decreto».
  - Art. 4, fr. I: «Cuando las mercancías a que se refiere la presente fracción se encuentren
    comprendidas en el Anexo I BIS del presente Decreto, el plazo de permanencia será hasta por
    seis meses; tratándose de las comprendidas en el Anexo I TER de este ordenamiento, el citado
    plazo será hasta por nueve meses, y para las señaladas en los Anexos II y III de este
    ordenamiento, el plazo de permanencia será hasta por doce meses. […] Lo dispuesto en los
    párrafos precedentes no le será aplicable a las empresas con Programa que cuenten con
    registro de empresa certificada.»
- **Modificación más reciente encontrada:** DOF 28-08-2025, nota 5766797
  (https://dof.gob.mx/nota_detalle.php?codigo=5766797&fecha=28/08/2025): modifica el **Anexo I**
  (mercancías que no pueden importarse temporalmente; agrega calzado, partidas 64.01 a 64.05). No
  cambia los plazos del art. 4 ni el art. 24, fr. IX.
- *Uso en la skill:* paso 2 (plazos cortos solo con el dato del usuario) y la obligación de
  control automatizado. **La skill no trae la lista de fracciones de esos anexos**: no decide si
  una fracción está en ellos.
- **Limitación declarada:** no se encontró en esta consulta un texto compilado oficial del
  Decreto IMMEX con todas sus reformas; los textos citados son los de cada publicación en el DOF.

## Lo que esta skill NO toma de ninguna fuente

- Montos de multas, recargos o contribuciones: no los calcula.
- La lista de fracciones de los Anexos I, I BIS, I TER, II y III del Decreto IMMEX.
- El Anexo 30 ni ningún reporte que se entrega a la autoridad.
- Si una diferencia obliga a rectificar un pedimento: lo pregunta al agente aduanal.
