import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Prdmp(DataOption, keyword='prdmp'):
    """
    Represents INP prdmp elements.

    Attributes:
        ndp: Increment for printing tallies.
        ndm: Increment for dumping to RUNTPE file.
        mct: Controls printing of MCTAL file.
        ndmp: Maximum number of dumps on RUNTPE file.
        dmmp: Controls frequently of tally fluctuation chart.
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


@dataclasses.dataclass
class PrdmpBuilder:
    """
    Builds ``Prdmp``.

    Attributes:
        ndp: Increment for printing tallies.
        ndm: Increment for dumping to RUNTPE file.
        mct: Controls printing of MCTAL file.
        ndmp: Maximum number of dumps on RUNTPE file.
        dmmp: Controls frequently of tally fluctuation chart.
    """

    ndp: str | int | types.IntegerOrJump
    ndm: str | int | types.IntegerOrJump
    mct: str | int | types.IntegerOrJump
    ndmp: str | int | types.IntegerOrJump
    dmmp: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``PrdmpBuilder`` into ``Prdmp``.

        Returns:
            ``Prdmp`` for ``PrdmpBuilder``.
        """

        if isinstance(self.ndp, types.Integer):
            ndp = self.ndp
        elif isinstance(self.ndp, int):
            ndp = types.IntegerOrJump(self.ndp)
        elif isinstance(self.ndp, str):
            ndp = types.IntegerOrJump.from_mcnp(self.ndp)

        if isinstance(self.ndm, types.Integer):
            ndm = self.ndm
        elif isinstance(self.ndm, int):
            ndm = types.IntegerOrJump(self.ndm)
        elif isinstance(self.ndm, str):
            ndm = types.IntegerOrJump.from_mcnp(self.ndm)

        if isinstance(self.mct, types.Integer):
            mct = self.mct
        elif isinstance(self.mct, int):
            mct = types.IntegerOrJump(self.mct)
        elif isinstance(self.mct, str):
            mct = types.IntegerOrJump.from_mcnp(self.mct)

        if isinstance(self.ndmp, types.Integer):
            ndmp = self.ndmp
        elif isinstance(self.ndmp, int):
            ndmp = types.IntegerOrJump(self.ndmp)
        elif isinstance(self.ndmp, str):
            ndmp = types.IntegerOrJump.from_mcnp(self.ndmp)

        if isinstance(self.dmmp, types.Integer):
            dmmp = self.dmmp
        elif isinstance(self.dmmp, int):
            dmmp = types.IntegerOrJump(self.dmmp)
        elif isinstance(self.dmmp, str):
            dmmp = types.IntegerOrJump.from_mcnp(self.dmmp)

        return Prdmp(
            ndp=ndp,
            ndm=ndm,
            mct=mct,
            ndmp=ndmp,
            dmmp=dmmp,
        )
