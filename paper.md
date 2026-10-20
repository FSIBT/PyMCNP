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

PyMCNP provides object-oriented, pythonic tooling for the Monte Carlo
N-Particle (MCNP) code [@Kulesza:2022]. MCNP uses custom text-based
file formats for input and output that are difficult to parse and
manipulate programmatically. As an open-source Python package and
command line interface (CLI), PyMCNP addresses this challenge by
providing parsers for MCNP's input (INP), particle track output
(PTRAC), output (OUTP), and mesh tally (MESHTAL) files. MCNP has a
very large number of cards and options, and although PyMCNP does not
cover all of them yet, it supports a large fraction; it has been
tested mainly with MCNP 6.1, and testing with MCNP 6.3 has
started. Input that PyMCNP cannot parse is reported by the command
line interface. The package enables users to load, validate, and
programmatically create or modify MCNP files through an
object-oriented Python API. PyMCNP also provides CLI tools for common
workflows including parallel simulation execution, output parsing and
plotting, file format conversion, and 3D visualization of simulation
geometry using PyVista [@pyvista]. By integrating MCNP into the Python
ecosystem, PyMCNP enables automated parameter scans, streamlined data
analysis, and simplified validation workflows that would be cumbersome
using MCNP's native file formats alone.

# Statement of Need

MCNP simulations often require iterative workflows: scanning
parameters to optimize shielding designs, validating models against
experimental data, or performing sensitivity analyses across multiple
configurations. However, MCNP's custom text-based file formats make
these workflows cumbersome. Creating input files with varying
parameters requires manual editing or fragile text manipulation
scripts. Extracting specific tallies from output files for plotting or
statistical analysis involves parsing complex, inconsistent ASCII
tables. Validating geometry before running lengthy simulations is
difficult without proper tooling. These limitations force researchers
to choose between time-consuming manual workflows or developing
one-off parsing scripts that are difficult to maintain and share.

Existing open-source MCNP tools address some of these challenges but
remain fragmented. Some packages provide input file parsing without
output analysis capabilities; others parse output files but cannot
generate or validate inputs. Most validate only part of MCNP's
extensive syntax, and, to our knowledge, none provide integrated
tooling across the full simulation workflow—from input generation and
validation through geometry visualization to output analysis and
plotting.

PyMCNP addresses these gaps by providing a unified Python interface
for MCNP's input and output formats alongside workflow automation
tools.  By bringing MCNP into the Python ecosystem, PyMCNP enables
researchers to automate parameter studies using standard loops and
conditionals, leverage scientific Python libraries (NumPy, Pandas,
Matplotlib) for analysis, validate complex geometries before
simulation, and share reproducible workflows as Python scripts. This
integration transforms MCNP from a standalone tool into a programmable
component of modern computational physics workflows.

# State of the Field

Several open-source tools provide programmatic access to MCNP files,
but each focuses on specific file formats or use cases, leaving gaps
in the overall workflow.

Input file handling: MontePy [@montepy] parses, edits, and writes MCNP
input files using an object-oriented interface. It uses generic
classes for many of MCNP's data cards, so validation of those cards is
limited to generic syntax checks rather than card-specific
requirements. MCNP-GO [@mcnpgo] and numjuggler [@numjuggler] provide
input manipulation through pattern matching and regular expressions,
which is effective for simple edits but lacks the structured
validation needed for complex file generation. To our knowledge, none
of these tools validate every card during both reading and writing.

Output file parsing: MCNPTools [@Bates:2022], developed at Los Alamos
National Laboratory, provides parsers for MESHTAL, PTRAC, and other
output formats but does not handle input files or the text-based OUTP
tables commonly used for tally analysis. The MCNP module of PyNE
[@pyne] likewise reads MESHTAL, PTRAC, and several other MCNP files,
and can read materials from input files, but it is not an input file
parser or writer. Conversely, the input-focused tools (MontePy,
MCNP-GO, numjuggler) do not parse output files, so users may need to
combine multiple packages or write custom parsers for end-to-end
workflows.

Integration and validation: To our knowledge, no existing tool
combines card-specific input validation with output parsing in a
single package. This fragmentation complicates workflows that require
generating inputs, running simulations, and analyzing results
programmatically.  Additionally, geometry visualization capabilities
are either absent or limited in current tools.

PyMCNP addresses these gaps by providing validated parsing of the
supported cards and tables for both input (INP) and output (PTRAC,
MESHTAL, OUTP) formats through a unified object-oriented
interface. PyMCNP implements context-free recursive-descent parsing
with card-specific validation classes for a large and growing set of
MCNP cards, and checks many of the restrictions described in the MCNP
manual. Cards and options that are not yet supported are reported
rather than silently dropped. By integrating input generation,
validation, geometry visualization, and output analysis in one
package, PyMCNP reduces the need to combine multiple tools and
supports streamlined, reproducible MCNP workflows.

# Software Design

PyMCNP's design addresses two key challenges: parsing MCNP's complex,
context-dependent syntax and validating user-generated files against
the restrictions PyMCNP knows about.

Parsing strategy: MCNP input files use inconsistent syntax across
different card types, with context-dependent keywords and optional
parameters. PyMCNP implements a recursive-descent parser that handles
this complexity through card-specific parsing logic. Each supported
MCNP card is represented by a dedicated class (e.g., pymcnp.inp.M for
materials, pymcnp.inp.So for sources) that knows how to parse and
validate its specific syntax. This approach helps PyMCNP handle edge
cases and variations that would break pattern-matching or regular
expression approaches.

