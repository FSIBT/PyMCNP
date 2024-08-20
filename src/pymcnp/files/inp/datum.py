"""
'datum' contains the class representing data cards.

'datum' packages the 'Datum' class, providing an importable interface
for data cards.
"""


import re
from typing import Self, Callable
from enum import StrEnum

from .card import Card
from .._utils import types
from .._utils import errors
from .._utils import parser


class Datum(Card):
    """
    'Datum' represents INP data cards.

    'Datum' abstracts the daua card syntax element and it
    encapsulates all functionallity for parsing data cards.

    Attributes:
        mnemonic: Data card mnemonic.
    """

    class DatumMnemonic(StrEnum):
        """
        'DatumMnemonic' represents data card mnemoincs.

        'DatumMnemonic' functions as a data types for surface
        cards. It selects between 'Datum' subclasses. It
        represents data card mnemonics as abstract syntax elements.
        """

        VOLUME = "vol"
        AREA = "area"
        TRANSFORMATION = "tr"
        UNIVERSE = "u"
        LATTICE = "lat"
        FILL = "fill"
        STOCHASTIC_GEOMETRY = "uran"
        DETERMINISTIC_MATERIALS = "dm"
        DETERMINISTIC_WEIGHT_WINDOW = "dawwg"
        EMBEDED_GEOMETRY = "embed"
        EMBEDED_CONTROL = "embee"
        EMBEDED_ENERGY_BOUNDARIES = "embeb"
        EMBEDED_ENERGY_MULTIPLIERS = "embem"
        EMBEDED_TIME_BOUNDARIES = "embtb"
        EMBEDED_TIME_MULTIPLIERS = "embtm"
        EMBEDED_DOSE_BOUNDARIES = "embde"
        EMBEDED_DOSE_MULTIPLIERS = "embdf"
        MATERIAL = "m"

        @classmethod
        def cast_datum_mnemonic(
            cls, string: str, hook: Callable[Self, bool] = lambda _: True
        ) -> Self:
            """
            'cast_datum_mnemonic' types casts from strings to datum mnemoincs.

            'cast_datum_mnemonic' creates datum mnemonic objects from
            strings. If the stirng is invalid or the hook returns false, it
            returns None.

            Returns:
                Datum mnemonic keyword from string.
            """

            string = string.lower()

            # Handling Star Modifier
            if string == "*tr":
                string = string[:1]

            # Handling Suffixes
            #           if string.startswith(()):
            #               if (
            #                   len(string) < 6
            #                   or types.cast_fortran_integer(string[5:]) is None
            #               ):
            #                   return None
            #
            #               string = string[:5]

            if string.startswith("dm"):
                if len(string) < 3 or types.cast_fortran_integer(string[2:]) is None:
                    return None

                string = string[:2]
            elif string.startswith("m"):
                if len(string) < 2 or types.cast_fortran_integer(string[1:]) is None:
                    return None

                string = string[:1]

            # Attempting Type Cast
            try:
                mnemonic = cls(string)

                if hook(mnemonic):
                    return mnemonic
            except ValueError:
                pass

            return None

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Datum'
        """

        super().__init__()

        self.mnemonic: DatumMnemonic = None
        self.parameters: tuple[any] = None

    def set_mnemonic(self, mnemonic: DatumMnemonic) -> None:
        """
        'set_mnemonic' sets surface card mnemoincs.

        'set_mnemonic' checks are valid. It raises errors
        if given None.

        Parameters:
            mnemonic: Data card mnemonic.

        Raises:
            MCNPSemanticError: Invalid surface card mnemonic.
        """

        if mnemonic is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC
            )

        self.mnemonic = mnemonic

    @classmethod
    def from_mcnp(cls, card: str) -> Self:
        """
        'from_mcnp' generates data card objects from INP.

        Parameters:
            card: INP to parse.

        Returns:
            datum (Datum): Data card object.
        """

        datum = cls()

        tokens = parser.Parser(
            re.split(r" |:|=", card),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES),
        )

        # Processing Mnemonic
        value = cls.DatumMnemonic.cast_datum_mnemonic(tokens.peekl())
        if value is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC
            )

        datum.set_mnemonic(value)

        # Processing Entries
        match datum.mnemonic:
            case "vol":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = Volume

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                has_no = tokens.peekl() == "no"
                if has_no:
                    tokens.popl()

                volumes = []
                while tokens:
                    volumes.append(types.cast_fortran_real(tokens.popl()))

                datum.set_parameters(has_no, *volumes)

            case "area":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = Area

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                areas = []
                while tokens:
                    areas.append(types.cast_fortran_real(tokens.popl()))

                datum.set_parameters(*areas)

            case "tr":
                if len(tokens) > 13:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                if len(tokens) < 13:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = Transformation

                # Processing Mnemonic
                suffix = types.cast_fortran_integer(tokens.popl()[2:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                entries = []
                while tokens:
                    entries.append(types.cast_fortran_real(tokens.popl()))

                datum.set_parameters(
                    tuple(entries[:3]),
                    (tuple(entries[3:6]), tuple(entries[6:9]), tuple(entries[9:12])),
                    int(entires[12]),
                )

            case "u":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = Universe

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                universes = []
                while tokens:
                    universes.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*universes)

            case "lat":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = Lattice

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                lattices = []
                while tokens:
                    lattices.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*lattices)

            case "fill":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = Fill

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                fills = []
                while tokens:
                    fills.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*fills)

            case "uran":
                if len(tokens) % 4 != 0:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = StochasticGeometry

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                transformations = []
                while tokens:
                    source = " ".join(
                        [tokens.popl(), tokens.popl(), tokens.popl(), tokens.popl()]
                    )
                    transformations.append(
                        StochasticGeometry.StochasticGeometryValue().from_mcnp(source)
                    )

                datum.set_parameters(*transformations)

            case "dm":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = DeterministicMaterials

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[2:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                materials = []
                while tokens:
                    materials.append(types.Zaid.cast_mcnp_zaid(tokens.popl()))

                datum.set_parameters(*materials)

            case "dawwg":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = DeterministicWeightWindow

                # Processing Mnemoninc
                tokens.popl()

                # Processing Parameters
                pairs = []
                while tokens:
                    paris.append(
                        DeterministicWeightWindow.DeterministicWeightWindowParameter.from_mcnp(
                            tokens.popl()
                        )
                    )

                datum.set_parameters(*pairs)

            case "embed":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = EmbededGeometry

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                pairs = []
                while tokens:
                    paris.append(
                        EmbededGeometry.EmbededGeometryParameter.from_mcnp(
                            tokens.popl()
                        )
                    )

                datum.set_parameters(*pairs)

            case "embee":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = EmbededElementalControl

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Designator
                designator = types.Designator.cast_mcnp_designator(tokens.popl())
                parameter.set_designator(designator)

                # Processing Parameters
                pairs = []
                while tokens:
                    paris.append(
                        EmbededElementalControl.EmbededElementalControlParameter.from_mcnp(
                            tokens.popl()
                        )
                    )

                datum.set_parameters(*pairs)

            case "embeb":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = EmbededElementalEnergyBoundaries

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                energies = []
                while tokens:
                    doses.append(types.cast_fortran_reals(tokens.popl()))

                datum.set_parameters(*energies)

            case "embem":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = EmbededElementalEnergyMultipliers

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                multipliers = []
                while tokens:
                    doses.append(types.cast_fortran_reals(tokens.popl()))

                datum.set_parameters(*multipliers)

            case "embtb":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = EmbededElementalTimeBoundaries

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                times = []
                while tokens:
                    doses.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*times)

            case "embtm":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = EmbededElementalTimeMultipliers

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                multipliers = []
                while tokens:
                    doses.append(types.cast_fortran_reals(tokens.popl()))

                datum.set_parameters(*multipliers)

            case "embde":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = EmbededElementalDoseBoundaries

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                doses = []
                while tokens:
                    doses.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*doses)

            case "embdf":
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = EmbededElementalDoseMultipliers

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                multipliers = []
                while tokens:
                    doses.append(types.cast_fortran_reals(tokens.popl()))

                datum.set_parameters(*multipliers)

            case "m":
                if len(tokens) < 2:
                    raise errors.MCNPSyntaxError(
                        errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES
                    )

                datum.__class__ = Material

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[1:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                substances = []
                while tokens:
                    source = " ".join([tokens.popl(), tokens.popl()])
                    paris.append(Material.MaterialParameter().from_mcnp(source))

                pairs = []
                while tokens:
                    source = "=".join([tokens.popl(), tokens.popl()])
                    paris.append(Material.MaterialParameter().from_mcnp(source))

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_DATUM_ENTRIES)

        return datum

    def to_mcnp(self) -> str:
        """
        'to_mcnp' generates INP from data card objects.

        Returns:
            source : INP for data card object.
        """

        # Formatting Number
        number_str = f"{self.number}" if self.number is not None else ""

        return f"{self.mnemonic}{number_str} {' '.join(self.parameters)}"

    def to_arguments(self) -> list:
        """
        'to_arguments' generates dictionaries from data card objects.

        Returns:
            Dictionary of data card object data.
        """

        return {
            "mnemoinc": self.mnemonic,
            "parameters": self.parameters,
        }


class Volume(Datum):
    """
    'Volume' represents volume data cards.

    'Volume' functions as a data subtype for 'Datum'. It
    represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Volume'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.VOLUME

        self.has_no: bool = None
        self.volumes: tuple[float] = None

    def set_parameters(self, has_no: bool, *volumes: float) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            has_no: No option flag.
            *volumes: Iterable of volumes.
        """

        self.has_no = has_no

        for parameter in volumes:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = volumes
        self.volumes = volumes


class Area(Datum):
    """
    'Area' represents surface area data cards.

    'Area' functions as a data subtype for 'Datum'. It
    represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Area'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.AREA

        self.areas: tuple[float] = None

    def set_parameters(self, *areas: float) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *areas: Iterable of areas.
        """

        for parameter in areas:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = areas
        self.areas = areas


class Transformation(Datum):
    """
    'Transformation' represents surface transformation data cards.

    'Transformation' functions as a data subtype for 'Datum'. It
    represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initializes 'Transformation'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.TRANSFORMATION

        self.suffix: tuple[float] = None
        self.displacement: tuple[float] = None
        self.rotation: tuple[tuple[float]] = None
        self.system: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets trasformation data card
        keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(
        self, displacement: tuple[float], rotation: tuple[tuple[float]], system: int
    ) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            parameters: Transformation specification.
        """

        # Processing displacement
        for entry in displacement:
            if entry is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.displacement = displacement

        # Processing rotation
        for row in rotation:
            for entry in row:
                if entry is None:
                    raise errors.MCNPSemanticError(
                        errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                    )

        self.rotation = rotation

        # Processing system
        if tokens.peekr() is None or tokens.peekr() not in {-1, 1}:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
            )

        self.system = system

        self.parameters = tuple(list(displacement) + list(*rotation) + [system])


class Universe(Datum):
    """
    'Universe' represents universe data cards.

    'Universe' functions as a data subtype for 'Datum'. It
    represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Universe'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.UNIVERSE

        self.unvierses: tuple[int] = None

    def set_parameters(self, *unvierses: int) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            unvierses: Iterable of universe numbers.
        """

        for parameter in unvierses:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = unvierses
        self.universes = unvierses


class Lattice(Datum):
    """
    'Lattice' represents lattice data cards.

    'Lattice' functions as a data subtype for 'Datum'. It
    represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Lattice'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.LATTICE

        self.lattices: tuple[int] = None

    def set_parameters(self, *lattices: int) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            lattices: Iterable of lattice specifiers.
        """

        for parameter in lattices:
            if parameter is None or parameter not in {1, 2}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = lattices
        self.lattices = lattices


class Fill(Datum):
    """
    'Fill' represents fill data cards.

    'Fill' functions as a data subtype for 'Datum'. It
    represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Fill'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.FILL

        self.fills: tuple[int] = None

    def set_parameters(self, *fills: int) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            fills: Iterable of universe numbers.
        """

        for parameter in fills:
            if parameter is None or not (parameter >= 0 and parameter <= 99_999_999):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = fills
        self.fills = fills


class StochasticGeometry(Datum):
    """
    'StochasticGeometry' represents stochastic geometry data cards.

    'StochasticGeometry' functions as a data subtype for 'Datum'. It
    represents datum cards as an abstract syntax element.
    """

    class StochasticGeometryValue:
        """
        'StochasticGeometryValue' represents stochastic geometry entry.

        'StochasticGeometryValue' stores universe numbers and maximum
        translations.
        """

        def __init__(self) -> Self:
            """
            '__init__' initalizes 'StochasticGeometryValue'
            """

            self.number: int = None
            self.maximum_x: float = None
            self.maximum_y: float = None
            self.maximum_z: float = None

        @classmethod
        def from_mcnp(cls, string: str) -> Self:
            """
            'from_mcnp' generates stochastic geometry entries.

            'from_mcnp' constructs instances of 'StochasticGeometryValue'
            from INP strings, so it functions as a class constructor.

            Parameters:
                string: INP to parse.

            Returns:
                Stochastic geometry value object.

            Raises:
                MCNPSemanticError: Invalid card parameter entry.
                MCNPSyntaxError: Invalid card paramter syntax.
            """

            entry = cls()

            tokens = parser.Parser(
                string.split(" "),
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES),
            )

            # Parsing Universe Number
            value = types.cast_fortran_integer(tokens.popl())
            if value is None or not (1 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

            self.number = value

            # Parsing Maximum Translations
            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

            self.maximum_x = value

            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

            self.maximum_y = value

            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

            self.maximum_z = value

            if tokens:
                raise errors.MCNPSyntaxError(
                    errors.MCNPSyntaxCodes.TOOMANY_DATUM_ENTRIES
                )

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'StochasticGeometry'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.STOCHASTIC_GEOMETRY

        self.lattices: tuple[StochasticGeometryValue] = None

    def set_parameters(self, *transformations: StochasticGeometryValue) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            transformations: Iterable of stochastic geometry values.
        """

        for parameter in transformations:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = transformations
        self.transformations = transformations


