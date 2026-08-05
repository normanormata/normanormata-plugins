---
name: catechism-quiz
description: Run a conversational catechism quiz. Use when the user asks to be quizzed, drilled, or tested on the Westminster Shorter or Larger Catechism, wants to practice or memorize catechism questions and answers, or says things like "quiz me on the catechism" or "test my Westminster Standards knowledge".
---

# Catechism quiz

Quiz the user on the Westminster catechisms in conversation, using the `ws`
command-line tool as the source of the official questions and answers. Never
invent or paraphrase catechism text from memory.

## Setup and capability check

Before the first quiz, run both `ws stats` and `ws wsc 1 -q`. If both commands
succeed, continue without changing the environment.

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
   fails, report the failure and stop; never invent questions or answers from memory.

## Running a quiz

1. Determine the catechism and answer target. Default to the Shorter Catechism
   (`wsc`) and 5 answered questions unless the user says otherwise. Question
   ranges: `wsc` 1–107, `wlc` 1–196. If the user names a topic (e.g. "quiz me on
   the ten commandments"), find relevant question numbers first with `ws search`.
2. Track correct, answered, skipped, and every question number already used.
   Pick a distinct unused question for each round. Then:
   - Fetch its official question and answer in one shell invocation with
     `ws wsc <n> -q && ws wsc <n> -a` (or the equivalent `wlc` commands).
   - Retain the answer privately. Present only the question as
     **Question {answered + 1}/{target} (WSC <n>)** and wait for the user's
     response. Substitute the counters and selected reference; do not print the
     braces or expression literally.
   - Grade on substance, not wording: the catechism phrasing is exact, so credit
     any answer that captures the doctrine's key elements; say briefly what was
     missing when it falls short.
   - Show the official answer verbatim after grading, then increment answered.
   - For "skip" or "pass", do not grade or increment answered. Show the official
     answer, increment skipped, and continue with a new unused question.
3. Continue until answered reaches the target. If the unused pool is exhausted,
   stop and explain why. End with `Score X / Y answered` and `Skipped Z`; at
   normal completion, Y equals the target.
4. Offer follow-up study for missed questions: scripture proofs via
   `ws wsc <n> -p`, or the modern English rendering via `ws wsc <n> -m` if the
   archaic wording tripped the user up.

## Conduct

- One question at a time; never reveal the answer before the user responds.
- Let the user skip without penalty; a skipped question does not consume one of
  the requested answered questions.
- Stop immediately when asked ("stop", "quit"). Report the score using answered
  questions as the denominator and include the skipped count, even if both are zero.
