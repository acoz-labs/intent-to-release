# Intent to Release Method

This is the normative contract. Skills route into it; templates and examples illustrate it. When they conflict, this method wins.

## Method at a glance

Intent to Release is a portable three-phase software lifecycle with exactly two product-authority gates. It separates deciding what is worth building, deciding how it can safely be built, and proving that the result is ready to release.

| Phase | Starts with | Produces | Product decision |
|---|---|---|---|
| Product Discovery | Ambiguous opportunity | Approved product brief | Gate 1: approve intent |
| Solution Design | Approved brief | Approved temporary solution plan | Gate 2: approve approach and envelope |
| Change Delivery | Merged approved plan | Reviewed, accepted, released change | No new product gate |

Review, tests, reconciliation, independent acceptance, and release checks remain mandatory quality controls. They are not product-authority gates.

## Artifact ownership

Each fact has one owner:

- Product deliberation and intent: product brief in an issue or equivalent durable product artifact.
- Executable commitment and lifecycle links: the same product brief's compact status ledger.
- Temporary technical planning: a reviewable repository plan, deleted after reconciliation.
- Implementation and validation evidence: the implementation change or pull request.
- Shipped behavior and operations: durable repository documentation.
- Candidate acceptance and release: candidate-bound acceptance and release records.

Link owners; do not copy their full contents into neighbouring artifacts.

## Phase 1: Product Discovery

Clarify the audience, problem, evidence, assumptions, critical tasks, desired outcome, acceptance criteria, scope, non-goals, risks, and stop signals. Compare opportunities before committing engineering effort. The brief must be understandable without private conversation.

### Product Authority Gate 1

One accountable product authority approves, revises, pauses, or stops the product intent and smallest delivery slice. Record the decision, person or role, and date. Approval authorizes Solution Design, not implementation.

## Phase 2: Solution Design

Inspect the actual repository. Decide the smallest architecture that satisfies the approved brief. Cover behavior, interfaces, state, invariants, errors, compatibility, authorization, privacy, tests, rollout, rollback, documentation promotion, and implementation slices. Record selected and rejected approaches. Contributor and maintainer review occurs inside the planning change.

### Product Authority Gate 2

Product authority approves the complete plan and an explicit execution envelope:

- `implementation`: code, tests, docs, and reviewed implementation only.
- `through-acceptance`: additionally merge, candidate creation, and independent acceptance.
- `through-release`: additionally production/public promotion and verification under repository policy.

Approval must precede implementation. New product outcomes, trust boundaries, irreversible risks, or authority beyond the envelope return here.

## Phase 3: Change Delivery

Implement from the approved plan. Prefer tests that fail before the behavior exists. Keep the change scoped and reviewable. Reconcile before final review:

1. Compare plan and actual behavior.
2. Classify material items as conforming, justified drift, unexplained drift, or design gap.
3. Resolve unexplained drift or return to Solution Design.
4. Promote shipped truth into durable docs.
5. Delete temporary plan files; history preserves design provenance.

An independent maintainer reviews the current implementation and reconciliation. Create one immutable candidate. An acceptor other than the implementing contributor verifies the original criteria against that exact candidate. Release promotes the accepted candidate without rebuilding it, verifies the outcome, records evidence, and keeps a rollback path.

## Adaptation rules

Use ordinary repository collaboration: issues may be tickets, plans may be reviewed branches, and implementation changes may be pull requests or equivalent. Preserve roles, artifact ownership, exact-candidate identity, independence, three phases, and exactly two gates. Do not require a specific host, stack, agent roster, deployment platform, or project board.

For a small change, shorten documents rather than deleting decisions. For an artifact with no staging environment, nominate and accept the exact artifact directly. Never invent staging.

## Failure and return rules

- Missing evidence: continue discovery and label uncertainty.
- Unapproved intent: do not design.
- Unapproved plan: do not implement.
- Material plan invalidation: return to Solution Design.
- Failed review or test: repair within delivery when the approved contract still holds.
- Rejected candidate: return to implementation; preserve evidence.
- Release failure: stop promotion, keep the accepted candidate identifiable, and execute the documented rollback or recovery path.
