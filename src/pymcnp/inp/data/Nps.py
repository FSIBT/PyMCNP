import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Nps(DataOption):
    """
    Represents INP nps elements.

    Attributes:
        npp: Total number of histories to run.
        npsmg: Number of history with direct source contributions.
    """

    _KEYWORD = 'nps'

    _ATTRS = {
        'npp': types.Integer,
        'npsmg': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Anps( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(self, npp: types.Integer, npsmg: types.Integer = None):
        """
        Initializes ``Nps``.

        Parameters:
            npp: Total number of histories to run.
            npsmg: Number of history with direct source contributions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if npp is None or not (npp.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, npp)
        if npsmg is not None and not (npsmg.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, npsmg)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                npp,
                npsmg,
            ]
        )

        self.npp: typing.Final[types.Integer] = npp
        self.npsmg: typing.Final[types.Integer] = npsmg


@dataclasses.dataclass
class NpsBuilder:
    """
    Builds ``Nps``.

    Attributes:
        npp: Total number of histories to run.
        npsmg: Number of history with direct source contributions.
    """

    npp: str | int | types.Integer
    npsmg: str | int | types.Integer = None

    def build(self):
        """
        Builds ``NpsBuilder`` into ``Nps``.

        Returns:
            ``Nps`` for ``NpsBuilder``.
        """

        npp = self.npp
        if isinstance(self.npp, types.Integer):
            npp = self.npp
        elif isinstance(self.npp, int):
            npp = types.Integer(self.npp)
        elif isinstance(self.npp, str):
            npp = types.Integer.from_mcnp(self.npp)

        npsmg = self.npsmg
        if isinstance(self.npsmg, types.Integer):
            npsmg = self.npsmg
        elif isinstance(self.npsmg, int):
            npsmg = types.Integer(self.npsmg)
        elif isinstance(self.npsmg, str):
            npsmg = types.Integer.from_mcnp(self.npsmg)

        return Nps(
            npp=npp,
            npsmg=npsmg,
        )

    @staticmethod
    def unbuild(ast: Nps):
        """
        Unbuilds ``Nps`` into ``NpsBuilder``

        Returns:
            ``NpsBuilder`` for ``Nps``.
        """

        return Nps(
            npp=copy.deepcopy(ast.npp),
            npsmg=copy.deepcopy(ast.npsmg),
        )
