from enum import Enum

import molmass

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _elements


class MaterialValue:
    """
    ``MaterialValue`` represents INP material data card
    entries.

    ``MaterialValue`` implements INP material specifications
    as a Python inner class. Its attributes store different mateiral
    entries, and its methods provide entry points and endpoints for working
    with material entries. ``Material`` depends on ``MateiralValue`` as a
    data type.

    Attributes:
        zaid: Material value Zaid specifier.
        fraction: Material value fraction.
    """

    def __init__(self, zaid: types.Zaid, fraction: types.McnpReal):
        """
        ``__init__`` initializes ``MaterialValue``.

        Parameters:
            zaid: Material value Zaid specifier.
            fraction: Material value fraction.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        self.zaid: types.Zaid = zaid
        self.fraction: types.McnpReal = fraction

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``MaterialValue`` objects from INP.

        ``from_mcnp`` constructs instances of ``MaterialValue`` from INP
        source strings, so it operates as a class constructor method and
        INP parser helper function.

        Parameters:
            source: INP for mateiral values.

        Returns:
            ``MaterialValue`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_DATUM_MATERIAL, TOOLONG_DATUM_MATERIAL.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(" "),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL),
        )

        zaid = types.Zaid.from_mcnp(tokens.popl())
        fraction = types.McnpReal.from_mcnp(tokens.popl())

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL)

        return MaterialValue(zaid, fraction)

    def to_mcnp(self):
        """
        ``to_mcnp`` generates INP from ``MaterialValue`` objects.

        ``to_mcnp`` creates INP source string from ``MaterialValue``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``MaterialValue`` object.
        """

        return f"{self.zaid.to_mcnp()} {self.fraction.to_mcnp()}"


class MaterialKeyword(str, Enum):
    """
    ``MaterialKeyword`` represents INP material data card option
    keywords.

    ``MaterialKeyword`` implements INP material data card option
    keywords as a Python inner class. It enumerates MCNP keywords and
    provides methods for casting strings to ``MaterialKeyword``
    instances. It represents the INP material data card option keyword
    syntax element, so ``Material`` and ``MaterialOption`` depend on
    ``MaterialKeyword`` as an enum.
    """

    GAS = "gas"
    ESTEP = "estep"
    HSTEP = "hstep"
    NLIB = "nlib"
    PLIB = "plib"
    PNLIB = "pnlib"
    ELIB = "elib"
    HLIB = "hlib"
    ALIB = "alib"
    SLIB = "slib"
    TLIB = "tlib"
    DLIB = "dlib"
    COND = "cond"
    REFI = "refi"
    REFC = "refc"
    REFS = "refs"

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``MaterialKeyword`` objects from INP.

        ``from_mcnp`` constructs instances of ``MaterialKeyword`` from
        INP source strings, so it operates as a class constructor
        method and INP parser helper function.

        Parameters:
            source: INP for material option keyword.

        Returns:
            ``MaterialKeyword`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        # Processing Keyword
        if source not in [enum.value for enum in MaterialKeyword]:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD
            )

        return MaterialKeyword(source)


class MaterialOption:
    """
    ``MaterialOption`` represents INP material data card
    options.

    ``MaterialOption`` implements INP material data card
    options. Its attributes store keywords and values, and its methods
    provide entry and endpoints for working with INP mateiral data card
    options. It represents the generic INP material data card option syntax
    element, so ``Material`` depends on ``MaterialOptino`` as a genric data
    structre and superclass.

    Attributes:
        keyword: INP material option keyword.
        value: INP material option value.
    """

    def __init__(self, keyword: MaterialKeyword, value: any):
        """
        ``__init__`` initializes ``MaterialOption``.

        Parameters:
            keyword: Material specification data card option keyword.
            value: Material specification data card option value.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_KEYWORD.
        """

        if keyword is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD
            )

        match keyword:
            case MaterialKeyword.GAS:
                obj = Gas(value)
            case MaterialKeyword.ESTEP:
                obj = Estep(value)
            case MaterialKeyword.HSTEP:
                obj = Hstep(value)
            case MaterialKeyword.NLIB:
                obj = Nlib(value)
            case MaterialKeyword.PLIB:
                obj = Plib(value)
            case MaterialKeyword.PNLIB:
                obj = Pnlib(value)
            case MaterialKeyword.ELIB:
                obj = Elib(value)
            case MaterialKeyword.HLIB:
                obj = Hlib(value)
            case MaterialKeyword.ALIB:
                obj = Alib(value)
            case MaterialKeyword.SLIB:
                obj = Slib(value)
            case MaterialKeyword.TLIB:
                obj = Tlib(value)
            case MaterialKeyword.DLIB:
                obj = Dlib(value)
            case MaterialKeyword.COND:
                obj = Cond(value)
            case MaterialKeyword.REFI:
                obj = Refi(value)
            case MaterialKeyword.REFC:
                assert False, "Unimplemented"
            case MaterialKeyword.REFS:
                assert False, "Unimplemented"

        self.__dict__ = obj.__dict__
        self.__class__ = obj.__class__

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``MaterialOption`` objects from INP.

        ``from_mcnp`` constructs instances of ``MaterialOption`` from INP
        source strings, so it operates as a class constructor method and
        INP parser helper function. Although defined on the superclass, it
        returns ``MaterialOption`` subclasses.

        Parameters:
            source: INP for material option.

        Returns:
            ``MaterialOption`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_DATUM_MATERIAL, TOOLONG_DATUM_MATERIAL.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split("="),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL),
        )

        # Processing Keyword
        keyword = MaterialKeyword.from_mcnp(tokens.popl())

        # Processing Values
        match keyword:
            case MaterialKeyword.GAS:
                value = types.McnpInteger.from_mcnp(tokens.popl())

            case (
                MaterialKeyword.ESTEP
                | MaterialKeyword.HSTEP
                | MaterialKeyword.COND
                | MaterialKeyword.REFI
            ):
                value = types.McnpReal.from_mcnp(tokens.popl())

            case (
                MaterialKeyword.NLIB
                | MaterialKeyword.PLIB
                | MaterialKeyword.PNLIB
                | MaterialKeyword.ELIB
                | MaterialKeyword.HLIB
                | MaterialKeyword.ALIB
                | MaterialKeyword.SLIB
                | MaterialKeyword.TLIB
                | MaterialKeyword.DLIB
            ):
                value = tokens.popl()

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL)

        return MaterialOption(keyword, value)

    def to_mcnp(self):
        """
        ``to_mcnp`` generates INP from ``MaterialOption`` objects.

        ``to_mcnp`` creates INP source string from ``MaterialOption``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``MaterialOption`` object.
        """

        return f"{self.keyword.to_mcnp()}={self.value.to_mcnp()}"


class Gas(MaterialOption):
    """
    ``Gas`` represents INP Gas material data card options.

    ``Gas`` inherits attributes from ``MaterialOption``. It represents the
    INP Gas material data card option syntax element.

    Attributes:
        state: Flag for density-effect corection.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            state: Flag for density-effect corection.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.GAS
        self.value = state
        self.state = state


