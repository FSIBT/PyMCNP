import re
import math

import molmass

from . import m_0
from . import _option
from ... import types
from ... import errors
from ... import _elements


class M_0(_option.DataOption):
    """
    Represents INP m variation #0 elements.
    """

    _KEYWORD = 'm'

    _ATTRS = {
        'suffix': types.Integer,
        'substances': types.Tuple(types.Substance),
        'options': types.Tuple(m_0.MOption_0),
    }

    _REGEX = re.compile(rf'\Am(\d+)((?: {types.Substance._REGEX.pattern[2:-2]})+?)((?: (?:{m_0.MOption_0._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, substances: list[str] | list[types.Substance], options: list[str] | list[m_0.MOption_0] = None):
        """
        Initializes ``M_0``.

        Parameters:
            suffix: Data card option suffix.
            substances: Tuple of material constituents.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.substances: types.Tuple(types.Substance) = substances
        self.options: types.Tuple(m_0.MOption_0) = options

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def substances(self) -> types.Tuple(types.Substance):
        """
        Tuple of material constituents

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._substances

    @substances.setter
    def substances(self, substances: list[str] | list[types.Substance]) -> None:
        """
        Sets ``substances``.

        Parameters:
            substances: Tuple of material constituents.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if substances is not None:
            array = []
            for item in substances:
                if isinstance(item, types.Substance):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Substance.from_mcnp(item))
            substances = types.Tuple(types.Substance)(array)

        if substances is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, substances)

        self._substances: types.Tuple(types.Substance) = substances

    @property
    def options(self) -> types.Tuple(m_0.MOption_0):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[m_0.MOption_0]) -> None:
        """
        Sets ``options``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, m_0.MOption_0):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(m_0.MOption_0.from_mcnp(item))
            options = types.Tuple(m_0.MOption_0)(array)

        self._options: types.Tuple(m_0.MOption_0) = options

    @staticmethod
    def from_formula(number: int, formulas: dict[str, float], is_weight: bool = True, cutoff: float = 0.01):
        """
        Generates ``M_0`` from INP.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            is_weight: Weight (atomic) fraction true (false) flag.
            cutoff: Nuclide fraction cutoff.

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
                entries = [
                    types.Substance(
                        zaid,
                        types.Real((-1 if is_weight else 1) * mixture_fraction * compound_fraction * isotropic_fraction),
                    )
                    for zaid, isotropic_fraction in zaids if mixture_fraction * compound_fraction * isotropic_fraction > cutoff
                ]

                substances += entries

        material = M_0(types.Integer(number), types.Tuple(types.Substance)(substances))
        material.comment = tuple(comments)

        return material