class DeterministicMaterials(Datum):
    """
    'DeterministicMaterials' represents deterministic material  data cards.

    'DeterministicMaterials' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'DeterministicMaterials'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.DETERMINISTIC_MATERIALS

        self.materials: tuple[types.Zaid] = None

    def set_parameters(self, *materials: types.Zaid) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            materials: Iterable of ZAID aliases.
        """

        for parameter in materials:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = materials
        self.materials = materials


class DeterministicWeightWindow(Datum):
    """
    'DeterministicWeightWindow' represents deterministics adjoint weight-window
    generator data cards.

    'DeterministicWeightWindow' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    class DeterministicWeightWindowParameter:
        """
        'DeterministicWeightWindowParameter' represents deterministics adjoint weight-window
        generator data card parameter.

        'DeterministicWeightWindowParameter' functions as a data type for
        'DeterministicWeightWindow'. It represents deterministics adjoint
        weight-window generator data card parameters as abstract syntax elements.
        """

        class DeterministicWeightWindowKeyword(StrEnum):
            """
            'DeterministicWeightWindowKeyword' represents deterministics adjoint weight-window
            generator data card parameter keywords.

            'DeterministicWeightWindowKeyword' functions as a data type for
            'DeterministicWeightWindowParameter' and 'DeterministicWeightWindow'. It
            represents card parameter keywords as abstract syntax elements.
            """

            POINTS = "points"
            #           XSEC = "xsec"
            #           TALLY = "tally"
            BLOCK = "block"
            NGROUP = "ngroup"
            ISN = "isn"
            NISO = "niso"
            MT = "mt"
            IQUAD = "iquad"
            FMMIX = "fmmix"
            NOSOLV = "nosolv"
            NOEDIT = "noedit"
            NOGEOD = "nogeod"
            NOMIX = "nomix"
            NOASG = "noasg"
            NOMACR = "nomacr"
            NOSLNP = "noslnp"
            NOEDTT = "noedtt"
            NOADJM = "noadjm"
            LIB = "lib"
            LIBNAME = "libname"
            FISSNEUT = "fissneut"
            LNG = "lng"
            BALXS = "balxs"
            NTICHI = "ntichi"
            IEVT = "ievt"
            SCT = "sct"
            ITH = "ith"
            TRCOR = "trcor"
            IBL = "ibl"
            IBR = "ibr"
            IBT = "ibt"
            IBB = "ibb"
            IBFRNT = "ibfrnt"
            BIBACK = "biback"
            EPSI = "epsi"
            OITM = "oitm"
            NOSIGF = "nosigf"
            SRCACC = "srcacc"
            DIFFSOL = "diffsol"
            TSASN = "tsasn"
            TSAEPSI = "tsaepsi"
            TSAITS = "tsaits"
            TSABETA = "tsabeta"
            PTCONV = "ptconv"
            NORM = "norm"
            XESCTP = "xesctp"
            FISSRP = "fissrp"
            SOURCP = "sourcp"
            ANGP = "angp"
            BALP = "balp"
            RAFLUX = "raflux"
            RMFLUX = "rmflux"
            AVATAR = "avatar"
            ASLEFT = "asleft"
            ASRITE = "asrite"
            ASBOTT = "asbott"
            ASTOP = "astop"
            ASFRNT = "asfrnt"
            ASBACK = "asback"
            MASSED = "massed"
            PTED = "pted"
            ZNED = "zned"
            RZFLUX = "rzflux"
            RXMFLUX = "rxmflux"
            EDOUTF = "edoutf"
            BYVLOP = "byvlop"
            AJED = "ajed"
            FLUXONE = "fluxone"

            @classmethod
            def cast_dawwg_keyword(
                cls, string: str, hook: Callable[Self, bool] = lambda _: True
            ) -> Self:
                """
                'cast_dawwg_keyword' types casts from strings to Deterministic adjoint
                weight window parameter keywords.

                'cast_dawwg_keyword' creates deterministic adjoint weight window
                parameter keywords objects from strings. If the string is invalid
                or the hook returns false, it returns None.

                Parameters:
                    string: String to cast.
                    hook: Postcast check.

                Returns:
                    Deterministic adjoint weight window parameter keyword from string.
                """

                string = string.lower()

                try:
                    keyword = cls(string)

                    if hook(keyword):
                        return keyword
                except ValueError:
                    pass

                return None

        def __init__(self) -> Self:
            """
            '__init__' initializes 'DeterministicWeightWindowParameter'
            """

            self.keyword: self.DeterministicWeightWindowKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: DeterministicWeightWindowKeyword) -> None:
            """
            'set_keyword' sets deterministic adjoint weight window
            parameter keywords.

            'set_keyword' checks keywords are valid. It
            raises errors if given None.

            Parameters:
                keyword: Deterministic adjoint weight window parameter keyword.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_KEYWORD
                )

            self.keyword = keyword

        @classmethod
        def from_mcnp(cls, string: str):
            """
            'from_mcnp' generates deterministic adjoint weight window parameter objects from.

            'from_mcnp' constructs instances of 'DeterministicWeightWindowParameter' from
            INP strings, so it functions as a class constructor. It
            transforms deterministic adjoint weight window parameter
            into their correct subclasses.

            Parameters:
                card: INP to parse.

            Returns:
               Deterministic adjoint weight window parameter object.

            Raises:
                MCNPSemanticError: Invalid deterministic adjoint weight window parameter entry.
                MCNPSyntaxError: Invalid deterministic adjoint weight window parameter syntax.
            """

            parameter = cls()

            tokens = parser.Parser(
                string.split("="),
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES),
            )

            # Processing Keyword
            value = cls.DeterministicWeightWindowKeyword.cast_keyword(tokens.peekl())
            parameter.set_keyword(value)

            # Processing Values
            match tokens.popl():
                case "points":
                    parameter.__class__ = DeterministicWeightWindow.Points

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                #                case "xsec":
                #                    parameter.__class__ = DeterministicWeightWindow.Xsec
                #
                #                    value = types.cast_fortran_integer(tokens.popl())
                #                    parameter.set_value(value)

                #                case "tally":
                #                    parameter.__class__ = DeterministicWeightWindow.Tally
                #
                #                    value = types.cast_fortran_integer(tokens.popl())
                #                    parameter.set_value(value)

                case "block":
                    parameter.__class__ = DeterministicWeightWindow.Block

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ngroup":
                    parameter.__class__ = DeterministicWeightWindow.Ngroup

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "isn":
                    parameter.__class__ = DeterministicWeightWindow.Isn

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "niso":
                    parameter.__class__ = DeterministicWeightWindow.Niso

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "mt":
                    parameter.__class__ = DeterministicWeightWindow.Mt

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "iquad":
                    parameter.__class__ = DeterministicWeightWindow.Iquad

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "fmmix":
                    parameter.__class__ = DeterministicWeightWindow.Fmmix

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "nosolv":
                    parameter.__class__ = DeterministicWeightWindow.Nosolv

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "noedit":
                    parameter.__class__ = DeterministicWeightWindow.Noedit

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "nogeod":
                    parameter.__class__ = DeterministicWeightWindow.Nogeod

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "nomix":
                    parameter.__class__ = DeterministicWeightWindow.Nomix

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "noasg":
                    parameter.__class__ = DeterministicWeightWindow.Noasg

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "nomacr":
                    parameter.__class__ = DeterministicWeightWindow.Nomacr

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "noslnp":
                    parameter.__class__ = DeterministicWeightWindow.Noslnp

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "noedtt":
                    parameter.__class__ = DeterministicWeightWindow.Noedtt

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "noadjm":
                    parameter.__class__ = DeterministicWeightWindow.Noadjm

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "lib":
                    parameter.__class__ = DeterministicWeightWindow.Lib

                    parameter.set_value(tokens.popl())

                case "libname":
                    parameter.__class__ = DeterministicWeightWindow.Libname

                    parameter.set_value(tokens.popl())

                case "fissneut":
                    parameter.__class__ = DeterministicWeightWindow.Fissneut

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "lng":
                    parameter.__class__ = DeterministicWeightWindow.Lng

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "balxs":
                    parameter.__class__ = DeterministicWeightWindow.Balxs

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ntichi":
                    parameter.__class__ = DeterministicWeightWindow.Ntichi

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ievt":
                    parameter.__class__ = DeterministicWeightWindow.Ievt

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "sct":
                    parameter.__class__ = DeterministicWeightWindow.Isct

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ith":
                    parameter.__class__ = DeterministicWeightWindow.Ith

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "trcor":
                    parameter.__class__ = DeterministicWeightWindow.Trcor

                    parameter.set_value(tokens.popl())

                case "ibl":
                    parameter.__class__ = DeterministicWeightWindow.Ibl

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ibr":
                    parameter.__class__ = DeterministicWeightWindow.Ibr

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ibt":
                    parameter.__class__ = DeterministicWeightWindow.Ibt

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ibb":
                    parameter.__class__ = DeterministicWeightWindow.Ibb

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ibfrnt":
                    parameter.__class__ = DeterministicWeightWindow.Ibfrnt

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "biback":
                    parameter.__class__ = DeterministicWeightWindow.Ibback

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "epsi":
                    parameter.__class__ = DeterministicWeightWindow.Epsi

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "oitm":
                    parameter.__class__ = DeterministicWeightWindow.Oitm

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "nosigf":
                    parameter.__class__ = DeterministicWeightWindow.Nosigf

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "srcacc":
                    parameter.__class__ = DeterministicWeightWindow.Srcacc

                    parameter.set_value(tokens.popl())

                case "diffsol":
                    parameter.__class__ = DeterministicWeightWindow.Diffsol

                    parameter.set_value(tokens.popl())

                case "tsasn":
                    parameter.__class__ = DeterministicWeightWindow.Tsasn

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "tsaepsi":
                    parameter.__class__ = DeterministicWeightWindow.Tsaepsi

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "tsaits":
                    parameter.__class__ = DeterministicWeightWindow.Tsaits

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "tsabeta":
                    parameter.__class__ = DeterministicWeightWindow.Tsabeta

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "ptconv":
                    parameter.__class__ = DeterministicWeightWindow.Ptconv

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "norm":
                    parameter.__class__ = DeterministicWeightWindow.Norm

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "xesctp":
                    parameter.__class__ = DeterministicWeightWindow.Xesctp

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "fissrp":
                    parameter.__class__ = DeterministicWeightWindow.Fissrp

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "sourcp":
                    parameter.__class__ = DeterministicWeightWindow.Sourcp

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "angp":
                    parameter.__class__ = DeterministicWeightWindow.Angp

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "balp":
                    parameter.__class__ = DeterministicWeightWindow.Balp

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "raflux":
                    parameter.__class__ = DeterministicWeightWindow.Raflux

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "rmflux":
                    parameter.__class__ = DeterministicWeightWindow.Rmflux

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "avatar":
                    parameter.__class__ = DeterministicWeightWindow.Avatar

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "asleft":
                    parameter.__class__ = DeterministicWeightWindow.Asleft

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "asrite":
                    parameter.__class__ = DeterministicWeightWindow.Asrite

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "asbott":
                    parameter.__class__ = DeterministicWeightWindow.Asbott

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "astop":
                    parameter.__class__ = DeterministicWeightWindow.Astop

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "asfrnt":
                    parameter.__class__ = DeterministicWeightWindow.Asfrnt

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "asback":
                    parameter.__class__ = DeterministicWeightWindow.Asback

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "massed":
                    parameter.__class__ = DeterministicWeightWindow.Massed

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "pted":
                    parameter.__class__ = DeterministicWeightWindow.Pted

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "zned":
                    parameter.__class__ = DeterministicWeightWindow.Zned

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "rzflux":
                    parameter.__class__ = DeterministicWeightWindow.Rzflux

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "rxmflux":
                    parameter.__class__ = DeterministicWeightWindow.Rzmflux

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "edoutf":
                    parameter.__class__ = DeterministicWeightWindow.Edoutf

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "byvlop":
                    parameter.__class__ = DeterministicWeightWindow.Byvlop

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "ajed":
                    parameter.__class__ = DeterministicWeightWindow.Ajed

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "fluxone":
                    parameter.__class__ = DeterministicWeightWindow.Fluxone

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

            if tokens:
                raise errors.MCNPSyntaxError(
                    errors.MCNPSyntaxCodes.TOOMANY_DATUM_ENTRIES
                )

    class Points(DeterministicWeightWindowParameter):
        """
        'Points' represents points deterministic weight window parameters.

        'Points' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Points'.
            """

            super().__init__()

            self.point: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  cpoints deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.point = value

    # class Xsec(DeterministicWeightWindowParameter):
    #    """
    #    'Xsec' represents xsec deterministic weight window parameters.
    #
    #    'Xsec' functions as a data subtype for 'DeterministicWeightWindowParameter'.
    #    It represents deterministic weight window parameter as abstract syntax elements.
    #    """
    #
    #    def __init__(self) -> Self:
    #        """
    #        '__init__' initializes 'Xsec'.
    #        """
    #
    #        super().__init__()
    #
    #        self.name: int = None
    #
    #    def set_value(self, value: str) -> None:
    #        """
    #        'set_value' sets xsec deterministic weight window
    #        parameter values.
    #
    #        'set_value' checks values are valid. It
    #        raises errors if given None.
    #
    #        Parameters:
    #            value: Parameter value.
    #
    #        Raises:
    #            MCNPSemanticError: Invalid deterministic weight window parameter value.
    #        """
    #
    #        if value is None:
    #            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE)
    #
    #        self.value = value
    #        self.name = value

    # class Tally(DeterministicWeightWindowParameter):
    #    """
    #    'Tally' represents tally deterministic weight window parameters.
    #
    #    'Tally' functions as a data subtype for 'DeterministicWeightWindowParameter'.
    #    It represents deterministic weight window parameter as abstract syntax elements.
    #    """
    #
    #    def __init__(self) -> Self:
    #        """
    #        '__init__' initializes 'Tally'.
    #        """
    #
    #        super().__init__()
    #
    #        self._: int = None
    #
    #    def set_value(self, value: int) -> None:
    #        """
    #        'set_value' sets  tally deterministic weight window
    #        parameter values.
    #
    #        'set_value' checks values are valid. It
    #        raises errors if given None.
    #
    #        Parameters:
    #            value: Parameter value.
    #
    #        Raises:
    #            MCNPSemanticError: Invalid deterministic weight window parameter value.
    #        """
    #
    #        if value is None:
    #            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE)
    #
    #        self.value = value
    #        self._ = value

    class Block(DeterministicWeightWindowParameter):
        """
        'Block' represents block deterministic weight window parameters.

        'Block' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Block'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  block deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {1, 3, 5, 6}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Ngroup(DeterministicWeightWindowParameter):
        """
        'Ngroup' represents ngroup deterministic weight window parameters.

        'Ngroup' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ngroup'.
            """

            super().__init__()

            self.energy_group_number: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ngroup deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.energy_group_number = value

    class Isn(DeterministicWeightWindowParameter):
        """
        'Isn' represents isn deterministic weight window parameters.

        'Isn' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Isn'.
            """

            super().__init__()

            self.sn_order: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets isn deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.sn_order = value

    class Niso(DeterministicWeightWindowParameter):
        """
        'Niso' represents niso deterministic weight window parameters.

        'Niso' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Niso'.
            """

            super().__init__()

            self.isotopes_number: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets niso deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.isotopes_number = value

    class Mt(DeterministicWeightWindowParameter):
        """
        'Mt' represents mt deterministic weight window parameters.

        'Mt' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Mt'.
            """

            super().__init__()

            self.materials_number: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets mt deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.materials_number = value

    class Iquad(DeterministicWeightWindowParameter):
        """
        'Iquad' represents iquad deterministic weight window parameters.

        'Iquad' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Iquad'.
            """

            super().__init__()

            self.quadrature: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets iquad deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {1, 3, 4, 5, 6, 7, 8, 9}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.quadrature = value

    class Fmmix(DeterministicWeightWindowParameter):
        """
        'Fmmix' represents fmmix deterministic weight window parameters.

        'Fmmix' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Fmmix'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets fmmix deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Nosolv(DeterministicWeightWindowParameter):
        """
        'Nosolv' represents nosolv deterministic weight window parameters.

        'Nosolv' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Nosolv'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets nosolv deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Noedit(DeterministicWeightWindowParameter):
        """
        'Noedit' represents noedit deterministic weight window parameters.

        'Noedit' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Noedit'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets noedit deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Nogeod(DeterministicWeightWindowParameter):
        """
        'Nogeod' represents nogeod deterministic weight window parameters.

        'Nogeod' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Nogeod'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets nogeod deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Nomix(DeterministicWeightWindowParameter):
        """
        'Nomix' represents nomix deterministic weight window parameters.

        'Nomix' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Nomix'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets nomix deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Noasg(DeterministicWeightWindowParameter):
        """
        'Noasg' represents noasg deterministic weight window parameters.

        'Noasg' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Noasg'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets noasg deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Nomacr(DeterministicWeightWindowParameter):
        """
        'Nomacr' represents nomacr deterministic weight window parameters.

        'Nomacr' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Nomacr'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets nomacr deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Noslnp(DeterministicWeightWindowParameter):
        """
        'Noslnp' represents noslnp deterministic weight window parameters.

        'Noslnp' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Noslnp'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets noslnp deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Noedtt(DeterministicWeightWindowParameter):
        """
        'Noedtt' represents noedtt deterministic weight window parameters.

        'Noedtt' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Noedtt'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets noedtt deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Noadjm(DeterministicWeightWindowParameter):
        """
        'Noadjm' represents noadjm deterministic weight window parameters.

        'Noadjm' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Noadjm'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets noadjm deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Lib(DeterministicWeightWindowParameter):
        """
        'Lib' represents lib deterministic weight window parameters.

        'Lib' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Lib'.
            """

            super().__init__()

            self.name: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets lib deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.name = value

    class Libname(DeterministicWeightWindowParameter):
        """
        'Libname' represents libname deterministic weight window parameters.

        'Libname' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Libname'.
            """

            super().__init__()

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets libname deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.filename = value

    class Fissneut(DeterministicWeightWindowParameter):
        """
        'Fissneut' represents fissneut deterministic weight window parameters.

        'Fissneut' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Fissneut'.
            """

            super().__init__()

            self.fission_neutron_flag: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets carfissneut deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.fission_neutron_flag = value

    class Lng(DeterministicWeightWindowParameter):
        """
        'Lng' represents lng deterministic weight window parameters.

        'Lng' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Lng'.
            """

            super().__init__()

            self.last_neutron_group_number: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' setslng deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.last_neutron_group_number = value

    class Balxs(DeterministicWeightWindowParameter):
        """
        'Balxs' represents balxs deterministic weight window parameters.

        'Balxs' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Balxs'.
            """

            super().__init__()

            self.cross_section_balance_control: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  balxs deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.cross_section_balance_control = value

    class Ntichi(DeterministicWeightWindowParameter):
        """
        'Ntichi' represents ntichi deterministic weight window parameters.

        'Ntichi' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ntichi'.
            """

            super().__init__()

            self.mendf_fission_fraction: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  cntichi deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.mendf_fission_fraction = value

    class Ievt(DeterministicWeightWindowParameter):
        """
        'Ievt' represents ievt deterministic weight window parameters.

        'Ievt' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ievt'.
            """

            super().__init__()

            self.calculation_type: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ievt deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1, 2, 3, 4}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.calculation_type = value

    class Isct(DeterministicWeightWindowParameter):
        """
        'Isct' represents sct deterministic weight window parameters.

        'Isct' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Isct'.
            """

            super().__init__()

            self.legendre_order: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets isct deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.legendre_order = value

    class Ith(DeterministicWeightWindowParameter):
        """
        'Ith' represents ith deterministic weight window parameters.

        'Ith' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ith'.
            """

            super().__init__()

            self.calculation_state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ith deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.calculation_state = value

    class Trcor(DeterministicWeightWindowParameter):
        """
        'Trcor' represents trcor deterministic weight window parameters.

        'Trcor' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Trcor'.
            """

            super().__init__()

            self.trcor: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets trcor deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.trcor = value

    class Ibl(DeterministicWeightWindowParameter):
        """
        'Ibl' represents ibl deterministic weight window parameters.

        'Ibl' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ibl'.
            """

            super().__init__()

            self.left_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ibl deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.left_boundary = value

    class Ibr(DeterministicWeightWindowParameter):
        """
        'Ibr' represents ibr deterministic weight window parameters.

        'Ibr' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ibr'.
            """

            super().__init__()

            self.right_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ibr deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.right_boundary = value

    class Ibt(DeterministicWeightWindowParameter):
        """
        'Ibt' represents ibt deterministic weight window parameters.

        'Ibt' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ibt'.
            """

            super().__init__()

            self.top_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ibt deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.top_boundary = value

    class Ibb(DeterministicWeightWindowParameter):
        """
        'Ibb' represents ibb deterministic weight window parameters.

        'Ibb' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ibb'.
            """

            super().__init__()

            self.bottom_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ibb deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.bottom_boundary = value

    class Ibfrnt(DeterministicWeightWindowParameter):
        """
        'Ibfrnt' represents ibfrnt deterministic weight window parameters.

        'Ibfrnt' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ibfrnt'.
            """

            super().__init__()

            self.front_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ibfrnt deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.front_boundary = value

    class Ibback(DeterministicWeightWindowParameter):
        """
        'Ibback' represents biback deterministic weight window parameters.

        'Ibback' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ibback'.
            """

            super().__init__()

            self.back_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ibback deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.back_boundary = value

    class Epsi(DeterministicWeightWindowParameter):
        """
        'Epsi' represents epsi deterministic weight window parameters.

        'Epsi' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Epsi'.
            """

            super().__init__()

            self.convergence_percision: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets epsi deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.convergence_percision = value

    class Oitm(DeterministicWeightWindowParameter):
        """
        'Oitm' represents oitm deterministic weight window parameters.

        'Oitm' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Oitm'.
            """

            super().__init__()

            self.maximum_outer_iteration: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets oitm deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.maximum_outer_iteration = value

    class Nosigf(DeterministicWeightWindowParameter):
        """
        'Nosigf' represents nosigf deterministic weight window parameters.

        'Nosigf' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Nosigf'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets nosigf deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Srcacc(DeterministicWeightWindowParameter):
        """
        'Srcacc' represents srcacc deterministic weight window parameters.

        'Srcacc' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Srcacc'.
            """

            super().__init__()

            self.transport_accelerations: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets  csrcacc deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.transport_accelerations = value

    class Diffsol(DeterministicWeightWindowParameter):
        """
        'Diffsol' represents diffsol deterministic weight window parameters.

        'Diffsol' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Diffsol'.
            """

            super().__init__()

            self.diffusion_operator_solver: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets  cadiffsol deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.diffusion_operator_solver = value

    class Tsasn(DeterministicWeightWindowParameter):
        """
        'Tsasn' represents tsasn deterministic weight window parameters.

        'Tsasn' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Tsasn'.
            """

            super().__init__()

            self.sn_order: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  tsasn deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.sn_order = value

    class Tsaepsi(DeterministicWeightWindowParameter):
        """
        'Tsaepsi' represents tsaepsi deterministic weight window parameters.

        'Tsaepsi' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Tsaepsi'.
            """

            super().__init__()

            self.convergence_criteria: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets  catsaepsi deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.convergence_criteria = value

    class Tsaits(DeterministicWeightWindowParameter):
        """
        'Tsaits' represents tsaits deterministic weight window parameters.

        'Tsaits' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Tsaits'.
            """

            super().__init__()

            self.maximum_tsa_iteration: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  ctsaits deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.maximum_tsa_iteration = value

    class Tsabeta(DeterministicWeightWindowParameter):
        """
        'Tsabeta' represents tsabeta deterministic weight window parameters.

        'Tsabeta' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Tsabeta'.
            """

            super().__init__()

            self.tsa_scattering_cross_section: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets  catsabeta deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.tsa_scattering_cross_section = value

    class Ptconv(DeterministicWeightWindowParameter):
        """
        'Ptconv' represents ptconv deterministic weight window parameters.

        'Ptconv' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ptconv'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  cptconv deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Norm(DeterministicWeightWindowParameter):
        """
        'Norm' represents norm deterministic weight window parameters.

        'Norm' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Norm'.
            """

            super().__init__()

            self.norm: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets norm deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.norm = value

    class Xesctp(DeterministicWeightWindowParameter):
        """
        'Xesctp' represents xesctp deterministic weight window parameters.

        'Xesctp' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Xesctp'.
            """

            super().__init__()

            self.cross_section_print_flag: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  cxesctp deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1, 2}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.cross_section_print_flag = value

    class Fissrp(DeterministicWeightWindowParameter):
        """
        'Fissrp' represents fissrp deterministic weight window parameters.

        'Fissrp' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Fissrp'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  cfissrp deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Sourcp(DeterministicWeightWindowParameter):
        """
        'Sourcp' represents sourcp deterministic weight window parameters.

        'Sourcp' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Sourcp'.
            """

            super().__init__()

            self.source_print_flag: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  csourcp deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1, 2, 3}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.source_print_flag = value

    class Angp(DeterministicWeightWindowParameter):
        """
        'Angp' represents angp deterministic weight window parameters.

        'Angp' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Angp'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets angp deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Balp(DeterministicWeightWindowParameter):
        """
        'Balp' represents balp deterministic weight window parameters.

        'Balp' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Balp'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets balp deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Raflux(DeterministicWeightWindowParameter):
        """
        'Raflux' represents raflux deterministic weight window parameters.

        'Raflux' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Raflux'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  craflux deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Rmflux(DeterministicWeightWindowParameter):
        """
        'Rmflux' represents rmflux deterministic weight window parameters.

        'Rmflux' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Rmflux'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  crmflux deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Avatar(DeterministicWeightWindowParameter):
        """
        'Avatar' represents avatar deterministic weight window parameters.

        'Avatar' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Avatar'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  cavatar deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Asleft(DeterministicWeightWindowParameter):
        """
        'Asleft' represents asleft deterministic weight window parameters.

        'Asleft' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Asleft'.
            """

            super().__init__()

            self.left_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets asleft deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.left_going_flux = value

    class Asrite(DeterministicWeightWindowParameter):
        """
        'Asrite' represents asrite deterministic weight window parameters.

        'Asrite' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Asrite'.
            """

            super().__init__()

            self.right_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets asrite deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.right_going_flux = value

    class Asbott(DeterministicWeightWindowParameter):
        """
        'Asbott' represents asbott deterministic weight window parameters.

        'Asbott' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Asbott'.
            """

            super().__init__()

            self.bottom_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets asbott deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.bottom_going_flux = value

    class Astop(DeterministicWeightWindowParameter):
        """
        'Astop' represents astop deterministic weight window parameters.

        'Astop' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Astop'.
            """

            super().__init__()

            self._: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets astop deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.top_going_flux = value

    class Asfrnt(DeterministicWeightWindowParameter):
        """
        'Asfrnt' represents asfrnt deterministic weight window parameters.

        'Asfrnt' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Asfrnt'.
            """

            super().__init__()

            self.front_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets asfrnt deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.front_going_flux = value

    class Asback(DeterministicWeightWindowParameter):
        """
        'Asback' represents asback deterministic weight window parameters.

        'Asback' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Asback'.
            """

            super().__init__()

            self.back_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets asback deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.back_going_flux = value

    class Massed(DeterministicWeightWindowParameter):
        """
        'Massed' represents massed deterministic weight window parameters.

        'Massed' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Massed'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets massed deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Pted(DeterministicWeightWindowParameter):
        """
        'Pted' represents pted deterministic weight window parameters.

        'Pted' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Pted'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets pted deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Zned(DeterministicWeightWindowParameter):
        """
        'Zned' represents zned deterministic weight window parameters.

        'Zned' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Zned'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets zned deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Rzflux(DeterministicWeightWindowParameter):
        """
        'Rzflux' represents rzflux deterministic weight window parameters.

        'Rzflux' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Rzflux'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets rzflux deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Rzmflux(DeterministicWeightWindowParameter):
        """
        'Rzmflux' represents rzmflux deterministic weight window parameters.

        'Rzmflux' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Rzmflux'.
            """

            super().__init__()

            self._: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets rxmflux deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self._ = value

    class Edoutf(DeterministicWeightWindowParameter):
        """
        'Edoutf' represents edoutf deterministic weight window parameters.

        'Edoutf' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Edoutf'.
            """

            super().__init__()

            self.ascii_output_control: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  cedoutf deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or not (-3 <= value <= 3):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.ascii_output_control = value

    class Byvlop(DeterministicWeightWindowParameter):
        """
        'Byvlop' represents byvlop deterministic weight window parameters.

        'Byvlop' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Byvlop'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets  cbyvlop deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Ajed(DeterministicWeightWindowParameter):
        """
        'Ajed' represents ajed deterministic weight window parameters.

        'Ajed' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Ajed'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets ajed deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    class Fluxone(DeterministicWeightWindowParameter):
        """
        'Fluxone' represents fluxone deterministic weight window parameters.

        'Fluxone' functions as a data subtype for 'DeterministicWeightWindowParameter'.
        It represents deterministic weight window parameter as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Fluxone'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets fluxone deterministic weight window
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid deterministic weight window parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DAWWG_VALUE
                )

            self.value = value
            self.state = value

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'DeterministicWeightWindow'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW

        self.pairs: tuple[self.DeterministicWeightWindowParameter] = None

    def set_parameters(self, *pairs: DeterministicWeightWindowParameter) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            pairs: Iterable of dawwg key-value pairs.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.pairs = pairs
        self.parameters = pairs


