import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Energy(_option.EmbeeOption):
    """
    Represents INP energy elements.

    Attributes:
        factor: Multiplicative conversion factor for energy-related output.
    """

    _KEYWORD = 'energy'

    _ATTRS = {
        'factor': types.Real,
    }

    _REGEX = re.compile(rf'\Aenergy( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, factor: types.Real):
        """
        Initializes ``Energy``.

        Parameters:
            factor: Multiplicative conversion factor for energy-related output.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if factor is None or not (factor.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, factor)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                factor,
            ]
        )

        self.factor: typing.Final[types.Real] = factor


@dataclasses.dataclass
class EnergyBuilder(_option.EmbeeOptionBuilder):
    """
    Builds ``Energy``.

    Attributes:
        factor: Multiplicative conversion factor for energy-related output.
    """

    factor: str | float | types.Real

    def build(self):
        """
        Builds ``EnergyBuilder`` into ``Energy``.

        Returns:
            ``Energy`` for ``EnergyBuilder``.
        """

        factor = self.factor
        if isinstance(self.factor, types.Real):
            factor = self.factor
        elif isinstance(self.factor, float) or isinstance(self.factor, int):
            factor = types.Real(self.factor)
        elif isinstance(self.factor, str):
            factor = types.Real.from_mcnp(self.factor)

        return Energy(
            factor=factor,
        )

    @staticmethod
    def unbuild(ast: Energy):
        """
        Unbuilds ``Energy`` into ``EnergyBuilder``

        Returns:
            ``EnergyBuilder`` for ``Energy``.
        """

        return EnergyBuilder(
            factor=copy.deepcopy(ast.factor),
        )
