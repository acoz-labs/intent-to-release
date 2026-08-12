# ADR 0001: Skills-only lifecycle plugin

- Status: Accepted

## Context

Users need focused phase entry points without loading or maintaining three
copies of the lifecycle, and v0.1 must remain portable and passive.

## Decision

Ship exactly three namespaced thin skills backed by one normative method,
portable templates, guidance, and one fictional example. Add no runtime
integration or executable plugin surface.

## Consequences

Trigger boundaries remain understandable and context stays small. Shared rules
must be edited in the method first, and static validators guard gate count,
skill count, and passive payload shape.
