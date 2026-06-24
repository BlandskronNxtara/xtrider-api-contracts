# ADR-0004 - Event Contracts

Estado: Propuesto

## Decision

Todo evento entre servicios usa un envelope con `event_id`, `event_type`, `event_version`, `occurred_at`, `producer`, `tenant_id`, `correlation_id` y `data`.

## Motivo

Los workflows, workers y auditoria necesitan trazabilidad y compatibilidad versionada.
