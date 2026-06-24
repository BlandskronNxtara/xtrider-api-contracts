# Tests

Validacion minima:

```powershell
python scripts/validate-json-schemas.py
python scripts/validate-yaml-structure.py
python scripts/validate-agent-docs.py
git diff --check
```

## Alcance actual

Los scripts validan sintaxis JSON, presencia de documentos agenticos y estructura minima de YAML/OpenAPI. La validacion profunda de JSON Schema contra ejemplos y OpenAPI queda para una fase con dependencias aprobadas.
