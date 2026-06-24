# Versioning

Los contratos siguen SemVer:

- `MAJOR`: breaking change.
- `MINOR`: nuevo campo opcional, nuevo endpoint compatible o nuevo evento versionado.
- `PATCH`: documentacion, ejemplos, aclaraciones o fix no breaking.

## Versiones de API

Las APIs HTTP usan version en path cuando aplica: `/api/v1/...`.

Los eventos usan `event_version`, por ejemplo `v1`.

Los JSON Schemas usan `$id` estable con version logica en el path cuando el contrato sea publicado externamente.

## Cambios compatibles

- Agregar campos opcionales.
- Agregar nuevos codigos de error documentados.
- Agregar endpoints nuevos.
- Agregar ejemplos.
- Aclarar descripcion sin cambiar semantica.

## Breaking changes

- Eliminar o renombrar campos.
- Cambiar tipos.
- Volver obligatorio un campo opcional.
- Cambiar significado de un codigo de error.
- Cambiar semantica de paginacion o metadata.
- Reutilizar `event_type` con payload incompatible.

Todo breaking change requiere entrada en `CHANGELOG.md`, ADR o nota de decision, y analisis de consumidores.
