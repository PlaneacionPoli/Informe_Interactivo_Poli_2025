# objetivos — Objetivos estratégicos (CMI)

Esta carpeta contiene dos capas de CMI:

- `objetivos.xlsx`: retos y metas de alto nivel por objetivo estratégico.
- `cmi_estrategico`: detalle complementario del CMI con valores SGING para meta, ejecución, cumplimiento y formato.

## Propósito de cada fuente

- `objetivos.xlsx` alimenta la slide **Objetivos Estratégicos** y es la fuente de los **retos/metas estratégicas**. Es la referencia de avance global por objetivo.
- `cmi_estrategico` no reemplaza a `objetivos.xlsx`; es una capa complementaria de detalle para el CMI estratégico con (nombres reales de columna, ver [`schema.md`](./schema.md#hoja-cmi_estrategico)):
  - `Indicador`, `Proceso`, `Periodicidad`, `Sentido`
  - `Linea`, `Objetivo`
  - `Meta`, `Ejecucion`, `Cumplimiento`, `Cumplimiento Real`
  - `Meta_Signo`, `Ejecucion_Signo`, `Decimales_Meta`, `Decimales_Ejecucion`
  - `Llave` (clave única del registro, para trazabilidad)
  - `orden` (opcional, minúscula) para controlar el orden de los indicadores dentro de cada línea/objetivo; los registros sin orden se muestran después de los ordenados.

## Flujo de actualización del CMI

1. Si actualizas el avance o el objetivo estratégico, usa `data/objetivos/objetivos.xlsx`.
2. Si actualizas el detalle del CMI a partir de SGING:
   - usa [`../indicadores/CMI Estrategico.xlsx`](../indicadores/CMI%20Estrategico.xlsx)
   - regenera el bundle de datos con `python scripts/bundle_data.py`
   - eso actualiza `data-bundle.js`. Además, `index.html` intenta un `fetch` en vivo de ese XLSX con SheetJS al cargar la página (ver [`../README.md`](../README.md#carga-en-vivo-de-cmi-estrategico)); cuando funciona, sobrescribe el `cmi_estrategico` del bundle en el navegador sin necesidad de regenerar nada.
3. `Resultados_Consolidados_SGING.xlsx` (en esta misma carpeta) es el archivo trasladado desde SGING y sirve como fuente de consulta oficial para los resultados consolidados.
4. `Catalogo de Indicadores.xlsx` es la fuente de mapeo de indicadores a `Linea_Estrategica` y `Objetivo_Estrategico`, pero **no está en este repositorio**: es un archivo externo del proyecto `SGING`, usado sólo como consulta cruzada al preparar datos.

## Nota importante

- En este repositorio, **`objetivos.xlsx` no es la fuente primaria de indicadores CMI**.
- El detalle del CMI estratégico proviene de SGING y se incorpora como capa `cmi_estrategico`.
- La app tiene lógica de presentación que usa `Meta_Signo`, `Ejecucion_Signo`, `Decimales_Meta` y `Decimales_Ejecucion`.

## Archivos de esta carpeta

- **`objetivos.xlsx`** (hoja `objetivos`): resumen ejecutivo por objetivo estratégico (id, nombre, meta, real, línea).
- **`Resultados_Consolidados_SGING.xlsx`**: archivo (no hoja) trasladado desde SGING, fuente oficial para validación y trazabilidad del CMI. No se bundlea automáticamente.

La hoja `cmi_estrategico` (detalle complementario del CMI con campos SGING) vive en un archivo aparte: [`../indicadores/CMI Estrategico.xlsx`](../indicadores/CMI%20Estrategico.xlsx) — ver [`../indicadores/README.md`](../indicadores/README.md).

## Ver también

- [`schema.md`](./schema.md) — definición de columnas.
