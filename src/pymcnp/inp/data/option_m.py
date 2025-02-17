import re
import typing

import molmass

from . import m
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _elements


class DataOption_M(_option.DataOption_, keyword='m'):
    """
    Represents INP data card m options.

    Attributes:
        substances: Tuple of material constituents.
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Am(\d+?)((( \S+)( \S+))+)(( (((gas)( \S+))|((estep)( \S+))|((hstep)( \S+))|((nlib)( \S+))|((plib)( \S+))|((pnlib)( \S+))|((elib)( \S+))|((hlib)( \S+))|((alib)( \S+))|((slib)( \S+))|((tlib)( \S+))|((dlib)( \S+))|((cond)( \S+))|((refi)( \S+))|((refc)(( \S+)+))|((refs)(( \S+)+))))+)?\Z'
    )

    def __init__(
        self,
        substances: tuple[m.MEntry_Substance],
        suffix: types.Integer,
        options: tuple[m.MOption_] = None,
    ):
        """
        Initializes ``DataOption_M``.

        Parameters:
            substances: Tuple of material constituents.
            suffix: Data card option suffix.
            options: Dictionary of options.

        Returns:
            ``DataOption_M``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if substances is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, substances)
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([substances, options])
        self.substances: typing.Final[tuple[m.MEntry_Substance]] = substances
        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[dict[str, m.MOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_M`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_M``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_M._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        substances = types._Tuple(
            [
                m.MEntry_Substance.from_mcnp(token[0])
                for token in m.MEntry_Substance._REGEX.finditer(tokens[2])
            ]
        )
        options = (
            types._Tuple(tuple(_parser.process_inp_option(m.MOption_, tokens[4])))
            if tokens[4]
            else None
        )

        return DataOption_M(substances, suffix, options)

    @staticmethod
    def from_formula(number: int, formulas: dict[str, float], atomic_or_weight: bool = True):
        """
        Generates ``DataOption_M`` from INP.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            atomic_or_weight: Atomtic/Weight fraction true/false flag.

        Returns:
            ``DataOption_M`` object.
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
                    m.MEntry_Substance(
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

        material = DataOption_M(substances, types.Integer(number), [])
        material.comment = tuple(comments)

        return material
