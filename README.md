# xtrider-api-contracts

Repositorio central de contratos publicos, esquemas JSON, especificaciones OpenAPI, eventos, errores, estandares de respuesta y documentacion AI-First para la plataforma Xtrider.

Este repositorio existe para que `xtrider-auth-service`, `xtrider-operational-service`, frontends Angular, workflows n8n, WhatsApp Gateway, workers futuros y agentes IA compartan contratos sin compartir dominio interno ni bases de datos.

## Principio

```txt
El contexto tambien es arquitectura.
```

Los microservicios no comparten logica de negocio. Comparten contratos versionados, ejemplos, codigos de error y reglas de compatibilidad.

## Contenido inicial

- Contratos base: `ApiResponse`, `ApiError`, `PaginatedResponse` y `AsyncJob`.
- Contratos AI-First para respuestas IA, uso, fuentes y recuperacion.
- Contrato base de eventos y ejemplo `contact-message.created`.
- OpenAPI inicial para endpoints publicos de contacto de `xtrider-auth-service`.
- Catalogos iniciales de errores por dominio.
- Documentacion operativa para agentes IA.
- Scripts y CI basicos de validacion.

## Estructura

```txt
openapi/      Especificaciones OpenAPI y componentes comunes
schemas/      JSON Schemas reutilizables
errors/       Codigos de error por dominio
examples/     Payloads validos de respuesta, error, evento, job e IA
docs/         Arquitectura, runbooks, seguridad y ADRs
skills/       Skills para agentes IA
scripts/      Validaciones locales
.github/      Instrucciones y workflows
```

## Uso rapido

```powershell
python scripts/validate-json-schemas.py
python scripts/validate-yaml-structure.py
python scripts/validate-agent-docs.py
git diff --check
```

Los scripts solo validan estructura local y sintaxis basica de contratos. No publican paquetes, no generan SDKs y no llaman servicios externos.

## Reglas duras

- No agregar modelos Django, SQLAlchemy ni entidades internas de servicios.
- No agregar queries SQL, repositorios, casos de uso, routers productivos ni adapters.
- No agregar secretos, tokens, llaves privadas ni variables reales.
- Todo cambio breaking debe quedar en `CHANGELOG.md` y tener analisis de impacto.
- `AGENTS.md` es la fuente operativa principal para agentes; `CLAUDE.md` y `GEMINI.md` solo remiten alli.

## Estado

Estado actual: fundacion inicial para MVP. Los servicios pueden empezar a alinear respuestas publicas, errores, paginacion, eventos y metadata sin acoplar su implementacion interna.
