import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Embem(DataOption):
    """
    Represents INP embem elements.

    Attributes:
        suffix: Data card option suffix.
        multipliers: Tuple of energy multipliers.
    """

    _KEYWORD = 'embem'

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aembem(\d+)((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, multipliers: types.Tuple[types.Real]):
        """
        Initializes ``Embem``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Tuple of energy multipliers.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, multipliers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multipliers,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.multipliers: typing.Final[types.Tuple[types.Real]] = multipliers


@dataclasses.dataclass
class EmbemBuilder:
    """
    Builds ``Embem``.

    Attributes:
        suffix: Data card option suffix.
        multipliers: Tuple of energy multipliers.
    """

    suffix: str | int | types.Integer
    multipliers: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``EmbemBuilder`` into ``Embem``.

        Returns:
            ``Embem`` for ``EmbemBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.multipliers:
            multipliers = []
            for item in self.multipliers:
                if isinstance(item, types.Real):
                    multipliers.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    multipliers.append(types.Real(item))
                elif isinstance(item, str):
                    multipliers.append(types.Real.from_mcnp(item))
            multipliers = types.Tuple(multipliers)
        else:
            multipliers = None

        return Embem(
            suffix=suffix,
            multipliers=multipliers,
        )

    @staticmethod
    def unbuild(ast: Embem):
        """
        Unbuilds ``Embem`` into ``EmbemBuilder``

        Returns:
            ``EmbemBuilder`` for ``Embem``.
        """

        return Embem(
            suffix=copy.deepcopy(ast.suffix),
            multipliers=copy.deepcopy(ast.multipliers),
        )
