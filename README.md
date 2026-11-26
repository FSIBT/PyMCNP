[![Documentation Status](https://readthedocs.org/projects/pymcnp/badge/?version=latest)](https://pymcnp.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pymcnp.svg)](https://badge.fury.io/py/pymcnp)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# PyMCNP

PyMCNP supports running [Monte Carlo N-Particle (MCNP) simulations](https://mcnp.lanl.gov/). It parses MCNP files, enabling automation such as parameter scans, creates MCNP geometry visualization using [pyvista](https://pyvista.org). PyMCNP provides a Python API for MCNP input and output files and a command line interface for interacting with MCNP and MCNP files.

Find more information on [ReadTheDocs](https://pymcnp.readthedocs.io).

## Installation

PyMCNP is available on [PyPI](https://pypi.org/project/pymcnp/) and can be "pip installed":

    pip install pymcnp

PyMCNP supports MCNP 6.1 to 6.3 and Python 3.11 to 3.15. MCNP itself is not included: get it from [RSICC](https://rsicc.ornl.gov). `pymcnp run` starts it as `mcnp6` from your `PATH` (`-c` names another command), and MCNP finds its nuclear data through `DATAPATH`. Everything except running MCNP works without it.

PyMCNP reads MCNP input files (INP), output files (OUTP), mesh tally files (MESHTAL), and ASCII particle track files (PTRAC, written with `PTRAC FILE=ASC`). It does not read MCTAL files or binary PTRAC files.

New to PyMCNP? [Getting Started](https://pymcnp.readthedocs.io/en/latest/getting_started.html) walks through checking, editing, visualizing, and running an input and reading its results.

## Example

Read an input file, scan the radius of a sphere, and write one input file per radius; then read the output of a run:

```python
import pymcnp

inp, rest = pymcnp.Inp.from_file('example_00.inp')
assert rest == ''  # The remainder is the text PyMCNP could not parse.
for i, copy in enumerate(inp.scan_with([500, 600, 700], lambda inp, r: setattr(inp.surface_cards(99)[0], 'r', r))):
    copy.to_file(f'sphere-{i}.inp')

outp, _ = pymcnp.Outp.from_file('example_00.outp')
print(outp.summary.ok, outp.summary.checks_passed)  # Did MCNP finish, and did the tallies pass the statistical checks?
print(outp.tally(1))  # Tally 1 as a pandas dataframe
```

The command line interface checks, runs, converts, plots, and visualizes MCNP files, e.g.:

    pymcnp check example_00.inp
    pymcnp run --command=mcnp6 sphere-*.inp
    pymcnp convert outp --csv example_00.outp
    pymcnp visualize example_00.inp

The files are in the [examples](https://github.com/FSIBT/PyMCNP/tree/main/examples) directory, which has many more examples.

## Automation with AI Coding Agents

PyMCNP ships a skill file, [SKILL.md](https://github.com/FSIBT/PyMCNP/blob/main/SKILL.md), that describes the API, the parsing contract, and the common pitfalls to an AI coding agent such as [Claude Code](https://claude.com/claude-code).
With the skill installed, an agent can write, scan, run, and plot MCNP models for you from a short description, so automating MCNP becomes easy even for complex geometries.
For Claude Code, save it as `~/.claude/skills/pymcnp/SKILL.md` (all your projects) or `.claude/skills/pymcnp/SKILL.md` (one project), taking the version that matches your installed PyMCNP:

    v=$(pymcnp --version | cut -d' ' -f2)
    mkdir -p ~/.claude/skills/pymcnp
    curl -fsSL "https://raw.githubusercontent.com/FSIBT/PyMCNP/v$v/SKILL.md" -o ~/.claude/skills/pymcnp/SKILL.md

[Using PyMCNP with AI agents](https://pymcnp.readthedocs.io/en/latest/skill.html) explains how to check that it loaded, how to use it with other agents, and what to ask.
The [example](https://pymcnp.readthedocs.io/en/latest/examples/automate.html) on ReadTheDocs, 441 iron discs over a rough concrete floor with a flux plot, was created this way from a short prompt.
Always review generated models and results before relying on them.

## Contributing

PyMCNP welcomes contributions, including issues, pull requests, and MCNP files that PyMCNP fails to parse or visualize.

For more information, see the [CONTRIBUTING.md](https://github.com/FSIBT/PyMCNP/blob/main/CONTRIBUTING.md) file.

## Copyright and License

For copyright and license information, see the [COPYRIGHT](https://github.com/FSIBT/PyMCNP/blob/main/COPYRIGHT) and [LICENSE](https://github.com/FSIBT/PyMCNP/blob/main/LICENSE) files.
