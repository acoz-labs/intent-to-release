# Intent to Release Lifecycle

The normative public contract is
`plugins/intent-to-release/references/method.md`. Three thin skills route into
its phases; templates and the Paper Airship example are bounded derivatives.

Exactly two product-authority gates approve product intent and then the complete
solution plus execution envelope. Engineering review, reconciliation,
independent acceptance, and release verification are quality controls.

Each knowledge category has one owner: the product brief owns intent and the
lifecycle ledger; a temporary repository plan owns design; the implementation
change owns code and validation evidence; durable repository docs own shipped
truth; candidate-bound records own acceptance and release. Reconciliation
classifies drift, promotes durable knowledge, and deletes the temporary plan.

The installed plugin has no persistence, executable code, credential, network
request, telemetry, app, hook, MCP server, or custom UI. Failure handling is
procedural: missing approval blocks the next phase; material contract or trust-
boundary changes return to Solution Design; rejected candidates return to
implementation; release failures preserve candidate identity and use the
repository rollback procedure.

The source-side publication boundary is intentionally stricter: an explicit
committed source SHA deterministically derives the manifest, public root SHA,
and artifact identity. Target-bound receipts bind immutable repository identity,
refs/objects, hosted/settings posture, privacy review, independent acceptance,
publication authority/event, tag, and anonymous installation. Caller-provided
public SHAs and self-asserted environment evidence are not authority.

The public repository contains a content-only manifest of paths, types, modes,
blob identities, content digests, and sizes. Private source provenance,
allowlist identity, privacy-review material, reviewer decision, and validation
evidence live in a separate source-side projection receipt. The builder rejects
symlinks, gitlinks, special entries, traversal, and unexpected executable modes;
forces SHA-1; and creates one reproducible neutral root commit.

Acceptance and publication form one receipt chain. Live pre-acceptance capture
queries immutable target identity, settings, refs and objects, hosted surfaces,
and actor authority. Product acceptance records that exact receipt digest.
Post-visibility capture extends it with the actual event actor, tag, anonymous
exact-SHA clone/install, and hosted-surface result. Release rejects target,
source, projection, artifact, or receipt substitution.

Private model-forward evidence binds an exact source projection and public SHA
to disposable-marketplace installation, plugin/three-skill preflight, public-
only prompt/output digests, strict semantic rubrics, and independent readable
review. Raw output and authentication material are neither committed nor
projected.
