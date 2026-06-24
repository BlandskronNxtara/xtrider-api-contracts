# Contrato Arquitectonico

`xtrider-api-contracts` es la fuente central de contratos externos y operativos de la plataforma Xtrider.

## Problema

Sin contratos centrales, cada servicio puede definir respuestas, errores, eventos, paginacion y metadata de forma distinta. Eso aumenta condiciones especiales en frontends, rompe workflows n8n, complica auditoria y deja a agentes IA sin contexto suficiente.

## Decision

Mantener en este repositorio contratos reutilizables y documentacion operativa:

- JSON Schema para respuestas, errores, jobs, IA, eventos, webhooks y auditoria.
- OpenAPI por servicio.
- Catalogos de error por dominio.
- Ejemplos validos.
- Reglas de versionado y analisis de breaking changes.
- Documentacion para agentes IA.

## Limites

Este repositorio no debe contener:

- Modelos internos de Django o SQLAlchemy.
- Queries SQL, repositorios, servicios de dominio o casos de uso.
- Routers productivos, workers o adapters.
- Conexiones a bases de datos.
- Secretos o variables reales.
- Logica que obligue a un microservicio a depender internamente de otro.

## Servicios impactados

- `xtrider-auth-service`: respuestas, errores, eventos tenant/user y OpenAPI.
- `xtrider-operational-service`: IA, jobs, eventos, analytics y contratos multi-tenant.
- `xtrider-front-app-angular`: SDK/tipos futuros, errores globales y paginacion.
- `xtrider-front-landing-angular`: contacto publico y respuestas de formulario.
- `xtrider-n8n-whatsapp-agent-service`: webhooks, eventos WhatsApp e IA.
- `xtrider-docker-despliege`: validacion y despliegue, sin logica de contratos.

## MVP contractual

La base minima incluye `ApiResponse`, `ApiError`, `PaginatedResponse`, `AsyncJob`, `DomainEvent`, un OpenAPI publico inicial y ejemplos validos.
