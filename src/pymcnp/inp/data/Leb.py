import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Leb(DataOption_, keyword='leb'):
    """
    Represents INP leb elements.

    Attributes:
        yzere: Y0 parameter in level-density formula for Z≤70.
        bzere: B0 parameter in level-density formula for Z≤70.
        yzero: Y0 parameter in level-density formula for Z≥71.
        bzero: B0 parameter in level-density formula for Z≥70.
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


@dataclasses.dataclass
class LebBuilder:
    """
    Builds ``Leb``.

    Attributes:
        yzere: Y0 parameter in level-density formula for Z≤70.
        bzere: B0 parameter in level-density formula for Z≤70.
        yzero: Y0 parameter in level-density formula for Z≥71.
        bzero: B0 parameter in level-density formula for Z≥70.
    """

    yzere: str | float | types.RealOrJump
    bzere: str | float | types.RealOrJump
    yzero: str | float | types.RealOrJump
    bzero: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``LebBuilder`` into ``Leb``.

        Returns:
            ``Leb`` for ``LebBuilder``.
        """

        if isinstance(self.yzere, types.Real):
            yzere = self.yzere
        elif isinstance(self.yzere, float) or isinstance(self.yzere, int):
            yzere = types.RealOrJump(self.yzere)
        elif isinstance(self.yzere, str):
            yzere = types.RealOrJump.from_mcnp(self.yzere)

        if isinstance(self.bzere, types.Real):
            bzere = self.bzere
        elif isinstance(self.bzere, float) or isinstance(self.bzere, int):
            bzere = types.RealOrJump(self.bzere)
        elif isinstance(self.bzere, str):
            bzere = types.RealOrJump.from_mcnp(self.bzere)

        if isinstance(self.yzero, types.Real):
            yzero = self.yzero
        elif isinstance(self.yzero, float) or isinstance(self.yzero, int):
            yzero = types.RealOrJump(self.yzero)
        elif isinstance(self.yzero, str):
            yzero = types.RealOrJump.from_mcnp(self.yzero)

        if isinstance(self.bzero, types.Real):
            bzero = self.bzero
        elif isinstance(self.bzero, float) or isinstance(self.bzero, int):
            bzero = types.RealOrJump(self.bzero)
        elif isinstance(self.bzero, str):
            bzero = types.RealOrJump.from_mcnp(self.bzero)

        return Leb(
            yzere=yzere,
            bzere=bzere,
            yzero=yzero,
            bzero=bzero,
        )
