import re
import copy
import typing
import dataclasses

import molmass

from . import m_0
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _elements


class M_0(_option.DataOption):
    """
    Represents INP m variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        substances: Tuple of material constituents.
        options: Dictionary of options.
    """

    _KEYWORD = 'm'

    _ATTRS = {
        'suffix': types.Integer,
        'substances': types.Tuple[types.Substance],
        'options': types.Tuple[m_0.MOption_0],
    }

    _REGEX = re.compile(rf'\Am(\d+)((?: {types.Substance._REGEX.pattern[2:-2]})+?)((?: (?:{m_0.MOption_0._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, suffix: types.Integer, substances: types.Tuple[types.Substance], options: types.Tuple[m_0.MOption_0] = None):
        """
        Initializes ``M_0``.

        Parameters:
            suffix: Data card option suffix.
            substances: Tuple of material constituents.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if substances is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, substances)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                substances,
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.substances: typing.Final[types.Tuple[types.Substance]] = substances
        self.options: typing.Final[types.Tuple[m_0.MOption_0]] = options

    @staticmethod
    def from_formula(number: int, formulas: dict[str, float], is_weight: bool = True):
        """
        Generates ``M_0`` from formulas.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            is_weight: Weight (atomic) fraction true (false) flag.

        Returns:
            ``M_0`` object.
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
                subcomments = [f'{element}-{zaid.a:03}' for zaid, _ in zaids]
                entries = [
                    types.Substance(
                        zaid,
                        types.Real((-1 if is_weight else 1) * mixture_fraction * compound_fraction * isotropic_fraction),
                    )
                    for zaid, isotropic_fraction in zaids
                ]

                comments += subcomments
                substances += entries

        material = M_0(types.Integer(number), types.Tuple(substances))
        material.comment = tuple(comments)

        return material


@dataclasses.dataclass
class MBuilder_0(_option.DataOptionBuilder):
    """
    Builds ``M_0``.

    Attributes:
        suffix: Data card option suffix.
        substances: Tuple of material constituents.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    substances: list[str] | list[types.Substance]
    options: list[str] | list[m_0.MOption_0] = None

    def build(self):
        """
        Builds ``MBuilder_0`` into ``M_0``.

        Returns:
            ``M_0`` for ``MBuilder_0``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.substances:
            substances = []
            for item in self.substances:
                if isinstance(item, types.Substance):
                    substances.append(item)
                elif isinstance(item, str):
                    substances.append(types.Substance.from_mcnp(item))
            substances = types.Tuple(substances)
        else:
            substances = None

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, m_0.MOption_0):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(m_0.MOption_0.from_mcnp(item))
                elif isinstance(item, m_0.MOptionBuilder_0):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return M_0(
            suffix=suffix,
            substances=substances,
            options=options,
        )

    @staticmethod
    def unbuild(ast: M_0):
        """
        Unbuilds ``M_0`` into ``MBuilder_0``

        Returns:
            ``MBuilder_0`` for ``M_0``.
        """

        return MBuilder_0(
            suffix=copy.deepcopy(ast.suffix),
            substances=copy.deepcopy(ast.substances),
            options=copy.deepcopy(ast.options),
        )

    @staticmethod
    def from_formula(number: int, formulas: dict[str, float], is_weight: bool = True):
        """
        Generates ``MBuilder_0`` from formulas.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            is_weight: Weight (atomic) fraction true (false) flag.

        Returns:
            ``MBuilder_0`` object.
        """

        return MBuilder_0.unbuild(M_0.from_formula(number, formulas, is_weight))
