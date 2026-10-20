---
title: 'PyMCNP'
tags:
  - Python
  - MCNP
authors:
  - given-names: Devin
    surname: Pease
    orcid: 0009-0006-1387-1640
    affiliation: "1, 2"
  - given-names: Mauricio
    surname: Ayllon Unzueta
    orcid: 0000-0001-7109-169X
    affiliation: "1"
  - given-names: Arun
    surname: Persaud
    orcid: 0000-0003-3186-8358
    affiliation: "1"
affiliations:
 - name: Accelerator Technology & Applied Physics Division. Lawrence Berkeley National Laboratory, CA 94720, United States
   index: 1
 - name: University of Arizona, United States
   index: 2
date: 14 October 2026
bibliography: paper.bib
---

# Summary

PyMCNP provides object-oriented, Pythonic tooling for the Monte Carlo
N-Particle (MCNP) code [@Kulesza:2022, @Werner:2017]. MCNP uses custom input
and output file formats, leading researchers to rely on labor-intensive manual
editing or fragile text-manipulation scripts. PyMCNP, an open-source Python
package and command-line interface (CLI), helps overcome these challenges by
providing parsers for MCNP’s input (INP), particle track output(PTRAC), output
(OUTP), and mesh tally (MESHTAL) files and utilities for common MCNP workflows,
including checking input files, converting tally formats, plotting tallies,
running simulations in parallel, and visualizing cell and surface geometries
using PyVista [@pyvista]. Although PyMCNP does not fully support all MCNP
syntax, it lets researchers programmatically create, load, read, write, modify,
and validate MCNP cards, options, blocks, and files by packaging more than 1000
classes with near-full support for MCNP versions 6.2 and 6.3. By providing a
comprehensive interface, PyMCNP streamlines workflows, prevents costly errors,
and lowers the barrier to using MCNP effectively and efficiently.

# Statement of Need

From scanning parameters and tuning geometries to validating models and running
sensitivity analyses, MCNP requires labor-intensive manual editing or fragile
text-manipulation scripts to check input files, convert tally formats, plot
tallies, run simulations in parallel, and visualize cell and surface
geometries. PyMCNP’s object-oriented, Pythonic interface rewrites these
workflows as simple Python scripts. For instance, PyMCNP turns creating input
files with varying material specifications from manual editing or one-off
scripts into for loops with assignments. Similarly, the Python package turns
extracting specific tallies from output files into function calls, replacing
complex scripts that parse specific, inconsistent OUTP blocks. MCNP’s file
format limits researchers to either time-consuming manual workflows or
unsharable parsing scripts.

Existing open-source MCNP tools address some of these complications; however,
they do not address them comprehensively. Some packages parse input files but
lack output analysis; others parse output files but cannot create or validate
inputs; and many lack visualization and plotting utilities. Moreover, most
parsers only partially parse MCNP’s extensive syntax and validate against its
semantic restrictions. To our knowledge, none provide integrated tooling across
the full simulation workflow, including input creation, visualization, and
execution, and output parsing, analysis, and plotting.

# State of the Field

Existing open-source tools provide programmatic access to MCNP files. However,
each tool focuses on specific file formats or use cases, leaving the
comprehensive workflow unsupported. PyMCNP addresses this by providing a
consistent interface for MCNP input and output files and a CLI that automates
basic workflows, including utilities for preparing, executing, and analyzing
simulations.

MontePy [@montepy] parses, edits, and writes MCNP input files using an
object-oriented interface. It uses generic classes for many of MCNP’s data
cards, so validation is limited to generic syntax checks rather than
card-specific requirements. MCNP-GO [@mcnpgo] and numjuggler
[@numjuggler] manipulate input via pattern matching and regular expressions,
which works for simple edits but lacks the context-free validation needed for
complex file generation. Moreover, to our knowledge at the time of publication,
none of these tools validate every card during reading, modification, and
writing.

MCNPTools [@Bates:2022], developed at Los Alamos National Laboratory, provides
parsers for MESHTAL, PTRAC, and other output formats but does not handle INP or
OUTP files. The MCNP module of PyNE [@pyne] likewise reads MESHTAL, PTRAC, and
several other MCNP files, and can read materials from input files, but it does
not include a full input file parser or writer. Conversely, the input-focused
tools (MontePy, MCNP-GO, numjuggler) do not parse output files, so users may
need to combine multiple packages or write custom scripts.

