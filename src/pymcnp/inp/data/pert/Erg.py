import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Erg(_option.PertOption):
    """
    Represents INP erg elements.

    Attributes:
        energy_lower_bound: Lower bound for energy pertubation.
        energy_upper_bound: Upper bound for energy pertubation.
    """

    _KEYWORD = 'erg'

    _ATTRS = {
        'energy_lower_bound': types.Real,
        'energy_upper_bound': types.Real,
    }

    _REGEX = re.compile(rf'\Aerg( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, energy_lower_bound: types.Real, energy_upper_bound: types.Real):
        """
        Initializes ``Erg``.

        Parameters:
            energy_lower_bound: Lower bound for energy pertubation.
            energy_upper_bound: Upper bound for energy pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if energy_lower_bound is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy_lower_bound)
        if energy_upper_bound is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy_upper_bound)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energy_lower_bound,
                energy_upper_bound,
            ]
        )

        self.energy_lower_bound: typing.Final[types.Real] = energy_lower_bound
        self.energy_upper_bound: typing.Final[types.Real] = energy_upper_bound


@dataclasses.dataclass
class ErgBuilder(_option.PertOptionBuilder):
    """
    Builds ``Erg``.

    Attributes:
        energy_lower_bound: Lower bound for energy pertubation.
        energy_upper_bound: Upper bound for energy pertubation.
    """

    energy_lower_bound: str | float | types.Real
    energy_upper_bound: str | float | types.Real

    def build(self):
        """
        Builds ``ErgBuilder`` into ``Erg``.

        Returns:
            ``Erg`` for ``ErgBuilder``.
        """

        energy_lower_bound = self.energy_lower_bound
        if isinstance(self.energy_lower_bound, types.Real):
            energy_lower_bound = self.energy_lower_bound
        elif isinstance(self.energy_lower_bound, float) or isinstance(self.energy_lower_bound, int):
            energy_lower_bound = types.Real(self.energy_lower_bound)
        elif isinstance(self.energy_lower_bound, str):
            energy_lower_bound = types.Real.from_mcnp(self.energy_lower_bound)

        energy_upper_bound = self.energy_upper_bound
        if isinstance(self.energy_upper_bound, types.Real):
            energy_upper_bound = self.energy_upper_bound
        elif isinstance(self.energy_upper_bound, float) or isinstance(self.energy_upper_bound, int):
            energy_upper_bound = types.Real(self.energy_upper_bound)
        elif isinstance(self.energy_upper_bound, str):
            energy_upper_bound = types.Real.from_mcnp(self.energy_upper_bound)

        return Erg(
            energy_lower_bound=energy_lower_bound,
            energy_upper_bound=energy_upper_bound,
        )

    @staticmethod
    def unbuild(ast: Erg):
        """
        Unbuilds ``Erg`` into ``ErgBuilder``

        Returns:
            ``ErgBuilder`` for ``Erg``.
        """

        return ErgBuilder(
            energy_lower_bound=copy.deepcopy(ast.energy_lower_bound),
            energy_upper_bound=copy.deepcopy(ast.energy_upper_bound),
        )
