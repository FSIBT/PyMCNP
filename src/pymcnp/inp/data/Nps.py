import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Nps(DataOption_, keyword='nps'):
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
            npp: Total number of histories to run.
            npsmg: Number of history with direct source contributions.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if npp is None or not (npp > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, npp)
        if npsmg is not None and not (npsmg > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, npsmg)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                npp,
                npsmg,
            ]
        )

        self.npp: typing.Final[types.Integer] = npp
        self.npsmg: typing.Final[types.Integer] = npsmg
