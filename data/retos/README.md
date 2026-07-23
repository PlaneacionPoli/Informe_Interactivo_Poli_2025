# retos — Consolidado de retos por unidad (PDI)

Contiene `Consolidado_Retos_PDI.xlsx`, hoja `Unidad`. Alimenta la fuente
`retos_unidades` usada en `index.html` (variable `D.retos_unidades` /
`allPMO`... ver `retosU` en el panel de retos).

## Cómo editar

1. Abre `Consolidado_Retos_PDI.xlsx`, hoja `Unidad`.
2. Cada fila es una unidad organizacional (`Unidad`) con su % de
   cumplimiento del año en curso (columna `2025`).
3. Para un nuevo año, agrega una columna con el nombre del año (`2026`,
   etc.) — el código en `index.html` que consuma este dato debe actualizarse
   para leer la columna del año correspondiente.
4. Guarda y regenera el bundle: `python scripts/bundle_data.py`.

## Ver también

- [`schema.md`](./schema.md) — columnas de `Consolidado_Retos_PDI.xlsx`.
