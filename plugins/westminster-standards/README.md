# Westminster Standards plugin

Ask Claude about the Westminster Standards — the Confession of Faith and the
Larger and Shorter Catechisms — and get exact, cited quotations from the
Orthodox Presbyterian Church constitutional text, with scripture proofs and
the 2025 Modern English Study Version (MESV).

## What it does

**Look up & cite passages** — ask things like:

- "What does the Westminster Confession say about baptism?"
- "Show me Shorter Catechism question 1 with its scripture proofs"
- "Give me WCF 21 in modern English"
- "Compare the constitutional and modern text of WCF 1.1"

**Catechism quiz** — say "quiz me on the Shorter Catechism" and Claude asks
official questions one at a time, grades your answers on substance, shows the
exact catechism wording, keeps score, and offers the proof texts for anything
you missed.

## Requirements

- macOS or Linux with Python 3.9+
- [`uv`](https://docs.astral.sh/uv/) or [`pipx`](https://pipx.pypa.io/)

On first use the plugin installs the
[`westminster-standards-cli`](https://pypi.org/project/westminster-standards-cli/)
tool from PyPI (`uv tool install westminster-standards-cli`). Everything runs
locally — the full corpus is bundled with the CLI, so no network access is
needed after install.

## Installing the plugin

Open the `.plugin` file with Claude (or drag it into a Cowork conversation) and
accept the install prompt.

## Data sources

Text derives from the OPC pages and documents linked from
<https://opc.org/confessions.html>: the constitutional text with scripture
proofs, and the 2025 Modern English Study Version. Per the OPC preface, the
MESV is a study aid and carries no constitutional authority.

## Source

CLI and plugin source: <https://github.com/normanormata/westminster_cli>
