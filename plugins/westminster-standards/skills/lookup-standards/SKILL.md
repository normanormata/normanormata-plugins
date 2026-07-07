---
name: lookup-standards
description: Look up, quote, and cite the Westminster Standards. Use when the user asks what the Westminster Confession of Faith, Shorter Catechism, or Larger Catechism says about a topic; asks to show or quote WCF/WSC/WLC by reference (e.g. "show WSC 1", "WCF chapter 21", "Larger Catechism 45"); asks for the scripture proofs behind a catechism answer or confession section; or wants the modern English rendering (2025 MESV) or a comparison of the constitutional and modern texts.
---

# Look up the Westminster Standards

Answer questions about the Westminster Standards by running the `ws` command-line tool and quoting its output. Never answer from memory — the corpus is the source of truth.

## Setup (first use only)

Health-check with `ws stats` (not just `command -v ws` — a stale install can
exist but fail):

- Command missing: `uv tool install westminster-standards-cli`. If `uv` is
  missing, install it first (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
  or use `pipx install westminster-standards-cli`.
- Command present but erroring: `uv tool install --force westminster-standards-cli`.
- `ws stats` succeeds: do nothing.

See `references/cli-reference.md` for troubleshooting.

## Commands

| Task | Command |
|------|---------|
| Search by topic | `ws search "chief end"` — matches entries containing ALL terms (not a phrase) |
| Regex search | `ws search --regex "bapti[sz]ed?"` — case-insensitive regular expression |
| Shorter Catechism Q&A | `ws wsc 1` (questions 1–107) |
| Larger Catechism Q&A | `ws wlc 1` (questions 1–196) |
| Confession section | `ws wcf 1.4` (chapters 1–33) |
| Whole confession chapter | `ws wcf 21` |
| Question or answer only | add `-q` or `-a` (catechisms only) |
| Scripture proofs | add `-p` — lettered proof references matching the printed OPC edition |
| Modern English (2025 MESV) | add `-m` |
| Both editions together | add `--compare` (cannot combine with `-m`) |
| List documents / entries | `ws list`, `ws list wsc` |

Flags combine: `ws wsc 1 -a -p` prints the answer plus proofs; `ws wlc 45 -q -m` prints the modern question only. Output is plain text when piped (no pager, no color codes) — use it directly.

Full command matrix, reference ranges, and sample outputs: `references/cli-reference.md`.

## Answer conventions

- Quote the standards **verbatim** — do not paraphrase quoted text.
- Always cite the reference (e.g., WSC 1, WCF 1.4, WLC 45).
- When the user names a topic rather than a reference, run `ws search` first, then show the most relevant entries in full.
- Offer scripture proofs (`-p`) when the user is studying a doctrine, and the MESV (`-m`) when the archaic language is a barrier.
- When quoting the MESV, note it is a study version with no constitutional authority in the OPC.
- `ws search` uses AND-of-terms matching: prefer two or three distinctive words; if a search returns nothing, retry with fewer or different terms, or use `--regex` for word variants (`justif(y|ication)`, `bapti[sz]`).
