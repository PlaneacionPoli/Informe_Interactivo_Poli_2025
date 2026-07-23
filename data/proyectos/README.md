# proyectos — Maestro de proyectos estratégicos

Esta carpeta contiene **dos fuentes independientes**, con esquemas distintos:

- `proyectos.xlsx` → bundle key `proyectos` (maestro simple, ver abajo).
- `centroDeProyectos_PMO_2026.xlsx` → bundle key `proyectos_pmo` (detalle PMO
  usado por el Gantt y el cruce con el CMI en cada slide de línea
  estratégica).

## Fuente `proyectos` (`proyectos.xlsx`)

Esta fuente alimenta la slide **Proyectos Estratégicos** y se cruza con `objetivos/objetivos.xlsx` por línea estratégica.

## Cómo editar

1. Abre `proyectos.xlsx`.
2. Edita las filas existentes o añade una nueva con el `id` siguiente de la serie.
3. `linea` debe coincidir con un `id` válido de `avance.xlsx`.
4. Guarda.

## Series de IDs

| Serie | Línea |
|-------|-------|
| `P-001` a `P-009` | calidad |
| `P-010` a `P-019` | educacion |
| `P-020` a `P-029` | expansion |
| `P-030` a `P-039` | experiencia |
| `P-040` a `P-049` | transformacion |
| `P-050` a `P-059` | sostenibilidad |

## Fuente `proyectos_pmo` (`centroDeProyectos_PMO_2026.xlsx`)

Detalle del centro de proyectos PMO usado por el Gantt de cada línea
estratégica en `index.html`. Se filtra por `4. Líneas estratégicas` y se
ordena por fecha de `Fin` (los sin `Fin` válido quedan al final).

- El proyecto se marca con badge **"Stand by"** en el Gantt cuando
  `0. Estado del proyecto` contiene la palabra "stand" (case-insensitive),
  en cuyo caso no se muestra el `%` de avance.
- `Comienzo` y `Fin` aceptan tanto texto `DD/MM/YYYY` como fecha serial de
  Excel (ambos son parseados por `parseDate()` en `index.html`).

Ver [`schema.md`](./schema.md#hoja-proyectos_pmo-centrodeproyectos_pmo_2026xlsx)
para la lista completa de columnas.

## Ver también

- [`schema.md`](./schema.md) — definición de columnas.
- [`../objetivos/schema.md`](../objetivos/schema.md) — para el CMI relacionado.
