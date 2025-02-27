import re
import typing


from .option_ import StopOption_
from ....utils import types
from ....utils import errors


class Nps(StopOption_, keyword='nps'):
    """
    Represents INP nps elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'npp': types.Integer,
        'npsmg': types.Integer,
    }

    _REGEX = re.compile(r'nps( \S+)( \S+)?')

    def __init__(self, npp: types.Integer, npsmg: types.Integer = None):
        """
        Initializes ``Nps``.

        Parameters:
            npp: Total number of histories before stop.
            npsmg: Number of histories before stop.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if npp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, npp)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                npp,
                npsmg,
            ]
        )

        self.npp: typing.Final[types.Integer] = npp
        self.npsmg: typing.Final[types.Integer] = npsmg
