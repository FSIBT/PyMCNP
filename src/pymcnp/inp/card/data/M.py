import typing
import collections
import dataclasses

import molmass

from .... import _elements
from .... import abc
from ... import literal
from ..Data import Data
from ... import option
from ... import group


class M(Data):
    """
    Represents m data cards.

    Attributes:
        keyword: m data card `M` symbol.
        suffix: m data card `n` parameter.
        z_f: m data card `z_f` parameter.
        options: m data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'M'] | str = abc.Terminal[r'M']('M')
    suffix: literal.Integer | int | str
    z_f: typing.Annotated[abc.Array, group.Constituent, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Constituent | str] | str = abc.Terminal[r'']('')
    options: typing.Annotated[abc.Array, option.data.M, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.M | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates m data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

    @staticmethod
    def from_formula(suffix: literal.Integer | int | str, formulas: dict[str, float], is_weight: bool = True, cutoff: float = 0.01):
        """
        Generates m data cards from formulas.

        Parameters:
            formulas: Dictionary of formulas and atomic/weight fractions.
            is_weight: Weight (atomic) fraction true (false) flag.
            cutoff: Nuclide fraction cutoff.

        Returns:
            Corresponding M data cards.
        """

        substances: list[group.Constituent] = []
        for formula, mixture_fraction in formulas.items():
            formula = molmass.Formula(formula)

            composition = formula.composition()
            for element in composition:
                compound_fraction = composition[element].fraction if is_weight else composition[element].mass / formula.mass

                zaids = [(f'{_elements.ELEMENTS[element]["z"]:03}{a:03}', isotropic_fraction) for a, isotropic_fraction in _elements.ELEMENTS[element]['fraction'].items()]
                entries = [
                    group.Constituent(z=zaid, f=-1 if is_weight else 1 * mixture_fraction * compound_fraction * isotropic_fraction)
                    for zaid, isotropic_fraction in zaids
                    if mixture_fraction * compound_fraction * isotropic_fraction > cutoff
                ]

                substances += entries

        material = M(suffix=suffix, z_f=abc.Array(*substances, spaces=[M._space[0](M._space[0]._default)] * (len(substances) - 1)))

        return material
