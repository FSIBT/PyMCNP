import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Embdf(_option.DataOption):
    """
    Represents INP embdf elements.

    Attributes:
        suffix: Data card option suffix.
        multipliers: Tuple of dose energy multipliers.
    """

    _KEYWORD = 'embdf'

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aembdf(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, multipliers: types.Tuple[types.Real]):
        """
        Initializes ``Embdf``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Tuple of dose energy multipliers.

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
class EmbdfBuilder(_option.DataOptionBuilder):
    """
    Builds ``Embdf``.

    Attributes:
        suffix: Data card option suffix.
        multipliers: Tuple of dose energy multipliers.
    """

    suffix: str | int | types.Integer
    multipliers: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``EmbdfBuilder`` into ``Embdf``.

        Returns:
            ``Embdf`` for ``EmbdfBuilder``.
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

        return Embdf(
            suffix=suffix,
            multipliers=multipliers,
        )

    @staticmethod
    def unbuild(ast: Embdf):
        """
        Unbuilds ``Embdf`` into ``EmbdfBuilder``

        Returns:
            ``EmbdfBuilder`` for ``Embdf``.
        """

        return EmbdfBuilder(
            suffix=copy.deepcopy(ast.suffix),
            multipliers=copy.deepcopy(ast.multipliers),
        )
