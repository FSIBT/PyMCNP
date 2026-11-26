# Using PyMCNP with AI Agents

PyMCNP ships a skill file, [`SKILL.md`](https://github.com/FSIBT/PyMCNP/blob/main/SKILL.md), for AI coding agents such as
[Claude Code](https://claude.com/claude-code). It is a short Markdown file that tells an agent how to use PyMCNP well:

- the parsing contract: every parser returns `(object, remainder)`, and a non-empty remainder means part of the file was not read;
- the API for building, scanning, checking and running inputs, and for reading OUTP, MESHTAL and PTRAC files;
- the common pitfalls, e.g., PTRAC files that do not fit in memory, PTRAC options that leave out the values you need,
  and OUTP tallies PyMCNP cannot parse yet;
- what to do when PyMCNP fails on a valid MCNP file: draft a GitHub issue with a minimal input instead of working around it.

With the skill installed, an agent can write, scan, run and plot MCNP models from a short description. The
[automation example](examples/automate.md), 441 iron discs over a rough concrete floor with a flux plot, was created
this way from a short prompt.

## Installing the Skill for Claude Code

Claude Code looks for skills in a folder named after the skill that holds a `SKILL.md` file:

| Scope | Location | Used in |
|---|---|---|
| Personal | `~/.claude/skills/pymcnp/SKILL.md` | all your projects on this machine |
| Project | `.claude/skills/pymcnp/SKILL.md` in the project | sessions in that project; commit it to share it with your team |

`SKILL.md` is not part of the installed Python package, so download it from GitHub. It exists from PyMCNP 1.0.0 on: for an older version the download fails with a 404, so upgrade first. Take the version that matches your
installed PyMCNP, since the skill describes that version's API; `pymcnp --version` prints it, also for `uv tool` and
`pipx` installs. For a personal install:

    v=$(pymcnp --version | cut -d' ' -f2)
    mkdir -p ~/.claude/skills/pymcnp
    curl -fsSL "https://raw.githubusercontent.com/FSIBT/PyMCNP/v$v/SKILL.md" -o ~/.claude/skills/pymcnp/SKILL.md

For a project install, run the same commands from the project's root directory with `.claude/skills/pymcnp` in place of
`~/.claude/skills/pymcnp`. If you installed PyMCNP from GitHub rather than from a release, the version has no tag: use
`main` in place of `v$v`, or copy `SKILL.md` from your clone of the repository.

To check that Claude Code found the skill, run `/skills` in a session, or ask "What does the pymcnp skill say about
PTRAC files?". Claude Code picks up a new skill in a running session; if it does not show up, run `/reload-skills` or
start a new session. The skill loads by itself when a task involves MCNP files, and `/pymcnp` loads it explicitly.

When you upgrade PyMCNP, download the skill again with the same commands, so that the agent does not use a stale API.

## Other Agents

`SKILL.md` is plain Markdown with a short YAML header (`name` and `description`), so any agent can use it:

- Agents that support the Agent Skills format read the same `pymcnp/SKILL.md` folder; see your agent's documentation for
  where it looks for skills.
- Agents that read an `AGENTS.md` file (or a similar rules file) in the project: save `SKILL.md` in the project, e.g., as
  `docs/pymcnp-skill.md`, and add a line such as "Before writing code that uses PyMCNP or MCNP files, read
  `docs/pymcnp-skill.md` and follow it."
- Otherwise, attach the file or paste its text into the conversation before you ask for MCNP work.

## What to Ask

Describe the goal, the files, and what you want back. For example:

- "Read `model.inp`, scan the radius of surface 99 from 500 to 700 cm in steps of 50, and write one input per radius.
  Run them with `mcnp6` four at a time and plot tally 1 of every run in one figure."
- "`ptrac` is a 20 GB PTRAC file from a run with `EVENT=SRC,BNK,SUR,COL,TER`. Write the photons entering cell 3 through
  surface 3 to a parquet file, with the nuclide each photon came from."
- "Check `deck.inp` with `pymcnp check`, fix the lines that are too long, and tell me about any card PyMCNP cannot
  parse."

## Reviewing the Results

An agent can make mistakes that still give a valid MCNP input, so check its work:

- Look at the geometry (`pymcnp visualize`, or `Visualize().to_show_cells(inp)`) before running a model.
- Check `outp.summary.ok` and `outp.summary.checks_passed` before trusting a tally, and read the warnings PyMCNP issues.
- Do not send export-controlled or otherwise sensitive inputs to a hosted model, and follow your MCNP licence.

## The Skill File

```{include} ../../SKILL.md
:start-line: 6
:heading-offset: 1
```
