import re
import typing
import dataclasses

import molmass

from . import m
from ._option import DataOption
from ...utils import types
from ...utils import errors
from ...utils import _elements


class M(DataOption, keyword='m'):
    """
    Represents INP m elements.

    Attributes:
        suffix: Data card option suffix.
        substances: Tuple of material constituents.
        options: Dictionary of options.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'substances': types.Tuple[types.Substance],
        'options': types.Tuple[m.MOption],
    }

    _REGEX = re.compile(
        rf'\Am(\d+)((?: {types.Substance._REGEX.pattern})+?)((?: (?:{m.MOption._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        substances: types.Tuple[types.Substance],
        options: types.Tuple[m.MOption] = None,
    ):
        """
        Initializes ``M``.

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
        self.options: typing.Final[types.Tuple[m.MOption]] = options

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
                        types.Real(
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

        material = M(types.Integer(number), types.Tuple(substances))
        material.comment = tuple(comments)

        return material


@dataclasses.dataclass
class MBuilder:
    """
    Builds ``M``.

    Attributes:
        suffix: Data card option suffix.
        substances: Tuple of material constituents.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    substances: list[str] | list[types.Substance]
    options: list[str] | list[m.MOption] = None

    def build(self):
        """
        Builds ``MBuilder`` into ``M``.

        Returns:
            ``M`` for ``MBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        substances = []
        for item in self.substances:
            if isinstance(item, types.Substance):
                substances.append(item)
            elif isinstance(item, str):
                substances.append(types.Substance.from_mcnp(item))
            else:
                substances.append(item.build())
        substances = types.Tuple(substances)

        options = []
        for item in self.options:
            if isinstance(item, m.MOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(m.MOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return M(
            suffix=suffix,
            substances=substances,
            options=options,
        )