class EmbededGeometry(Datum):
    """
    'EmbededGeometry' represents embeded geometry specification
    data cards.

    'DeterministicMaterials' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    class EmbededGeometryParameter:
        """
        'EmbededGeometryParameter' represents embeded geometry
        specification data card parameter.

        'EmbededGeometryParameter' functions as a data type for
        'EmbededGeometry'. It represents embded geometry
        speciifcation data card parameters as abstract syntax elements.
        """

        class EmbededGeometryKeyword(StrEnum):
            """
             'EmbededGeometryKeyword' represents embeded
            geometry specification data card parameter keywords.

             'EmbededGeometryKeyword' functions as a data type for
             'EmbededGeometryParameter' and 'EmbededGeometry'. It
             represents card parameter keywords as abstract syntax elements.
            """

            #           MATCELL = "matcell"
            MESHOGEO = "meshgeo"
            MGEOIN = "mgeoin"
            MEEOUT = "meeout"
            MEEIN = "meein"
            CALC_VOLS = "calc_vols"
            DEBUG = "debug"
            FILETYPE = "filetype"
            GMVFILE = "gmvfile"
            LENGTH = "length"
            MCNPUMFILE = "mcnpumfile"
            #           OVERLAP = "overlap"

            @classmethod
            def cast_embed_keyword(
                cls, string: str, hook: Callable[Self, bool] = lambda: True
            ):
                """
                'cast_embed_keyword' types casts from strings to embeded geometry
                specification data card parameter keywords.

                'cast_embed_keyword' creates embeded geometry specification data card
                parameter keywords objects from strings. If the string is invalid
                or the hook returns false, it returns None.

                Parameters:
                    string: String to cast.
                    hook: Postcast check.

                Returns:
                    Embeded geometry specification parameter keyword from string.
                """

                string = string.lower()

                try:
                    keyword = cls(string)

                    if hook(keyword):
                        return keyword
                except ValueError:
                    pass

                return None

        def __init__(self) -> Self:
            """
            '__init__' initializes 'EmbededGeometryParameter'
            """

            self.keyword: self.EmbededGeometryKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: EmbededGeometryKeyword) -> None:
            """
            'set_keyword' sets deterministic embeded geometry specification
            parameter keywords.

            'set_keyword' checks keywords are valid. It
            raises errors if given None.

            Parameters:
                keyword: Embeded geometry specification parameter keywords.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_KEYWORD
                )

            self.keyword = keyword

        @classmethod
        def from_mcnp(cls, string: str):
            """
            'from_mcnp' generates embeded geometry specification parameter objects.

            'from_mcnp' constructs instances of 'EmbededGeometryParameter'
            from INP strings, so it functions as a class constructor. It
            transforms embeded geometry specification parameter into their
            correct subclasses.

            Parameters:
                card: INP to parse.

            Returns:
               Embeded gemoetry specification parameter object.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter entry.
                MCNPSyntaxError: Invalid embeded geometry specification parameter syntax.
            """

            parameter = cls()

            tokens = parser.Parser(
                string.split("="),
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES),
            )

            # Processing Keyword
            value = cls.EmbededGeometryKeyword.cast_keyword(tokens.peekl())
            parameter.set_keyword(value)

            # Processing Values
            match tokens.popl():
                #                case "matcell":
                #                    parameter.__class__ = EmbededGeometry.Matcell
                #
                #                    value =
                #                    parameter.set_parameter(value)

                case "meshgeo":
                    parameter.__class__ = EmbededGeometry.Meshgeo

                    parameter.set_parameter(tokens.popl())

                case "mgeoin":
                    parameter.__class__ = EmbededGeometry.Mgeoin

                    parameter.set_parameter(tokens.popl())

                case "meeout":
                    parameter.__class__ = EmbededGeometry.Meeout

                    parameter.set_parameter(tokens.popl())

                case "meein":
                    parameter.__class__ = EmbededGeometry.Meein

                    parameter.set_parameter(tokens.popl())

                case "calc_vols":
                    parameter.__class__ = EmbededGeometry.CalcVols

                    parameter.set_parameter(tokens.popl())

                case "debug":
                    parameter.__class__ = EmbededGeometry.Debug

                    parameter.set_parameter(tokens.popl())

                case "filetype":
                    parameter.__class__ = EmbededGeometry.Filetype

                    parameter.set_parameter(tokens.popl())

                case "gmvfile":
                    parameter.__class__ = EmbededGeometry.Gmvfile

                    parameter.set_parameter(tokens.popl())

                case "length":
                    parameter.__class__ = EmbededGeometry.Length

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_parameter(value)

                case "mcnpumfile":
                    parameter.__class__ = EmbededGeometry.Mcnpumfile

                    parameter.set_parameter(tokens.popl())

            #                case "overlap":
            #                    parameter.__class__ = EmbededGeometry.Overlap
            #
            #                    value =
            #                    parameter.set_parameter(value)

            if tokens:
                raise errors.MCNPSyntaxError(
                    errors.MCNPSyntaxCodes.TOOMANY_DATUM_ENTRIES
                )

    #    class Matcell(EmbededGeometryParameter):
    #        """
    #        'Matcell' represents matcell embeded geometry specification parameters.
    #
    #        'Matcell' functions as a data subtype for 'EmbededGeometryParameter'.
    #        It represents embeded geometry specification parameters as abstract syntax elements.
    #        """
    #
    #        def __init__(self) -> Self:
    #            """
    #            '__init__' initializes 'Matcell'.
    #            """
    #
    #            super().__init__()
    #
    #            self._: any = None
    #
    #        def set_value(self, value: int) -> None:
    #            """
    #            'set_value' sets matcell embeded geometry specification
    #            parameter values.
    #
    #            'set_value' checks values are valid. It
    #            raises errors if given None.
    #
    #            Parameters:
    #                value: Parameter value.
    #
    #            Raises:
    #                MCNPSemanticError: Invalid embeded geometry specification parameter value.
    #            """
    #
    #            if value is None:
    #                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EMBED_VALUE)
    #
    #            self.value = value
    #            self._ = value

    class Meshgeo(EmbededGeometryParameter):
        """
        'Meshgeo' represents meshgeo embeded geometry specification parameters.

        'Meshgeo' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Meshgeo'.
            """

            super().__init__()

            self.format: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets meshgeo embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or value not in {"lnk3dnt", "abaqus", "mcnpum"}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.format = value

    class Mgeoin(EmbededGeometryParameter):
        """
        'Mgeoin' represents mgeoin embeded geometry specification parameters.

        'Mgeoin' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Mgeoin'.
            """

            super().__init__()

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets mgeoin embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.filename = value

    class Meeout(EmbededGeometryParameter):
        """
        'Meeout' represents meeout embeded geometry specification parameters.

        'Meeout' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Meeout'.
            """

            super().__init__()

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets meeout embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.filename = value

    class Meein(EmbededGeometryParameter):
        """
        'Meein' represents meein embeded geometry specification parameters.

        'Meein' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Meein'.
            """

            super().__init__()

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets meein embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.filename = value

    class CalcVols(EmbededGeometryParameter):
        """
        'CalcVols' represents calc_vols embeded geometry specification parameters.

        'CalcVols' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'CalcVols'.
            """

            super().__init__()

            self.yes_no: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets calc_vols embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or value not in {"yes", "no"}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.yes_no = value

    class Debug(EmbededGeometryParameter):
        """
        'Debug' represents debug embeded geometry specification parameters.

        'Debug' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Debug'.
            """

            super().__init__()

            self.format: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets debug embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or value not in {"echomesh"}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.format = value

    class Filetype(EmbededGeometryParameter):
        """
        'Filetype' represents filetype embeded geometry specification parameters.

        'Filetype' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Filetype'.
            """

            super().__init__()

            self.type: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets filetype embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or value not in {"ascii", "binary"}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self._ = value

    class Gmvfile(EmbededGeometryParameter):
        """
        'Gmvfile' represents gmvfile embeded geometry specification parameters.

        'Gmvfile' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Gmvfile'.
            """

            super().__init__()

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets gmvfile embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.filename = value

    class Length(EmbededGeometryParameter):
        """
        'Length' represents length embeded geometry specification parameters.

        'Length' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Length'.
            """

            super().__init__()

            self.factor: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets length embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.factor = value

    class Mcnpumfile(EmbededGeometryParameter):
        """
        'Mcnpumfile' represents mcnpumfile embeded geometry specification parameters.

        'Mcnpumfile' functions as a data subtype for 'EmbededGeometryParameter'.
        It represents embeded geometry specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initializes 'Mcnpumfile'.
            """

            super().__init__()

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets mcnpumfile embeded geometry specification
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter value.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBED_VALUE
                )

            self.value = value
            self.filename = value

    #    class Overlap(EmbededGeometryParameter):
    #        """
    #        'Overlap' represents overlap embeded geometry specification parameters.
    #
    #        'Overlap' functions as a data subtype for 'EmbededGeometryParameter'.
    #        It represents embeded geometry specification parameters as abstract syntax elements.
    #        """
    #
    #        def __init__(self) -> Self:
    #            """
    #            '__init__' initializes 'Overlap'.
    #            """
    #
    #            super().__init__()
    #
    #            self._: any = None
    #
    #        def set_value(self, value: int) -> None:
    #            """
    #            'set_value' sets overlap embeded geometry specification
    #            parameter values.
    #
    #            'set_value' checks values are valid. It
    #            raises errors if given None.
    #
    #            Parameters:
    #                value: Parameter value.
    #
    #            Raises:
    #                MCNPSemanticError: Invalid embeded geometry specification parameter value.
    #            """
    #
    #            if value is None:
    #                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EMBED_VALUE)
    #
    #            self.value = value
    #            self._ = value

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'EmbededGeometry'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_GEOMETRY

        self.suffix: int = None
        self.pairs: tuple[types.Zaid] = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets embeded geometry specification
        data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(self, *pairs: EmbededGeometryParameter) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            pairs: Iterable of embed key-value pairs.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.pairs = pairs
        self.parameters = pairs


