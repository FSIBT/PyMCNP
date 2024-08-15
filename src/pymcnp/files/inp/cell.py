"""
'cell' contains the class representing cell cards.

'cell' packages the 'Cell' class, providing an importable interface
for cell cards.
"""


import re
from typing import Self, Callable
from enum import StrEnum

from . import card
from .._utils import parser
from .._utils import errors
from .._utils import types


class Cell(card.Card):
    """
    'Cell' represents cell cards.

    'Cell' abstracts the cell card syntax element and it
    encapsulates all functionallity for parsing cell cards.

    Attributes:
        number: Cell card number.
        material: Cell material number.
        density: Cell density value.
        geometry: Cell geometry specification.
        parameters: Cell parameter table.
    """

    class CellGeometry:
        """
        'CellGeometry' represents cell card geometry formulas.

        'CellGeometry' functions as a data type for 'Cell'. It
        represents cell card geometry formulas as abstract
        syntax elements.

        Attributes:
            string: String representation.
            postfix: Postfix representation.
        """

        _OPERATIONS_ORDER = {"#": 0, " ": 1, ":": 2}

        def __init__(self) -> Self:
            """
            '__init__' initializes 'CellGeometry'
            """

            self.string: str = None
            self.postfix: tuple[str] = None

        @classmethod
        def from_mcnp(cls, source: str) -> Self:
            """
            'from_mcnp' generates cell geometry objects from.

            'from_mcnp' constructs instances of 'CellGeometry' from INP
            strings, so it functions as a class constructor. It
            transforms cell parameters into correct subclasses.

            Parameters:
                source: INP for cell geometry.

            Returns:
                Cell geometry object.

            Raises:
                MCNPSemanticError: Invalid cell geometry.
                MCNPSyntaxError: Extra tokens in cell geometry.
            """

            geometry = cls()

            source = parser.Preprocessor.process_inp(source)

            # Running Shunting-Yard Algorithm
            ops_stack = parser.Parser(
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY)
            )
            out_stack = parser.Parser(
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY)
            )
            inp_stack = re.findall(
                r"#|:| : |[()]| [()]|[()] | [()] | |[+-]?\d+", source
            )

            if "".join(inp_stack) != source:
                raise errors.MCNPSyntaxError(
                    errors.MCNPSyntaxCodes.TOOLONG_CELL_GEOMETRY
                )

            for token in inp_stack:
                if re.match(r"[+-]?\d+", token):
                    # Processing Surface Number

                    value = types.cast_fortran_integer(token)
                    if value is None or not (
                        value != 0 and -99_999_999 <= value <= 99_999_999
                    ):
                        raise errors.MCNPSemanticError(
                            errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY
                        )

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
                        and cls._OPERATIONS_ORDER[ops_stack.peekr()]
                        >= cls._OPERATIONS_ORDER[token]
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
            'to_mcnp' generates from cell geometry objects.

            'to_mcnp' provides an MCNP endpoints for writing
            INP source strings.

            Returns:
                INP for cell card object.
            """

            return self.string

    class CellParameter:
        """
        'CellParameter' represents cell card parameters.

        'CellParameter' functions as a data type for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.

        Attributes:
            keyword: cell card parameter keyword.
            value: cell card parameter value.
        """

        class CellKeyword(StrEnum):
            """
            'CellKeyword' represents cell card keywords.

            'CellParameter' functions as a data type for 'CellParameter'
            and 'Cell'. It represents cell card parameter keywords
            as abstract syntax elements.
            """

            IMP = "imp"
            VOL = "vol"
            PWT = "pwt"
            EXT = "ext"
            FCL = "fcl"
            WWN = "wwn"
            DXC = "dxc"
            NONU = "nonu"
            PD = "pd"
            TMP = "tmp"
            U = "u"
            TRCL = "trcl"
            LAT = "lat"
            FILL = "fill"
            ELPT = "elpt"
            COSY = "cosy"
            BFLCL = "bflcl"
            UNC = "unc"

            @classmethod
            def cast_cell_keyword(
                cls, string: str, hook: Callable[Self, bool] = lambda _: True
            ) -> Self:
                """
                'cast_cell_keyword' types casts from strings to cell keywords.

                'cast_cell_keyword' creates cell parameter keywords objects from
                strings. If the string is invalid or the hook returns false,
                it returns None.

                Returns:
                    Cell parameter keyword from string.
                """

                string = string.lower()

                if string.startswith("*"):
                    string = string[:1]

                if string.startswith(("wwn", "dxc", "tmp")):
                    if (
                        len(string) < 4
                        and types.cast_fortran_integer(string[:3]) is None
                    ):
                        return None

                    string = string[:3]
                elif string.startswith("pd"):
                    if (
                        len(string) < 3
                        and types.cast_fortran_integer(string[:2]) is None
                    ):
                        return None

                    string = string[:2]

                try:
                    keyword = cls(string)

                    if hook(keyword):
                        return keyword
                except ValueError:
                    pass

                return None

            def to_mcnp(self) -> str:
                """
                'to_mcnp' generates from cell card parameter keyword objects.

                'to_mcnp' provides an MCNP endpoints for writing
                source strings.

                Returns:
                    INP for cell card parameter keyword object.
                """

                return self.value

        def __init__(self) -> Self:
            """
            '__init__' initializes 'CellParameter'.
            """

            self.keyword: self.CellKeyword = None
            self.value: any = None

        @classmethod
        def from_mcnp(cls, string: str):
            """
            'from_mcnp' generates cell card parameter objects from.

            'from_mcnp' constructs instances of 'CellParameter' from
            INP strings, so it functions as a class constructor. It
            transforms cell parameters into their correct subclasses.

            Parameters:
                card: INP to parse.

            Returns:
                Cell card parameter object.

            Raises:
                MCNPSemanticError: Invalid cell card parameter entry.
                MCNPSyntaxError: Invalid cell card paramter syntax.
            """

            parameter = cls()

            tokens = parser.Parser(
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_PARAMETERS)
            ).from_string(string, r":|=")

            # Processing Keyword
            value = cls.CellKeyword.cast_cell_keyword(tokens.peekl())
            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_KEYWORD
                )
            parameter.set_keyword(value)

            # Processing Value & Designator
            match parameter.keyword:
                case "imp":
                    parameter.__class__ = Cell.Importance

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case "vol":
                    parameter.__class__ = Cell.Volume

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_real(tokens.popr())
                    parameter.set_value(value)

                case "pwt":
                    parameter.__class__ = Cell.ProtonWeight

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_real(tokens.popr())
                    parameter.set_value(value)

                case "ext":
                    parameter.__class__ = Cell.ExponentialTransform

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case "fcl":
                    parameter.__class__ = Cell.ForcedCollision

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case "wwn":
                    parameter.__class__ = Cell.WeightWindowBounds

                    # Processing Suffix/Keyword
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    parameter.set_suffix(suffix)

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case "dxc":
                    parameter.__class__ = Cell.DxtranContribution

                    # Processing Suffix/Keyword
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    parameter.set_suffix(suffix)

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case "nonu":
                    parameter.__class__ = Cell.FissionTurnOff

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                case "pd":
                    parameter.__class__ = Cell.DetectorContribution

                    # Processing Suffix/Keyword
                    suffix = types.cast_fortran_integer(tokens.popl()[2:])
                    parameter.set_suffix(suffix)

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                case "tmp":
                    parameter.__class__ = Cell.GasThermalTemperature

                    # Processing Suffix/Keyword
                    suffix = types.cast_fortran_integer(tokens.popl()[3:])
                    parameter.set_suffix(suffix)

                    # Processing Value
                    value = types.cast_fortran_real(tokens.popr())
                    parameter.set_value(value)

                case "u":
                    parameter.__class__ = Cell.Universe

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                case "trcl":
                    parameter.__class__ = Cell.CoordinateTransformation

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                case "lat":
                    parameter.__class__ = Cell.Lattice

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                case "fill":
                    parameter.__class__ = Cell.Fill

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                case "elpt":
                    parameter.__class__ = Cell.EnergyCutoff

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_real(tokens.popr())
                    parameter.set_value(value)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

                case "cosy":
                    parameter.__class__ = Cell.Cosy

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                case "bflcl":
                    parameter.__class__ = Cell.Bfield

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                case "unc":
                    parameter.__class__ = Cell.UncolidedSecondaries

                    # Processing Keyword
                    tokens.popl()

                    # Processing Value
                    value = types.cast_fortran_integer(tokens.popr())
                    parameter.set_value(value)

                    # Processing Designator
                    designator = types.Designator.cast_mcnp_designator(tokens.popr())
                    parameter.set_designator(designator)

            # Checking for Remaining Tokens
            if tokens:
                raise errors.MCNPSyntaxError(
                    errors.MCNPSyntaxCodes.TOOLONG_CELL_PARAMETERS
                )

            return parameter

        def set_keyword(self, keyword: CellKeyword) -> None:
            """
            'set_keyword' sets cell parameter keywords.

            'set_keyword' checks keywords are valid. It
            raises errors if given None.

            Parameters:
                keyword: Cell parameter keyword.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_KEYWORD
                )

            self.keyword = keyword

        def to_mcnp(self) -> str:
            """
            'to_mcnp' generates from cell card parameter objects.

            'to_mcnp' provides an MCNP endpoints for writing INP
            source strings.

            Returns:
                INP for cell card parameter object.
            """

            # Processing Suffix
            suffix_str = (
                self.suffix
                if hasattr(self, "suffix") and self.suffix is not None
                else ""
            )

            # Processing Designator
            designator_str = (
                f":{','.join(self.designator)}"
                if hasattr(self, "designator") and self.designator is not None
                else ""
            )

            return f"{self.keyword}{suffix_str}{designator_str}={self.value}"

        def to_arguments(self) -> dict:
            """
            'to_arguments' generates dictionary from cell card parameter objects.

            'to_arguments' creates dictionaries whose keys are
            attribute names, and whose values are attribute value.

            Returns:
                arguments (dict): Dictionary for cell card parameter object.
            """

            return {
                "keyword": self.keyword.to_mcnp(),
                "suffix": self.suffix if hasattr(self.__class__, "suffix") else None,
                "designator": self.designator
                if hasattr(self.__class__, "designator")
                else None,
                "value": self.value,
            }

    class Importance(CellParameter):
        """
        'Importance' represents cell card particle importance parameters.

        'Importance' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'Importance'
            """

            super().__init__()

            self.importance: int = None
            self.designator: tuple[types.Designator] = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets cell card particle importance parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                importance: Cell particle importance.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (value >= 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.importance = value
            self.value = value

        def set_designator(self, designator: tuple[types.Designator]) -> None:
            """
            'set_designator' checks designators are valid.
            It raises errors if given None.

            Parameters:
                designator: cell card parameter designator.
            """

            if designator is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR
                )

            self.designator = designator

    class Volume(CellParameter):
        """
        'Volume' represents cell card volume parameters.

        'Volume' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'Volume'
            """

            super().__init__()

            self.volume: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets cell card volume parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                volume: Cell volume.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (value > 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.volume = value
            self.value = value

    class ProtonWeight(CellParameter):
        """
        'ProtonWeight' represents cell card proton weight parameters.

        'ProtonWeight' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'ProtonWeight'
            """

            super().__init__()

            self.weight: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets cell card proton weight parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                weight: Cell collision-generated proton number/weight.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.weight = value
            self.value = value

    class ExponentialTransform(CellParameter):
        """
        'ExponentialTransform' represents cell card exponential transformation parameters.

        'ExponentialTransform' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'ExponentialTransform'
            """

            super().__init__()

            self.stretch: any = None
            self.designator: types.Designator = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card exponential transformation parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                stretch: Cell stretch specifier.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.stretch = value
            self.value = value

        def set_designator(self, designator: types.Designator) -> None:
            """
            'set_designator' sets cell card exponential transformation parameter designator.

            'set_designator' checks designators are valid.
            It raises errors if given None.

            Parameters:
                designator: cell card parameter designator.
            """

            if designator is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR
                )

            self.designator = designator

    class ForcedCollision(CellParameter):
        """
        'ForcedCollision' represents cell card forced-collision parameters.

        'ForcedCollision' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'ForcedCollision'
            """

            super().__init__()

            self.control: any = None
            self.designator: types.Designator = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card forced-collision parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                control: Cell forced-collision.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (-1 <= value <= 1):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.control = value
            self.value = value

        def set_designator(self, designator: types.Designator) -> None:
            """
            'set_designator' sets cell card forced-collision parameter designator.

            'set_designator' checks designators are valid.
            It raises errors if given None.

            Parameters:
                designator: cell card parameter designator.
            """

            if designator is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR
                )

            self.designator = designator

    class WeightWindowBounds(CellParameter):
        """
        'WeightWindowBounds' represents cell card space-, time-, and energy-dependent weight window bound parameters.

        'WeightWindowBounds' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'WeightWindowBounds'
            """

            super().__init__()

            self.weight: any = None
            self.designator: types.Designator = None
            self.suffix: int = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card space-, time-, and energy-dependent weight window bound parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                weight: Cell weight window bounds.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (value == -1 or value >= 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.weight = value
            self.value = value

        def set_designator(self, designator: types.Designator) -> None:
            """
            'set_designator' sets cell card space-, time-, and energy-dependent weight window bound parameter designator.

            'set_designator' checks designators are valid.
            It raises errors if given None.

            Parameters:
                designator: cell card parameter designator.
            """

            if designator is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR
                )

            self.designator = designator

        def set_suffix(self, suffix: int) -> None:
            """
            'set_suffix' sets cell card space-, time-, and energy-dependent weight window bound parameter keyword suffix.

            'set_suffix' checks suffixes are valid.
            It raises errors if given None.

            Parameters:
                suffix (int): cell card keyword suffix.
            """

            if suffix is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_SUFFIX
                )

            self.suffix = suffix

    class DxtranContribution(CellParameter):
        """
        'DxtranContribution' represents cell card DXTRAN sphere contribution parameters.

        'DxtranContribution' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'DxtranContribution'
            """

            super().__init__()

            self.probability: any = None
            self.designator: types.Designator = None
            self.suffix: int = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card DXTRAN sphere contribution parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                probability: Cell DXTRAN sphere contribution probability.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (0 <= value <= 1):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.probability = value
            self.value = value

        def set_designator(self, designator: types.Designator) -> None:
            """
            'set_designator' sets cell card DXTRAN sphere contribution parameter designator.

            'set_designator' checks designators are valid.
            It raises errors if given None.

            Parameters:
                designator: cell card parameter designator.
            """

            if designator is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR
                )

            self.designator = designator

        def set_suffix(self, suffix: int) -> None:
            """
            'set_suffix' sets cell card DXTRAN sphere contribution parameter keyword suffix.

            'set_suffix' checks suffixes are valid.
            It raises errors if given None.

            Parameters:
                suffix (int): cell card keyword suffix.
            """

            if suffix is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_SUFFIX
                )

            self.suffix = suffix

    class FissionTurnOff(CellParameter):
        """
        'FissionTurnOff' represents cell card fission on/off parameters.

        'FissionTurnOff' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'FissionTurnOff'
            """

            super().__init__()

            self.setting: any = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card fission on/off parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                setting: Cell fission on/off setting.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (value in {0, 1, 2}):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.setting = value
            self.value = value

    class DetectorContribution(CellParameter):
        """
        'DetectorContribution' represents cell card point detector contribution parameters.

        'DetectorContribution' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'DetectorContribution'
            """

            super().__init__()

            self.probability: any = None
            self.suffix: int = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card point detector contribution parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                probability: Cell point detector contribution probability.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (0 <= value <= 1):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.probability = value
            self.value = value

        def set_suffix(self, suffix: int) -> None:
            """
            'set_suffix' sets cell card point detector contribution parameter keyword suffix.

            'set_suffix' checks suffixes are valid.
            It raises errors if given None.

            Parameters:
                suffix (int): cell card keyword suffix.
            """

            if suffix is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_SUFFIX
                )

            self.suffix = suffix

    class GasThermalTemperature(CellParameter):
        """
        'GasThermalTemperature' represents cell card time-dependent thermal temperature parameters.

        'GasThermalTemperature' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'GasThermalTemperature'
            """

            super().__init__()

            self.temperature: any = None
            self.suffix: int = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card time-dependent thermal temperature parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                temperature: Cell temperature.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (value >= 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.temperature = value
            self.value = value

        def set_suffix(self, suffix: int) -> None:
            """
            'set_suffix' sets cell card time-dependent thermal temperature parameter keyword suffix.

            'set_suffix' checks suffixes are valid.
            It raises errors if given None.

            Parameters:
                suffix: cell card keyword suffix.
            """

            if suffix is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_SUFFIX
                )

            self.suffix = suffix

    class Universe(CellParameter):
        """
        'Universe' represents cell card universe parameters.

        'Universe' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'Universe'
            """

            super().__init__()

            self.number: any = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card universe parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                number: Cell universe number.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (-99_999_999 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.number = value
            self.value = value

    class CoordinateTransformation(CellParameter):
        """
        'CoordinateTransformation' represents cell card transformation parameters.

        'CoordinateTransformation' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'CoordinateTransformation'
            """

            super().__init__()

            self.number: any = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card transformation parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                number: Cell transformation number.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.number = value
            self.value = value

    class Lattice(CellParameter):
        """
        'Lattice' represents cell card lattice shape parameters.

        'Lattice' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'Lattice'
            """

            super().__init__()

            self.shape: any = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card lattice shape parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                shape: Cell shape setting.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (value in {1, 2}):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.shape = value
            self.value = value

    class Fill(CellParameter):
        """
        'Fill' represents cell card filling universe parameters.

        'Fill' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'Fill'
            """

            super().__init__()

            self.number: any = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card filling universe parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                number: Cell filling universe number.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (0 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.number = value
            self.value = value

    class EnergyCutoff(CellParameter):
        """
        'EnergyCutoff' represents cell card lower energy cutoff parameters.

        'EnergyCutoff' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'EnergyCutoff'
            """

            super().__init__()

            self.cutoff: any = None
            self.designator: types.Designator = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card lower energy cutoff parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                cutoff: Cell energy cutoff.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.cutoff = value
            self.value = value

        def set_designator(self, designator: types.Designator) -> None:
            """
            'set_designator' sets cell card lower energy cutoff parameter designator.

            'set_designator' checks designators are valid.
            It raises errors if given None.

            Parameters:
                designator: cell card parameter designator.
            """

            if designator is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR
                )

            self.designator = designator

    class Cosy(CellParameter):
        """
        'Cosy' represents cell card cosy map parameters.

        'Cosy' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'Cosy'
            """

            super().__init__()

            self.number: any = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card cosy map parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                number: Cell cosy map number.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None and (value >= 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.number = value
            self.value = value

    class Bfield(CellParameter):
        """
        'Bfield' represents cell card magnetic/B field parameters.

        'Bfield' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'Bfield'
            """

            super().__init__()

            self.number: any = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card magnetic/B field parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                number: Cell magnetic field number.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (value >= 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.number = value
            self.value = value

    class UncolidedSecondaries(CellParameter):
        """
        'UncolidedSecondaries' represents cell card uncollided particle secondaries behavior parameters.

        'UncolidedSecondaries' functions as a data subtype for 'Cell'. It
        represents cell card parameter as abstract syntax
        elements.
        """

        def __init__(self):
            """
            '__init__' initalizes 'UncolidedSecondaries'
            """

            super().__init__()

            self.setting: any = None
            self.designator: types.Designator = None

        def set_value(self, value: any) -> None:
            """
            'set_value' sets cell card uncollided particle secondaries behavior parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                setting: Cell uncollided secondaries setting.

            Raises:
                MCNPSemanticError: Invalid cell card parameter value.
            """

            if value is None or not (value in {0, 1}):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_PARAMETER_VALUE
                )

            self.setting = value
            self.value = value

        def set_designator(self, designator: types.Designator) -> None:
            """
            'set_designator' sets cell card uncollided particle secondaries behavior parameter designator.

            'set_designator' checks designators are valid.
            It raises errors if given None.

            Parameters:
                designator: cell card parameter designator.

            Raises:
                MCNPSemanticError: Invalid cell card paramter designators.
            """

            if designator is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR
                )

            self.designator = designator

    def __init__(self) -> Self:
        """
        '__init__' initializes 'Cell'.
        """

        super().__init__()

        self.number: int = None
        self.mateiral: int = None
        self.density: float = None
        self.geometry: str = None
        self.parameters: tuple[self.CellParameter] = None

    def set_number(self, number: int) -> None:
        """
        'set_number' sets cell card number.

        'set_number' checks numbers are greater than
        or equal to 1 and less than or equal to 99,999,999.
        It raises errors if given None.

        Parameters:
            number: cell card number.

        Raises:
            MCNPSemanticError: Invalid cell card number.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_NUMBER)

        self.number = number
        self.id = number

    def set_material(self, material: int) -> None:
        """
        'set_material' sets cell card material.

        'set_material' checks numbers are greater than
        or equal to 0 and less than or equal to 99,999,999.
        It raises errors if given None.

        Parameters:
            material: cell card material or void.

        Raises:
            MCNPSemanticError: Invalid cell card material.
        """

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_CELL_MATERIAL
            )

        self.material = material

    def set_density(self, density: float) -> None:
        """
        'set_density' sets cell card densities.

        'set_density' checks numbers are not
        equal to zero. It raises errors if given None.

        Parameters:
            density: cell card density.

        Raises:
            MCNPSemanticError: Invalid cell card density.
        """

        if density is None or density == 0:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_CELL_DENSITY
            )

        self.density = density

    def set_geometry(self, geometry: CellGeometry) -> None:
        """
        'set_geometry' sets cell card geometries.

        'set_geometry' checks geometries are valid.
        It raises errors if given None.

        Parameters:
            geometry: cell card geometry.

        Raises:
            MCNPSemanticError: Invalid cell card geometry.
        """

        if geometry is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY
            )

        self.geometry = geometry

    def set_parameters(self, parameters: tuple[CellParameter]) -> None:
        """
        'set_parameters' sets cell card parameters.

        'set_parameters' checks cell parameters are valid.
        It raises errors if given None.

        Parameters:
            parameters: Tuple of cell card parameters.

        Raises:
            MCNPSemanticError: Invalid cell card parameters.
        """

        params = []

        for parameter in parameters:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_CELL_PARAMETER
                )

            params.append(parameter)

        self.parameters = tuple(params)

    @classmethod
    def from_mcnp(cls, card: str) -> Self:
        """
        'from_mcnp' generates cell card objects from.

        'from_mcnp' constructs instances of 'Cell' from INP
        strings, so it functions as a class constructor.

        Parameters:
            card: INP to parse.

        Returns:
            Cell card object.

        Raises:
            MCNPSemanticError: Invalid cell card values.
            MCNPSyntaxError: Invalid cell card syntax.
        """

        cell = cls()
        tokens = parser.Parser(
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL)
        ).from_string(card, " ")

        value = types.cast_fortran_integer(tokens.popl())
        cell.set_number(value)

        # Processing Material Number
        value = types.cast_fortran_integer(tokens.popl())
        cell.set_material(value)

        # Processing Material Density
        if cell.material != 0:
            value = types.cast_fortran_real(tokens.popl())
            cell.set_density(value)

        # Processing Parameters
        parameters = []

        entries = re.split(r":|=", tokens.peekr())
        value = cls.CellParameter.CellKeyword.cast_cell_keyword(entries[0])

        while value is not None:
            parameter = cls.CellParameter().from_mcnp(tokens.popr())
            parameters.append(parameter)

            entries = re.split(r":|=", tokens.peekr())
            value = cls.CellParameter.CellKeyword.cast_cell_keyword(entries[0])

        cell.set_parameters(tuple(parameters))

        # Processing Geometry
        print(tokens)
        cell.geometry = cls.CellGeometry().from_mcnp(" ".join(tokens.deque))

        return cell

    def to_mcnp(self) -> str:
        """
        'to_mcnp' generates from cell card objects.

        'to_mcnp' provides an MCNP endpoints for writing INP
        source strings.

        Returns:
            INP for cell card object.
        """

        # Formatting Density
        density_str = f" {self.density}" if self.material else ""

        # Formatting Geometry
        geometry_str = self.geometry.to_mcnp()

        # Formatting Parameters
        parameters_str = " ".join(param.to_mcnp() for param in self.parameters)

        return parser.Postprocessor.add_continuation_lines(
            f"{self.number} {self.material}{density_str} {geometry_str} {parameters_str}"
        )

    def to_arguments(self) -> dict:
        """
        'to_arguments' generates dictionary from cell card objects.

        'to_arguments' creates dictionaries whose keys are
        attribute names, and whose values are attribute value.

        Returns:
            Dictionary for cell card object.
        """

        return {
            "j": self.number,
            "m": self.material,
            "d": self.density,
            "geom": self.geometry.to_mcnp(),
            "params": [param.to_arguments() for param in self.parameters],
        }
