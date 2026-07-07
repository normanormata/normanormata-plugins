# ws CLI reference

`ws` (also installed as `westminster` and `wsc`) reads the Orthodox Presbyterian
Church constitutional text of the Westminster Standards, bundled with scripture
proof references and the 2025 Modern English Study Version (MESV).

## Documents and reference ranges

| Id | Document | References |
|----|----------|------------|
| `wcf` | Westminster Confession of Faith | chapters `1`–`33`; sections like `1.1`, `10.3` |
| `wlc` | Westminster Larger Catechism | questions `1`–`196` |
| `wsc` | Westminster Shorter Catechism | questions `1`–`107` |

## Reading commands

```sh
ws wsc 1              # Shorter Catechism Q&A 1
ws wlc 45             # Larger Catechism Q&A 45
ws wcf 1.4            # Confession chapter 1, section 4
ws wcf 21             # Whole chapter 21 (all sections)
ws show wsc 1         # Explicit form, same output
```

Flags (combine freely unless noted):

| Flag | Effect | Valid on |
|------|--------|----------|
| `-q` / `--question` | print only the question | catechism entries |
| `-a` / `--answer` | print only the answer | catechism entries |
| `-p` / `--proofs` | append lettered scripture proof references (OPC printed edition letters) | all entries and chapters |
| `-m` / `--mesv` | show the 2025 Modern English Study Version text | all entries and chapters |
| `--compare` | show constitutional and MESV texts stacked | all entries and chapters; mutually exclusive with `-m` |

Notes:

- `-q`/`-a` on a confession reference exits 1 with an error.
- WLC 188 has no scripture proofs in the printed edition; `-p` shows none there.
- The MESV is a study aid; the OPC preface states it carries no constitutional authority.

## Search and discovery

```sh
ws search "chief end"     # AND-of-terms across all documents (not phrase search)
ws list                   # the three documents with entry counts
ws list wsc               # every entry in a document (ref + first line)
ws stats                  # corpus counts
ws sources                # OPC source pages
```

Search matches entries containing **all** terms, case-insensitively, anywhere in
the entry (including its reference and document name). Prefer distinctive terms;
broaden by removing terms if nothing matches.

## Sample outputs (piped — plain text, no color, no pager)

`ws wsc 1 -p`:

```
WSC · 1   Westminster Shorter Catechism
──────────────────────────────────────────────────────

Q. What is the chief end of man?

A. Man's chief end is to glorify God, and to enjoy him forever.

Scripture Proofs
  a. Ps. 86:9; Isa. 60:21; Rom. 11:36; 1 Cor. 6:20; 1 Cor. 10:31; Rev. 4:11
  b. Ps. 16:5-11; Ps. 144:15; Isa. 12:2; Luke 2:10; Phil. 4:4; Rev. 21:3-4
```

`ws wsc 1 -q` prints just: `What is the chief end of man?`

`ws search "effectual calling"` prints a match count then `DOC ref  preview` lines.

## Install and troubleshooting

Preferred install (any macOS/Linux machine with Python 3.9+):

```sh
uv tool install westminster-standards-cli
```

- No `uv`? Install it first: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  (then ensure `~/.local/bin` is on PATH), or use `pipx install westminster-standards-cli`.
- `ws` not found after install: `uv tool update-shell` or add `~/.local/bin` to PATH.
- Upgrade: `uv tool upgrade westminster-standards-cli`.
- The package bundles the full corpus — no network access is needed at runtime.
- Exit codes: 0 success, 1 lookup/validation error (message on stderr), 2 usage error.
