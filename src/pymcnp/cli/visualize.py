"""
Usage:
    pymcnp visualize <file>
"""

from docopt import docopt

from . import _io
from .. import files


def main() -> None:
    """
    Executes the ``pymcnp visualize`` command.

    ``pymcnp visualize`` visualizes INP files using PyVISTA.
    """

    _io.warning()

    # Processing CLI arguments.
    args = docopt(__doc__)
    inp = args['<file>']

    # Reading INP file(s).
    try:
        inp = files.inp.Inp.from_mcnp_file(inp)
    except files.utils.errors.McnpError as err:
        _io.error(err.__str__())
    except FileNotFoundError:
        _io.error(f'[red][bold]IoError:[/][/] ``{inp}`` not found.')

    # Visualizing!
    data = inp.to_pyvista()
    data.plot()

    _io.done()
