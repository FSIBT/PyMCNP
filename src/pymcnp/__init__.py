from . import inp
from . import outp
from . import ptrac
from . import utils
from .Inp import Inp

read_input = Inp.from_mcnp_file
read_ptrac = ptrac.Ptrac.from_mcnp_file

__all__ = [
    'inp',
    'outp',
    'ptrac',
    'utils',
    'Inp',
]