class EmbededElementalControl(Datum):
    """
    'EmbededElementalControl' represents embeded elemental edits
    control data cards.

    'DeterministicMaterials' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    class EmbededElementalControlParameter:
        """
        'EmbededElementalControlParameter' represents embeded elemental edits
        control data card parameter.

        'EmbededElementalControlParameter' functions as a data type for
        'EmbededElementalControl'. It represents embded geometry
        speciifcation data card parameters as abstract syntax elements.
        """

        class EmbededElementalControlKeyword(StrEnum):
            """
            'EmbededElementalControlKeyword' represents embeded
            elemental edits control data card parameter keywords.

            'EmbededElementalControlKeyword' functions as a data type for
            'EmbededElementalControlParameter' and 'EmbededElementalControl'. It
            represents card parameter keywords as abstract syntax elements.
            """

            EMBED = "embed"
            ENERGY = "energy"
            TIME = "time"
            ATOM = "atom"
            FACTOR = "factor"
            #           REACTION_LIST = "list"
            MAT = "mat"
            MTYPE = "mtype"

            @classmethod
            def cast_embed_keyword(
                cls, string: str, hook: Callable[Self, bool] = lambda: True
            ):
                """
                'cast_embed_keyword' types casts from strings to embeded elemental
                edits control data card parameter keywords.

                'cast_embed_keyword' creates embeded elemental edits control data card
                parameter keywords objects from strings. If the string is invalid
                or the hook returns false, it returns None.

                Parameters:
                    string: String to cast.
                    hook: Postcast check.

                Returns:
                    Embeded elemental edits control parameter keyword from string.
                """

                string = string.lower()

                try:
                    keyword = cls(string)

                    if hook(keyword):
                        return keyword
                except ValueError:
                    pass

                return None

        def __init__(self) -> Self:
            """
            '__init__' initializes 'EmbededElementalControlParameter'
            """

            self.keyword: self.EmbededElementalControlKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: EmbededElementalControlKeyword) -> None:
            """
            'set_keyword' sets deterministic embeded elemental
            edits control parameter keywords.

            'set_keyword' checks keywords are valid. It
            raises errors if given None.

            Parameters:
                keyword: Embeded elemental edits parameter keywords.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBEE_KEYWORD
                )

            self.keyword = keyword

        @classmethod
        def from_mcnp(cls, string: str):
            """
            'from_mcnp' generates embeded elemental edits control parameter objects.

            'from_mcnp' constructs instances of 'EmbededElementalControlParameter'
            from INP strings, so it functions as a class constructor. It
            transforms embeded elemental edits control parameter into their
            correct subclasses.

            Parameters:
                card: INP to parse.

            Returns:
               Embeded gemoetry specification parameter object.

            Raises:
                MCNPSemanticError: Invalid embeded geometry specification parameter entry.
                MCNPSyntaxError: Invalid embeded geometry specification parameter syntax.
            """

            parameter = cls()

            tokens = parser.Parser(
                string.split("="),
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES),
            )

            # Processing Keyword
            value = cls.EmbededElementalKeyword.cast_keyword(tokens.peekl())
            parameter.set_keyword(value)

            # Processing Values
            match tokens.popl():
                case "embed":
                    parameter.__class__ = EmbededElementalControl.Embed

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "energy":
                    parameter.__class__ = EmbededElementalControl.Energy

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "time":
                    parameter.__class__ = EmbededElementalControl.Time

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "atom":
                    parameter.__class__ = EmbededElementalControl.Atom

                    parameter.set_value(tokens.popl())

                case "factor":
                    parameter.__class__ = EmbededElementalControl.Factor

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                #                case "list":
                #                    parameter.__class__ = EmbededElementalControl.ReactionList
                #
                #                    value =
                #                    parameter.set_value(value)

                case "mat":
                    parameter.__class__ = EmbededElementalControl.Mat

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "mtype":
                    parameter.__class__ = EmbededElementalControl.Mtype

                    parameter.set_value(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(
                    errors.MCNPSyntaxCodes.TOOMANY_DATUM_ENTRIES
                )

    class Embed(EmbededElementalControlParameter):
        """
        'Embed' represents Embed embeded elemental edits control parameters.

        'Embed' functions as a data subtype for 'EmbededElementalControlParameter'.
        It represents embeded elemental edits control parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Embed'.
            """

            super().__init__()

            self.number: any = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets Embed embeded elemental edits control
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded elemental edits control parameter value.
            """

            if value is None or not (1 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBEE_VALUE
                )

            self.value = value
            self.number = value

    class Energy(EmbededElementalControlParameter):
        """
        'Energy' represents Energy embeded elemental edits control parameters.

        'Energy' functions as a data subtype for 'EmbededElementalControlParameter'.
        It represents embeded elemental edits control parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Energy'.
            """

            super().__init__()

            self.factor: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets Energy embeded elemental edits control
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded elemental edits control parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBEE_VALUE
                )

            self.value = value
            self.factor = value

    class Time(EmbededElementalControlParameter):
        """
        'Time' represents Time embeded elemental edits control parameters.

        'Time' functions as a data subtype for 'EmbededElementalControlParameter'.
        It represents embeded elemental edits control parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Time'.
            """

            super().__init__()

            self.factor: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets Time embeded elemental edits control
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded elemental edits control parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBEE_VALUE
                )

            self.value = value
            self.factor = value

    class Atom(EmbededElementalControlParameter):
        """
        'Atom' represents Atom embeded elemental edits control parameters.

        'Atom' functions as a data subtype for 'EmbededElementalControlParameter'.
        It represents embeded elemental edits control parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Atom'.
            """

            super().__init__()

            self.yes_no: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets Atom embeded elemental edits control
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded elemental edits control parameter value.
            """

            if value is None or value not in {"yes", "no"}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBEE_VALUE
                )

            self.value = value
            self.yes_no = value

    class Factor(EmbededElementalControlParameter):
        """
        'Factor' represents Factor embeded elemental edits control parameters.

        'Factor' functions as a data subtype for 'EmbededElementalControlParameter'.
        It represents embeded elemental edits control parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Factor'.
            """

            super().__init__()

            self.factor: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets Factor embeded elemental edits control
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded elemental edits control parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBEE_VALUE
                )

            self.value = value
            self.factor = value

    #    class ReactionList(EmbededElementalControlParameter):
    #        """
    #        'ReactionList' represents ReactionList embeded elemental edits control parameters.
    #
    #        'ReactionList' functions as a data subtype for 'EmbededElementalControlParameter'.
    #        It represents embeded elemental edits control parameters as abstract syntax elements.
    #        """
    #
    #        def __init__(self) -> Self:
    #            """
    #            '__init__' initialzies 'ReactionList'.
    #            """
    #
    #            super().__init__()
    #
    #            self._: any = None
    #
    #        def set_value(self, value: int) -> None:
    #            """
    #            'set_value' sets ReactionList embeded elemental edits control
    #            parameter values.
    #
    #            'set_value' checks values are valid. It
    #            raises errors if given None.
    #
    #            Parameters:
    #                value: Parameter value.
    #
    #            Raises:
    #                MCNPSemanticError: Invalid embeded elemental edits control  windeter value.
    #            """
    #
    #            if value is None:
    #                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EMBEE_VALUE)
    #
    #            self.value = value
    #            self._ = value

    class Mat(EmbededElementalControlParameter):
        """
        'Mat' represents Mat embeded elemental edits control parameters.

        'Mat' functions as a data subtype for 'EmbededElementalControlParameter'.
        It represents embeded elemental edits control parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.number: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets Mat embeded elemental edits control
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded elemental edits control parameter value.
            """

            if value is None or not (0 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBEE_VALUE
                )

            self.value = value
            self.number = value

    class Mtype(EmbededElementalControlParameter):
        """
        'Mtype' represents Mtype embeded elemental edits control parameters.

        'Mtype' functions as a data subtype for 'EmbededElementalControlParameter'.
        It represents embeded elemental edits control parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mtype'.
            """

            super().__init__()

            self.type: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets Mtype embeded elemental edits control
            parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid embeded elemental edits control parameter value.
            """

            if value is None or value not in {
                "flux",
                "isotopic",
                "population",
                "reaction",
                "source",
                "tracks",
            }:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_EMBEE_VALUE
                )

            self.value = value
            self.type = value

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'EmbededElementalControl'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_CONTROL

        self.suffix: int = None
        self.pairs: tuple[types.Zaid] = None
        self.designator: tuple[types.Designator] = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets embeded elemental edits control
        data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

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

    def set_parameters(self, *pairs: EmbededElementalControlParameter) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            pairs: Iterable of embee key-value pairs.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.pairs = pairs
        self.parameters = pairs


class EmbededElementalEnergyBoundaries(Datum):
    """
    'EmbededElementalEnergyBoundaries' represents embeded elemental edits energy bin
    boundaries data cards.

    'EmbededElementalEnergyBoundaries' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'EmbededElementalEnergyBoundaries'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_ENERGY_BOUNDARIES

        self.energies: tuple[float] = None
        self.suffix: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets embeded elemental edits energy bin boundaries
        data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(self, *energies: float) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *energies: Iterable of energies.
        """

        for parameter in energies:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = energies
        self.energies = energies


class EmbededElementalEnergyMultipliers(Datum):
    """
    'EmbededElementalEnergyMultipliers' represents embeded elemental edits energy bin
    multipliers data cards.

    'EmbededElementalEnergyMultipliers' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'EmbededElementalEnergyMultipliers'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_ENERGY_MULTIPLIERS

        self.multipliers: tuple[float] = None
        self.suffix: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets embeded elemental edits energy bin
        multiplier data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(self, *multipliers: float) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *multipliers: Iterable of multipliers.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = multipliers
        self.multipliers = multipliers


