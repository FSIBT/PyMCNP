Command Line Interface
======================

The command line interface (CLI) provides command line access to the main functions of PyMCNP. It has the following options:


.. code-block ::

     Usage:
         pymcnp run [<args>...]
         pymcnp check [<args>...]
         pymcnp visualize [<args>...]
         pymcnp convert [<args>...]
         pymcnp plot [<args>...]
         pymcnp help <command>

     Commands:
         run        Run MCNP.
         check      Check if we can parse an input file.
         visualize  Create a 3D visualization of an input file.
         convert    Convert the output of an MCNP run into a pandas dataframe.
         plot       Plot the output of an MCNP simulation.
         help       Show help for a specific command


Running files
-------------

`pymcnp run` allows you to run input file.

Currently, it just runs the file, but in future we plan to support
automated parallization. The idea is that a single input file with can
be split in multiple runs that each run less particles and those runs
can the be distributed across multiple cores or even multiple
computers. To achieve this, we rely on `GNU parallel`.


Checking input files
--------------------

To check if PyMCNP can parse your input file, you can use `pymcnp check <file>`.

If you want to reformat the input file to a standard output format,
you can use `pymcnp check --fix <file>`. This will read in the file
and then output it to a new file to the screen or to a file, if you
specify `-o <output>`.

In case PyMCNP cannot parse your input file (MCNP allows for many
special input formats and we do not support all of them), feel free to
create a git issue.


Visualizing input geometry
--------------------------

For visualization we rely on `cadquery`, a python-based CAD program. You can use `pymcnp visualize <file>` and PyMCNP will output a new script that can be copied into the `cq-editor`. Cadquery and the cq-editor need to be installed separately.

Converting output files
-----------------------

MCNP produces many output files, for example for F<n> tallies. These
are ascii-based files, but for plotting in python these are not very
easy to access. PyMCNP provides functions to convert these into, for
example, pandas dataframes. The `pymcnp convert <outputfile>` provides
a command line interface to convert files to pandas dataframes.

If multiple tallies are in an output file, you need to specify which one you want to convert.

Plotting output files
---------------------

Similar to converting output files, this command line option allows
you to convert a file to pandas and then create a plot. By default it
will open a matplotlib window to show the plot, but with an option, it
can save the plot as pdf.


