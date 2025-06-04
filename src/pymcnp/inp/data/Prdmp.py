import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types


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

    _KEYWORD = 'prdmp'

    _ATTRS = {
        'ndp': types.Integer,
        'ndm': types.Integer,
        'mct': types.Integer,
        'ndmp': types.Integer,
        'dmmp': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Aprdmp( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        ndp: types.Integer = None,
        ndm: types.Integer = None,
        mct: types.Integer = None,
        ndmp: types.Integer = None,
        dmmp: types.Integer = None,
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

    ndp: str | int | types.Integer = None
    ndm: str | int | types.Integer = None
    mct: str | int | types.Integer = None
    ndmp: str | int | types.Integer = None
    dmmp: str | int | types.Integer = None

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

    @staticmethod
    def unbuild(ast: Prdmp):
        """
        Unbuilds ``Prdmp`` into ``PrdmpBuilder``

        Returns:
            ``PrdmpBuilder`` for ``Prdmp``.
        """

        return Prdmp(
            ndp=copy.deepcopy(ast.ndp),
            ndm=copy.deepcopy(ast.ndm),
            mct=copy.deepcopy(ast.mct),
            ndmp=copy.deepcopy(ast.ndmp),
            dmmp=copy.deepcopy(ast.dmmp),
        )