class EmbededElementalTimeBoundaries(Datum):
    """
    'EmbededElementalTimeBoundaries' represents embeded elemental edits time bin
    boundaries data cards.

    'EmbededElementalTimeBoundaries' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'EmbededElementalTimeBoundaries'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_TIME_BOUNDARIES

        self.energies: tuple[float] = None
        self.suffix: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets embeded elemental edits time bin boundaries
        data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(self, *times: float) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *times: Iterable of times.
        """

        for parameter in times:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = times
        self.times = times


class EmbededElementalTimeMultipliers(Datum):
    """
    'EmbededElementalTimeMultipliers' represents embeded elemental edits time bin
    multipliers data cards.

    'EmbededElementalTimeMultipliers' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'EmbededElementalTimeMultipliers'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_TIME_MULTIPLIERS

        self.multipliers: tuple[float] = None
        self.suffix: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets embeded elemental edits time bin
        multiplier data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(self, *multipliers: float) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *multipliers: Iterable of multipliers.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = multipliers
        self.multipliers = multipliers


class EmbededElementalDoseBoundaries(Datum):
    """
    'EmbededElementalDoseBoundaries' represents embeded elemental edits dose bin
    boundaries data cards.

    'EmbededElementalDoseBoundaries' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'EmbededElementalDoseBoundaries'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_DOSE_BOUNDARIES

        self.energies: tuple[float] = None
        self.suffix: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets embeded elemental edits dose bin boundaries
        data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(self, *doses: float) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *doses: Iterable of doses.
        """

        for parameter in doses:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = doses
        self.doses = doses


class EmbededElementalDoseMultipliers(Datum):
    """
    'EmbededElementalDoseMultipliers' represents embeded elemental edits dose bin
    multipliers data cards.

    'EmbededElementalDoseMultipliers' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'EmbededElementalDoseMultipliers'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_DOSE_MULTIPLIERS

        self.multipliers: tuple[float] = None
        self.suffix: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets embeded elemental edits dose bin
        multiplier data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(self, *multipliers: float) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *multipliers: Iterable of multipliers.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = multipliers
        self.multipliers = multipliers


