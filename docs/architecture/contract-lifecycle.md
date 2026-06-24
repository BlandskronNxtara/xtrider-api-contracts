# Contract Lifecycle

1. Identificar productor, consumidores y dominio.
2. Revisar contratos existentes.
3. Crear o modificar schema/OpenAPI con version compatible.
4. Agregar ejemplo valido.
5. Actualizar errores si aplica.
6. Documentar impacto en `CHANGELOG.md`.
7. Ejecutar validaciones.
8. Coordinar adopcion en servicios consumidores.

## Breaking changes

Un breaking change nunca se mezcla como ajuste menor. Debe tener nueva version o plan de migracion.
