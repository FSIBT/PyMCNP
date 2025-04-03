import re
import typing

import molmass

from . import m
from .option_ import DataOption_
from ...utils import types
from ...utils import errors
from ...utils import _elements


class M(DataOption_, keyword='m'):
    """
    Represents INP m elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'substances': types.Tuple[types.Substance],
        'options': types.Tuple[m.MOption_],
    }

    _REGEX = re.compile(
        rf'\Am(\d+)((?: {types.Substance._REGEX.pattern})+?)((?: (?:{m.MOption_._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        substances: types.Tuple[types.Substance],
        options: types.Tuple[m.MOption_] = None,
    ):
        """
        Initializes ``M``.

        Parameters:
            suffix: Data card option suffix.
            substances: Tuple of material constituents.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if substances is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, substances)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                substances,
                options,
            ]
        )

        self.suffix: typing.Final[types.IntegerOrJump] = suffix
        self.substances: typing.Final[types.Tuple[types.Substance]] = substances
        self.options: typing.Final[types.Tuple[m.MOption_]] = options

    @staticmethod
    def from_formula(number: int, formulas: dict[str, float], atomic_or_weight: bool = True):
        """
        Generates ``M`` from INP.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            atomic_or_weight: Atomtic/Weight fraction true/false flag.

        Returns:
            ``M`` object.
        """

        substances = []
        comments = []
        for formula, mixture_fraction in formulas.items():
            formula = molmass.Formula(formula)

            composition = formula.composition()
            for element in composition:
                compound_fraction = (
                    composition[element].fraction
                    if atomic_or_weight
                    else composition[element].mass / formula.mass
                )

                zaids = [
                    (
                        types.Zaid(_elements.ELEMENTS[element]['z'], a),
                        isotropic_fraction,
                    )
                    for a, isotropic_fraction in _elements.ELEMENTS[element]['fraction'].items()
                ]
                subcomments = [f'{element}-{zaid.a:03}' for zaid, _ in zaids]
                entries = [
                    types.Substance(
                        zaid,
                        types.RealOrJump(
                            (-1 if atomic_or_weight else 1)
                            * mixture_fraction
                            * compound_fraction
                            * isotropic_fraction
                        ),
                    )
                    for zaid, isotropic_fraction in zaids
                ]

                comments += subcomments
                substances += entries

        material = M(types.IntegerOrJump(number), types.Tuple(substances))
        material.comment = tuple(comments)

        return material
