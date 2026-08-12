# Intent to Release

Intent to Release is an MIT-licensed Codex plugin for solo developers and small
teams who want a deliberate, reviewable path from an ambiguous software idea to
an independently accepted release without adopting a heavyweight framework.

It provides exactly three focused skills and two product-authority gates:

- `$intent-to-release-discover` shapes and approves product intent.
- `$intent-to-release-design` designs the solution and approves its execution envelope.
- `$intent-to-release-deliver` implements, reconciles, reviews, accepts, and releases.

## Install

Clone the repository, add its root as a local Codex plugin marketplace, and
install `intent-to-release`. Start a fresh conversation so Codex discovers the
three skills, then invoke the skill matching the current phase. Use Codex's
current plugin marketplace UI or CLI; the product does not bundle an installer.

The [canonical method](plugins/intent-to-release/references/method.md),
[portable templates](plugins/intent-to-release/assets/templates), and fictional
[Paper Airship example](plugins/intent-to-release/references/example/README.md)
work with ordinary repository collaboration and require no specific stack,
host, project board, service, credential, or private context.

## Development

Use the repo-local commands first:

```sh
bin/container bin/ci
```

`bin/ci` validates plugin and skill schemas, content invariants, passive/privacy
boundaries, projection behavior, and release identity contracts.

Public validation is self-contained: run `bin/ci`. Release-control provenance
is deliberately absent from the public tree; the private source process derives
the exact public candidate and independently reviews its privacy boundary.

## Trust boundary

The installed plugin is passive Markdown and JSON. It makes no network request,
collects no telemetry, needs no credential, and includes no executable hook,
MCP server, app, or custom UI. See [Security](SECURITY.md).
