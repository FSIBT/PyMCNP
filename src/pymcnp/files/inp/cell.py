"""
``cell`` contains the class representing INP cell cards.

``cell`` packages the ``Cell`` class, providing an object-oriented, importable
interface for INP cell cards.
"""


import re
from enum import StrEnum
from typing import Union

from . import card
from ..utils import _parser
from ..utils import errors
from ..utils import types


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
        options: Cell card parameter table.
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
        """

        _OPERATIONS_ORDER = {"#": 0, " ": 1, ":": 2}

        def __init__(self, formula: str):
            """
            ``__init__`` initializes ``CellGeometry``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                formula: INP for cell geometry.

            Raises:
                MCNPSemanticError: INVALID_CELL_GEOMETRY.
                MCNPSyntaxError: TOOFEW_CELL_GEOMETRY, TOOLONG_CELL_GEOMETRY.
            """

            formula = _parser.Preprocessor.process_inp(formula, hasColumnarData=False)

            if not formula:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY)

            # Running Shunting-Yard Algorithm
            ops_stack = _parser.Parser([], errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY))
            out_stack = _parser.Parser([], errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY))
            inp_stack = re.findall(r"#|:| : |[()]| [()]|[()] | [()] | |[+-]?\d+", formula)

            if "".join(inp_stack) != formula:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY)

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
                        and self._OPERATIONS_ORDER[ops_stack.peekr()] >= self._OPERATIONS_ORDER[token]
                    ):
                        out_stack.pushr(ops_stack.popr())

                    ops_stack.pushr(token)

                else:
                    # Unrecognized Character
                    assert False

            while ops_stack:
                out_stack.pushr(ops_stack.popr())

            self.formula = formula

        @staticmethod
        def from_mcnp(source: str) -> str:
            """
            ``from_mcnp`` generates ``CellGeometry`` objects from INP.

            ``from_mcnp`` constructs instances of ``CellGeometry`` from INP
            source strings, so it operates as a class constructor method
            and INP parser helper function.

            Parameters:
                source: INP for cell card geometry.

            Returns:
                ``CellGeometry`` object.
            """

            return Cell.CellGeometry(source)

        def to_mcnp(self) -> str:
            """
            ``to_mcnp`` generates INP from ``CellGeometry`` objects.

            ``to_mcnp`` creates INP source string from ``CellGeometry``
            objects, so it provides an MCNP endpoint.

            Returns:
                INP string for ``CellGeometry`` object.
            """

            return self.formula

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
            COORDINATE_TRANSFORMATION_ANGLE = "*trcl"
            LATTICE = "lat"
            FILL = "fill"
            FILL_ANGLE = "*fill"
            ENERGY_CUTOFF = "elpt"
            COSY = "cosy"
            BFIELD = "bflcl"
            UNCOLLIDED_SECONDARIES = "unc"

            @staticmethod
            def from_mcnp(source: str):
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

                source = _parser.Preprocessor.process_inp(source)

                if source not in [enum.value for enum in Cell.CellOption.CellKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD)

                return Cell.CellOption.CellKeyword(source)

            def to_mcnp(self) -> str:
                """
                ``to_mcnp`` generates INP from ``CellKeyword`` objects.

                ``to_mcnp`` creates INP source string from ``CellKeyword``
                objects, so it provides an MCNP endpoint.

                Returns:
                    INP string for ``CellKeyword`` object.
                """

                return self.value

        def __init__(self, keyword: CellKeyword, value: any, suffix: int = None, designator: types.Designator = None):
            """
            ``__init__`` initializes ``CellOption``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                keyword: Cell card option keyword.
                value: Cell card option value.
                suffix: Cell card option suffix.
                designator: Cell card option particle designator.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD)

            match keyword:
                case Cell.CellOption.CellKeyword.IMPORTANCE:
                    obj = Cell.Importance(value, designator)
                case Cell.CellOption.CellKeyword.VOLUME:
                    obj = Cell.Volume(value)
                case Cell.CellOption.CellKeyword.PHOTON_WEIGHT:
                    obj = Cell.PhotonWeight(value)
                case Cell.CellOption.CellKeyword.EXPONENTIAL_TRANSFORM:
                    obj = Cell.ExponentialTransform(value, designator)
                case Cell.CellOption.CellKeyword.FORCED_COLLISION:
                    obj = Cell.ForcedCollision(value, designator)
                case Cell.CellOption.CellKeyword.WEIGHT_WINDOW_BOUNDS:
                    obj = Cell.WeightWindowBounds(value, designator, suffix)
                case Cell.CellOption.CellKeyword.DXTRAN_CONTRIBUTION:
                    obj = Cell.DxtranContribution(value, designator, suffix)
                case Cell.CellOption.CellKeyword.FISSION_TURNOFF:
                    obj = Cell.FissionTurnoff(value)
                case Cell.CellOption.CellKeyword.DETECTOR_CONTRIBUTION:
                    obj = Cell.DetectorContribution(value, suffix)
                case Cell.CellOption.CellKeyword.GAS_THERMAL_TEMPERATURE:
                    obj = Cell.GasThermalTemperature(value, suffix)
                case Cell.CellOption.CellKeyword.UNIVERSE:
                    obj = Cell.Universe(value)
                case Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION:
                    obj = Cell.CoordinateTransformation(value, is_angle=False)
                case Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION_ANGLE:
                    obj = Cell.CoordinateTransformation(value, is_angle=True)
                case Cell.CellOption.CellKeyword.LATTICE:
                    obj = Cell.Lattice(value)
                case Cell.CellOption.CellKeyword.FILL:
                    obj = Cell.Fill(value, is_angle=False)
                case Cell.CellOption.CellKeyword.FILL_ANGLE:
                    obj = Cell.Fill(value, is_angle=True)
                case Cell.CellOption.CellKeyword.ENERGY_CUTOFF:
                    obj = Cell.EnergyCutoff(value, designator)
                case Cell.CellOption.CellKeyword.COSY:
                    obj = Cell.Cosy(value)
                case Cell.CellOption.CellKeyword.BFIELD:
                    obj = Cell.Bfield(value)
                case Cell.CellOption.CellKeyword.UNCOLLIDED_SECONDARIES:
                    obj = Cell.UncollidedSecondaries(value, designator)
                case _:
                    assert False, "Impossible"

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(source: str):
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
                MCNPSemanticError: INVALID_CELL_OPTION.
                MCNPSyntaxError: TOOFEW_CELL_OPTION, TOOLONG_CELL_OPTION.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(
                re.split(r":|=| ", source), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_OPTION)
            )

            # Processing Keyword
            keyword = re.search(r"^[a-zA-z*]+", tokens.peekl())
            keyword = keyword.group() if keyword else ""
            keyword = Cell.CellOption.CellKeyword.from_mcnp(keyword)

            # Processing Values, Suffixes, & Designators
            suffix = None
            match keyword:
                case Cell.CellOption.CellKeyword.IMPORTANCE:
                    tokens.popl()
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())

                case Cell.CellOption.CellKeyword.VOLUME:
                    tokens.popl()
                    value = types.cast_fortran_real(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.PHOTON_WEIGHT:
                    tokens.popl()
                    value = types.cast_fortran_real(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.EXPONENTIAL_TRANSFORM:
                    tokens.popl()
                    value = types.cast_fortran_real(tokens.popr())
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())

                case Cell.CellOption.CellKeyword.FORCED_COLLISION:
                    tokens.popl()
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())

                case Cell.CellOption.CellKeyword.WEIGHT_WINDOW_BOUNDS:
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())

                case Cell.CellOption.CellKeyword.DXTRAN_CONTRIBUTION:
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())

                case Cell.CellOption.CellKeyword.FISSION_TURNOFF:
                    tokens.popl()
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.DETECTOR_CONTRIBUTION:
                    suffix = types.cast_fortran_integer(tokens.popl()[2:])
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.GAS_THERMAL_TEMPERATURE:
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    value = types.cast_fortran_real(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.UNIVERSE:
                    tokens.popl()
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.LATTICE:
                    tokens.popl()
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.ENERGY_CUTOFF:
                    tokens.popl()
                    value = types.cast_fortran_real(tokens.popr())
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())

                case Cell.CellOption.CellKeyword.COSY:
                    tokens.popl()
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.BFIELD:
                    tokens.popl()
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = None

                case Cell.CellOption.CellKeyword.UNCOLLIDED_SECONDARIES:
                    tokens.popl()
                    value = types.cast_fortran_integer(tokens.popr())
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())

                case Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION | Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION_ANGLE:
                    tokens.popl()
                    entries = [types.cast_fortran_integer(tokens.popl()) for token in range(0, len(tokens))]
                    designator = None

                    if len(entries) == 13:
                        value = tuple(entries)
                    elif len(entries) == 1:
                        value = entries[0]
                    else:
                        raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.TOOLONG_CELL_OPTION)

                case Cell.CellOption.CellKeyword.FILL | Cell.CellOption.CellKeyword.FILL_ANGLE:
                    tokens.popl()
                    entries = [types.cast_fortran_integer(tokens.popl()) for token in range(0, len(tokens))]
                    designator = None

                    if ":" in source:
                        if len(entries) <= 6:
                            raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.TOOFEW_CELL_OPTION)

                        value = (
                            (entries[0], entries[1]),
                            (entries[2], entries[3]),
                            (entries[4], entries[5]),
                            tuple(entries[6:]),
                        )
                    else:
                        if len(entries) == 1:
                            value = (entries[0], None)
                        elif len(entries) == 2:
                            value = (entries[0], entries[1])
                        elif len(entries) == 14:
                            value = tuple(entries)
                        else:
                            raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.TOOFEW_CELL_OPTION)

                case _:
                    assert False, "Impossible"

            # Checking for Remaining Tokens
            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_CELL_OPTION)

            return Cell.CellOption(keyword, value, suffix=suffix, designator=designator)

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

            value_str = ""
            if isinstance(self.value, tuple):
                value_str = " ".join([str(param) for param in self.value])
            else:
                value_str = self.value

            return f"{self.keyword}{suffix_str}{designator_str}={value_str}"

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

    class Importance(CellOption):
        """
        ``Importance`` represents INP cell card importance options.

        ``Importance`` inherits attributes from ``CellOption``. It represents
        the INP cell card importance option syntax element.

        Attributes:
            importance: Cell importance.
            designator: Cell card option particle designator.
        """

        def __init__(self, importance: int, designator: types.Designator):
            """
            ``__init__`` initializes ``Importance``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                importance: Cell importance.
                designator: Cell card option particle designator.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if importance is None or not (importance >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if designator is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.IMPORTANCE
            self.importance: final[int] = importance
            self.value: final[int] = importance
            self.designator: final[types.Designator] = designator

    class Volume(CellOption):
        """
        ``Volume`` represents INP cell card volume options.

        ``Volume`` inherits attributes from ``CellOption``. It represents the
        INP cell card volume option syntax element.

        Attributes:
            volume: Cell volume.
        """

        def __init__(self, volume: float):
            """
            ``__init__`` initializes ``Volume``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                volume: Cell volume.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if volume is None or not (volume > 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.keyword: final[CellOption.Keyword] = Cell.CellOption.CellKeyword.VOLUME
            self.volume: final[float] = volume
            self.value: final[float] = volume

    class PhotonWeight(CellOption):
        """
        ``PhotonWeight`` represents INP cell card photon weight options.

        ``PhotonWeight`` inherits attributes from ``CellOption``. It represents
        the INP cell card photon weight option syntax element.

        Attributes:
            weight: Cell weight of photons produced at neutron collisions.
        """

        def __init__(self, weight: float):
            """
            ``__init__`` initializes ``PhotonWeight``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                weight: Cell weight of photons produced at neutron collisions.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if weight is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.PHOTON_WEIGHT
            self.weight: final[float] = weight
            self.value: final[float] = weight

    class ExponentialTransform(CellOption):
        """
        ``ExponentialTransform`` represents INP cell card exponential transform
        options.

        ``ExponentialTransform`` inherits attributes from ``CellOption``. It
        represents the INP cell card exponential transfrom option syntax
        element.

        Attributes:
            stretch: Cell exponential transform stretching specifier.
            designator: Cell card option particle designator.
        """

        def __init__(self, stretch: any, designator: types.Designator):
            """
            ``__init__`` initializes ``ExponentialTransform``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                stretch: Cell exponential transform stretching specifier.
                designator: Cell card option particle designator.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if stretch is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if designator is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.EXPONENTIAL_TRANSFORM
            self.stretch: final[any] = stretch
            self.value: final[any] = stretch
            self.designator: final[types.Desigantor] = designator

    class ForcedCollision(CellOption):
        """
        ``ForcedCollision`` represents INP cell card forced collision options.

        ``ForcedCollision`` inherits attributes from ``CellOption``. It
        represents the INP cell card forced collision option syntax element.

        Attributes:
            control: Cell forced-collision control.
            designator: Cell card option particle designator.
        """

        def __init__(self, control: float, designator: types.Designator):
            """
            ``__init__`` initializes ``ForcedCollision``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                control: Cell forced-collision control.
                designator: Cell card option particle designator.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if control is None or not (-1 <= control <= 1):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if designator is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.FORCED_COLLISION
            self.control: final[float] = control
            self.value: final[float] = control
            self.designator: final[types.Designator] = designator

    class WeightWindowBounds(CellOption):
        """
        ``WeightWindowBounds`` represents INP cell card space-, time-, and
        energy-dependent weight-window bounds options.

        ``WeightWindowBounds`` inherits attributes from ``CellOption``. It
        represents the INP cell card space-, time-, and energy-dependent
        weight-window bounds option syntax element.

        Attributes:
            bound: Cell weight-window space, time, or energy lower bound.
        """

        def __init__(self, bound: float, designator: types.Designator, suffix: int):
            """
            ``__init__`` initializes ``WeightWindowBounds``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                bound: Cell weight-window space, time, or energy lower bound.
                suffix: Cell card option suffix.
                designator: Cell card option particle designator.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if bound is None or not (bound == -1 or bound >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if designator is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)

            if suffix is None or not (suffix >= 1):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.WEIGHT_WINDOW_BOUNDS
            self.weight: final[float] = bound
            self.value: final[float] = bound
            self.designator: final[types.Designator] = designator
            self.suffix: final[int] = suffix

    class DxtranContribution(CellOption):
        """
        ``DxtranContribution`` represents INP cell card DXTRAN contribution
        options.

        ``DxtranContribution`` inherits attributes from ``CellOption``. It
        represents the INP cell card DXTRAN contribution option syntax element.

        Attributes:
            probability: Cell probability of DXTRAN contribution.
            suffix: Cell card option suffix.
            designator: Cell card option particle designator.
        """

        def __init__(self, probability: float, designator: types.Designator, suffix: int):
            """
            ``__init__`` initializes ``DxtranContribution``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                probability: Cell probability of DXTRAN contribution.
                suffix: Cell card option suffix.
                designator: Cell card option particle designator.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if probability is None or not (0 <= probability <= 1):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if designator is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)

            if suffix is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.DXTRAN_CONTRIBUTION
            self.probability: final[float] = probability
            self.value: final[float] = probability
            self.designator: final[types.Designator] = designator
            self.suffix: final[int] = suffix

    class FissionTurnoff(CellOption):
        """
        ``FissionTurnoff`` represents INP cell card fission turnoff options.

        ``FissionTurnoff`` inherits attributes from ``CellOption``. It
        represents the INP cell card fission turnoff option syntax element.

        Attributes:
            setting: Cell fission setting.
        """

        def __init__(self, setting: int):
            """
            ``__init_`` initializes ``FissionTurnoff``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                setting: Cell fission setting.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if setting is None or not (setting in {0, 1, 2}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.FISSION_TURNOFF
            self.setting: final[int] = setting
            self.value: final[int] = setting

    class DetectorContribution(CellOption):
        """
        ``DetectorContribution`` represents INP cell card detector contribution
        options.

        ``DetectorContribution`` inherits attributes from ``CellOption``. It
        represents the INP cell card detector contribution option syntax
        element.

        Attributes:
            probability: Cell probability of DXTRAN contribution.
            suffix: Cell card option suffix.
        """

        def __init__(self, probability: float, suffix: int):
            """
            ``__init_`` initializes ``DetectorContribution``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                probability: Cell probability of DXTRAN contribution.
                suffix: Cell card option suffix.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if probability is None or not (0 <= probability <= 1):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if suffix is None or not (0 < suffix <= 9999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.DETECTOR_CONTRIBUTION
            self.probability: final[float] = probability
            self.value: final[float] = probability
            self.suffix: final[int] = suffix

    class GasThermalTemperature(CellOption):
        """
        ``GasThermalTemperature`` represents INP cell card gas thermal
        temperature options.

        ``GasThermalTemperature`` inherits attributes from ``CellOption``. It
        represents the INP cell card gas thermal temperature option syntax
        element.

        Attributes:
            temperature: Cell temperature at suffix time index.
            suffix: Cell card option suffix.
        """

        def __init__(self, temperature: float, suffix: int):
            """
            ``__init_`` initializes ``GasThermalTemperature``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                temperature: Cell temperature at suffix time index.
                suffix: Cell card option suffix.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if temperature is None or not (temperature > 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if suffix is None or not (0 < suffix <= 99):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.GAS_THERMAL_TEMPERATURE
            self.temperature: final[float] = temperature
            self.value: final[float] = temperature
            self.suffix: final[int] = suffix

    class Universe(CellOption):
        """
        ``Universe`` represents INP cell card universe options.

        ``Universe`` inherits attributes from ``CellOption``. It represents
        the INP cell card universe option syntax element.

        Attributes:
            number: Cell universe number.
        """

        def __init__(self, number: int):
            """
            ``__init__`` initializes ``Universe``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                number: Cell universe number.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if number is None or not (-99_999_999 <= number <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.UNIVERSE
            self.number: final[int] = number
            self.value: final[int] = number

    class CoordinateTransformation(CellOption):
        """
        ``CoordinateTransformation`` represents INP cell card coordinate
        transformation options.

        ``CoordinateTransformation`` inherits attributes from ``CellOption``.
        It represents the INP cell card coordinate transformation option syntax
        element.

        Attributes:
            number: Cell coordinate transformation number.
            displacement: Cell coordinate transformation displacement vector.
            rotation: Cell coordinate transformation rotation matrix.
            system: Cell coordinate transformation coordinate system setting.
            is_angle: Cell coordinate angle units setting.
        """

        def __init__(self, value: Union[tuple, int], is_angle: bool = False):
            """
            ``__init__`` initializes ``CoordinateTransformation``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Since the INP cell coordinate transformations have two forms,
            ``__init__`` takes different value(s). It takes ``number`` or
            (``displacement``, ``rotation``, ``system``).

            Parameters:
                value: Cell coordinate transformation option value(s).
                is_angle: Cell coordinate angle units setting.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if is_angle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD)

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if is_angle:
                self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION_ANGLE
            else:
                self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION

            if isinstance(value, tuple):
                if len(value) != 13:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                for entry in value[:-1]:
                    if entry is None:
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                if value[-1] is None or value[-1] not in {-1, 1}:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                self.number: final[int] = None
                self.displacement: final[tuple[float]] = value[:3]
                self.rotation: final[tuple[float]] = value[3:-1]
                self.system: final[int] = value[-1]
                self.value: final[tuple] = value
                self.is_angle: final[bool] = is_angle
            elif isinstance(value, int):
                if not (1 <= value <= 999):
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                self.number: final[int] = value
                self.displacement: final[tuple[float]] = None
                self.rotation: final[tuple[float]] = None
                self.system: final[int] = None
                self.value: final[int] = value
                self.is_angle: final[bool] = is_angle
            else:
                assert False, "Impossible"

    class Lattice(CellOption):
        """
        ``Lattice`` represents INP cell card lattice options.

        ``Lattice`` inherits attributes from ``CellOption``. It represents the
        INP cell card lattice option syntax element.

        Attributes:
            shape: Cell lattice shape.
        """

        def __init__(self, shape: int):
            """
            ``__init__`` initializes ``Lattice``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                shape: Cell lattice shape.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if shape is None or not (shape in {1, 2}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.LATTICE
            self.shape: final[int] = shape
            self.value: final[int] = shape

    class Fill(CellOption):
        """
        ``Fill`` represents INP cell card fill options.

        ``Fill`` inherits attributes from ``CellOption``. It represents the
        INP cell card fill option syntax element.

        Attributes:
            number: Cell arbitrary universe number for fill.
            transform: Cell optional transformation number.
            displacement: Cell optional tranformation displacement vector.
            rotation: Cell optional tranformation rotation matrix.
            system: Cell optional tranformation coordinate system.
            ibounds: i direction upper and lower bounds.
            jbounds: j direction upper and lower bounds.
            kbounds: k direction upper and lower bounds.
            numbers: List of universe numbers to fill.
            is_angle: Cell coordinate angle units setting.
        """

        def __init__(self, value: tuple, is_angle: bool = False):
            """
            ``__init__`` initializes ``Fill``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Since the INP cell fill options have three forms,  ``__init__``
            takes different value(s). It takes (``number``, ``transform``)
            tuples, (``number``, displacment``, ``rotation``, ``system``)
            tuples, or (``ibounds``, ``jbounds``, ``kbounds``, ``numbers``).

            Parameters:
                value: Fill cell option value or value(s) tuple.
                is_angle: Cell coordinate angle units setting.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_KEYWORD.
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if is_angle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD)

            if value is None or not value:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if is_angle:
                self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.FILL_ANGLE
            else:
                self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.FILL

            if isinstance(value[0], int):
                if len(value) == 2:
                    if value[0] is None or not (0 <= value[0] <= 99_999_999):
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                    if value[1] is not None and not (0 <= value[1] <= 999):
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                    self.number: final[int] = value[0]
                    self.transform: final[int] = value[1]
                    self.displacement: final[tuple[int]] = None
                    self.rotation: final[tuple[tuple[int]]] = None
                    self.system: final[int] = None
                    self.ibounds: final[tuple[int]] = None
                    self.jbounds: final[tuple[int]] = None
                    self.kbounds: final[tuple[int]] = None
                    self.numbers: final[tuple[int]] = None
                    self.value: final[tuple] = value
                    self.is_angle: final[bool] = is_angle
                elif len(value) == 14:
                    if value[0] is None or not (0 <= value[0] <= 99_999_999):
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                    for entry in value[1:-1]:
                        if entry is None:
                            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                    if value[-1] is None or value[-1] not in {-1, 1}:
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                    self.number: final[int] = value[0]
                    self.transform: final[int] = None
                    self.displacement: final[tuple[int]] = value[1:4]
                    self.rotation: final[tuple[int]] = value[4:12]
                    self.system: final[int] = value[13]
                    self.ibounds: final[tuple[int]] = None
                    self.jbounds: final[tuple[int]] = None
                    self.kbounds: final[tuple[int]] = None
                    self.numbers: final[tuple[int]] = None
                    self.value: final[tuple] = value
                    self.is_angle: final[bool] = is_angle
            elif isinstance(value[0], tuple):
                if (
                    value[0] is None
                    or len(value[0]) != 2
                    or value[0][0] is None
                    or value[0][1] is None
                    or not (0 <= value[0][0])
                    or not (0 <= value[0][1])
                    or not (value[0][0] <= value[0][1])
                ):
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                if (
                    value[1] is None
                    or len(value[1]) != 2
                    or value[1][0] is None
                    or value[1][1] is None
                    or not (0 <= value[1][0])
                    or not (0 <= value[1][1])
                    or not (value[1][0] <= value[1][1])
                ):
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                if (
                    value[2] is None
                    or len(value[2]) != 2
                    or value[2][0] is None
                    or value[2][1] is None
                    or not (0 <= value[2][0])
                    or not (0 <= value[2][1])
                    or not (value[2][0] <= value[2][1])
                ):
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                if value[3] is None or len(value[3]) != (
                    (value[0][1] - value[0][0] + 1) * (value[1][1] - value[1][0] + 1) * (value[2][1] - value[2][0] + 1)
                ):
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                for number in value[3]:
                    if number is None or not (0 <= number <= 99_999_999):
                        raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

                self.number: final[int] = None
                self.transform: final[int] = None
                self.displacement: final[tuple[int]] = None
                self.rotation: final[tuple[tuple[int]]] = None
                self.system: final[int] = None
                self.ibounds: final[tuple[int]] = value[0]
                self.jbounds: final[tuple[int]] = value[1]
                self.kbounds: final[tuple[int]] = value[2]
                self.numbers: final[tuple[int]] = value[3]
                self.value: final[tuple] = value
                self.is_angle: final[bool] = is_angle
            else:
                assert False, "Nope"

    class EnergyCutoff(CellOption):
        """
        ``EnergyCutoff`` represents INP cell card energy cutoff options.

        ``EnergyCutoff`` inherits attributes from ``CellOption``. It represents
        the INP cell card energy cutoff option syntax element.

        Attributes:
            cutoff: Cell energy cutoff.
            designator: Cell card option particle designator.
        """

        def __init__(self, cutoff: float, designator: types.Designator):
            """
            ``__init__`` initializes ``EnergyCutoff``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                cutoff: Cell energy cutoff.
                designator: Cell card option particle designator.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if cutoff is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if designator is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)

            self.keyword: final[Cell.CellOption.CellKeyword] = Cell.CellOption.CellKeyword.ENERGY_CUTOFF
            self.value: final[float] = cutoff
            self.cutoff: final[float] = cutoff
            self.designator: final[types.Designator] = designator

    class Cosy(CellOption):
        """
        ``Cosy`` represents INP cell card cosy map options.

        ``Cosy`` inherits attributes from ``CellOption``. It represents the INP
        cell card cosy map option syntax element.

        Attributes:
            number: Cell cosy map number.
        """

        def __init__(self, number: int):
            """
            ``__init_`` initializes ``Cosy``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                number: Cell cosy map number.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if number is None or not (number in {1, 2, 3, 4, 5, 6}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.keyword: final[CellOption.CellKeyword] = Cell.CellOption.CellKeyword.COSY
            self.value: final[int] = number
            self.number: final[int] = number

    class Bfield(CellOption):
        """
        ``Bfield`` represents INP cell card magnetic field options.

        ``Bfield`` inherits attributes from ``CellOption``. It represents the
        INP cell card magnetic field option syntax element.

        Attributes:
            number: Cell magnetic field number.
        """

        def __init__(self, number: int):
            """
            ``__init__`` initializes ``Bfield``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                number: Cell magnetic field number.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
            """

            if number is None or not (number >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            self.keyword: final[CellOption.Cellkeyword] = Cell.CellOption.CellKeyword.BFIELD
            self.value: final[int] = number
            self.number: final[int] = number

    class UncollidedSecondaries(CellOption):
        """
        ``UncollidedSecondaries`` represents INP cell card uncollided
        secondaries options.

        ``UncollidedSecondaries`` inherits attributes from ``CellOption``. It
        represents the INP cell card uncollided secondaires option syntax
        element.

        Attributes:
            setting: Cell uncollided secondaries setting.
            designator: Cell card option particle designator.
        """

        def __init__(self, setting: int, designator: types.Designator):
            """
            ``__init__`` initializes ``UncollidedSecoies``.

            ``__init__`` checks given arguments before assigning the given
            value to their cooresponding attributes. If given an unrecognized
            argument, it raises semantic errors.

            Parameters:
                setting: Cell uncollided secondaries setting.
                designator: Cell card option particle designator.

            Raises:
                MCNPSemanticError: INVALID_CELL_OPTION_VALUE.
                MCNPSemanticError: INVALID_CELL_OPTION_DESIGNATOR.
            """

            if setting is None or not (setting in {0, 1}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)

            if designator is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)

            self.keyword: final[Cell.CellOption.Cellkeyword] = Cell.CellOption.CellKeyword.UNCOLLIDED_SECONDARIES
            self.value: final[int] = setting
            self.setting: final[int] = setting
            self.designator: final[types.Designator] = designator

    def __init__(self, number: int, material: int, density: float, geometry: CellGeometry, options: tuple[CellOption]):
        """
        ``__init__`` initializes ``Cell``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            number: Cell card number.
            material: Cell card material number.
            density: Cell card density value.
            geometry: Cell card geometry specification.
            parameters: Cell card parameter table.

        Raises:
            MCNPSemanticError: INVALID_CELL_NUMBER.
            MCNPSemanticError: INVALID_CELL_MATERIAL.
            MCNPSemanticError: INVALID_CELL_DENSITY.
            MCNPSemanticError: INVALID_CELL_MATERIAL.
            MCNPSemanticError: INVALID_CELL_GEOMETRY.
            MCNPSemanticError: INVALID_CELL_OPTION.
        """

        super().__init__(number)

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_NUMBER)

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_MATERIAL)

        if material != 0:
            if density is None or (density == 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_DENSITY)

        if geometry is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY)

        if options is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION)

        for option in options:
            if option is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION)

        self.number: final[int] = number
        self.material: final[int] = material
        self.density: final[int] = density if material != 0 else None
        self.geometry: final[CellGeometry] = geometry
        self.options: final[tuple[CellOption]] = options

    @staticmethod
    def from_mcnp(source: str, line: int = None):
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

        # Processing Inline Comment
        comment = None
        if "$" in source:
            source, comment = source.split("$")

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(re.split(r" |=", source), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL))

        # Processing Number, Material, & Density
        number = types.cast_fortran_integer(tokens.popl())
        material = types.cast_fortran_integer(tokens.popl())
        density = types.cast_fortran_real(tokens.popl()) if material != 0 else None

        # Processing Geometry
        geometry = []
        while tokens:
            try:
                try_keyword = re.search(r"[*]?[A-Za-z]+", tokens.peekl()).group()
                Cell.CellOption.CellKeyword.from_mcnp(try_keyword)
                break
            except:
                geometry.append(tokens.popl())
                pass

        geometry = Cell.CellGeometry(" ".join(geometry))

        # Processing Options
        options = []
        while tokens:
            keyword = tokens.popl()
            values = []
            while tokens:
                try:
                    try_keyword = re.search(r"([*]?[A-Za-z]+)", tokens.peekl()).group()
                    Cell.CellOption.CellKeyword.from_mcnp(try_keyword)
                    break
                except:
                    values.append(tokens.popl())
                    pass

            option = Cell.CellOption.from_mcnp(f"{keyword}={" ".join(values)}")
            options.append(option)

        options = tuple(options)

        cell = Cell(number, material, density, geometry, options)
        cell.line = line
        cell.comment = comment

        return cell

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Cell`` objects.

        ``to_mcnp`` creates INP source string from ``Cell`` objects,
        so it provides an MCNP endpoint.

        Returns:
            INP string for ``Cell`` object.
        """

        density_str = self.density if self.material else " "
        geometry_str = self.geometry.to_mcnp()
        options_str = " ".join(option.to_mcnp() for option in self.options)

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.number} {self.material} {density_str} {geometry_str} {options_str}"
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
            "params": [option.to_arguments() for option in self.options],
        }
