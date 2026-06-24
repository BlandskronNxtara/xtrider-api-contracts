# Data Schema Rules

- Usar JSON Schema draft 2020-12.
- Incluir `$schema`, `$id` y `title`.
- Declarar `required` explicitamente.
- Preferir `additionalProperties: false` en contratos externos.
- No usar nombres ambiguos como `payload` si `data` ya tiene contrato claro.
- Mantener snake_case en APIs actuales de backend.
- Mantener timestamps ISO 8601 con `format: date-time`.
