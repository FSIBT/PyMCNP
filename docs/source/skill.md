# Skill File

PyMCNP ships a [skill file](https://github.com/FSIBT/PyMCNP/blob/main/SKILL.md) (`SKILL.md`) that describes the API, the parsing contract, and the common pitfalls to an AI coding agent such as [Claude Code](https://claude.com/claude-code).
With the skill installed (for Claude Code, copy it to `~/.claude/skills/pymcnp/SKILL.md`), an agent can write, scan, run, and plot MCNP models for you from a short description, so automating MCNP becomes easy even for complex geometries.
The example above was created this way from a short prompt.

Always review generated models and results before relying on them.

```{eval-rst}
.. literalinclude:: ../../skill.md
   :language: markdown
```
