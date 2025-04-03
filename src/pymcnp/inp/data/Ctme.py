import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ctme(DataOption_, keyword='ctme'):
    """
    Represents INP ctme elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'tme': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Actme( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, tme: types.IntegerOrJump):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tme is None or not (tme >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tme)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tme,
            ]
        )

        self.tme: typing.Final[types.IntegerOrJump] = tme
