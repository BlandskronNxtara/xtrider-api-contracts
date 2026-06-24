# Integration Map

## Servicios actuales

| Servicio | Usa contratos | Publica contratos |
| --- | --- | --- |
| `xtrider-auth-service` | response, error, contact, tenant, user | OpenAPI IAM, eventos tenant/user/contact |
| `xtrider-operational-service` | response, error, AI, jobs, events | OpenAPI operational, eventos lead/conversation |
| `xtrider-front-landing-angular` | contact public API, public errors | Ninguno |
| `xtrider-front-app-angular` | OpenAPI/SDK futuro, errors, pagination | Ninguno |
| `xtrider-n8n-whatsapp-agent-service` | webhook, AI, events, jobs | Eventos/workflow outputs |
| `xtrider-docker-despliege` | Validaciones y healthchecks | Ninguno |

## MVP

El primer contrato aplicado es el formulario publico de contacto: landing Angular obtiene CSRF desde Django y envia `ContactMessageCreate`.
