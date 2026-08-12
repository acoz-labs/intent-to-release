# Development

Use the repo-local validation entrypoint:

```sh
bin/container bin/ci
```

If container support is not ready for this repo yet:

```sh
bin/ci
```

Document language runtimes, package managers, environment variables, and local
service dependencies here as the project becomes concrete.

## Product validation

The product uses only Python's standard library and shell utilities. Run:

```sh
bin/validate-product
python3 -m unittest discover -s tests -v
```

The development container installs Python 3 solely to execute these repository
checks; the projected plugin remains Markdown and JSON only.

The official plugin and skill creator validators require PyYAML. Keep it
ephemeral rather than adding a product/runtime dependency. The designated host
and clean-clone lane runs `bin/run-official-validators`, which discovers tools
under `CODEX_HOME` or accepts the portable `CODEX_PLUGIN_VALIDATOR` and
`CODEX_SKILL_VALIDATOR` overrides. Missing tooling fails that lane.

```sh
REQUIRE_OFFICIAL_VALIDATORS=1 bin/ci
```

Container and hosted CI run all repository-owned checks but do not claim the
external creator lane. Real install evidence runs with
`RUN_CODEX_INSTALL_TEST=1` against a disposable `CODEX_HOME`; it never installs
into the operator's normal profile.

The private evidence lane runs model-mediated routing and the fictional Paper
Airship chain against an exact projected commit:

```sh
bin/run-forward-evidence <full-source-sha> <private-evidence.json> --auth-file <existing-codex-auth-file>
```

The runner creates an isolated Codex home, copies only the supplied
authentication file with mode `0600`, installs the projected repository
marketplace, verifies the installed plugin and exact three-skill set, and runs
every case in a separate ephemeral context with repository rules disabled. The
new home contains no pre-existing personal configuration, memory, or history;
Codex's generated plugin registration remains enabled. It records prompt and output digests plus
rubric outcomes, then removes the temporary home. The evidence file and raw
model outputs are private validation material and must not be committed or
projected.

For independent semantic review, `--private-output-dir <new-directory>` retains
mode-`0600` responses outside the temporary home. Omit it when deterministic
rubric evidence is sufficient.

When host-local language execution is supported, commit exact versions in a
root `mise.toml` and install them with:

```sh
mise install
```

Container-only repositories may omit host runtime pins. Application packages
remain owned by the ecosystem manifest and lockfile.
