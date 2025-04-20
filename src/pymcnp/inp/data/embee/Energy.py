import re
import typing
import dataclasses


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Energy(EmbeeOption_, keyword='energy'):
    """
    Represents INP energy elements.

    Attributes:
        factor: Multiplicative conversion factor for energy-related output.
    """

    _ATTRS = {
        'factor': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aenergy( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, factor: types.RealOrJump):
        """
        Initializes ``Energy``.

        Parameters:
            factor: Multiplicative conversion factor for energy-related output.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if factor is None or not (factor > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, factor)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                factor,
            ]
        )

        self.factor: typing.Final[types.RealOrJump] = factor


@dataclasses.dataclass
class EnergyBuilder:
    """
    Builds ``Energy``.

    Attributes:
        factor: Multiplicative conversion factor for energy-related output.
    """

    factor: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``EnergyBuilder`` into ``Energy``.

        Returns:
            ``Energy`` for ``EnergyBuilder``.
        """

        if isinstance(self.factor, types.Real):
            factor = self.factor
        elif isinstance(self.factor, float) or isinstance(self.factor, int):
            factor = types.RealOrJump(self.factor)
        elif isinstance(self.factor, str):
            factor = types.RealOrJump.from_mcnp(self.factor)

        return Energy(
            factor=factor,
        )
