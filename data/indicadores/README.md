# indicadores — Detalle CMI Estratégico (SGING)

Esta carpeta contiene `CMI Estrategico.xlsx`, la fuente de detalle del Cuadro de
Mando Integral trasladada desde SGING. Alimenta la fuente `cmi_estrategico`
que se muestra dentro de cada slide de línea estratégica (sección "CMI
Estratégico" agrupada por objetivo).

No confundir con `data/objetivos/objetivos.xlsx`: ese archivo tiene el rol de
retos/metas globales por objetivo; este archivo tiene el detalle de
indicadores individuales (meta, ejecución, cumplimiento, formato).

## Cómo editar

1. Abre `CMI Estrategico.xlsx`, hoja `CMI Estrategico`.
2. Edita `Meta`, `Ejecucion` o `Cumplimiento` de la fila del indicador.
3. Si necesitas fijar el orden de aparición dentro de una línea/objetivo,
   agrega/edita la columna `orden` (o `Orden`) con un entero 1-N. Si dejas
   la columna vacía en algunas filas de una línea donde otras sí la tienen,
   esas filas se muestran al final.
4. Guarda el archivo.
5. Regenera el bundle: `python scripts/bundle_data.py` (actualiza
   `data-bundle.js`).
6. Si sirves la app por HTTP (no `file://`), `index.html` también intenta
   leer este XLSX en vivo con SheetJS al cargar la página — ver
   [`../README.md`](../README.md#carga-en-vivo-de-cmi-estrategico). Eso
   significa que un cambio guardado en el archivo puede verse recargando el
   navegador, incluso sin regenerar el bundle, siempre que se sirva por
   HTTP/HTTPS.

## Fuente de verificación

`data/objetivos/Resultados_Consolidados_SGING.xlsx` es el archivo trasladado
desde SGING para validar y trazar los resultados consolidados de este CMI.
`Catalogo de Indicadores.xlsx` (mapeo indicador → línea → objetivo) es un
archivo **externo**, del proyecto `SGING`, no versionado en este repositorio.

## Ver también

- [`schema.md`](./schema.md) — columnas de `CMI Estrategico.xlsx`.
- [`../objetivos/schema.md`](../objetivos/schema.md) — ficha completa de la
  hoja `cmi_estrategico` (se documenta ahí junto a `objetivos` por ser el
  mismo CMI).