PyMCNP combines these approaches by providing validated parsing for input
(INP) and output (PTRAC, MESHTAL, OUTP) formats through an object-oriented,
Pythonic interface. PyMCNP implements context-free recursive-descent parsers
for a large set of cards, options, blocks, and files. The package checks many
restrictions described in the MCNP manual and reports unsupported syntax rather
than silently dropping or handling it. PyMCNP extends these parsers with
utilities that automate workflows for checking, converting, plotting, running,
and visualizing MCNP files. PyMCNP reduces the need to combine multiple tools
and supports streamlined, reproducible MCNP workflows.

# Software Design

PyMCNP’s architecture addresses MCNP’s complex, context-dependent syntax and
numerous semantic restrictions by implementing parsers that follow
object-oriented design principles through Pythonic design, base classes, and
encapsulation.

PyMCNP injects recursive-descent parsers into dedicated classes for each card,
option, and block. Each class represents supported nonterminal symbols; for
example, `pymcnp.inp.card.M` encodes material cards and `pymcnp.inp.card.Sdef`
represents source cards. Each class specifies the syntax of the nonterminal it
represents and checks pertinent semantic restrictions. To enable duck typing,
abstract syntax tree classes universally implement the `from_mcnp` and
`to_mcnp` methods as inverses, which read and write MCNP, respectively. This
isomorphism and the polymorphism it induces help PyMCNP handle edge cases that
break pattern-matching or regular-expression approaches.

PyMCNP then simplifies these classes by constructing deep hierarchies of
abstract base classes extensively for static type checking and Pythonic duck
typing. For example, all INP cards, including the class for source cards
`pymcnp.inp.card.Sdef` and the class for material cards `pymcnp.inp.card.M`,
inherit from the base class for all cards `pymcnp.inp.Card`. PyMCNP then treats
these base classes as alternations, dispatching between forms to support
multi-form cards, options, and blocks, such as INP tally cards or PTRAC
blocks.

Building on these classes, PyMCNP implements dunder methods to make classes more
ergonomic and Pythonic. For instance, the `pymcnp.inp.literal.Geometry` class,
which represents cell geometry formulas, implements
`pymcnp.inp.literal.Geometry.__and__`. So, researchers can combine cell
formulas in Python using the same boolean logic as in MCNP. Similarly, PyMCNP
breaks down utilities such as parallel simulation and PTRAC filtering into
overridable classes, namely `pymcnp.Run` and `pymcnp.PtracFilter` for easy
reuse.

PyMCNP relies on encapsulation to keep files, cards, options, and blocks valid.
PyMCNP’s abstract syntax tree classes validate values whenever they are set by
using properties extensively. As a result, PyMCNP objects remain correct
throughout the read-modify-write process. For instance, when loading or
modifying box surface cards, PyMCNP always checks that the box vectors are
orthogonal, enforcing the semantic restriction specified in the manual. The
library prevents common mistakes early, rather than at simulation time. PyMCNP
provides an ergonomic, Pythonic, and object-oriented interface for MCNP files
and tooling, simplifying workflows.

# Research Impact Statement

PyMCNP streamlines MCNP workflows. For example, by combining the interface with
simple Python loops that generate inputs, researchers can calculate optimal
shielding thicknesses for radiation protection and tune detector geometries for
maximum sensitivity using reusable, shareable scripts. They can then produce
publication-ready plots, run simulations in parallel, and parse results using
PyMCNP's CLI or utility classes.

Because MCNP requires explicit isotopic composition for all materials,
material-study input files require cumbersome definitions. With PyMCNP,
however, researchers can automate file generation for their parameter scan. For
instance, investigators can model soil with varying water content or concrete
with different aggregate compositions. Alternatively, they can simulate
biological tissue with patient-specific densities by using from_formula to
generate material cards directly from chemical formulas. So, PyMCNP simplifies
sensitivity studies by automating manual isotope tabulation.

Early validation of input files can catch costly errors before they run costly,
lengthy, or incorrect simulations. PyMCNP’s geometry visualization lets
researchers verify complex shielding configurations, detector arrangements, or
phantom geometries before committing costly computational resources to
potentially flawed simulations. Similarly, PyMCNP’s syntax and semantic
validation catches simple, easy-to-miss mistakes before researchers spend
resources on erroneous simulations. For large-scale studies on shared computing
clusters where failed simulations waste limited allocation time, PyMCNP saves
significant resources by failing incorrect files early.

By providing Pythonic, object-oriented tooling for MCNP, PyMCNP lowers the
barrier to entry for fields increasingly reliant on Monte Carlo methods,
including medical physics, nuclear engineering, radiation protection, and
detector development.

# AI Usage Disclosure

Large language models were used for review, editing, and fixes for versions
0.10.0 and 1.0.0. Versions 0.9.0, 0.7.0, 0.2.0, and 0.1.0 did not use large
language models. PyMCNP was largely developed, drafted, and designed without
large language models.
