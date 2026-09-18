# Local candidate acceptance and delivery

The current workflow is [portable verification](operations/local-verification.md).
Use a fixed merged commit and retained artifact. The maintainer performs the
scenarios below, including the issue's specific criteria, and records observed
results with openable evidence in the structured acceptance report. Run the
configured validation on that same commit and publish the receipt independently
of the implementation author. No owner sign-off or Actions runner is required.

Use `bin/sdlc-release nominate`, `bin/sdlc-evidence run --phase acceptance
--candidate ... --report ...`, and `bin/sdlc-evidence publish`. Then run the release
gate before any promotion. Execute the repository-specific procedure below,
record the release scenarios, and use `bin/sdlc-release record` and `finalize`.
The acting agent must perform the work; a report is an attestation, not a substitute
for execution. Record failure honestly and resolve it before release.

Retain a private attempt record **before** deployment/publication. Bind it to the
issue, accepted digest, prior deployed artifact, backup/recovery plan and target.
Serialize changes to the target. After interruption, inspect actual external
state before retrying; do not repeat an uncertain migration or publication.
Publish sanitized logs and reports, keeping credentials/config/data outside Git.
The release report must name the previous artifact (or explicit initial release)
and recovery procedure, as well as each configured release criterion.

Persistent staging is optional. Temporary isolated acceptance instances are
allowed and should be removed after evidence capture. Never use production data,
queues or external side effects for destructive acceptance. Promotion uses the
same accepted bytes, never a fresh build from moving main.

## Source and candidate authority

Product changes originate in the private source repository and its reproducible
public-candidate process. This repository may receive direct reviewed governance
updates from the shared template; those are not plugin releases and do not alter
immutable v0.1.0 payloads. Release-bearing work is tracked in the source repository
while public Issues are disabled. Do not enable public Issues merely for evidence
or copy private receipts here. Public PRs can hold sanitized validation evidence.

- `issue-criteria`: follow the source issue's specific product requirements.
- `retained-public-package`: verify the published candidate was generated from
  the reviewed source and matches the accepted public SHA/manifest/package hash.
- `privacy-and-installation`: validate privacy/passive boundaries and install
  the exact retained public payload in isolation.

## Publication and completion

Execute the source repository's `docs/delivery.md` procedure. Its portable gate
and acceptance bind the complete source implementation set and retained public
artifact; the public PR receives independent current-head review under its active
branch rules. Do not invent a second public issue or rebuild the plugin here.

- `published-same-bytes`: verify the target's product tree/package matches the
  source-accepted candidate, separating the generic governance overlay.
- `anonymous-installation`: verify anonymous download/clone and actual install.
- `immutable-tags`: keep historical tags immutable; retain the previous package
  and recover through a reviewed corrective release. Finalize the private source
  issue only after public delivery evidence is verified.
