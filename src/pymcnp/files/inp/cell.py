"""
``cell`` contains the class representing INP cell cards.

``cell`` packages the ``Cell`` class, providing an object-oriented, importable
interface for INP cell cards.
"""


import re
from enum import StrEnum

from . import card
from .._utils import parser
from .._utils import errors
from .._utils import types


class Cell(card.Card):
    """
    ``Cell`` represents INP cell cards.

    ``Cell`` implements INP cell cards as a Python class. Its attributes store
    INP cell card input parameters, and its methods provide entry points and
    endpoints for working with MCNP cells. It represents the INP cell card
    syntax element, and it inherits from the ``Card`` super class.

    Attributes:
        number: Cell card number.
        material: Cell card material number.
        density: Cell card density value.
        geometry: Cell card geometry specification.
        parameters: Cell card parameter table.
    """

    class CellGeometry:
        """
        ``CellGeometry`` represents INP cell card geometry formulas.

        ``CellGeometry`` implements INP cell card geometry formulas as a
        Python inner class. Its attributes store different representations of
        INP cell card geometry formulas, and its methods provide entry points
        and endpoints for working with MCNP cell geometries. It represents the
        INP cell card geometry formula syntax element, so ``Cell`` depends on
        ``CellGeometry`` as a data type.

        Attributes:
            string: Geometry formula string representation.
            postfix: Geometry formula postfix representation.
        """

        _OPERATIONS_ORDER = {"#": 0, " ": 1, ":": 2}

        def __init__(self):
            """
            ``__init__`` initializes ``CellGeometry``.
            """

            self.string: str = None
            self.postfix: tuple[str] = None

        @classmethod
        def from_mcnp(cls, source: str):
            """
            ``from_mcnp`` generates ``CellGeometry`` objects from INP.

            ``from_mcnp`` constructs instances of ``CellGeometry`` from INP
            source strings, so it operates as a class constructor method and
            INP parser helper function. It runs the running shunting-yard
            algorithm to transform geometry formulas from infix notation to
            postfix notation while checking for syntax/semantic errors.

            Parameters:
                source: INP for cell geometry.

            Returns:
                ``CellGeometry`` object.

            Raises:
                MCNPSemanticError: INVALID_CELL_GEOMETRY.
                MCNPSyntaxError: TOOFEW_CELL_GEOMETRY, TOOLONG_CELL_GEOMETRY.
            """

            geometry = cls()

            source = parser.Preprocessor.process_inp(source)

            # Running Shunting-Yard Algorithm
            ops_stack = parser.Parser([], errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY))
            out_stack = parser.Parser([], errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY))
            inp_stack = re.findall(r"#|:| : |[()]| [()]|[()] | [()] | |[+-]?\d+", source)

            if "".join(inp_stack) != source:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_CELL_GEOMETRY)

            for token in inp_stack:
                if re.match(r"[+-]?\d+", token):
                    # Processing Surface Number

                    entry = types.cast_fortran_integer(token)
                    if entry is None or not (entry != 0 and -99_999_999 <= entry <= 99_999_999):
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY)

                    out_stack.pushr(token)

                elif re.match(r"#", token):
                    # Processing Unary Operator
                    ops_stack.pushr(token)

                elif re.match(r"([(]| [(]|[(] | [(] )", token):
                    # Processing Left Parenthesis
                    ops_stack.pushr("(")

                elif re.match(r"([)]| [)]|[)] | [)] )", token):
                    # Processing Right Parenthesis
                    while ops_stack.peekr() != "(":
                        out_stack.pushr(ops_stack.popr())

                    ops_stack.popr()

                elif re.match(r":| : | |: | :", token):
                    # Processing Binary Operator
                    token = token.strip() if token != " " else token

                    while (
                        ops_stack
                        and ops_stack.peekr() not in {"(", ")"}
                        and cls._OPERATIONS_ORDER[ops_stack.peekr()] >= cls._OPERATIONS_ORDER[token]
                    ):
                        out_stack.pushr(ops_stack.popr())

                    ops_stack.pushr(token)

                else:
                    # Unrecognized Character
                    assert False

            while ops_stack:
                out_stack.pushr(ops_stack.popr())

            geometry.postfix = tuple(out_stack.deque)
            geometry.string = source

            return geometry

        def to_mcnp(self) -> str:
            """
            ``to_mcnp`` generates INP from ``CellGeometry`` objects.

            ``to_mcnp`` creates INP source string from ``CellGeometry``
            objects, so it provides an MCNP endpoint.

            Returns:
                INP string for ``CellGeometry`` object.
            """

            return self.string

    class CellOption:
        """
        ``CellOption`` represents INP cell card options.

        ``CellOption`` implements INP cell card options. Its attributes store
        keywords and values, and its methods provide entry and endpoints for
        working with MCNP cell card options. It represents the generic INP cell
        card option syntax element, so ``Cell`` depends on ``CellOption`` as a
        generic data structure and superclass.

        Attributes:
            keyword: Cell card option keyword.
            value: Cell card option value.
        """

        class CellKeyword(StrEnum):
            """
            ``CellKeyword`` represents INP cell card option keywords.

            ``CellKeyword`` implements INP cell card option keywords as a
            Python inner class. It enumerates MCNP keywords and provides
            methods for casting strings to ``CellKeyword`` instances. It
            represents the INP cell card option keyword syntax element, so
            ``Cell`` and ``CellOption`` depends on ``CellKeyword`` as an enum.
            """

            IMPORTANCE = "imp"
            VOLUME = "vol"
            PHOTON_WEIGHT = "pwt"
            EXPONENTIAL_TRANSFORM = "ext"
            FORCED_COLLISION = "fcl"
            WEIGHT_WINDOW_BOUNDS = "wwn"
            DXTRAN_CONTRIBUTION = "dxc"
            FISSION_TURNOFF = "nonu"
            DETECTOR_CONTRIBUTION = "pd"
            GAS_THERMAL_TEMPERATURE = "tmp"
            UNIVERSE = "u"
            COORDINATE_TRANSFORMATION = "trcl"
            LATTICE = "lat"
            FILL = "fill"
            ENERGY_CUTOFF = "elpt"
            COSY = "cosy"
            BFIELD = "bflcl"
            UNCOLLIDED_SECONDARIES = "unc"

            @classmethod
            def from_mcnp(cls, source: str):
                """
                ``from_mcnp`` generates ``CellKeyword`` objects from INP.

                ``from_mcnp`` constructs instances of ``CellKeyword`` from INP
                source strings, so it operates as a class constructor method
                and INP parser helper function.

                Parameters:
                    source: INP for cell card option keyword.

                Returns:
                    ``CellKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_CELL_OPTION_KEYWORD.
                """

                source = parser.Preprocessor.process_inp(source)

                # Handling Star Modifier
                if source == "*trcl":
                    source = source[:1]

                # Handling Suffixes
                if source.startswith(("wwn", "dxc", "tmp")):
                    if len(source) < 4 or types.cast_fortran_integer(source[3:]) is None:
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD)

                    source = source[:3]
                elif source.startswith("pd"):
                    if len(source) < 3 and types.cast_fortran_integer(source[2:]) is None:
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD)

                    source = source[:2]

                # Processing Keyword
                if source not in [enum.value for enum in cls]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD)

                return cls(source)

            def to_mcnp(self) -> str:
                """
                ``to_mcnp`` generates INP from ``CellKeyword`` objects.

                ``to_mcnp`` creates INP source string from ``CellKeyword``
                objects, so it provides an MCNP endpoint.

                Returns:
                    INP string for ``CellKeyword`` object.
                """

                return self.value

        def __init__(self):
            """
            ``__init__`` initializes ``CellOption``.
            """

            self.keyword: self.CellKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: CellKeyword) -> None:
            """
            ``set_keyword`` stores INP cell card option keywords.

            ``set_keyword`` checks given arguments before assigning the
            given value to``CellOption.keyword``. If given an unrecognized
            argument, it raises semantic errors.

            Warnings:
                ``set_keyword`` reinitializes ``CellOption`` instances since
                its attributes depend of keyword. When the given keyword does
                not equal ``CellOption.keyword``, all attributes reset.

            Parameters:
                keyword: Cell card option keyword.

            Raises:
                MCNPSemanticError: INVALID_OPTION_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_OPTION_KEYWORD)

            if keyword != self.keyword:
                match keyword:
                    case self.CellKeyword.IMPORTANCE:
                        obj = Cell.Importance()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.VOLUME:
                        obj = Cell.Volume()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.PHOTON_WEIGHT:
                        obj = Cell.PhotonWeight()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.EXPONENTIAL_TRANSFORM:
                        obj = Cell.ExponentialTransform()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.FORCED_COLLISION:
                        obj = Cell.ForcedCollision()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.WEIGHT_WINDOW_BOUNDS:
                        obj = Cell.WeightWindowBounds()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.DXTRAN_CONTRIBUTION:
                        obj = Cell.DxtranContribution()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.FISSION_TURNOFF:
                        obj = Cell.FissionTurnoff()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.DETECTOR_CONTRIBUTION:
                        obj = Cell.DetectorContribution()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.GAS_THERMAL_TEMPERATURE:
                        obj = Cell.GasThermalTemperature()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.UNIVERSE:
                        obj = Cell.Universe()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.COORDINATE_TRANSFORMATION:
                        obj = Cell.CoordinateTransformation()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.LATTICE:
                        obj = Cell.Lattice()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.FILL:
                        obj = Cell.Fill()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.ENERGY_CUTOFF:
                        obj = Cell.EnergyCutoff()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.COSY:
                        obj = Cell.Cosy()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.BFIELD:
                        obj = Cell.Bfield()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case self.CellKeyword.UNCOLLIDED_SECONDARIES:
                        obj = Cell.UncollidedSecondaries()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__

        @classmethod
        def from_mcnp(cls, source: str):
            """
            ``from_mcnp`` generates ``CellOption`` objects from INP.

            ``from_mcnp`` constructs instances of ``CellOption`` from INP
            source strings, so it operates as a class constructor method and
            INP parser helper function. Although defined on the superclass, it
            returns ``CellOption`` subclasses.

            Parameters:
                source: INP for cell card option.

            Returns:
                ``CellOption`` object.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_KEYWORD.
                MCNPSyntaxError: TOOFEW_CELL_OPTION, TOOLONG_CELL_OPTION.
            """

            parameter = cls()

            source = parser.Preprocessor.process_inp(source)
            tokens = parser.Parser(re.split(r":|=", source), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_OPTION))

            # Processing Keyword
            keyword = cls.CellKeyword.from_mcnp(tokens.peekl())
            parameter.set_keyword(keyword)

            # Processing Values, Suffixes, & Designators
            match keyword:
                case cls.CellKeyword.IMPORTANCE:
                    # Processing Keyword
                    tokens.popl()

                    print(parameter.__class__)

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case cls.CellKeyword.VOLUME:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_real(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.PHOTON_WEIGHT:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_real(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.EXPONENTIAL_TRANSFORM:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case cls.CellKeyword.FORCED_COLLISION:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case cls.CellKeyword.WEIGHT_WINDOW_BOUNDS:
                    # Processing Suffix/Keyword
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    parameter.set_suffix(suffix)

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case cls.CellKeyword.DXTRAN_CONTRIBUTION:
                    # Processing Suffix/Keyword
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    parameter.set_suffix(suffix)

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case cls.CellKeyword.FISSION_TURNOFF:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.DETECTOR_CONTRIBUTION:
                    # Processing Suffix/Keyword
                    suffix = types.cast_fortran_integer(tokens.popl()[2:])
                    parameter.set_suffix(suffix)

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.GAS_THERMAL_TEMPERATURE:
                    # Processing Suffix/Keyword
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    parameter.set_suffix(suffix)

                    # Processing Value
                    entry = types.cast_fortran_real(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.UNIVERSE:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.COORDINATE_TRANSFORMATION:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.LATTICE:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.FILL:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.ENERGY_CUTOFF:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_real(tokens.popr())
                    parameter.set_value(entry)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case cls.CellKeyword.COSY:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.BFIELD:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                case cls.CellKeyword.UNCOLLIDED_SECONDARIES:
                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    entry = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(entry)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

            # Checking for Remaining Tokens
            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_CELL_OPTION)

            return parameter

        def to_mcnp(self) -> str:
            """
            ``to_mcnp`` generates INP from ``CellOption`` objects.

            ``to_mcnp`` creates INP source string from ``CellOption`` objects,
            so it provides an MCNP endpoint. Although defined on the
            superclass, it returns corrent INP for ``CellOption`` subclasses.

            Returns:
                INP string for ``CellOption`` object.
            """

            # Processing Suffix
            suffix_str = self.suffix if hasattr(self, "suffix") and self.suffix is not None else ""

            # Processing Designator
            designator_str = (
                f":{','.join(self.designator)}" if hasattr(self, "designator") and self.designator is not None else ""
            )

            return f"{self.keyword}{suffix_str}{designator_str}={self.value}"

        def to_arguments(self) -> dict:
            """
            ``to_arguments`` makes dictionaries from ``CellOption`` objects.

            ``to_arguments`` creates Python dictionaries from ``CellOption``
            objects, so it provides an MCNP endpoint. The dictionary keys
            follow the MCNP manual. Although defined on the superclass, it
            returns key-value pairs suffixes and designators as required.

            Returns:
                Dictionary for ``CellOption`` object.
            """

            return {
                "keyword": self.keyword.to_mcnp(),
                "m": self.suffix if hasattr(self.__class__, "suffix") else None,
                "n": self.designator if hasattr(self.__class__, "designator") else None,
                "value": self.value,
            }

    class CellOption_Designator(CellOption):
        """
        ``CellOption_Designator`` represents INP cell card options with
        designators.

        ``CellOption_Designator`` extends ``CellOption`` by adding attributes
        for storing and methods for parsing keyword designators. It represents
        the generic INP cell card option syntax element with designators.

        Attributes:
            designator: Cell card option keyword designator.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``CellOption_Designator``.
            """

            super().__init__()

            self.designator: tuple[types.Designator] = None

        def set_designator(self, designator: tuple[types.Designator]) -> None:
            """
            ``set_designator`` stores INP cell card option designators.

            ``set_designator`` checks for valid designators before assigning
            the given value to ``CellOption_Designator.designator``. If given
            an unrecognized argument, it raises semantic errors.

            Parameters:
                designators: Cell card option designator.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_DESIGNATOR.
            """

            if designator is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)

            self.designator = designator

    class CellOption_Suffix(CellOption):
        """
        ``CellOption_Suffix`` represents INP cell card options with suffixes.

        ``CellOption_Suffix`` extends ``CellOption`` by adding attributes for
        storing and methods for parsing keyword suffixes. It represents the
        generic INP cell card option syntax element with suffixes.

        Attributes:
            suffix: Cell card option keyword suffix.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``CellOption_Suffix``.
            """

            super().__init__()

            self.suffix: int = None

        def set_suffix(self, suffix: int) -> None:
            """
            ``set_suffix`` stores INP cell card option suffixes.

            ``set_suffix`` checks for valid suffixes before assigning the given
            value to ``CellOption_Suffix.suffix``. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                suffix: Cell card option suffix.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_SUFFIX.
            """

            if suffix is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX)

            self.suffix = suffix

    class Importance(CellOption_Designator):
        """
        ``Importance`` represents INP cell card importance options.

        ``Importance`` inherits attributes from ``CellOption_Designator``, i.e.
        ``CellOption`` with designator support. It represents the INP cell card
        importance option syntax element.

        Attributes:
            importance: Cell importance.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``Importance``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.IMPORTANCE

            self.importance: int = None

        def set_value(self, importance: int) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``Importance.importance`` and ``Importance.value``. If
            given an unrecognized argument, it raises semantic errors.

            Parameters:
                importance: Cell importance.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if importance is None or not (importance >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.importance = importance
            self.value = importance

    class Volume(CellOption):
        """
        ``Volume`` represents INP cell card volume options.

        ``Volume`` inherits attributes from ``CellOption``. It represents the
        INP cell card volume option syntax element.

        Attributes:
            volume: Cell volume.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Volume``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.VOLUME

            self.volume: float = None

        def set_value(self, volume: float) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``Volume.volume`` and ``Volume.value``. If given an
            unrecognized argument, it raises semantic errors.

            Parameters:
                volume: Cell volume.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if volume is None or not (volume > 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.volume = volume
            self.value = volume

    class PhotonWeight(CellOption):
        """
        ``PhotonWeight`` represents INP cell card photon weight options.

        ``PhotonWeight`` inherits attributes from ``CellOption``. It represents
        the INP cell card photon weight option syntax element.

        Attributes:
            weight: Cell weight of photons produced at neutron collisions.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``PhotonWeight``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.PHOTON_WEIGHT

            self.weight: float = None

        def set_value(self, weight: float) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``PhotonWeight.weight`` and ``PhotonWeight.value``. If
            given an unrecognized arguments, it raises semantic errors.

            Parameters:
                weight: Cell weight of photons produced at neutron collisions.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if weight is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.weight = weight
            self.value = weight

    class ExponentialTransform(CellOption_Designator):
        """
        ``ExponentialTransform`` represents INP cell card exponential transform
        options.

        ``ExponentialTransform`` inherits attributes from
        ``CellOption_Designator``, i.e. ``CellOption`` with designator support.
        It represents the INP cell card exponential transfrom option syntax
        element.

        Attributes:
            stretch: Cell exponential transform stretching specifier.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``ExponentialTransform``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.EXPONENTIAL_TRANSFORM

            self.stretch: any = None

        def set_value(self, stretch: any) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``ExponentialTransform.stretch`` and
            ``ExponentialTransform.value``. If given an unrecognized argument,
            it raises semantic errors.

            Parameters:
                stretch: Cell exponential transform stretching specifier.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if stretch is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.stretch = stretch
            self.value = stretch

    class ForcedCollision(CellOption_Designator):
        """
        ``ForcedCollision`` represents INP cell card forced collision options.

        ``ForcedCollision`` inherits attributes from ``CellOption_Designator``,
        i.e. ``CellOption`` with designator support. It represents the INP cell
        card forced collision option syntax element.

        Attributes:
            control: Cell forced-collision control.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``ForcedCollision``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.FORCED_COLLISION

            self.control: float = None

        def set_value(self, control: float) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``ForcedCollision.control`` and ``ForcedCollision.value``.
            If given an unrecognized argument, it raises semantic errors.

            Parameters:
                control: Cell forced-collision control.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if control is None or not (-1 <= control <= 1):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.control = control
            self.value = control

    class WeightWindowBounds(CellOption_Designator, CellOption_Suffix):
        """
        ``WeightWindowBounds`` represents INP cell card space-, time-, and
        energy-dependent weight-window bounds options.

        ``WeightWindowBounds`` inherits attributes from
        ``CellOption_Designator``, i.e. ``CellOption`` with designator support
        and ``CellOption_Suffix``, i.e. ``CellOption`` with suffix support. It
        represents the INP cell card space-, time-, and energy-dependent
        weight-window bounds option syntax element.

        Attributes:
            bound: Cell weight-window space, time, or energy lower bound.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``WeightWindowBounds``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.WEIGHT_WINDOW_BOUNDS

            self.bound: float = None

        def set_value(self, bound: float) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``WeightWindowBounds.bound`` and
            ``WeightWindowBounds.value``. If given an unrecognized argument, it
            raises semantic errors.

            Parameters:
                bound: Cell weight-window space, time, or energy lower bound.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if bound is None or not (bound == -1 or bound >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.weight = bound
            self.value = bound

    class DxtranContribution(CellOption_Designator, CellOption_Suffix):
        """
        ``DxtranContribution`` represents INP cell card DXTRAN contribution
        options.

        ``DxtranContribution`` inherits attributes from
        ``CellOption_Designator``, i.e. ``CellOption`` with designator support
        and ``CellOption_Suffix``, i.e. ``CellOption`` with suffix support. It
        represents the INP cell card DXTRAN contribution option syntax element.

        Attributes:
            probability: Cell probability of DXTRAN contribution.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``DxtranContribution``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.DXTRAN_CONTRIBUTION

            self.probability: float = None

        def set_value(self, probability: float) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DxtranContribution.probability`` and
            ``DxtranContribution.value``. If given an unrecognized argument, it
            raises semantic errors.

            Parameters:
                probability: Cell probability of DXTRAN contribution.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if probability is None or not (0 <= probability <= 1):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.probability = probability
            self.value = probability

    class FissionTurnoff(CellOption):
        """
        ``FissionTurnoff`` represents INP cell card fission turnoff options.

        ``FissionTurnoff`` inherits attributes from ``CellOption``. It
        represents  the INP cell card fission turnoff option syntax element.

        Attributes:
            setting: Cell fission setting.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``FissionTurnoff``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.FISSION_TURNOFF

            self.setting: int = None

        def set_value(self, setting: int) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``FissionTurnoff.setting`` and ``FissionTurnoff.value``.
            If given an unrecognized argument, it raises semantic errors.

            Parameters:
                setting: Cell fission setting.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if setting is None or not (setting in {0, 1, 2}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.setting = setting
            self.value = setting

    class DetectorContribution(CellOption_Suffix):
        """
        ``DxtranContribution`` represents INP cell card detector contribution
        options.

        ``DxtranContribution`` inherits attributes from ``CellOption_Suffix``,
        i.e. ``CellOption`` with suffix support. It represents the INP cell
        card detector contribution option syntax element.

        Attributes:
            probability: Cell probability of DXTRAN contribution.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``DetectorContribution``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.DETECTOR_CONTRIBUTION

            self.probability: float = None

        def set_value(self, probability: float) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DetectorContribution.probability`` and
            ``DetectorContribution.value``. If given an unrecognized argument,
            it raises semantic errors.

            Parameters:
                probability: Cell probability of DXTRAN contribution.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if probability is None or not (0 <= probability <= 1):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.probability = probability
            self.value = probability

    class GasThermalTemperature(CellOption_Suffix):
        """
        ``GasThermalTemperature`` represents INP cell card gas thermal
        temperature options.

        ``GasThermalTemperature`` inherits attributes from
        `CellOption_Suffix``, i.e. ``CellOption`` with suffix support. It
        represents the INP cell card gas thermal temperature option syntax
        element.

        Attributes:
            temperature: Cell temperature at suffix time index.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``GasThermaTemperature``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.GAS_THERMAL_TEMPERATURE

            self.temperature: any = None

        def set_value(self, temperature: any) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``GasThermalTemperature.temperature`` and
            ``GasThermalTemperature.value``. If given an unrecognized argument,
            it raises semantic errors.

            Parameters:
                temperature: Cell temperature at suffix time index.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if temperature is None or not (temperature >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.temperature = temperature
            self.value = temperature

    class Universe(CellOption):
        """
        ``Universe`` represents INP cell card universe options.

        ``Universe`` inherits attributes from ``CellOption``. It represents
        the INP cell card universe option syntax element.

        Attributes:
            number: Cell universe number.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``Universe``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.UNIVERSE

            self.number: int = None

        def set_value(self, number: int) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``Universe.number`` and ``Universe.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                number: Cell universe number.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if number is None or not (-99_999_999 <= number <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.number = number
            self.value = number

    class CoordinateTransformation(CellOption):
        """
        ``CoordinateTransformation`` represents INP cell card coordinate
        transformation options.

        ``CoordinateTransformation`` inherits attributes from ``CellOption``.
        It represents the INP cell card coordinate transformation option syntax
        element.

        Attributes:
            number: Cell coordinate transformation number.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``CoordinateTrsformation``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION

            self.number: int = None

        def set_value(self, number: int) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``CoordinateTransformation.number`` and
            ``CoordinateTransformation.value``. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                number: Cell coordinate transformation number.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if number is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.number = number
            self.value = number

    class Lattice(CellOption):
        """
        ``Lattice`` represents INP cell card lattice options.

        ``Lattice`` inherits attributes from ``CellOption``. It represents the
        INP cell card lattice option syntax element.

        Attributes:
            shape: Cell lattice shape.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``Lattice``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.LATTICE

            self.shape: int = None

        def set_value(self, shape: int) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``Lattice.shape`` and ``Lattice.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                shape: Cell lattice shape.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if shape is None or not (shape in {1, 2}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.shape = shape
            self.value = shape

    class Fill(CellOption):
        """
        ``Fill`` represents INP cell card fill options.

        ``Fill`` inherits attributes from ``CellOption``. It represents the
        INP cell card fill option syntax element.

        Attributes:
            number: Cell arbitrary universe number for fill.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``Fill``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.FILL

            self.number: any = None

        def set_value(self, value: any) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``Fill.number`` and ``Fill.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                number: Cell arbitrary universe number for fill.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if value is None or not (0 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.number = value
            self.value = value

    class EnergyCutoff(CellOption_Designator):
        """
        ``EnergyCutoff`` represents INP cell card energy cutoff options.

        ``EnergyCutoff`` inherits attributes from ``CellOption_Designator``,
        i.e. ``CellOption`` with designator support. It represents the INP cell
        card energy cutoff option syntax element.

        Attributes:
            cutoff: Cell energy cutoff.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``EnergyCutoff``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.ENERGY_CUTOFF

            self.cutoff: float = None

        def set_value(self, cutoff: float) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EnergyCutoff.cutoff`` and ``EnergyCutoff.value``. If
            given an unrecognized argument, it raises semantic errors.

            Parameters:
                cutoff: Cell energy cutoff.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if cutoff is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.cutoff = cutoff
            self.value = cutoff

    class Cosy(CellOption):
        """
        ``Cosy`` represents INP cell card cosy map options.

        ``Cosy`` inherits attributes from ``CellOption``. It represents the INP
        cell card cosy map option syntax element.

        Attributes:
            number: Cell cosy map number.
        """

        def __init__(self):
            """
            ``__init_`` initializes ``Cosy``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.COSY

            self.number: int = None

        def set_value(self, number: int) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``Cosy.number`` and ``Cosy.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                number: Cell cosy map number.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if number is None and (number >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.number = number
            self.value = number

    class Bfield(CellOption):
        """
        ``Bfield`` represents INP cell card magnetic field options.

        ``Bfield`` inherits attributes from ``CellOption``. It represents the
        INP cell card magnetic field option syntax element.

        Attributes:
            number: Cell magnetic field number.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Bfield``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.BFIELD

            self.number: int = None

        def set_value(self, number: int) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``Bfield.number`` and ``Bfield.value``. If given an
            unrecognized argument, it raises semantic errors.

            Parameters:
                number: Cell magnetic field number.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if number is None or not (number >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.number = number
            self.value = number

    class UncollidedSecondaries(CellOption_Designator):
        """
        ``UncollidedSecondaries`` represents INP cell card uncollided
        secondaries options.

        ``UncollidedSecondaries`` inherits attributes from
        ``CellOption_Designator``, i.e. ``CellOption`` with designator support.
        It represents the INP cell card uncollided secondaires option syntax
        element.

        Attributes:
            setting: Cell uncollided secondaries setting.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``UncollidedSecondaries``.
            """

            super().__init__()
            self.keyword = Cell.CellOption.CellKeyword.UNCOLLIDED_SECONDARIES

            self.setting: any = None

        def set_value(self, value: any) -> None:
            """
            ``set_value`` stores INP cell card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``UncollidedSecondaries.setting`` and
            ``UncollidedSecondaries.value``. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                setting: Cell uncollided secondaries setting.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if value is None or not (value in {0, 1}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.setting = value
            self.value = value

    def __init__(self):
        """
        ``__init__`` initializes ``Cell``.
        """

        super().__init__()

        self.number: int = None
        self.mateiral: int = None
        self.density: float = None
        self.geometry: str = None
        self.options: tuple[Cell.CellOption] = None

    def set_number(self, number: int) -> None:
        """
        ``set_number`` stores INP cell card number.

        ``set_number`` checks given arguments before assigning the given value
        to ``Cell.number``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            number: Cell card number.

        Raises:
            MCNPSemanticError: INVALID_CELL_NUMBER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_NUMBER)

        self.number = number
        self.id = number

    def set_material(self, material: int) -> None:
        """
        ``set_material`` stores INP cell card material.

        ``set_material`` checks given arguments before assigning the given
        value to ``Cell.material``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            number: Cell card number.

        Raises:
            MCNPSemanticError: INVALID_CELL_MATERIAL.
        """

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_MATERIAL)

        self.material = material

    def set_density(self, density: float) -> None:
        """
        ``set_density`` stores INP cell card material.

        ``set_density`` checks given arguments before assigning the given value
        to ``Cell.density``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            density: Cell card density.

        Raises:
            MCNPSemanticError: INVALID_CELL_DENSITY.
        """

        if density is None or density == 0:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_DENSITY)

        self.density = density

    def set_geometry(self, geometry: CellGeometry) -> None:
        """
        ``set_geometry`` stores INP cell card geometry.

        ``set_geometry`` checks given arguments before assigning the given
        value to ``Cell.geometry``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            geometry: Cell card geometry.

        Raises:
            MCNPSemanticError: INVALID_CELL_GEOMETRY.
        """

        if geometry is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY)

        self.geometry = geometry

    def set_options(self, options: tuple[CellOption]) -> None:
        """
        ``set_options`` stores INP cell card geometry.

        ``set_options`` checks given arguments before assigning the given value
        to ``Cell.options``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            options: Cell card options.

        Raises:
            MCNPSemanticError: INVALID_CELL_OPTION.
        """

        for option in options:
            if option is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION)

        self.options = options

    @classmethod
    def from_mcnp(cls, source: str, line: int = None):
        """
        ``from_mcnp`` generates ``Cell`` objects from INP.

        ``from_mcnp`` constructs instances of ``Cell`` from INP source strings,
        so it operates as a class constructor method and INP parser helper
        function.

        Parameters:
            source: INP for cell.
            line: Line number.

        Returns:
            ``Cell`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_CELL, TOOLONG_CELL.
        """

        cell = cls()

        # Processing Line Number
        cell.line = line

        # Processing Inline Comment
        if "$" in source:
            source, comment = source.split("$")
            cell.comment = comment

        source = parser.Preprocessor.process_inp(source)
        tokens = parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL))

        # Processing Number
        entry = types.cast_fortran_integer(tokens.popl())
        cell.set_number(entry)

        # Processing Material
        entry = types.cast_fortran_integer(tokens.popl())
        cell.set_material(entry)

        # Processing Density
        if cell.material != 0:
            entry = types.cast_fortran_real(tokens.popl())
            cell.set_density(entry)

        # Processing Geometry
        geometry = []
        while tokens:
            keyword, *_ = re.split(r":|=", tokens.peekl())

            # Adding geometries to list until option keyword found.
            try:
                cls.CellOption.CellKeyword.from_mcnp(keyword)
                break
            except errors.MCNPSemanticError as err:
                geometry.append(tokens.popl())
                pass

        entry = cls.CellGeometry().from_mcnp(" ".join(geometry))
        cell.set_geometry(entry)

        # Processing Options
        entries = []
        while tokens:
            # Adding values to list until option keyword found.
            values = []
            while tokens:
                keyword, *_ = re.split(r":|=", tokens.peekl())

                # Adding values to list until option keyword found.
                try:
                    cls.CellOption.CellKeyword.from_mcnp(keyword)
                    break
                except errors.MCNPSemanticError as err:
                    values.append(tokens.popl())
                    pass

            entry = cls.CellOption().from_mcnp(tokens.popl() + " " + " ".join(values))
            entries.append(entry)

        cell.set_options(tuple(entries))

        return cell

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Cell`` objects.

        ``to_mcnp`` creates INP source string from ``Cell`` objects,
        so it provides an MCNP endpoint.

        Returns:
            INP string for ``Cell`` object.
        """

        # Formatting Density
        density_str = f" {self.density}" if self.material else ""

        # Formatting Geometry
        geometry_str = self.geometry.to_mcnp()

        # Formatting Parameters
        options_str = " ".join(param.to_mcnp() for param in self.options)

        return parser.Postprocessor.add_continuation_lines(
            f"{self.number} {self.material}{density_str} {geometry_str} {options_str}"
        )

    def to_arguments(self) -> dict:
        """
        ``to_arguments`` makes dictionaries from ``Cell`` objects.

        ``to_arguments`` creates Python dictionaries from ``Cell`` objects, so
        it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual.

        Returns:
            Dictionary for ``Cell`` object.
        """

        return {
            "j": self.number,
            "m": self.material,
            "d": self.density,
            "geom": self.geometry.to_mcnp(),
            "params": [param.to_arguments() for param in self.options],
        }
