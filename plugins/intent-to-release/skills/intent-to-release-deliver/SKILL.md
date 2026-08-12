---
name: intent-to-release-deliver
description: Implement, verify, reconcile, review, independently accept, and release an approved software change. Use only when a merged solution plan records Product Authority Gate 2 and its execution envelope. Do not use to discover product intent, choose an unapproved architecture, or exceed the approved envelope.
---

# Deliver

Require a merged Gate-2-approved plan. Read [the Change Delivery phase](../../references/method.md#phase-3-change-delivery), [the reconciliation template](../../assets/templates/reconciliation.md), and [the release record](../../assets/templates/release.md).

1. Implement the smallest approved slice with tests and durable docs.
2. Open a reviewable implementation change linked to the product brief and plan.
3. Reconcile actual behavior against the plan; explain drift, promote durable knowledge, and delete temporary plan files.
4. Obtain independent engineering review of the current change.
5. Build or identify one immutable candidate; do not rebuild between acceptance and release.
6. Have someone other than the implementing contributor verify the original acceptance criteria against that exact candidate.
7. Promote and verify only within the approved execution envelope; record release and rollback evidence.

Internal review, reconciliation, verification, acceptance, and release checks are quality controls—not extra product-authority gates. Return to Solution Design when evidence changes the outcome, trust boundary, major approach, or authority required.

Label the response **Change Delivery** and identify the recorded **Product
Authority Gate 2** decision before describing implementation or release work.