class Estep(MaterialOption):
    """
    ``Estep`` represents INP Estep material data card options.

    ``Estep`` inherits attributes from ``MaterialOption``. It represents the
    INP Estep material data card option syntax element.

    Attributes:
        step: Energy step increment.
    """

    def __init__(self, step: types.McnpReal):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            step: Energy step increment.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if step is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.ESTEP
        self.value = step
        self.step = step


class Hstep(MaterialOption):
    """
    ``Hstep`` represents INP Hstep material data card options.

    ``Hstep`` inherits attributes from ``MaterialOption``. It represents the
    INP Hstep material data card option syntax element.

    Attributes:
        step: Energy step increment.
    """

    def __init__(self, step: types.McnpReal):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            step: Energy step increment.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if step is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.HSTEP
        self.value = step
        self.step = step


class Nlib(MaterialOption):
    """
    ``Nlib`` represents INP Nlib material data card options.

    ``Nlib`` inherits attributes from ``MaterialOption``. It represents the
    INP Nlib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            abx: Table identifier default.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.NLIB
        self.value = abx
        self.abx = abx


class Plib(MaterialOption):
    """
    ``Plib`` represents INP Plib material data card options.

    ``Plib`` inherits attributes from ``MaterialOption``. It represents the
    INP Plib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            abx: Table identifier default.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.PLIB
        self.value = abx
        self.abx = abx


class Pnlib(MaterialOption):
    """
    ``Pnlib`` represents INP Pnlib material data card options.

    ``Pnlib`` inherits attributes from ``MaterialOption``. It represents the
    INP Pnlib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            value: Material data card option value.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.PNLIB
        self.value = abx
        self.abx = abx


class Elib(MaterialOption):
    """
    ``Elib`` represents INP Elib material data card options.

    ``Elib`` inherits attributes from ``MaterialOption``. It represents the
    INP Elib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            abx: Table identifier default.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.ELIB
        self.value = abx
        self.abx = abx


