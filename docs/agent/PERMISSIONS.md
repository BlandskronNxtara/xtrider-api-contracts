# Agent Permissions

## Permitido

- Leer contratos, ejemplos y documentacion.
- Crear schemas nuevos con justificacion.
- Agregar ejemplos.
- Actualizar OpenAPI cuando existe contrato real en un servicio.
- Ejecutar scripts de validacion locales.

## Requiere aprobacion

- Breaking changes.
- Eliminar o renombrar contratos publicados.
- Agregar dependencias.
- Crear SDKs generados.
- Cambiar CI de release/publicacion.

## Prohibido

- Agregar secretos.
- Leer o copiar `.env`.
- Crear logica de negocio.
- Crear modelos internos de servicios.
- Inventar contratos productivos sin productor/consumidor claro.
