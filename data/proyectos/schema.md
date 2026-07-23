# proyectos — Maestro de proyectos estratégicos

Esta carpeta tiene dos hojas/fuentes distintas: `proyectos` (maestro simple)
y `proyectos_pmo` (detalle PMO, en `centroDeProyectos_PMO_2026.xlsx`). Ver
columnas de cada una abajo.

## Hoja `proyectos` (`proyectos.xlsx`)

| # | Columna | Tipo | Descripción |
|---|---------|------|-------------|
| 1 | `id` | string | Identificador (`P-001`, `P-002`, …). |
| 2 | `nombre` | string | Nombre del proyecto. |
| 3 | `linea` | enum | Línea estratégica asociada (`calidad`, `educacion`, `expansion`, `experiencia`, `transformacion`, `sostenibilidad`). |
| 4 | `avance` | número 0-100 | % de avance del proyecto. |
| 5 | `unidad` | string | Unidad responsable del proyecto. |

## Convenciones (`proyectos`)

- IDs incrementales por línea: `P-001` a `P-009` calidad, `P-010` a `P-019` educación, etc.
- 17 proyectos en total (3-4 por línea).
- `avance` debe ser entero entre 0 y 100.

## Hoja `proyectos_pmo` (`centroDeProyectos_PMO_2026.xlsx`)

Nombres de columna reales (tal como están en el XLSX y en `data-bundle.js`,
sin normalizar — incluyen prefijos numéricos y tildes):

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `Nombre del proyecto` | string | Nombre del proyecto. |
| `0. Estado del proyecto` | string | Estado (`Cierre`, `En ejecución`, `Stand by`, etc.). Si contiene "stand", el Gantt muestra el badge "Stand by". |
| `ILUMNO` | string | `SI`/`NO`, marca si el proyecto es de Ilumno. |
| `% completado` | string | % de avance mostrado en el Gantt (texto, ej. `99%`). |
| `% Esperado centro de proyectos` | string | % esperado según el centro de proyectos. |
| `Ind. cumplimiento PWA` | string | Indicador de cumplimiento (ratio). |
| `Propietario` | string | Responsable del proyecto. |
| `0. Sponsor` | string | Patrocinador del proyecto. |
| `4. Líneas estratégicas` | string | Línea estratégica; se filtra por `.includes()` contra el nombre de línea. |
| `2. Vicerrectoría` | string | Vicerrectoría responsable. |
| `3. Area` | string | Área responsable. |
| `5. Orden interna OPEX` | string | Código de orden interna OPEX. |
| `5.1. Presupuesto OPEX` | string | Presupuesto OPEX asignado. |
| `5.2. Presupuesto OPEX ejecutado` | string | Presupuesto OPEX ejecutado. |
| `6. Orden inversión CAPEX` | string | Código de orden CAPEX. |
| `6.1. presupuesto CAPEX` | string | Presupuesto CAPEX asignado. |
| `6.2. Presupuesto CAPEX ejecutado` | string | Presupuesto CAPEX ejecutado. |
| `7. Fecha de seguimiento` | string | Fecha del último seguimiento. |
| `Comienzo` | date/serial | Fecha de inicio (texto `DD/MM/YYYY` o serial Excel). |
| `Fin` | date/serial | Fecha de fin (texto `DD/MM/YYYY` o serial Excel); usada para ordenar el Gantt. |
| `Avance` | string | Descripción textual del avance. |
| `Siguientes Tareas` | string | Próximas tareas del proyecto. |
| `Riesgos` | string | Riesgos identificados. |
| `Impactos Generados` | string | Impactos generados por el proyecto. |
| `Entregables` | string | Entregables del proyecto. |
| `Objetivo del proyecto` | string | Objetivo estratégico asociado al proyecto. |

53 proyectos en el archivo actual.