class Hlib(MaterialOption):
    """
    ``Hlib`` represents INP Hlib material data card options.

    ``Hlib`` inherits attributes from ``MaterialOption``. It represents the
    INP Hlib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            abx: Table identifier default.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.HLIB
        self.value = abx
        self.abx = abx


class Alib(MaterialOption):
    """
    ``Alib`` represents INP Alib material data card options.

    ``Alib`` inherits attributes from ``MaterialOption``. It represents the
    INP Alib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            abx: Table identifier default.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.ALIB
        self.value = abx
        self.abx = abx


class Slib(MaterialOption):
    """
    ``Slib`` represents INP Slib material data card options.

    ``Slib`` inherits attributes from ``MaterialOption``. It represents the
    INP Slib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            abx: Table identifier default.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.SLIB
        self.value = abx
        self.abx = abx


class Tlib(MaterialOption):
    """
    ``Tlib`` represents INP Tlib material data card options.

    ``Tlib`` inherits attributes from ``MaterialOption``. It represents the
    INP Tlib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            abx: Table identifier default.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.TLIB
        self.value = abx
        self.abx = abx


class Dlib(MaterialOption):
    """
    ``Dlib`` represents INP Dlib material data card options.

    ``Dlib`` inherits attributes from ``MaterialOption``. It represents the
    INP Dlib material data card option syntax element.

    Attributes:
        abx: Table identifier default.
    """

    def __init__(self, abx: str):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            abx: Table identifier default.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if abx is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.DLIB
        self.value = abx
        self.abx = abx


class Cond(MaterialOption):
    """
    ``Cond`` represents INP Cond material data card options.

    ``Cond`` inherits attributes from ``MaterialOption``. It represents the
    INP Cond material data card option syntax element.

    Attributes:
        conducation_state: Conduction state of material for ELO3.
    """

    def __init__(self, conducation_state: types.McnpReal):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            conducation_state: Conduction state of material for ELO3.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if conducation_state is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.COND
        self.value = conducation_state
        self.conducation_state = conducation_state


class Refi(MaterialOption):
    """
    ``Refi`` represents INP Refi material data card options.

    ``Refi`` inherits attributes from ``MaterialOption``. It represents the
    INP Refi material data card option syntax element.

    Attributes:
        index: Constant refractive index.
    """

    def __init__(self, index: types.McnpReal):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            index: Constant refractive index.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
        """

        if index is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE
            )

        self.keyword = MaterialKeyword.REFI
        self.value = index
        self.index = index


class Material(Datum):
    """
    ``Material`` represents INP matieral specification data cards.

    ``Material`` inherits attributes from ``Datum``. It represents the INP
    material data card syntax element.

    Attributes:
        substances: Tuple of substance specification.
        paris: Tuple of key-value pairs.
    """

    def __init__(
        self,
        substances: tuple[types.Zaid],
        pairs: tuple[MaterialOption],
        suffix: types.McnpInteger,
    ):
        """
        ``__init__`` initializes ``Material``.

        Parameters:
            substances: Tuple of substance specification.
            pairs: Tuple of key-value pairs.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in substances:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS
                )

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS
                )

        self.paris = pairs
        self.substances = substances

        _card.Card.__init__(self, f"m{suffix}")
        self.mnemonic = DatumMnemonic.MATERIAL
        self.parameters = tuple(list(substances) + list(pairs))
        self.suffix = suffix

    @staticmethod
    def from_formula(
        number: int, formulas: dict[str, float], atomic_or_weight: bool = True
    ):
        """
        ``from_formula`` generates ``Datum`` objects from INP.

        ``from_formula`` constructs instances of ``Datum`` from chemcials
        formulas and fractions, so it operates as a class constructor method.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            atomic_or_weight: Atomtic/Weight fraction true/false flag.

        Returns:
            ``Datum`` object.
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
                        types.Zaid(_elements.ELEMENTS[element]["z"], a),
                        isotropic_fraction,
                    )
                    for a, isotropic_fraction in _elements.ELEMENTS[element][
                        "fraction"
                    ].items()
                ]
                subcomments = [f"{element}-{zaid.a:03}" for zaid, _ in zaids]
                entries = [
                    MaterialValue(
                        zaid,
                        types.McnpReal(
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

        material = Material(substances, {}, suffix=types.McnpInteger(number))
        material.comment = tuple(comments)

        return material

    def to_mcnp(self) -> str:
        """Overrides the baseclass function."""

        if self.comment and isinstance(self.comment, tuple):
            if len(self.comment) == len(self.substances):
                return f"m{self.suffix.to_mcnp()} " + "\n   ".join(
                    f"{substance.to_mcnp()} $ {comment}"
                    for substance, comment in zip(self.substances, self.comment)
                )
            else:
                return super().to_mcnp() + "".join(
                    f" $ {comment}" for comment in self.comments
                )
        else:
            return super().to_mcnp()
