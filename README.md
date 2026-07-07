# normanormata plugin marketplace

Claude plugins by [normanormata](https://github.com/normanormata), for
Claude Code and Claude Cowork.

## Install

Add the marketplace once, then install any plugin from it.

### Claude Cowork (desktop app)

1. Open **Customize** in the sidebar, then select **Plugins**.
2. Select **Add marketplace** and enter `normanormata/normanormata-plugins`
   (or the full URL `https://github.com/normanormata/normanormata-plugins`).
3. Select **Browse plugins**, choose the plugin you want, and click **Install**.

### Claude Code (CLI / IDE)

Run these slash commands in a Claude Code session:

```
/plugin marketplace add normanormata/normanormata-plugins
/plugin install <plugin-name>@normanormata
```

Or from your shell:

```sh
claude plugin marketplace add normanormata/normanormata-plugins
claude plugin install <plugin-name>@normanormata
```

### Updating

Pick up new plugin versions with `/plugin marketplace update normanormata`
(Claude Code) or by refreshing the marketplace from the Plugins page (Cowork).

## Plugins

### westminster-standards

Study the Westminster Standards — the Confession of Faith and the Larger and
Shorter Catechisms. Look up, quote, and cite entries with exact OPC
constitutional text, including lettered scripture proofs and the 2025 Modern
English Study Version, and take a conversational catechism quiz that grades on
substance and keeps score.

```
/plugin install westminster-standards@normanormata
```

Example prompts:

- "What does the Westminster Confession say about baptism?"
- "Show me Shorter Catechism question 1 with its scripture proofs"
- "Compare the constitutional and modern text of WCF 1.1"
- "Quiz me on the Shorter Catechism"

Powered by the
[`westminster-standards-cli`](https://pypi.org/project/westminster-standards-cli/)
([source](https://github.com/normanormata/westminster_cli)), installed from
PyPI on first use (requires Python 3.9+ and [`uv`](https://docs.astral.sh/uv/)
or [`pipx`](https://pipx.pypa.io/)). Everything runs locally; the full corpus
is bundled with the CLI. Text derives from the OPC pages and documents linked
from <https://opc.org/confessions.html>; per the OPC preface, the 2025 MESV is
a study aid and carries no constitutional authority.