class Material(Datum):
    """
    'Material' represents material specification data cards.

    'Material' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    class MaterialValue:
        """
        'MaterialValue' represents material specification entries.

        'MaterialValue' stores zaid and fraction values.
        """

        def __init__(self) -> Self:
            """
            '__init__' initalizes 'MaterialValue'
            """

            self.zaid: types.Zaid = None
            self.fraction: float = None

        @classmethod
        def from_mcnp(cls, string: str) -> Self:
            """
            'from_mcnp' generates stochastic geometry entries.

            'from_mcnp' constructs instances of 'MaterialValue'
            from INP strings, so it functions as a class constructor.

            Parameters:
                string: INP to parse.

            Returns:
                Material specification value object.

            Raises:
                MCNPSemanticError: Invalid card parameter entry.
                MCNPSyntaxError: Invalid card paramter syntax.
            """

            entry = cls()

            tokens = parser.Parser(
                string.split(" "),
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES),
            )

            # Parsing zzzaaa
            value = types.Zaid().cast_mcnp_zaid(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

            self.zaid = value

            # Parsing fraction
            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

            self.fraction = value

    class MaterialParameter:
        """
        'MaterialParameter' represents material specification parameters.

        'MaterialParameter' functions as a data type for
        'Matieral'. It represents material specification data card
        parameters as abstract syntax elements.
        """

        class MaterialKeyword(StrEnum):
            """
            'MaterialKeyword' represents material specification keywords.

            'MaterialKeyword' functions as a data type for 'MaterialParameter'
            and 'Material'. It represents card parameter keywords as abstract
            syntax elements.
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
            #           REFC = "refc"
            #           REFS = "refs"

            @classmethod
            def cast_material_keyword(
                cls, string: str, hook: Callable[Self, bool]
            ) -> Self:
                """
                'cast_material_keyword' types casts from strings to material specification
                parameter keywords.

                'cast_material_keyword' creates material specification data card
                parameter keywords objects from strings. If the string is invalid
                or the hook returns false, it returns None.

                Parameters:
                    string: String to cast.
                    hook: Postcast check.

                Returns:
                    Material specification parameter keyword from string.
                """

                string = string.lower()

                try:
                    keyword = cls(string)

                    if hook(keyword):
                        return keyword
                except ValueError:
                    pass

                return None

        def __init__(self) -> Self:
            """
            '__init__' initializes 'MaterialParameter'
            """

            self.keyword: MaterialKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: MaterialKeyword) -> None:
            """
            'set_keyword' sets deterministic embeded elemental
            edits control parameter keywords.

            'set_keyword' checks keywords are valid. It
            raises errors if given None.

            Parameters:
                keyword: Material specification parameter keywords.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_KEYWORD
                )

            self.keyword = keyword

        @classmethod
        def from_mcnp(cls, string: str):
            """
            'from_mcnp' generates material specification parameter objects.

            'from_mcnp' constructs instances of 'MaterialParameter'
            from INP strings, so it functions as a class constructor. It
            transforms embeded geometry specification parameter into their
            correct subclasses.

            Parameters:
                card: INP to parse.

            Returns:
               Material specification parameter object.

            Raises:
                MCNPSemanticError: Invalid material specification parameter entry.
                MCNPSyntaxError: Invalid material specification parameter syntax.
            """

            parameter = cls()

            tokens = parser.Parser(
                string.split(" "),
                errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_ENTRIES),
            )

            # Processing Keyword
            value = cls.EmbededGeometryKeyword.cast_keyword(tokens.peekl())
            parameter.set_keyword(value)

            # Processing Values
            match tokens.popl():
                case "gas":
                    parameter.__class__ = Gas

                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "estep":
                    parameter.__class__ = Estep

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "hstep":
                    parameter.__class__ = Hstep

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "nlib":
                    parameter.__class__ = Nlib

                    parameter.set_value(tokens.popl())

                case "plib":
                    parameter.__class__ = Plib

                    parameter.set_value(tokens.popl())

                case "pnlib":
                    parameter.__class__ = Pnlib

                    parameter.set_value(tokens.popl())

                case "elib":
                    parameter.__class__ = Elib

                    parameter.set_value(tokens.popl())

                case "hlib":
                    parameter.__class__ = Hlib

                    parameter.set_value(tokens.popl())

                case "alib":
                    parameter.__class__ = Alib

                    parameter.set_value(tokens.popl())

                case "slib":
                    parameter.__class__ = Slib

                    parameter.set_value(tokens.popl())

                case "tlib":
                    parameter.__class__ = Tlib

                    parameter.set_value(tokens.popl())

                case "dlib":
                    parameter.__class__ = Dlib

                    parameter.set_value(tokens.popl())

                case "cond":
                    parameter.__class__ = Cond

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "refi":
                    parameter.__class__ = Refi

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

    #                case "refc":
    #                    parameter.__class__ = Refc
    #
    #                    value =
    #                    parameter.set_value(value)
    #
    #                case "refs":
    #                    parameter.__class__ = Refs
    #
    #                    value =
    #                    parameter.set_value(value)

    class Gas(MaterialParameter):
        """
        'Gas' represents gas material specification parameters.

        'Gas' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets gas material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.state = value

    class Estep(MaterialParameter):
        """
        'Estep' represents estep material specification parameters.

        'Estep' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.step: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets estep material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.step = value

    class Hstep(MaterialParameter):
        """
        'Hstep' represents hstep material specification parameters.

        'Hstep' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.step: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets hstep material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.step = value

    class Nlib(MaterialParameter):
        """
        'Nlib' represents nlib material specification parameters.

        'Nlib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets nlib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.abx = value

    class Plib(MaterialParameter):
        """
        'Plib' represents plib material specification parameters.

        'Plib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets plib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self._ = value

    class Pnlib(MaterialParameter):
        """
        'Pnlib' represents pnlib material specification parameters.

        'Pnlib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets pnlib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.abx = value

    class Elib(MaterialParameter):
        """
        'Elib' represents elib material specification parameters.

        'Elib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: int) -> None:
            """
            'set_value' sets elib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.abx = value

    class Hlib(MaterialParameter):
        """
        'Hlib' represents hlib material specification parameters.

        'Hlib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets hlib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.abx = value

    class Alib(MaterialParameter):
        """
        'Alib' represents alib material specification parameters.

        'Alib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets alib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.abx = value

    class Slib(MaterialParameter):
        """
        'Slib' represents slib material specification parameters.

        'Slib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets slib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.abx = value

    class Tlib(MaterialParameter):
        """
        'Tlib' represents tlib material specification parameters.

        'Tlib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets tlib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.abx = value

    class Dlib(MaterialParameter):
        """
        'Dlib' represents dlib material specification parameters.

        'Dlib' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            'set_value' sets dlib material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.abx = value

    class Cond(MaterialParameter):
        """
        'Cond' represents cond material specification parameters.

        'Cond' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.conducation_state: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets cond material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.conducation_state = value

    class Refi(MaterialParameter):
        """
        'Refi' represents refi material specification parameters.

        'Refi' functions as a data subtype for 'MaterialParameter'.
        It represents material specification parameters as abstract syntax elements.
        """

        def __init__(self) -> Self:
            """
            '__init__' initialzies 'Mat'.
            """

            super().__init__()

            self.constant_refracive_index: float = None

        def set_value(self, value: float) -> None:
            """
            'set_value' sets refi material specification parameter values.

            'set_value' checks values are valid. It
            raises errors if given None.

            Parameters:
                value: Parameter value.

            Raises:
                MCNPSemanticError: Invalid material specification parameter value.
            """

            if value is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE
                )

            self.value = value
            self.constant_refracive_index = value

    #    class Refc(MaterialParameter):
    #        """
    #        'Refc' represents refc material specification parameters.
    #
    #        'Refc' functions as a data subtype for 'MaterialParameter'.
    #        It represents material specification parameters as abstract syntax elements.
    #        """
    #
    #        def __init__(self) -> Self:
    #            """
    #            '__init__' initialzies 'Mat'.
    #            """
    #
    #            super().__init__()
    #
    #            self._: int = None
    #
    #        def set_value(self, value: int) -> None:
    #            """
    #            'set_value' sets refc material specification parameter values.
    #
    #            'set_value' checks values are valid. It
    #            raises errors if given None.
    #
    #            Parameters:
    #                value: Parameter value.
    #
    #            Raises:
    #                MCNPSemanticError: Invalid material specification parameter value.
    #            """
    #
    #            if value is None:
    #                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)
    #
    #            self.value = value
    #            self._ = value

    #    class Refs(MaterialParameter):
    #        """
    #        'Refs' represents refs material specification parameters.
    #
    #        'Refs' functions as a data subtype for 'MaterialParameter'.
    #        It represents material specification parameters as abstract syntax elements.
    #        """
    #
    #        def __init__(self) -> Self:
    #            """
    #            '__init__' initialzies 'Mat'.
    #            """
    #
    #            super().__init__()
    #
    #            self._: int = None
    #
    #        def set_value(self, value: int) -> None:
    #            """
    #            'set_value' sets refs material specification parameter values.
    #
    #            'set_value' checks values are valid. It
    #            raises errors if given None.
    #
    #            Parameters:
    #                value: Parameter value.
    #
    #            Raises:
    #                MCNPSemanticError: Invalid material specification parameter value.
    #            """
    #
    #            if value is None:
    #                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)
    #
    #            self.value = value
    #            self._ = value

    def __init__(self) -> Self:
        """
        '__init__' initialzies 'Material'.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.MATERIAL

        self.suffix: int = None
        self.substances: tuple[MaterialValue] = None
        self.paris: tuple[MaterialParameter] = None

    def set_parameters(
        self, substances: tuple[MaterialValue], pairs: tuple[MaterialParameter]
    ) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            substances: Iterable of material values.
            paris: Iterable of key-value pairs.
        """

        for parameter in substances:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.substances = substances

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.paris = pairs

        self.parameters = tuple(list(substances) + list(pairs))

    @classmethod
    def from_formula(cls, formulas: dict[str, float]) -> Self:
        """
        'from_formula'
        """

        material = cls()

        elements = {}
        for formula, fraction in formulas.items():
            tokens = parser.Parser(types.ELEMENTS_PATTERN.findall(formula), SyntaxError)

            atoms = {}
            while tokens:
                # Checking first token is not numeric.
                if tokens.peekl() not in types.ELEMENTS:
                    raise SyntaxError

                element = tokens.popl()

                if not tokens or tokens.peekl() in types.ELEMENTS:
                    # Adding symbol without subscript
                    atoms[element] = 1
                elif types.cast_fortran_integer(tokens.peekl()) is not None:
                    # Adding symbol with subscript
                    atoms[element] = types.cast_fortran_integer(tokens.popl())
                else:
                    raise SyntaxError

            total = sum(atoms.values())

            # Adding current forumla elements to dictionary.
            for atom, count in atoms.items():
                if atom not in elements:
                    elements[atom] = fraction * (count / total)
                else:
                    elements[atom] += fraction * (count / total)

        substances = []
        for element, fraction in elements.items():
            zaid = types.Zaid()
            zaid.z = types.ELEMENTS[element]
            zaid.a = 0

            substance = cls.MaterialValue()
            substance.zaid = zaid
            substance.fraction = fraction

            substances.append(substance)

        material.set_parameters(tuple(substances), ())

        return material


