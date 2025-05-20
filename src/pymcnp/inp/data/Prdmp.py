import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Prdmp(DataOption):
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
            InpError: SEMANTICS_OPTION.
        """

        if ndp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ndp)
        if ndm is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ndm)
        if mct is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, mct)
        if ndmp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ndmp)
        if dmmp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, dmmp)

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

    ndp: str | int | types.Integer
    ndm: str | int | types.Integer
    mct: str | int | types.Integer
    ndmp: str | int | types.Integer
    dmmp: str | int | types.Integer

    def build(self):
        """
        Builds ``PrdmpBuilder`` into ``Prdmp``.

        Returns:
            ``Prdmp`` for ``PrdmpBuilder``.
        """

        ndp = self.ndp
        if isinstance(self.ndp, types.Integer):
            ndp = self.ndp
        elif isinstance(self.ndp, int):
            ndp = types.Integer(self.ndp)
        elif isinstance(self.ndp, str):
            ndp = types.Integer.from_mcnp(self.ndp)

        ndm = self.ndm
        if isinstance(self.ndm, types.Integer):
            ndm = self.ndm
        elif isinstance(self.ndm, int):
            ndm = types.Integer(self.ndm)
        elif isinstance(self.ndm, str):
            ndm = types.Integer.from_mcnp(self.ndm)

        mct = self.mct
        if isinstance(self.mct, types.Integer):
            mct = self.mct
        elif isinstance(self.mct, int):
            mct = types.Integer(self.mct)
        elif isinstance(self.mct, str):
            mct = types.Integer.from_mcnp(self.mct)

        ndmp = self.ndmp
        if isinstance(self.ndmp, types.Integer):
            ndmp = self.ndmp
        elif isinstance(self.ndmp, int):
            ndmp = types.Integer(self.ndmp)
        elif isinstance(self.ndmp, str):
            ndmp = types.Integer.from_mcnp(self.ndmp)

        dmmp = self.dmmp
        if isinstance(self.dmmp, types.Integer):
            dmmp = self.dmmp
        elif isinstance(self.dmmp, int):
            dmmp = types.Integer(self.dmmp)
        elif isinstance(self.dmmp, str):
            dmmp = types.Integer.from_mcnp(self.dmmp)

        return Prdmp(
            ndp=ndp,
            ndm=ndm,
            mct=mct,
            ndmp=ndmp,
            dmmp=dmmp,
        )
