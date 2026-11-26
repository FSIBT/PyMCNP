import re

from .... import abc
from ..Data import Data


class PtracSpace(abc.Terminal):
    """
    Represents separators between the values of ptrac data options, e.g., ``EVENT=SRC,COL``.

    MCNP separates the values with commas; spaces work too.
    """

    _pattern = re.compile(r'( *, *| *(?:\$.+)?\n {1,5} *| +&(?: *\$.*)?\n *| *\n +| +)', re.IGNORECASE)
    _default = ','


class Ptrac(Data):
    """
    Represents ptrac data options.
    """
