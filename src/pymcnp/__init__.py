import importlib.metadata

from . import _cli
from . import _show
from . import abc
from . import inp
from . import meshtal
from . import outp
from . import ptrac
from .Inp import Inp
from .Meshtal import Meshtal
from .Outp import Outp
from .Ptrac import Ptrac
from .Check import Check
from .Plot import Plot
from .PtracFilter import PtracFilter
from .PtracProcessor import PtracProcessor
from .Run import Run
from .Run import Result
from .Visualize import Visualize

try:
    __version__ = importlib.metadata.version('pymcnp')
except importlib.metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = 'unknown'

__all__ = (
    '__version__',
    '_cli',
    '_show',
    'abc',
    'inp',
    'meshtal',
    'outp',
    'ptrac',
    'Inp',
    'Meshtal',
    'Outp',
    'Ptrac',
    'Check',
    'Plot',
    'PtracFilter',
    'PtracProcessor',
    'Run',
    'Result',
    'Visualize',
)
