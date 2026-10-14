import re

import molmass

from . import m_0
from . import _field
from . import _card
from .. import types
from .. import _elements


NUMBER = iter(range(1, 100000000))


class M_0(_field.Fields, _card.Card):
    """
    Represents INP `m` elements variation #0.
    """

    _KEYWORD = 'm'

    _ORDER = ('substances', 'suffix', 'options')

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, default=lambda card: next(NUMBER), numeric=int, invalid=lambda self, value: not 1 <= value <= 99_999_999)
    substances = _field.Field.tuple(types.Substance, 'Tuple of material constituents', required=True, numeric=())
    options = _field.Field.tuple(m_0.MOption_0, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Am(\d+)((?: {types.Substance._REGEX.pattern[2:-2]})+?)((?: (?:{m_0.MOption_0._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    @staticmethod
    def from_formula(formulas: dict[str, float], is_weight: bool = True, cutoff: float = 0.01):
        """
        Generates `M_0` from INP.

        Parameters:
            formulas: Dictionary of formulas and atomic/weight fractions.
            is_weight: Weight (atomic) fraction true (false) flag.
            cutoff: Nuclide fraction cutoff.

        Returns:
            `M_0` object.
        """

        substances = []
        comments = []
        for formula, mixture_fraction in formulas.items():
            formula = molmass.Formula(formula)

            composition = formula.composition()
            for element in composition:
                compound_fraction = composition[element].fraction if is_weight else composition[element].mass / formula.mass

                zaids = [
                    (
                        types.Zaid(_elements.ELEMENTS[element]['z'], a),
                        isotropic_fraction,
                    )
                    for a, isotropic_fraction in _elements.ELEMENTS[element]['fraction'].items()
                ]
                entries = [
                    types.Substance(
                        zaid,
                        types.Real((-1 if is_weight else 1) * mixture_fraction * compound_fraction * isotropic_fraction),
                    )
                    for zaid, isotropic_fraction in zaids
                    if mixture_fraction * compound_fraction * isotropic_fraction > cutoff
                ]

                substances += entries

        material = M_0(types.Tuple(types.Substance)(substances))
        material.comment = tuple(comments)

        return material
