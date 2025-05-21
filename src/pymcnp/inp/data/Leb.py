import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Leb(DataOption):
    """
    Represents INP leb elements.

    Attributes:
        yzere: Y0 parameter in level-density formula for Z≤70.
        bzere: B0 parameter in level-density formula for Z≤70.
        yzero: Y0 parameter in level-density formula for Z≥71.
        bzero: B0 parameter in level-density formula for Z≥70.
    """

    _KEYWORD = 'leb'

    _ATTRS = {
        'yzere': types.Real,
        'bzere': types.Real,
        'yzero': types.Real,
        'bzero': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aleb( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(self, yzere: types.Real, bzere: types.Real, yzero: types.Real, bzero: types.Real):
        """
        Initializes ``Leb``.

        Parameters:
            yzere: Y0 parameter in level-density formula for Z≤70.
            bzere: B0 parameter in level-density formula for Z≤70.
            yzero: Y0 parameter in level-density formula for Z≥71.
            bzero: B0 parameter in level-density formula for Z≥70.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if yzere is None or not (yzere.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, yzere)
        if bzere is None or not (bzere.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bzere)
        if yzero is None or not (yzero.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, yzero)
        if bzero is None or not (bzero.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bzero)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                yzere,
                bzere,
                yzero,
                bzero,
            ]
        )

        self.yzere: typing.Final[types.Real] = yzere
        self.bzere: typing.Final[types.Real] = bzere
        self.yzero: typing.Final[types.Real] = yzero
        self.bzero: typing.Final[types.Real] = bzero


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

    yzere: str | float | types.Real
    bzere: str | float | types.Real
    yzero: str | float | types.Real
    bzero: str | float | types.Real

    def build(self):
        """
        Builds ``LebBuilder`` into ``Leb``.

        Returns:
            ``Leb`` for ``LebBuilder``.
        """

        yzere = self.yzere
        if isinstance(self.yzere, types.Real):
            yzere = self.yzere
        elif isinstance(self.yzere, float) or isinstance(self.yzere, int):
            yzere = types.Real(self.yzere)
        elif isinstance(self.yzere, str):
            yzere = types.Real.from_mcnp(self.yzere)

        bzere = self.bzere
        if isinstance(self.bzere, types.Real):
            bzere = self.bzere
        elif isinstance(self.bzere, float) or isinstance(self.bzere, int):
            bzere = types.Real(self.bzere)
        elif isinstance(self.bzere, str):
            bzere = types.Real.from_mcnp(self.bzere)

        yzero = self.yzero
        if isinstance(self.yzero, types.Real):
            yzero = self.yzero
        elif isinstance(self.yzero, float) or isinstance(self.yzero, int):
            yzero = types.Real(self.yzero)
        elif isinstance(self.yzero, str):
            yzero = types.Real.from_mcnp(self.yzero)

        bzero = self.bzero
        if isinstance(self.bzero, types.Real):
            bzero = self.bzero
        elif isinstance(self.bzero, float) or isinstance(self.bzero, int):
            bzero = types.Real(self.bzero)
        elif isinstance(self.bzero, str):
            bzero = types.Real.from_mcnp(self.bzero)

        return Leb(
            yzere=yzere,
            bzere=bzere,
            yzero=yzero,
            bzero=bzero,
        )

    @staticmethod
    def unbuild(ast: Leb):
        """
        Unbuilds ``Leb`` into ``LebBuilder``

        Returns:
            ``LebBuilder`` for ``Leb``.
        """

        return Leb(
            yzere=copy.deepcopy(ast.yzere),
            bzere=copy.deepcopy(ast.bzere),
            yzero=copy.deepcopy(ast.yzero),
            bzero=copy.deepcopy(ast.bzero),
        )
