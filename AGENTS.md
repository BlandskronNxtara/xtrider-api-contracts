# AGENTS.md

Fuente operativa para agentes IA que trabajen en `xtrider-api-contracts`.

## Proposito

Repositorio central de contratos publicos de Xtrider: OpenAPI, JSON Schema, eventos, webhooks, errores, respuestas estandar, contratos de IA, ejemplos y reglas de versionado.

No contiene logica de negocio ni modelos internos de microservicios.

## Rutas prioritarias

| Ruta | Uso |
| --- | --- |
| `CONTRACT.md` | Alcance, limites e impacto arquitectonico |
| `VERSIONING.md` | Versionado, compatibilidad y breaking changes |
| `schemas/` | JSON Schemas reutilizables |
| `openapi/` | Especificaciones OpenAPI por servicio |
| `errors/` | Catalogos de error por dominio |
| `examples/` | Payloads validos |
| `docs/agent/` | Permisos, pruebas, seguridad y runbooks |
| `skills/` | Guias especializadas para agentes |
| `scripts/` | Validaciones locales |

## Reglas

- Compartir contratos si; compartir dominio interno no.
- Mantener contratos versionados y trazables.
- No crear endpoints, eventos o codigos sin justificar consumidor, productor e impacto.
- No agregar secretos, `.env`, credenciales, tokens ni datos reales.
- No agregar SDKs generados, paquetes publicados o dependencias sin aprobacion humana.
- `CLAUDE.md` y `GEMINI.md` deben remitir aqui sin duplicar reglas.

## Cambios que requieren aprobacion

- Breaking changes.
- Eliminacion o renombre de schemas publicados.
- Cambios de versionado.
- Nuevos workflows de release/publicacion.
- Dependencias nuevas.
- Generacion de SDKs o clientes.

## Validaciones

```powershell
python scripts/validate-json-schemas.py
python scripts/validate-yaml-structure.py
python scripts/validate-agent-docs.py
git diff --check
```

Si se modifican OpenAPI o YAML, ejecutar la validacion estructural y revisar manualmente referencias y ejemplos hasta que exista validador completo.

## Definicion de terminado

Entregar resumen de archivos, justificacion arquitectonica, servicios impactados, contratos impactados, breaking changes, validaciones ejecutadas y riesgos pendientes.
