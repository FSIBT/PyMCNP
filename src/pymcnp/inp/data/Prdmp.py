import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Prdmp(DataOption_, keyword='prdmp'):
    """
    Represents INP prdmp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'ndp': types.IntegerOrJump,
        'ndm': types.IntegerOrJump,
        'mct': types.IntegerOrJump,
        'ndmp': types.IntegerOrJump,
        'dmmp': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Aprdmp( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        ndp: types.IntegerOrJump,
        ndm: types.IntegerOrJump,
        mct: types.IntegerOrJump,
        ndmp: types.IntegerOrJump,
        dmmp: types.IntegerOrJump,
    ):
        """
        Initializes ``Prdmp``.

        Parameters:
            ndp: Increment for printing tallies.
            ndm: Increment for dumping to RUNTPE file.
            mct: Controls printing of MCTAL file.
            ndmp: Maximum number of dumps on RUNTPE file.
            dmmp: Controls frequently of tally fluctuation chart.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ndp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ndp)
        if ndm is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ndm)
        if mct is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, mct)
        if ndmp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ndmp)
        if dmmp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, dmmp)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ndp,
                ndm,
                mct,
                ndmp,
                dmmp,
            ]
        )

        self.ndp: typing.Final[types.IntegerOrJump] = ndp
        self.ndm: typing.Final[types.IntegerOrJump] = ndm
        self.mct: typing.Final[types.IntegerOrJump] = mct
        self.ndmp: typing.Final[types.IntegerOrJump] = ndmp
        self.dmmp: typing.Final[types.IntegerOrJump] = dmmp
