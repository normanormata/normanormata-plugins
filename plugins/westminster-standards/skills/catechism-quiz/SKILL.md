---
name: catechism-quiz
description: Run a conversational catechism quiz. Use when the user asks to be quizzed, drilled, or tested on the Westminster Shorter or Larger Catechism, wants to practice or memorize catechism questions and answers, or says things like "quiz me on the catechism" or "test my Westminster Standards knowledge".
---

# Catechism quiz

Quiz the user on the Westminster catechisms in conversation, using the `ws`
command-line tool as the source of the official questions and answers. Never
invent or paraphrase catechism text from memory.

## Setup (first use only)

Health-check with `ws stats`. If the command is missing, install with
`uv tool install westminster-standards-cli` (install uv first via
`curl -LsSf https://astral.sh/uv/install.sh | sh` if needed, or use
`pipx install westminster-standards-cli`). If `ws` exists but errors, repair
with `uv tool install --force westminster-standards-cli`. If `ws stats`
succeeds, do nothing.

## Running a quiz

1. Determine the catechism and length. Default to the Shorter Catechism (`wsc`)
   and 5 questions unless the user says otherwise. Question ranges: `wsc` 1–107,
   `wlc` 1–196. If the user names a topic (e.g. "quiz me on the ten commandments"),
   find relevant question numbers first with `ws search`.
2. Pick distinct random question numbers in range. For each round:
   - Fetch the question: `ws wsc <n> -q` (or `ws wlc <n> -q`).
   - Present it as **Question k/N (WSC <n>)** and wait for the user's answer.
   - Fetch the official answer: `ws wsc <n> -a`.
   - Grade on substance, not wording: the catechism phrasing is exact, so credit
     any answer that captures the doctrine's key elements; say briefly what was
     missing when it falls short.
   - Always show the official answer verbatim after grading.
3. Keep a running score and end with `Score X / N`, mirroring the CLI's own quiz.
4. Offer follow-up study for missed questions: scripture proofs via
   `ws wsc <n> -p`, or the modern English rendering via `ws wsc <n> -m` if the
   archaic wording tripped the user up.

## Conduct

- One question at a time; never reveal the answer before the user responds.
- Let the user skip ("skip", "pass") without penalty — it doesn't count toward the score.
- Stop immediately when asked ("stop", "quit") and show the score for answered questions.
- Batch the two CLI calls for a round (`-q` and `-a`) in one shell invocation to stay fast,
  but only reveal the answer after the user has responded.