Validation and correctness: PyMCNP validates MCNP syntax at both read
and write time. When loading existing files, the parser checks
card-specific requirements—for example, verifying that the vectors
defining a BOX surface are orthogonal. When constructing files
programmatically, classes validate parameters as they are set, making
it harder to create invalid files. These checks catch many common
mistakes, but they do not replace running MCNP, which remains the
final authority on whether an input is valid.

Consistent API: All file format parsers (pymcnp.Inp, pymcnp.Ptrac,
pymcnp.Meshtal, pymcnp.Outp) provide from_mcnp() and to_mcnp() methods
for reading and writing files. This consistency simplifies workflows
that process multiple file types. For example, a parameter scan script
follows the same pattern whether modifying input geometry or parsing
output tallies.

Pythonic interface: PyMCNP represents MCNP constructs using Python
idioms. Cell geometry, normally specified with boolean operators in
MCNP syntax (e.g., 1 -2 3), can be constructed using Python's & and |
operators: surface1 & ~surface2 & surface3. This allows users familiar
with Python to work with MCNP concepts naturally while maintaining the
underlying MCNP semantics.

The result is a library where common tasks—loading a file, modifying
parameters, validating geometry, writing output—require minimal code
while catching many common mistakes early. This design philosophy
prioritizes user productivity and error prevention over flexibility
that could produce invalid MCNP files.

PyMCNP's design follows object oriented design principles by
emphasizing: abstraction, inheritance, polymorphism, and
encapsulation. PyMCNP abstracts INP, PTRAC, OUTP, and MESHTAL
nonterminals and utilities into Pythonic classes. For example, the
`pymcnp.types.Geometry` class represents INP cell card geometry
formula and implements dunder methods, such as
`pymcnp.types.Geometry.__and__` to provide a Pythonic interface for
MCNP. Similarly, PyMCNP breaks down utilities, such as parallel
simulation running and PTRAC filtering, into classes, namely
`pymcnp.Run` and `pymcnp.FilterPtrac`. The Python package `pymcnp`
integrates these abstractions into a coherent system by creating a
hierarchy of classes. Every class in PyMCNP builds on layers of
abstract base classes, enabling sophisticated type hinting, consistent
overriding, and Pythonic duck typing. For example, all INP cards,
including `pymcnp.inp.So` and `pymcnp.inp.M`, inherit from
`pymcnp.inp.Card` base class. Moreover, PyMCNP supports nonterminals
with different variations, e.g., INP cards or PTRAC blocks with
multiple forms, by providing superclasses that dispatch between
specific variations, simplifying parsing. The abstract base classes at
the center of the PyMCNP library support polymorphism and duck typing
by providing a common interface for working with INP, PTRAC, OUTP, and
MESHTAL nonterminals, streamlining the PyMCNP workflow. For instance,
the parser subpackages, namely `pymcnp.inp`, `pymcnp.ptrac`,
`pymcnp.outp`, and `pymcnp.meshtal`, all implement the `from_mcnp` and
`to_mcnp` methods which read and write MCNP, respectively. Finally,
PyMCNP leverages encapsulation to keep objects consistent with the
checks it implements. PyMCNP's abstract syntax tree classes hide their
internal state and validate new values whenever set, so objects stay
consistent with those checks after they are modified. For example,
when setting or initializing the vectors of an INP `BOX` surface card,
PyMCNP checks that they are orthogonal, enforcing the restriction
outlined in the manual. By emphasizing on abstraction, inheritance,
polymorphism, and encapsulation, PyMCNP provides an ergonomic,
Pythonic, and object-oriented interface for MCNP files and tooling
that simplifies user workflows.

# Research Impact Statement

PyMCNP makes computational physics workflows easier than they are with
MCNP's native file formats alone. Parameter optimization studies—such
as determining optimal shielding thickness for radiation protection or
tuning detector geometries for maximum sensitivity—can now be
automated through simple Python loops that generate inputs, execute
simulations in parallel, parse results, and produce publication-ready
plots. What previously required manual file editing and ad-hoc parsing
scripts for each study becomes a reusable, shareable Python script.

The package particularly impacts workflows involving complex
materials. MCNP requires explicit isotopic composition for all
materials, making it cumbersome to model materials with variable
properties (soil with varying water content, concrete with different
aggregate compositions, biological tissue with patient-specific
densities). With PyMCNP, researchers can define Python functions that
generate material cards from high-level parameters, enabling
sensitivity studies across material variations without manual isotope
tabulation.

Early validation can catch costly errors before simulation. PyMCNP's
geometry visualization allows researchers to visually verify complex
shielding configurations, detector arrangements, or phantom geometries
before committing computational resources to potentially flawed
simulations. This is particularly valuable for large-scale studies on
shared computing clusters where failed simulations waste limited
allocation time.

By integrating MCNP into the Python scientific computing ecosystem,
PyMCNP makes Monte Carlo particle transport accessible to researchers
who are proficient in Python but not in MCNP's text-based
workflow. Graduate students and domain scientists can leverage
existing Python knowledge to conduct radiation transport studies
without first mastering MCNP's syntax and file manipulation
conventions. This lowers the barrier to entry for fields increasingly
reliant on Monte Carlo methods: medical physics, nuclear engineering,
radiation protection, and detector development.

# AI Usage Disclosure

General artificial intelligence (claude-code) was used for additional
code review, rewrite, and code fixes for version 0.10.0 and 1.0.0. Version 0.9
an earlier were written without the use of coding agents and AI.
