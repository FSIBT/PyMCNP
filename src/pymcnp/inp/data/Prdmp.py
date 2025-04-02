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
        'ndp': types.Integer,
        'ndm': types.Integer,
        'mct': types.Integer,
        'ndmp': types.Integer,
        'dmmp': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Aprdmp( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        ndp: types.Integer,
        ndm: types.Integer,
        mct: types.Integer,
        ndmp: types.Integer,
        dmmp: types.Integer,
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

        self.ndp: typing.Final[types.Integer] = ndp
        self.ndm: typing.Final[types.Integer] = ndm
        self.mct: typing.Final[types.Integer] = mct
        self.ndmp: typing.Final[types.Integer] = ndmp
        self.dmmp: typing.Final[types.Integer] = dmmp
