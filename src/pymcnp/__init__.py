from . import inp
from . import outp
from . import ptrac
from . import utils
from .Inp import Inp
from .Ptrac import Ptrac

read_input = Inp.from_mcnp_file
read_ptrac = Ptrac.from_mcnp_file

__all__ = [
    'inp',
    'outp',
    'ptrac',
    'utils',
    'Inp',
]
