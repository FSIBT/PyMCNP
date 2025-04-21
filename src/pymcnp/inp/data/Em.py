import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Em(DataOption, keyword='em'):
    """
    Represents INP em elements.

    Attributes:
        suffix: Data card option suffix.
        multipliers: Energy bin multiplier to apply.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aem(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, multipliers: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Em``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Energy bin multiplier to apply.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multipliers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multipliers,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.multipliers: typing.Final[types.Tuple[types.RealOrJump]] = multipliers


@dataclasses.dataclass
class EmBuilder:
    """
    Builds ``Em``.

    Attributes:
        suffix: Data card option suffix.
        multipliers: Energy bin multiplier to apply.
    """

    suffix: str | int | types.Integer
    multipliers: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``EmBuilder`` into ``Em``.

        Returns:
            ``Em`` for ``EmBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        multipliers = []
        for item in self.multipliers:
            if isinstance(item, types.RealOrJump):
                multipliers.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                multipliers.append(types.RealOrJump(item))
            elif isinstance(item, str):
                multipliers.append(types.RealOrJump.from_mcnp(item))
        multipliers = types.Tuple(multipliers)

        return Em(
            suffix=suffix,
            multipliers=multipliers,
        )
