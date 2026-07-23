# objetivos — Objetivos estratégicos (CMI)

Hoja: `objetivos` y `cmi_estrategico`.

## Hoja `objetivos`

Esta hoja representa la fuente de **retos y metas de alto nivel**. No debe utilizarse como fuente detallada de indicadores del CMI.

| # | Columna | Tipo | Descripción |
|---|---------|------|-------------|
| 1 | `id` | string | Identificador (`OE-01` a `OE-12`). |
| 2 | `nombre` | string | Nombre del objetivo estratégico. |
| 3 | `perspectiva` | enum | Perspectiva CMI: `Financiera`, `Clientes/Mercado`, `Procesos internos`, `Aprendizaje`. |
| 4 | `meta` | número 0-100 | % meta del objetivo. |
| 5 | `real` | número 0-100 | % real alcanzado. |
| 6 | `linea` | enum | Línea estratégica: `calidad`, `educacion`, `expansion`, `experiencia`, `transformacion`, `sostenibilidad`. |

## Hoja `cmi_estrategico`

> El archivo físico de esta hoja **no** es `objetivos.xlsx`: vive en [`data/indicadores/CMI Estrategico.xlsx`](../indicadores/CMI%20Estrategico.xlsx) (hoja `CMI Estrategico`). Se documenta aquí porque es la capa de detalle del mismo CMI. Ver [`data/indicadores/schema.md`](../indicadores/schema.md) para la ficha completa de esa fuente.

Nombres de columna reales (tal como aparecen en el XLSX y en `data-bundle.js`; **no** están en minúscula/snake_case):

| # | Columna | Tipo | Descripción |
|---|---------|------|-------------|
| 1 | `Id` | string | Identificador del indicador en el catálogo SGING. |
| 2 | `Indicador` | string | Nombre del indicador. |
| 3 | `Proceso` | string | Proceso institucional asociado. |
| 4 | `Periodicidad` | string | Frecuencia de medición (`Semestral`, `Anual`, etc.). |
| 5 | `Sentido` | string | `Positivo` o `Negativo`. |
| 6 | `Fecha` | serial Excel | Fecha del corte de medición (número serial, no texto `DD/MM/YYYY`). |
| 7 | `Año` | number | Año del corte. |
| 8 | `Mes` | string | Mes del corte. |
| 9 | `Periodo` | string | Periodo del corte (`2025-2`, etc.). |
| 10 | `Linea` | enum | Línea estratégica del indicador. |
| 11 | `Objetivo` | string | Objetivo estratégico asociado. |
| 12 | `orden` (opcional) | entero 1-N | Columna opcional, minúscula (o `Orden`). Controla el orden del indicador dentro de su línea/objetivo. Si **ninguna** fila de la línea tiene `orden`, se conserva el orden original de la hoja; si **alguna** fila sí lo tiene, las filas sin `orden` se envían al final. |
| 13 | `Meta` | number | Meta del indicador. |
| 14 | `Ejecucion` | number | Ejecución real del indicador. |
| 15 | `Cumplimiento` | number | Ratio de cumplimiento (ejecución/meta), ej. `1.0189...`. |
| 16 | `Cumplimiento Real` | number | Cumplimiento sin tope (puede superar 1), usado para trazabilidad. |
| 17 | `Meta_Signo` | string | Signo/formato de la meta: `DEC`, `ENT`, `%`, `$`. |
| 18 | `Ejecucion_Signo` | string | Signo/formato de la ejecución: `DEC`, `ENT`, `%`, `$`. |
| 19 | `Decimales_Meta` | number | Decimales a mostrar para la meta. |
| 20 | `Decimales_Ejecucion` | number | Decimales a mostrar para la ejecución. |
| 21 | `Llave` | string | Clave única del registro (`Id-Año-Mes-Día`), usada como clave de agrupación/orden en `index.html`. |

Nota: `fuente` y `estado` (mencionados en una versión anterior de esta ficha) **no existen** en el archivo actual; si se agregan más adelante, actualiza esta tabla.

## Notas de integración

- La hoja `cmi_estrategico` se usa para el detalle compatible con SGING y debe actualizarse editando `data/indicadores/CMI Estrategico.xlsx` y/o cotejando contra `Resultados_Consolidados_SGING.xlsx`.
- `Catalogo de Indicadores.xlsx` (la referencia de asociación indicador → `Linea_Estrategica` → `Objetivo_Estrategico`) **no está en este repositorio**: es un archivo externo del proyecto `SGING` (`.../Proyectos_DS/SGING/data/raw/Catalogo de Indicadores.xlsx`). Úsalo como consulta cruzada, no como fuente a versionar aquí.
- En la app, `data-bundle.js` trae el `cmi_estrategico` regenerado por `scripts/bundle_data.py`, pero `index.html` además intenta un `fetch` en vivo de `data/indicadores/CMI Estrategico.xlsx` con SheetJS (`vendor/xlsx.full.min.js`) al cargar la página; si el fetch funciona (servido por HTTP, no `file://`), **sobrescribe** el `cmi_estrategico` del bundle con la versión más reciente del XLSX sin necesidad de regenerar el bundle. Ver [`../README.md`](../../README.md#carga-en-vivo-de-cmi-estrategico).

## Fuente oficial

El archivo trasladado [Resultados_Consolidados_SGING.xlsx](Resultados_Consolidados_SGING.xlsx) debe considerarse la fuente oficial de consulta para la actualización del CMI estratégico cuando se requiera revisar los resultados consolidados desde SGING.

## Convenciones

- 12 objetivos en total (2 por línea estratégica).
- IDs `OE-01` a `OE-12` correlativos.
- `meta` es típicamente 100; `real` refleja el avance del año.
- La hoja `cmi_estrategico` se usa como detalle complementario del CMI con estructura compatible con la lógica de SGING, mientras que la hoja `objetivos` conserva el rol de fuente de retos y metas estratégicas.
