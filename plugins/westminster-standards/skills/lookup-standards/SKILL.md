---
name: lookup-standards
description: Look up, quote, and cite the Westminster Standards. Use when the user asks what the Westminster Confession of Faith, Shorter Catechism, or Larger Catechism says about a topic; asks to show or quote WCF/WSC/WLC by reference (e.g. "show WSC 1", "WCF chapter 21", "Larger Catechism 45"); asks for the scripture proofs behind a catechism answer or confession section; or wants the modern English rendering (2025 MESV) or a comparison of the constitutional and modern texts.
---

# Look up the Westminster Standards

Answer questions about the Westminster Standards by running the `ws` command-line tool and quoting its output. Never answer from memory — the corpus is the source of truth.

## Setup and capability check

Before the first lookup, run both `ws stats` and
`ws search --regex '(?!)'`. The second command intentionally returns no matches
and verifies regex support. If both commands succeed, continue without changing
the environment.

If either command is missing or fails:

1. Explain that `westminster-standards-cli` is missing or incompatible. Ask for
   explicit permission before running any install or repair command.
2. When available, inspect `uv tool list` and `pipx list --short`. Prefer the
   package manager that already lists `westminster-standards-cli`; otherwise
   prefer `uv`, then `pipx`.
3. Show the exact command before asking. Use
   `uv tool install westminster-standards-cli` or
   `pipx install westminster-standards-cli` when missing, adding `--force` when
   repairing an incompatible install. These commands install the latest release.
4. If neither package manager exists, ask separately before installing one and
   provide its official installation instructions. Do not combine package-manager
   installation and CLI installation without telling the user about both changes.
5. After approval and installation, rerun both capability checks. If either still
   fails, report the failure and stop; never substitute an answer from memory.

See `references/cli-reference.md` for additional troubleshooting.

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
