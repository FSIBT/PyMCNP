from . import inp
from . import outp
from . import ptrac
from . import utils
from .version import __version__

read_input = inp.Inp.from_mcnp_file
read_ptrac = ptrac.Ptrac.from_mcnp_file

__all__ = [
    'inp',
    'outp',
    'ptrac',
    'utils',
    'read_input',
    'read_ptrac',
    '__version__',
]
