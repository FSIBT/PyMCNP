import re
import typing


from .option_ import StopOption_
from ....utils import types
from ....utils import errors


class Ctme(StopOption_, keyword='ctme'):
    """
    Represents INP ctme elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'tme': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Actme( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, tme: types.RealOrJump):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: Computer time before stop.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tme is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tme)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tme,
            ]
        )

        self.tme: typing.Final[types.RealOrJump] = tme
