# Informe: Flujo de actualización del CMI estratégico con SGING

## Propósito

Este documento describe cómo se actualiza el CMI estratégico en el proyecto `Informe_Interactivo`, cuál es la fuente de información real y cómo encaja SGING en el flujo de datos.

## Hallazgos principales

- `data/objetivos/objetivos.xlsx` es la fuente de los **retos y metas de alto nivel**.
- El detalle del CMI estratégico proviene de SGING y se incorpora como `cmi_estrategico`.
- La app actual consume `cmi_estrategico` desde `data-bundle.js`.
- `Catalogo de Indicadores.xlsx` es la fuente de mapeo de indicador → línea estratégica → objetivo estratégico. **No está en este repositorio**: es un archivo externo del proyecto `SGING` (`.../Proyectos_DS/SGING/data/raw/Catalogo de Indicadores.xlsx`), usado sólo como consulta cruzada al preparar datos (ver `extract_catalogo_sging.py`).
- `Resultados_Consolidados_SGING.xlsx` es la referencia oficial trasladada desde SGING para validar resultados consolidados.

## Flujo actual en el repositorio

1. `scripts/bundle_data.py` incluye la fuente:
   - `('cmi_estrategico', 'CMI Estrategico', 'indicadores/CMI Estrategico.xlsx')`
2. Al ejecutar `python scripts/bundle_data.py`, se regenera `data-bundle.js`.
3. En `index.html`, la app lee `window.PDI_DATA.cmi_estrategico` y muestra:
   - `Meta`
   - `Ejecucion`
   - `Cumplimiento`
   - `Meta_Signo`
   - `Ejecucion_Signo`
   - `Decimales_Meta`
   - `Decimales_Ejecucion`
4. `data/sources/sources.js` sólo define la fuente `objetivos` para la carga dinámica de `data/objetivos/objetivos.xlsx`.
5. **Nuevo**: `index.html` ahora carga `vendor/xlsx.full.min.js` (SheetJS) y, al iniciar, intenta `fetch('./data/indicadores/CMI Estrategico.xlsx')` directamente en el navegador. Si el `fetch` funciona (servido por HTTP/HTTPS), sobrescribe `window.PDI_DATA.cmi_estrategico` con la versión más fresca del XLSX, sin depender de que se haya regenerado `data-bundle.js`. Si falla (p. ej. abierto con doble clic `file://`), se conserva el `cmi_estrategico` que ya trae el bundle.

## Roles de las fuentes

- `data/objetivos/objetivos.xlsx`
  - Rol: **retos/metas globales**.
  - Uso: slide `Objetivos Estratégicos`.

- `indicadores/CMI Estrategico.xlsx`
  - Rol: **detalle SGING del CMI**.
  - Uso: datos consolidados de indicadores con signo y formato.

- `Resultados_Consolidados_SGING.xlsx`
  - Rol: **referencia oficial de SGING**.
  - Uso: verificación y trazabilidad del CMI estratégico.

- `Catalogo de Indicadores.xlsx`
  - Rol: **mapeo estratégico**.
  - Uso: asociación de indicador con `Linea_Estrategica` y `Objetivo_Estrategico`.
  - Externo al repositorio (vive en el proyecto `SGING`).

- `data/proyectos/centroDeProyectos_PMO_2026.xlsx` (bundle key `proyectos_pmo`)
  - Rol: **detalle PMO de proyectos**.
  - Uso: Gantt por línea estratégica en cada slide (fechas, % avance, estado, presupuesto).

- `data/retos/Consolidado_Retos_PDI.xlsx` (bundle key `retos_unidades`)
  - Rol: **cumplimiento por unidad organizacional**.
  - Uso: panel de retos por unidad.

## Lógica de formato de valores

- En `index.html`, la función `formatValue(value, signo, decimales)` aplica:
  - `%` → agrega `%`
  - `$` → agrega `$`
  - `DEC`, `ENT` → deja el número sin sufijo
- Esta lógica es la que permite presentar los valores con el formato SGING correcto.

## Conclusión

El documento `data/objetivos/README.md` ahora deja claro que:
- `objetivos.xlsx` es la fuente estratégica de retos/metas.
- `cmi_estrategico` es la capa detallada del CMI basada en SGING.
- El mapeo completo SGING debe apoyarse en `Catalogo de Indicadores.xlsx`.

## Recomendaciones inmediatas

1. Para actualizar el CMI detallado, usa `indicadores/CMI Estrategico.xlsx` y regenera `data-bundle.js`.
2. Para validar el mapeo de línea y objetivo, consulta `Catalogo de Indicadores.xlsx`.
3. Conserva `objetivos.xlsx` sólo para los 12 objetivos y su avance global.
4. Si se desea una integración más dinámica, considere exponer `cmi_estrategico` en `data/sources/sources.js` o agregar una fuente equivalente.
