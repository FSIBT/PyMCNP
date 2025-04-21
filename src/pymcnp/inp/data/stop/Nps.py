import re
import typing
import dataclasses


from ._option import StopOption
from ....utils import types
from ....utils import errors


class Nps(StopOption, keyword='nps'):
    """
    Represents INP nps elements.

    Attributes:
        npp: Total number of histories before stop.
        npsmg: Number of histories before stop.
    """

    _ATTRS = {
        'npp': types.IntegerOrJump,
        'npsmg': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Anps( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?\Z'
    )

    def __init__(self, npp: types.IntegerOrJump, npsmg: types.IntegerOrJump = None):
        """
        Initializes ``Nps``.

        Parameters:
            npp: Total number of histories before stop.
            npsmg: Number of histories before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if npp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, npp)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                npp,
                npsmg,
            ]
        )

        self.npp: typing.Final[types.IntegerOrJump] = npp
        self.npsmg: typing.Final[types.IntegerOrJump] = npsmg


@dataclasses.dataclass
class NpsBuilder:
    """
    Builds ``Nps``.

    Attributes:
        npp: Total number of histories before stop.
        npsmg: Number of histories before stop.
    """

    npp: str | int | types.IntegerOrJump
    npsmg: str | int | types.IntegerOrJump = None

    def build(self):
        """
        Builds ``NpsBuilder`` into ``Nps``.

        Returns:
            ``Nps`` for ``NpsBuilder``.
        """

        if isinstance(self.npp, types.Integer):
            npp = self.npp
        elif isinstance(self.npp, int):
            npp = types.IntegerOrJump(self.npp)
        elif isinstance(self.npp, str):
            npp = types.IntegerOrJump.from_mcnp(self.npp)

        npsmg = None
        if isinstance(self.npsmg, types.Integer):
            npsmg = self.npsmg
        elif isinstance(self.npsmg, int):
            npsmg = types.IntegerOrJump(self.npsmg)
        elif isinstance(self.npsmg, str):
            npsmg = types.IntegerOrJump.from_mcnp(self.npsmg)

        return Nps(
            npp=npp,
            npsmg=npsmg,
        )
