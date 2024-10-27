Python Package
==============

Overview
--------

The PyMCNP Python package provides subpackages for parsing MCNP files:

* ``pymcnp.inp``: Parsers for MCNP ``.inp`` input files.
* ``pymcnp.ptrac``: Parsers for MCNP ``.ptrac`` output files.
* ``pymcnp.cli``: Runs the command line, and provides the ``Run`` class.

PyMCNP represents MCNP syntax elements as Python classes, providing an
interface for interacting with MCNP source strings/files. These
classes include entrypoint/constructor methods and endpoint methods
for creating and observing PyMCNP object and the underlying MCNP
source code. Objects in PyMCNP have ``from_*`` methods which act as
entrypoints/constructors for building PyMCNP objects:

* **From MCNP**. ``from_mcnp`` transforms MCNP source strings into
  PyMCNP objects by parsing strings and returning instances of classes
  representing MCNP syntax elements.
* **From MCNP Files**. ``from_mcnp_file`` constructs PyMCNP object by
  reading MCNP source files, such as ``.inp`` and ``.ptrac`` files,
  and calling ``from_mcnp`` on their contents. Only file-level syntax
  objects, such as ``Inp`` and ``Ptrac``, have this method.

Similarly, each object in PyMCNP has ``to_*`` methods which act as
endpoints for outputing various representation of MCNP source code:

* **To MCNP**. ``to_mcnp`` methods translate PyMCNP object into MCNP
  source strings. Calling ``to_mcnp`` on PyMCNP objects constructed
  with ``from_mcnp`` will not return the original MCNP source strings
  passed to ``from_mcnp``. ``from_mcnp`` and ``to_mcnp`` are not
  inverses.
* **To MCNP File**. ``to_mcnp_file`` methods create/write to MCNP
  source files from PyMCNP objects. It writes ``to_mcnp`` output to
  files. Only file-level syntax objects, such as ``Inp`` and
  ``Ptrac``, have this method.
* **To Cadquery**. ``to_cadquery`` methods generate Cadquery source
  strings for visualizes PyMCNP objects using computer aided design
  (CAD). Only certain ``Surfaces`` and ``Surface`` subclasses support
  ``to_cadquery`` methods.
* **To Cadquery File**. ``to_cadquery_file`` methods create/write to
  Cadquery source files from PyMCNP objects. It writes ``to_cadquery``
  output to files. Only ``Surfaces`` supports this method.
* **To Arguments**. ``to_arguments`` methods return Python nested
  dictionaries whose keys corresond to MCNP manual notation for MCNP
  syntax elements.

To modify an input object in python, PyMCNP provides a ``modify``
function, defined in Functions.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 1

   pymcnp-inp.rst
   pymcnp-ptrac.rst
   pymcnp-utils.rst
   pymcnp-cli.rst
   supported-elements.rst
   functions.rst

