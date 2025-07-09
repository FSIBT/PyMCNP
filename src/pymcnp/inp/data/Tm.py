import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Tm(_option.DataOption):
    """
    Represents INP tm elements.

    Attributes:
        suffix: Data card option suffix.
        multipliers: Time bin multiplier to apply.
    """

    _KEYWORD = 'tm'

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Atm(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, multipliers: types.Tuple[types.Real]):
        """
        Initializes ``Tm``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Time bin multiplier to apply.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
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
class TmBuilder(_option.DataOptionBuilder):
    """
    Builds ``Tm``.

    Attributes:
        suffix: Data card option suffix.
        multipliers: Time bin multiplier to apply.
    """

    suffix: str | int | types.Integer
    multipliers: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``TmBuilder`` into ``Tm``.

        Returns:
            ``Tm`` for ``TmBuilder``.
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

        return Tm(
            suffix=suffix,
            multipliers=multipliers,
        )

    @staticmethod
    def unbuild(ast: Tm):
        """
        Unbuilds ``Tm`` into ``TmBuilder``

        Returns:
            ``TmBuilder`` for ``Tm``.
        """

        return TmBuilder(
            suffix=copy.deepcopy(ast.suffix),
            multipliers=copy.deepcopy(ast.multipliers),
        )
