# Service Boundaries

## Regla principal

```txt
Compartir contratos si.
Compartir dominio interno no.
```

## Permitido

- JSON Schema.
- OpenAPI.
- Ejemplos.
- Codigos de error.
- Eventos.
- Metadata de trazabilidad.
- Guias de generacion de SDK.

## Prohibido

- Modelos Django o SQLAlchemy.
- Queries SQL.
- Repositorios de datos.
- Servicios de dominio.
- Routers productivos.
- Workers.
- Secretos.

Si un cambio requiere importar este repositorio como dependencia de runtime para ejecutar logica, probablemente esta mal ubicado.