class MaterialNeutronScattering(Datum):
    """
    'MaterialNeutronScattering' represents thermal neutron
    scattering data cards.

    'MaterialNeutronScattering' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'MaterialNeutronScattering'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.THERMAL_NETURON_SCATTERING

        self.identifiers: tuple[str] = None
        self.suffix: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets thermal neutron scattering
        data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

    def set_parameters(self, *identifiers: str) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *identifiers: Iterable of identifiers.
        """

        for parameter in identifiers:
            if parameter is None or not parmeter:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = identifiers
        self.identifiers = identifiers


class MaterialNuclideSubstitution(Datum):
    """
    'MaterialNuclideSubstitution' represents thermal neutron
    scattering data cards.

    'MaterialNuclideSubstitution' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'MaterialNuclideSubstitution'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.THERMAL_NETURON_SCATTERING

        self.zaids: tuple[types.Zaid] = None
        self.suffix: int = None
        self.designator: tuple[types.Designator] = None

    def set_suffix(self, suffix: int) -> None:
        """
        'set_suffix' sets thermal neutron scattering
        data card keyword suffixes.

        'set_suffix' checks suffixes are valid.
        It raises errors if given None.

        Parameters:
            suffix: Data card mnemonic suffix.
        """

        if suffix is None and not (1 <= suffix <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX
            )

        self.suffix = suffix

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

    def set_parameters(self, *zaids: types.Zaid) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *zaids: Iterable of zaids.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = zaids
        self.zaids = zaids


class OnTheFlyBroadening(Datum):
    """
    'OnTheFlyBroadening' represents on-the-fly broadening data cards.

    'OnTheFlyBroadening' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'OnTheFlyBroadening'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.ONTHEFLY_BROADENING

        self.zaids: tuple[types.Zaid] = None

    def set_parameters(self, *zaids: types.Zaid) -> None:
        """
        'set_parameters' sets data card parameters.

        'set_parameters' checks parameter entries are valid, and
        it raises errors if given None.

        Parameters:
            *zaids: Iterable of zaids.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETER
                )

        self.parameters = zaids
        self.zaids = zaids


class TotalFission(Datum):
    """
    'TotalFission' represents the total fission card.

    'TotalFission' functions as a data subtype for 'Datum'.
    It represents datum cards as an abstract syntax element.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Volume'
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.TOTAL_FISSION

        self.has_no: bool = None
