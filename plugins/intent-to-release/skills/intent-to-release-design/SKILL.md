---
name: intent-to-release-design
description: Convert an approved product brief into a repository-native solution plan and obtain Product Authority Gate 2. Use when product intent is already approved and technical approach, verification, rollout, rollback, documentation promotion, or execution authority must be decided before implementation. Do not use for ambiguous product discovery or delivery of an already approved plan.
---

# Design

Require a Gate-1-approved brief. Read [the Solution Design phase](../../references/method.md#phase-2-solution-design) and copy [the solution plan pack](../../assets/templates/solution-plan/README.md).

1. Inspect the repository and current external constraints.
2. Record context, selected approach, alternatives, boundaries, interfaces, failure modes, privacy/security, migration, and non-goals.
3. Design verification, rollout, rollback, documentation promotion, and reviewable implementation slices.
4. Obtain internal contributor and maintainer review in the planning change.
5. Ask product authority for **Product Authority Gate 2**, including an execution envelope: `implementation`, `through-acceptance`, or `through-release`.
6. Merge the approved planning-only change before implementation begins.

Do not write production code in this phase. Return to discovery if the product outcome changes materially. Output one approved temporary solution plan linked from the product brief.
