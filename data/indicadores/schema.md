# indicadores — CMI Estratégico (SGING)

Hoja: `CMI Estrategico`. Bundle key: `cmi_estrategico`.

Ver la ficha completa de columnas en
[`../objetivos/schema.md`](../objetivos/schema.md#hoja-cmi_estrategico) —
se documenta ahí para mantener juntas las dos capas del mismo CMI
(`objetivos` = retos/metas globales, `cmi_estrategico` = detalle por
indicador).

## Resumen rápido

| Columna | Descripción |
|---------|-------------|
| `Id`, `Indicador`, `Proceso` | Identificación del indicador. |
| `Periodicidad`, `Sentido`, `Fecha`, `Año`, `Mes`, `Periodo` | Metadatos de la medición. |
| `Linea`, `Objetivo` | Ubicación del indicador en el CMI. |
| `orden` (opcional) | Orden de despliegue dentro de la línea/objetivo. |
| `Meta`, `Ejecucion`, `Cumplimiento`, `Cumplimiento Real` | Valores numéricos del indicador. |
| `Meta_Signo`, `Ejecucion_Signo`, `Decimales_Meta`, `Decimales_Ejecucion` | Formato de presentación (`formatValue()` en `index.html`). |
| `Llave` | Clave única del registro. |
