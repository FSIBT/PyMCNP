import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Leb(DataOption_, keyword='leb'):
    """
    Represents INP leb elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'yzere': types.RealOrJump,
        'bzere': types.RealOrJump,
        'yzero': types.RealOrJump,
        'bzero': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aleb( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        yzere: types.RealOrJump,
        bzere: types.RealOrJump,
        yzero: types.RealOrJump,
        bzero: types.RealOrJump,
    ):
        """
        Initializes ``Leb``.

        Parameters:
            yzere: Y0 parameter in level-density formula for Z≤70.
            bzere: B0 parameter in level-density formula for Z≤70.
            yzero: Y0 parameter in level-density formula for Z≥71.
            bzero: B0 parameter in level-density formula for Z≥70.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if yzere is None or not (yzere > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, yzere)
        if bzere is None or not (bzere > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bzere)
        if yzero is None or not (yzero > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, yzero)
        if bzero is None or not (bzero > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bzero)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                yzere,
                bzere,
                yzero,
                bzero,
            ]
        )

        self.yzere: typing.Final[types.RealOrJump] = yzere
        self.bzere: typing.Final[types.RealOrJump] = bzere
        self.yzero: typing.Final[types.RealOrJump] = yzero
        self.bzero: typing.Final[types.RealOrJump] = bzero
