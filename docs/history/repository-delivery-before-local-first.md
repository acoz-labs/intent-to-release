# Historical repository delivery instructions

Superseded by `../delivery.md` and the shared portable SDLC. Historical
workflow/owner/staging gates below are not current authority.

# Repository-specific instructions

Shared delivery rules are in `docs/operations/sdlc.md`. They supersede older
mandatory planning/owner gates and prospective self-review exceptions. Historical
records remain evidence. Product behavior, privacy boundaries and actual
validation/release requirements remain in force.

## Product and repository governance

The plugin payload under plugins/intent-to-release is a separately versioned
product. Its existing three-skill method is product content, not this repository's
contributor workflow. Run bin/ci for product validation as well as the SDLC checks.
The existing immutable v0.1.0 product tree/tag and receipts remain historical
release evidence. Shared repository-governance files come from the reviewed
software-repo-template; they are not personal control-plane content or a new
plugin release. Do not copy private publication receipts into the public repo.
Changes to generated plugin payloads must still originate in the source repo.

## Delivery configuration

Delivery profile: `artifact`.
