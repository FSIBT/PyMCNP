"""
``datum`` contains the class representing INP data cards.

``datum`` packages the ``Datum`` class, providing an object-oriented,
importable interface for INP datum cards.
"""


import re
from typing import Callable
from enum import StrEnum

from .card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Datum(Card):
    """
    ``Datum`` represents INP data cards.

    ``Datum`` implements INP data cards as a Python class. Its attributes store
    INP data card input parameters, and its methods provide entry points and
    endpoints for working with MCNP cells. It represents the INP data card
    syntax element, and it inherits from the ``Card`` super class.

    Attributes:
        mnemonic: Data card mnemonics.
        parameters: Data card parameters.
    """

    class DatumMnemonic(StrEnum):
        """
        ``DatumMnemonic`` represents INP data card mnemonics

        ``DatumMnemonic`` implements INP data card mnemonics as a Python inner
        class. It enumerates MCNP mnemonics and provides methods for casting
        strings to ``DatumMnemonic`` instances. It represents the INP data card
        mnemonics syntax element, so ``Datum`` depends on ``DatumMnemonic`` as
        an enum.
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

        @staticmethod
        def from_mcnp(cls, source: str):
            """
            ``from_mcnp`` generates ``DatumMnemonic`` objects from INP.

            ``from_mcnp`` constructs instances of ``DatumMnemonic`` from INP
            source strings, so it operates as a class constructor method
            and INP parser helper function.

            Parameters:
                source: INP for data card mnemonic.

            Returns:
                ``DatumMnemonic`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MNEMONIC.
            """

            source = _parser.Preprocessor.process_inp(source)

            # Handling Star Modifier
            if string == "*tr":
                string = string[:1]

            # Handling Suffixes
            if string.startswith("dm"):
                if len(string) < 3 or types.cast_fortran_integer(string[2:]) is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC)

                string = string[:2]
            elif string.startswith("m"):
                if len(string) < 2 or types.cast_fortran_integer(string[1:]) is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC)

                string = string[:1]

            # Processing Keyword
            if source not in [enum.value for enum in cls]:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC)

            return cls(source)

    def __init__(
        self,
        mnemonic: DatumMnemonic,
        parameters: tuple[any],
    ):
        """
        ``__init__`` initializes ``Datum``.

        Parameters:
            number: Data card mnemonic.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MNEMONIC.
        """

        super().__init__(mnemonic + str(suffix) if suffix is not None else mnemonic)

        if mnemonic is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC)

        match mnemoinc:
            case cls.DatumMnemonic.VOLUME:
                obj = Volume()
            case cls.DatumMnemonic.AREA:
                obj = Area()
            case cls.DatumMnemonic.TRANSFORMATION:
                obj = Transformation()
            case cls.DatumMnemonic.UNIVERSE:
                obj = Universe()
            case cls.DatumMnemonic.LATTICE:
                obj = Lattice()
            case cls.DatumMnemonic.FILL:
                obj = Fill()
            case cls.DatumMnemonic.STOCHASTIC_GEOMETRY:
                obj = StochasticGeometry()
            case cls.DatumMnemonic.DETERMINISTIC_MATERIALS:
                obj = DeterministicMaterials()
            case cls.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW:
                obj = DeterministicWeightWindow()
            case cls.DatumMnemonic.EMBEDED_GEOMETRY:
                obj = EmbeddedGeometry()
            case cls.DatumMnemonic.EMBEDED_CONTROL:
                obj = EmbeddedControl()
            case cls.DatumMnemonic.EMBEDED_ENERGY_BOUNDARIES:
                obj = EmbeddedEnergyBoundaries()
            case cls.DatumMnemonic.EMBEDED_ENERGY_MULTIPLIERS:
                obj = EmbeddedEnergyMultipliers()
            case cls.DatumMnemonic.EMBEDED_TIME_BOUNDARIES:
                obj = EmbeddedTimeBoundaries()
            case cls.DatumMnemonic.EMBEDED_TIME_MULTIPLIERS:
                obj = EmbeddedTimeMultipliers()
            case cls.DatumMnemonic.EMBEDED_DOSE_BOUNDARIES:
                obj = EmbeddedDoseBoundaries
            case cls.DatumMnemonic.EMBEDED_DOSE_MULTIPLIERS:
                obj = EmbeddedDoseMultipliers()
            case cls.DatumMnemonic.MATERIAL:
                obj = Material()

        self.__dict__ = obj.__dict__
        self.__class__ = obj.__class__

    def set_mnemonic(self, mnemonic: DatumMnemonic) -> None:
        """
        ``set_mnemonic`` stores INP data card mnemonic.

        ``set_mnemonic`` checks given arguments before assigning the given
        value to ``Datum.mnemonic``. If given an unrecognized argument, it
        raises semantic errors.

        """

        if mnemonic is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC)

        if mnemonic != self.mnemonic:
            match mnemoinc:
                case cls.DatumMnemonic.VOLUME:
                    obj = Volume()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.AREA:
                    obj = Area()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.TRANSFORMATION:
                    obj = Transformation()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.UNIVERSE:
                    obj = Universe()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.LATTICE:
                    obj = Lattice()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.FILL:
                    obj = Fill()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.STOCHASTIC_GEOMETRY:
                    obj = StochasticGeometry()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.DETERMINISTIC_MATERIALS:
                    obj = DeterministicMaterials()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW:
                    obj = DeterministicWeightWindow()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_GEOMETRY:
                    obj = EmbeddedGeometry()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_CONTROL:
                    obj = EmbeddedControl()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_ENERGY_BOUNDARIES:
                    obj = EmbeddedEnergyBoundaries()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_ENERGY_MULTIPLIERS:
                    obj = EmbeddedEnergyMultipliers()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_TIME_BOUNDARIES:
                    obj = EmbeddedTimeBoundaries()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_TIME_MULTIPLIERS:
                    obj = EmbeddedTimeMultipliers()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_DOSE_BOUNDARIES:
                    obj = EmbeddedDoseBoundaries
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_DOSE_MULTIPLIERS:
                    obj = EmbeddedDoseMultipliers()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.MATERIAL:
                    obj = Material()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__

    @staticmethod
    def from_mcnp(cls, source: str, line: int = None):
        """
        ``from_mcnp`` generates ``Datum`` objects from INP.

        ``from_mcnp`` constructs instances of ``Datum`` from INP source
        strings, so it operates as a class constructor method and INP parser
        helper function.

        Parameters:
            source: INP for datum.
            line: Line number.

        Returns:
            ``Datum`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_DATUM, TOOLONG_DATUM.
        """

        datum = cls()

        # Processing Line Number
        datum.line = line

        # Processing Inline Comment
        if "$" in source:
            source, comment = source.split("$")
            datum.comment = comment

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(re.split(r" |:|=", card), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM))

        # Processing Mnemonic
        mnemonic = cls.DatumMnemonic.from_mcnp(tokens.peekl())
        datum.set_mnemonic(mnemonic)

        # Processing Entries
        match mnemonic:
            case cls.DatumMnemonic.VOLUME:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

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

            case cls.DatumMnemonic.AREA:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                areas = []
                while tokens:
                    areas.append(types.cast_fortran_real(tokens.popl()))

                datum.set_parameters(*areas)

            case cls.DatumMnemonic.TRANSFORMATION:
                if len(tokens) > 13:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                if len(tokens) < 13:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

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

            case cls.DatumMnemonic.UNIVERSE:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                universes = []
                while tokens:
                    universes.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*universes)

            case cls.DatumMnemonic.LATTICE:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                lattices = []
                while tokens:
                    lattices.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*lattices)

            case cls.DatumMnemonic.FILL:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                fills = []
                while tokens:
                    fills.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*fills)

            case cls.DatumMnemonic.STOCHASTIC_GEOMETRY:
                if len(tokens) % 4 != 0:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Mnemonic
                tokens.popl()

                # Processing Parameters
                transformions = []
                while tokens:
                    source = " ".join([tokens.popl(), tokens.popl(), tokens.popl(), tokens.popl()])
                    transformions.append(StochasticGeometry.StochasticGeometryValue().from_mcnp(source))

                datum.set_parameters(*transformions)

            case cls.DatumMnemonic.DETERMINISTIC_MATERIALS:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[2:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                materials = []
                while tokens:
                    materials.append(types.Zaid.cast_mcnp_zaid(tokens.popl()))

                datum.set_parameters(*materials)

            case cls.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Mnemoninc
                tokens.popl()

                # Processing Parameters
                pairs = []
                while tokens:
                    paris.append(DeterministicWeightWindow.DeterministicWeightWindowOption.from_mcnp(tokens.popl()))

                datum.set_parameters(*pairs)

            case cls.DatumMnemonic.EMBEDED_GEOMETRY:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                pairs = []
                while tokens:
                    paris.append(EmbeddedGeometry.EmbeddedGeometryOption.from_mcnp(tokens.popl()))

                datum.set_parameters(*pairs)

            case cls.DatumMnemonic.EMBEDED_CONTROL:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Designator
                designator = types.Designator.cast_mcnp_designator(tokens.popl())
                parameter.set_designator(designator)

                # Processing Parameters
                pairs = []
                while tokens:
                    paris.append(EmbeddedControl.EmbeddedControlOption.from_mcnp(tokens.popl()))

                datum.set_parameters(*pairs)

            case cls.DatumMnemonic.EMBEDED_ENERGY_BOUNDARIES:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                energies = []
                while tokens:
                    doses.append(types.cast_fortran_reals(tokens.popl()))

                datum.set_parameters(*energies)

            case cls.DatumMnemonic.EMBEDED_ENERGY_MULTIPLIERS:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                multipliers = []
                while tokens:
                    doses.append(types.cast_fortran_reals(tokens.popl()))

                datum.set_parameters(*multipliers)

            case cls.DatumMnemonic.EMBEDED_TIME_BOUNDARIES:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                times = []
                while tokens:
                    doses.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*times)

            case cls.DatumMnemonic.EMBEDED_TIME_MULTIPLIERS:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                multipliers = []
                while tokens:
                    doses.append(types.cast_fortran_reals(tokens.popl()))

                datum.set_parameters(*multipliers)

            case cls.DatumMnemonic.EMBEDED_DOSE_BOUNDARIES:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                doses = []
                while tokens:
                    doses.append(types.cast_fortran_integer(tokens.popl()))

                datum.set_parameters(*doses)

            case cls.DatumMnemonic.EMBEDED_DOSE_MULTIPLIERS:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                multipliers = []
                while tokens:
                    doses.append(types.cast_fortran_reals(tokens.popl()))

                datum.set_parameters(*multipliers)

            case cls.DatumMnemonic.MATERIAL:
                if len(tokens) < 2:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                # Processing Suffix
                suffix = types.cast_fortran_integer(tokens.popl()[1:])
                parameter.set_suffix(suffix)

                # Processing Parameters
                substances = []
                while tokens:
                    source = " ".join([tokens.popl(), tokens.popl()])
                    paris.append(Material.MaterialOption().from_mcnp(source))

                pairs = []
                while tokens:
                    source = "=".join([tokens.popl(), tokens.popl()])
                    paris.append(Material.MaterialOption().from_mcnp(source))

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM)

        return datum

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Datum`` objects.

        ``to_mcnp`` creates INP source string from ``Datum``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``Datum`` object.
        """

        # Formatting Number
        number_str = f"{self.number}" if self.number is not None else ""

        return f"{self.mnemonic}{number_str} {' '.join(self.parameters)}"

    def to_arguments(self) -> list:
        """
        ``to_arguments`` makes dictionaries from ``Datum`` objects.

        ``to_arguments`` creates Python dictionaries from ``Datum`` objects, so
        it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual. Although defined on the superclass, it returns key-value pairs
        suffixes and designators as required.

        Returns:
            Dictionary for ``Datum`` object.
        """

        return {
            "mnemonic": self.mnemonic,
            "m": self.suffix if hasattr(self.__class__, "suffix") else None,
            "n": self.designator if hasattr(self.__class__, "designator") else None,
            "parameters": self.parameters,
        }


class Volume(Datum):
    """
    ``Volume`` represents INP volume data cards.

    ``Volume`` inherits attributes from ``Datum``. It represents the INP volume
    data card syntax element.

    Attributes:
        has_no: No volume calculation option.
        volumes: Tuple of cell volumes.
    """

    def __init__(self, volumes: tuple[float], has_no: bool = False):
        """
        ``__init__`` initializes ``Volume``.

        Parameters:
            has_no: No volume calculation option.
            volumes: Tuple of cell volumes.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        super().__init__()

        for entry in volumes:
            if entry is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if has_no is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.VOLUME
        self.parameters = (has_no, volumes)

        self.has_no = has_no
        self.volumes = volumes


class Area(Datum):
    """
    ``Area`` represents INP area data cards.

    ``Area`` inherits attributes from ``Datum``. It represents the INP area
    data card syntax element.

    Attributes:
        areas: Tuple of cell areas.
    """

    def __init__(self, areas: tuple[float]):
        """
        ``__init__`` initializes ``Area``.

        Parameters:
            areas: Tuple of cell areas.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in areas:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic: final[DatumMnemonic] = Datum.DatumMnemonic.AREA
        self.parameters: final[[tuple[float]]] = areas

        self.areas: final[tuple[float]] = areas


class Transformation(Datum):
    """
    ``Transformation`` represents INP transformion data cards.

    ``Transformation`` inherits attributes from ``Datum``. It represents the INP
    transformion data card syntax element.

    Attributes:
        displacement: Transformation displacement vector.
        rotation: Transformation rotation matrix.
        system: Transformation coordinate system setting.
        suffix: Data card suffix.
    """

    def __init__(self, displacement: tuple[float], rotation: tuple[float], system: int, suffix: int):
        """
        ``__init__`` initializes ``Transformation``.

        Parameters:
            displacement: Transformation displacement vector.
            rotation: Transformation rotation matrix.
            system: Transformation coordinate system setting.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSematnicCodes.INVALID_DATUM_SUFFIX)

        for entry in displacement:
            if entry is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for row in rotation:
            for entry in row:
                if entry is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if system is None or system not in {-1, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.suffix = suffix
        self.mnemonic = Datum.DatumMnemonic.TRANSFORMATION
        self.parameters = tuple(displacement, rotation, system)

        self.displacement = displacement
        self.rotation = rotation
        self.system = system


class Universe(Datum):
    """
    ``Universe`` represents INP universe data cards.

    ``Universe`` inherits attributes from ``Datum``. It represents the INP
    universe data card syntax element.

    Attributes:
        universes: Tuple of cell universe numbers.
    """

    def __init__(self, universes: tuple[int]):
        """
        ``__init__`` initializes ``Universe``.

        Parameters:
            universes: Tuple of cell universe numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in unvierses:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.UNIVERSE
        self.universes = unvierses

        self.parameters = unvierses


class Lattice(Datum):
    """
    ``Lattice`` represents INP lattice data cards.

    ``Lattice`` inherits attributes from ``Datum``. It represents the INP
    lattice data card syntax element.

    Attributes:
        lattices: Tuple of cell lattice numbers.
    """

    def __init__(self, lattices: tuple[int]):
        """
        ``__init__`` initializes ``Lattice``.

        Parameters:
            lattices: Tuple of cell lattice numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in lattices:
            if parameter is None or parameter not in {1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.LATTICE
        self.lattices = lattices

        self.parameters = lattices


class Fill(Datum):
    """
    ``Fill`` represents INP fill data cards.

    ``Fill`` inherits attributes from ``Datum``. It represents the INP
    universe data card syntax element.

    Attributes:
        fills: Tuple of universe numbers.
    """

    def __init__(self, fills: tuple[int]):
        """
        ``__init__`` initializes ``Fill``.

        Parameters:
            *fills: Tuple of universe numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in fills:
            if parameter is None or not (parameter >= 0 and parameter <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.FILL
        self.parameters = fills

        self.fills = fills


class StochasticGeometry(Datum):
    """
    ``StochasticGeometry`` represents INP stochastic geometry data cards.

    ``StochasticGeometry`` inherits attributes from ``Datum``. It represents
    the INP universe data card syntax element.

    Attributes:
        transformions: Tuple of stochastric geometry transformions.
    """

    class StochasticGeometryValue:
        """
        ``StochasticGeometryValue`` represents INP stochastic geometry data
        card entries.

        ``StochasticGeometryValue`` implements INP stochastic geometry
        specifications as a Python inner class. Its attributes store different
        stochastic geometry entries, and its methods provide entry points
        and endpoints for working with stochastic geometry entries.
        ``StochasticGeometry`` depends on ``StochasticGeometryValue`` as a data
        type.

        Attributes:
            number: Stochastic geometry universe number.
            maximum_x: Stochastic geometry maximum translation in x direction.
            maximum_y: Stochastic geometry maximum translation in y direction.
            maximum_z: Stochastic geometry maximum translation in z direction.
        """

        def __init__(self, number: int, maximum_x: float, maximum_y: float, maximum_z: float):
            """
            ``__init__`` initializes ``StochasticGeometryValue``.

            Parameters:
                number: Stochastic geometry universe number.
                maximum_x: Stochastic geometry maximum translation in x direction.
                maximum_y: Stochastic geometry maximum translation in y direction.
                maximum_z: Stochastic geometry maximum translation in z direction.

            Raises:
                MCNPSemanticCodes: INVALID_DATUM_PARAMETERS.
            """

            if number is None or not (1 <= number <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if maximum_x is None:
                raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if maximum_y is None:
                raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if maximum_z is None:
                raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.number: final[int] = number
            self.maximum_x: final[float] = maximum_x
            self.maximum_y: final[float] = maximum_y
            self.maximum_z: final[float] = maximum_z

        @staticmethod
        def from_mcnp(cls, source: str):
            """
            ``from_mcnp`` generates ``StochasticGeometryValue`` objects from
            INP.

            ``from_mcnp`` constructs instances of ``StochasticGeometryValue``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function.

            Parameters:
                source: INP for stochastic geometry values.

            Returns:
                ``StochasticGeometryValue`` object.

            Raises:
                MCNPSyntaxError: TOOFEW_DATUM_URAN, TOOLONG_DATUM_URAN.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_URAN))

            number = tokens.popl()
            maximum_x = tokens.popl()
            maximum_y = tokens.popl()
            maximum_z = tokens.popl()

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_URAN)

            return StochasticGeometryValue(number, maximum_x, maximum_y, maximum_z)

    def __init__(self, transformions: tuple[StochasticGeometryValue]):
        """
        ``__init__`` initializes ``StochasticGeometry``.

         Parameters:
            *transformions: Tuple of stochastric geometry transformions.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in transformions:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.STOCHASTIC_GEOMETRY
        self.parameters = transformions

        self.transformions = transformions


class DeterministicMaterials(Datum):
    """
    ``DeterministicMaterials`` represents INP deterministic materials data
    cards.

    ``DeterministicMaterials`` inherits attributes from ``Datum``. It
    represents the INP deterministic materials data card syntax element.

    Attributes:
        materials: Tuple of Zaids.
        suffix: Data card suffix.
    """

    def __init__(self, materials: tuple[types.Zaid], suffix: int):
        """
        ``__init__`` initializes ``DeterministicMaterials``.

        Parameters:
            materials: Tuple of ZAID aliases.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in materials:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.DETERMINISTIC_MATERIALS
        self.parameters = materials
        self.suffix = suffix

        self.materials = materials


class DeterministicWeightWindow(Datum):
    """
    ``DeterministicWeightWindow`` represents INP deterministic weight window
    data cards.

    ``DeterministicWeightWindow`` inherits attributes from ``Datum``. It
    represents the INP deterministic weight window data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
    """

    class DeterministicWeightWindowOption:
        """
        ``DeterministicWeightWindowOption`` represents INP deterministic weight
        window data card options.

        ``DeterministicWeightWindowOption`` implements INP deterministic weight
        window data card options. Its attributes store keywords and values, and
        its methods provide entry and endpoints for working with INP
        deterministic weight window data card options. It represents the
        generic INP deterministic weight window data card option syntax
        element, so ``DeterministicWeightWindow`` depends on
        ``DeterministicWeightWindowOption`` as a generic data structure and
        superclass.

        Attributes:
            keyword: Deterministic weight window data card option keyword.
            value: Deterministic weight window data card option value.
        """

        class DeterministicWeightWindowKeyword(StrEnum):
            """
            ``DeterministicWeightWindowKeyword`` represents INP deterministic
            weight window data card keywords.

            ``DeterministicWeightWindowKeyword`` implements INP deterministic
            weight window data card keywords as a Python inner class. It
            enumerates MCNP keywords and provides methods for casting strings
            to ``DeterministicWeightWindowKeyword`` instances. It represents
            the INP deterministic weight window data card keyword syntax
            element, so ``DeterministicWeightWindow`` and
            ``DeterministicWeightWindowOption`` depend on
            ``DeterministicWeightWindowKeyword`` as an enum.
            """

            POINTS = "points"
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

            @staticmethod
            def from_mcnp(cls, source: str):
                """
                ``from_mcnp`` generates ``DeterministicWeightWindowKeyword``
                objects from INP.

                ``from_mcnp`` constructs instances of
                ``DeterministicWeightWindowKeyword`` from INP source strings,
                so it operates as a class constructor method and INP parser
                helper function.

                Parameters:
                    source: INP for deterministic weight window keyword.

                Returns:
                    ``DeterministicWeightWindowKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
                """

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in DeterministicWeightWindowKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

                return DeterministicWeightWindowKeyword(source)

        def __init__(self, keyword: DeterministicWeightWindowKeyword, value: any):
            """
            ``__init__`` initializes ``DeterministicWeightWindowOption``.

            Parameters:
                keyword: Deterministic weight window data card option keyword.
                value:  Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

            match keyword:
                case DeterministicWeightWindowKeyword.POINTS:
                    obj = DeterministicWeightWindow.Points(keyword, value)
                case DeterministicWeightWindowKeyword.XSEC:
                    obj = DeterministicWeightWindow.Xsec(keyword, value)
                case DeterministicWeightWindowKeyword.TALLY:
                    obj = DeterministicWeightWindow.Tally(keyword, value)
                case DeterministicWeightWindowKeyword.BLOCK:
                    obj = DeterministicWeightWindow.Block(keyword, value)
                case DeterministicWeightWindowKeyword.NGROUP:
                    obj = DeterministicWeightWindow.Ngroup(keyword, value)
                case DeterministicWeightWindowKeyword.ISN:
                    obj = DeterministicWeightWindow.Isn(keyword, value)
                case DeterministicWeightWindowKeyword.NISO:
                    obj = DeterministicWeightWindow.Niso(keyword, value)
                case DeterministicWeightWindowKeyword.MT:
                    obj = DeterministicWeightWindow.Mt(keyword, value)
                case DeterministicWeightWindowKeyword.IQUAD:
                    obj = DeterministicWeightWindow.Iquad(keyword, value)
                case DeterministicWeightWindowKeyword.FMMIX:
                    obj = DeterministicWeightWindow.Fmmix(keyword, value)
                case DeterministicWeightWindowKeyword.NOSOLV:
                    obj = DeterministicWeightWindow.Nosolv(keyword, value)
                case DeterministicWeightWindowKeyword.NOEDIT:
                    obj = DeterministicWeightWindow.Noedit(keyword, value)
                case DeterministicWeightWindowKeyword.NOGEOD:
                    obj = DeterministicWeightWindow.Nogeod(keyword, value)
                case DeterministicWeightWindowKeyword.NOMIX:
                    obj = DeterministicWeightWindow.Nomix(keyword, value)
                case DeterministicWeightWindowKeyword.NOASG:
                    obj = DeterministicWeightWindow.Noasg(keyword, value)
                case DeterministicWeightWindowKeyword.NOMACR:
                    obj = DeterministicWeightWindow.Nomacr(keyword, value)
                case DeterministicWeightWindowKeyword.NOSLNP:
                    obj = DeterministicWeightWindow.Noslnp(keyword, value)
                case DeterministicWeightWindowKeyword.NOEDTT:
                    obj = DeterministicWeightWindow.Noedtt(keyword, value)
                case DeterministicWeightWindowKeyword.NOADJM:
                    obj = DeterministicWeightWindow.Noadjm(keyword, value)
                case DeterministicWeightWindowKeyword.LIB:
                    obj = DeterministicWeightWindow.Lib(keyword, value)
                case DeterministicWeightWindowKeyword.LIBNAME:
                    obj = DeterministicWeightWindow.Libname(keyword, value)
                case DeterministicWeightWindowKeyword.FISSNEUT:
                    obj = DeterministicWeightWindow.Fissneut(keyword, value)
                case DeterministicWeightWindowKeyword.LNG:
                    obj = DeterministicWeightWindow.Lng(keyword, value)
                case DeterministicWeightWindowKeyword.BALXS:
                    obj = DeterministicWeightWindow.Balxs(keyword, value)
                case DeterministicWeightWindowKeyword.NTICHI:
                    obj = DeterministicWeightWindow.Ntichi(keyword, value)
                case DeterministicWeightWindowKeyword.IEVT:
                    obj = DeterministicWeightWindow.Ievt(keyword, value)
                case DeterministicWeightWindowKeyword.SCT:
                    obj = DeterministicWeightWindow.Isct(keyword, value)
                case DeterministicWeightWindowKeyword.ITH:
                    obj = DeterministicWeightWindow.Ith(keyword, value)
                case DeterministicWeightWindowKeyword.TRCOR:
                    obj = DeterministicWeightWindow.Trcor(keyword, value)
                case DeterministicWeightWindowKeyword.IBL:
                    obj = DeterministicWeightWindow.Ibl(keyword, value)
                case DeterministicWeightWindowKeyword.IBR:
                    obj = DeterministicWeightWindow.Ibr(keyword, value)
                case DeterministicWeightWindowKeyword.IBT:
                    obj = DeterministicWeightWindow.Ibt(keyword, value)
                case DeterministicWeightWindowKeyword.IBB:
                    obj = DeterministicWeightWindow.Ibb(keyword, value)
                case DeterministicWeightWindowKeyword.IBFRNT:
                    obj = DeterministicWeightWindow.Ibfrnt(keyword, value)
                case DeterministicWeightWindowKeyword.BIBACK:
                    obj = DeterministicWeightWindow.Ibback(keyword, value)
                case DeterministicWeightWindowKeyword.EPSI:
                    obj = DeterministicWeightWindow.Epsi(keyword, value)
                case DeterministicWeightWindowKeyword.OITM:
                    obj = DeterministicWeightWindow.Oitm(keyword, value)
                case DeterministicWeightWindowKeyword.NOSIGF:
                    obj = DeterministicWeightWindow.Nosigf(keyword, value)
                case DeterministicWeightWindowKeyword.SRCACC:
                    obj = DeterministicWeightWindow.Srcacc(keyword, value)
                case DeterministicWeightWindowKeyword.DIFFSOL:
                    obj = DeterministicWeightWindow.Diffsol(keyword, value)
                case DeterministicWeightWindowKeyword.TSASN:
                    obj = DeterministicWeightWindow.Tsasn(keyword, value)
                case DeterministicWeightWindowKeyword.TSAEPSI:
                    obj = DeterministicWeightWindow.Tsaepsi(keyword, value)
                case DeterministicWeightWindowKeyword.TSAITS:
                    obj = DeterministicWeightWindow.Tsaits(keyword, value)
                case DeterministicWeightWindowKeyword.TSABETA:
                    obj = DeterministicWeightWindow.Tsabeta(keyword, value)
                case DeterministicWeightWindowKeyword.PTCONV:
                    obj = DeterministicWeightWindow.Ptconv(keyword, value)
                case DeterministicWeightWindowKeyword.NORM:
                    obj = DeterministicWeightWindow.Norm(keyword, value)
                case DeterministicWeightWindowKeyword.XESCTP:
                    obj = DeterministicWeightWindow.Xesctp(keyword, value)
                case DeterministicWeightWindowKeyword.FISSRP:
                    obj = DeterministicWeightWindow.Fissrp(keyword, value)
                case DeterministicWeightWindowKeyword.SOURCP:
                    obj = DeterministicWeightWindow.Sourcp(keyword, value)
                case DeterministicWeightWindowKeyword.ANGP:
                    obj = DeterministicWeightWindow.Angp(keyword, value)
                case DeterministicWeightWindowKeyword.BALP:
                    obj = DeterministicWeightWindow.Balp(keyword, value)
                case DeterministicWeightWindowKeyword.RAFLUX:
                    obj = DeterministicWeightWindow.Raflux(keyword, value)
                case DeterministicWeightWindowKeyword.RMFLUX:
                    obj = DeterministicWeightWindow.Rmflux(keyword, value)
                case DeterministicWeightWindowKeyword.AVATAR:
                    obj = DeterministicWeightWindow.Avatar(keyword, value)
                case DeterministicWeightWindowKeyword.ASLEFT:
                    obj = DeterministicWeightWindow.Asleft(keyword, value)
                case DeterministicWeightWindowKeyword.ASRITE:
                    obj = DeterministicWeightWindow.Asrite(keyword, value)
                case DeterministicWeightWindowKeyword.ASBOTT:
                    obj = DeterministicWeightWindow.Asbott(keyword, value)
                case DeterministicWeightWindowKeyword.ASTOP:
                    obj = DeterministicWeightWindow.Astop(keyword, value)
                case DeterministicWeightWindowKeyword.ASFRNT:
                    obj = DeterministicWeightWindow.Asfrnt(keyword, value)
                case DeterministicWeightWindowKeyword.ASBACK:
                    obj = DeterministicWeightWindow.Asback(keyword, value)
                case DeterministicWeightWindowKeyword.MASSED:
                    obj = DeterministicWeightWindow.Massed(keyword, value)
                case DeterministicWeightWindowKeyword.PTED:
                    obj = DeterministicWeightWindow.Pted(keyword, value)
                case DeterministicWeightWindowKeyword.ZNED:
                    obj = DeterministicWeightWindow.Zned(keyword, value)
                case DeterministicWeightWindowKeyword.RZFLUX:
                    obj = DeterministicWeightWindow.Rzflux(keyword, value)
                case DeterministicWeightWindowKeyword.RXMFLUX:
                    obj = DeterministicWeightWindow.Rzmflux(keyword, value)
                case DeterministicWeightWindowKeyword.EDOUTF:
                    obj = DeterministicWeightWindow.Edoutf(keyword, value)
                case DeterministicWeightWindowKeyword.BYVLOP:
                    obj = DeterministicWeightWindow.Byvlop(keyword, value)
                case DeterministicWeightWindowKeyword.AJED:
                    obj = DeterministicWeightWindow.Ajed(keyword, value)
                case DeterministicWeightWindowKeyword.FLUXONE:
                    obj = DeterministicWeightWindow.Fluxone(keyword, value)

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(cls, string: str):
            """
            ``from_mcnp`` generates ``DeterministicWeightWindowOption`` objects
            from INP.

            ``from_mcnp`` constructs instances of
            ``DeterministicWeightWindowOption`` from INP source strings, so it
            operates as a class constructor method and INP parser helper
            function. Although defined on the superclass, it returns
            ``DeterministicWeightWindowOption`` subclasses.

            Parameters:
                source: INP for deterministic weight window data card option.

            Returns:
                ``DeterministicWeightWindowOption`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
                MCNPSyntaxError: TOOFEW_DATUM_DAWWG, TOOLONG_DATUM_DAWWG.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_DAWWG))

            # Processing Keyword
            keyword = DeterministicWeightWindowOption.DeterministicWeightWindowKeyword.cast_keyword(tokens.peekl())

            # Processing Values
            match keyword:
                case DeterministicWeightWindowKeyword.POINTS | DeterministicWeightWindowKeyword.BLOCK | DeterministicWeightWindowKeyword.NGROUP | DeterministicWeightWindowKeyword.ISN | DeterministicWeightWindowKeyword.NISO | DeterministicWeightWindowKeyword.MT | DeterministicWeightWindowKeyword.IQUAD | DeterministicWeightWindowKeyword.FMMIX | DeterministicWeightWindowKeyword.NOSOLV | DeterministicWeightWindowKeyword.NOEDIT | DeterministicWeightWindowKeyword.NOGEOD | DeterministicWeightWindowKeyword.NOMIX | DeterministicWeightWindowKeyword.NOASG | DeterministicWeightWindowKeyword.NOMACR | DeterministicWeightWindowKeyword.NOSLNP | DeterministicWeightWindowKeyword.NOEDTT | DeterministicWeightWindowKeyword.NOADJM | DeterministicWeightWindowKeyword.FISSNEUT | DeterministicWeightWindowKeyword.LNG | DeterministicWeightWindowKeyword.BALXS | DeterministicWeightWindowKeyword.NTICHI | DeterministicWeightWindowKeyword.IEVT | DeterministicWeightWindowKeyword.SCT | DeterministicWeightWindowKeyword.ITH | DeterministicWeightWindowKeyword.TRCOR | DeterministicWeightWindowKeyword.IBL | DeterministicWeightWindowKeyword.IBR | DeterministicWeightWindowKeyword.IBT | DeterministicWeightWindowKeyword.IBB | DeterministicWeightWindowKeyword.IBFRNT | DeterministicWeightWindowKeyword.BIBACK | DeterministicWeightWindowKeyword.OITM | DeterministicWeightWindowKeyword.NOSIGF | DeterministicWeightWindowKeyword.TSASN | DeterministicWeightWindowKeyword.TSAEPSI | DeterministicWeightWindowKeyword.PTCONV | DeterministicWeightWindowKeyword.XESCTP | DeterministicWeightWindowKeyword.FISSRP | DeterministicWeightWindowKeyword.SOURCP | DeterministicWeightWindowKeyword.ANGP | DeterministicWeightWindowKeyword.BALP | DeterministicWeightWindowKeyword.RAFLUX | DeterministicWeightWindowKeyword.RMFLUX | DeterministicWeightWindowKeyword.AVATAR | DeterministicWeightWindowKeyword.ASLEFT | DeterministicWeightWindowKeyword.ASRITE | DeterministicWeightWindowKeyword.ASBOTT | DeterministicWeightWindowKeyword.ASTOP | DeterministicWeightWindowKeyword.ASFRNT | DeterministicWeightWindowKeyword.ASBACK | DeterministicWeightWindowKeyword.MASSED | DeterministicWeightWindowKeyword.PTED | DeterministicWeightWindowKeyword.ZNED | DeterministicWeightWindowKeyword.RZFLUX | DeterministicWeightWindowKeyword.RXMFLUX | DeterministicWeightWindowKeyword.EDOUTF | DeterministicWeightWindowKeyword.BYVLOP | DeterministicWeightWindowKeyword.AJED | DeterministicWeightWindowKeyword.FLUXONE:
                    value = types.cast_fortran_integer(tokens.popl())
                case DeterministicWeightWindowKeyword.LIB | DeterministicWeightWindowKeyword.LIBNAME | DeterministicWeightWindowKeyword.TRCOR | DeterministicWeightWindowKeyword.SRCACC | DeterministicWeightWindowKeyword.DIFFSOL:
                    value = types.cast_fortran_real(tokens.popl())
                case DeterministicWeightWindowKeyword.EPSI | DeterministicWeightWindowKeyword.TSAEPSI | DeterministicWeightWindowKeyword.TSAITS | DeterministicWeightWindowKeyword.TSABETA:
                    value = tokens.popl()
                case _:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_DAWWG)

            return DeterministicWeightWindowOption(keyword, value)

    class Points(DeterministicWeightWindowOption):
        """
        ``Points`` represents INP points deterministic weight window data card
        options.

        ``Points`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP points
        deterministic weight window data card option syntax element.

        Attributes:
            point: Deterministic weight window data card sample point count.
        """

        def __init__(self, point: int):
            """
            ``__init__`` initializes ``Points``.

            Parameters:
                point: Deterministic weight window data card sample point count.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.POINTS
            self.value = value

            self.point = value

    class Block(DeterministicWeightWindowOption):
        """
        ``Block`` represents INP block deterministic weight window data card
        options.

        ``Block`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP block deterministic weight window data card
        option syntax element.

        Attributes:
            state: PARTISN input file passed value setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Block``.

            Parameters:
                state: PARTISN input file passed value setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {1, 3, 5, 6}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BLOCK
            self.value = value

            self.state = value

    class Ngroup(DeterministicWeightWindowOption):
        """
        ``Ngroup`` represents INP ngroup deterministic weight window data card
        options.

        ``Ngroup`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ngroup
        deterministic weight window data card option syntax element.

        Attributes:
            energy_group_number: DAWWG energy group count.
        """

        def __init__(self, energy_group_number: int):
            """
            ``__init__`` initializes ``Ngroup``.

            Parameters:
                energy_group_number: DAWWG energy group count.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NGROUP
            self.value = value

            self.energy_group_number = value

    class Isn(DeterministicWeightWindowOption):
        """
        ``Isn`` represents INP isn deterministic weight window data card
        options.

        ``Isn`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP isn deterministic weight window data option
        syntax element.

        Attributes:
            sn_order: DAWWG Sn order.
        """

        def __init__(self, sn_order: int):
            """
            ``__init__`` initializes ``Isn``.

            Parameters:
                sn_order: DAWWG Sn order.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ISN
            self.value = value

            self.sn_order = value

    class Niso(DeterministicWeightWindowOption):
        """
        ``Niso`` represents INP niso deterministic weight window data card
        options.

        ``Niso`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP niso deterministic weight window data card option
        syntax element.

        Attributes:
            isotopes_number: DAWWG isotopes number.
        """

        def __init__(self, isotopes_number: int):
            """
            ``__init__`` initializes ``Niso``.

            Parameters:
                isotopes_number: DAWWG isotopes number.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NISO
            self.value = value

            self.isotopes_number = value

    class Mt(DeterministicWeightWindowOption):
        """
        ``Mt`` represents INP mt deterministic weight window data card options.

        ``Mt`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP mt deterministic weight window data card option
        syntax element.

        Attributes:
            materials_number: DAWWG materials number.
        """

        def __init__(self, materials_number: int):
            """
            ``__init__`` initializes ``Mt``.

            Parameters:
                materials_number: DAWWG materials number.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.MT
            self.value = value

            self.materials_number = value

    class Iquad(DeterministicWeightWindowOption):
        """
        ``Iquad`` represents INP iquad deterministic weight window data card
        options.

        ``Iquad`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP iquad deterministic weight window data card
        option syntax element.

        Attributes:
            quadrature: DAWWG quadrature.
        """

        def __init__(self, quadrature: int):
            """
            ``__init__`` initializes ``Iquad``.

            Parameters:
                quadrature: DAWWG quadrature.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {1, 3, 4, 5, 6, 7, 8, 9}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IQUAD
            self.value = value

            self.quadrature = value

    class Fmmix(DeterministicWeightWindowOption):
        """
        ``Fmmix`` represents INP fmmix deterministic weight window data card
        options.

        ``Fmmix`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP fmmix deterministic weight window data card
        option sytnax element.

        Attributes:
            state: DAWWG LNK3DNT reading comprehension toggle.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Fmmix``.

            Parameters:
                state: DAWWG LNK3DNT reading comprehension toggle.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.FMMIX
            self.value = value

            self.state = value

    class Nosolv(DeterministicWeightWindowOption):
        """
        ``Nosolv`` represents INP nosolv deterministic weight window data card
        options.

        ``Nosolv`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP nosolv
        deterministic weight window data card option syntax element

        Attributes:
            state: Suppress solver module setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nosolv``.

            Parameters:
                state: Suppress solver module setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOSOLV
            self.value = value

            self.state = value

    class Noedit(DeterministicWeightWindowOption):
        """
        ``Noedit`` represents INP noedit deterministic weight window data card
        options.

        ``Noedit`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP noedit
        deterministic weight window data card option syntax element.

        Attributes:
            state: Suppress edit module setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noedit``.

            Parameters:
                state: Suppress edit module setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOEDIT
            self.value = value

            self.state = value

    class Nogeod(DeterministicWeightWindowOption):
        """
        ``Nogeod`` represents INP nogeod deterministic weight window data card
        options.

        ``Nogeod`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP nogeod
        deterministic weight window data card option syntax element.

        Attributes:
            state: Supress writing GEODST file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nogeod``.

            Parameters:
                state: Supress writing GEODST file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOGEOD
            self.value = value

            self.state = value

    class Nomix(DeterministicWeightWindowOption):
        """
        ``Nomix`` represents INP nomix deterministic weight window data card
        options.

        ``Nomix`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP nomix deterministic weight window data card
        option syntax element.

        Attributes:
            state: Suppress writing mixing file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nomix``.

            Parameters:
                state: Suppress writing mixing file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOMIX
            self.value = value

            self.state = value

    class Noasg(DeterministicWeightWindowOption):
        """
        ``Noasg`` represents INP noasg deterministic weight window data card
        options.

        ``Noasg`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP noasg deterministic weight window data card
        option syntax element.

        Attributes:
            state: Suppress wirting ASGMAT file seting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noasg``.

            Parameters:
                state: Suppress wirting ASGMAT file seting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOASG
            self.value = value

            self.state = value

    class Nomacr(DeterministicWeightWindowOption):
        """
        ``Nomacr`` represents INP nomacr deterministic weight window data card
        options.

        ``Nomacr`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP nomacr
        deterministic weight window data card option syntax element.

        Attributes:
            state: Suppress writing MACRXS file.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nomacr``.

            Parameters:
                state: Suppress writing MACRXS file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOMACR
            self.value = value

            self.state = value

    class Noslnp(DeterministicWeightWindowOption):
        """
        ``Noslnp`` represents INP noslnp deterministic weight window data card
        options.

        ``Noslnp`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP noslnp
        deterministic weight window data card option syntax element.

        Attributes:
            state: Suppress writing SOLINP file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noslnp``.

            Parameters:
                state: Suppress writing SOLINP file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOSLNP
            self.value = value

            self.state = value

    class Noedtt(DeterministicWeightWindowOption):
        """
        ``Noedtt`` represents INP noedtt deterministic weight window data card
        options.

        ``Noedtt`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP noedtt
        deterministic weight window data card option syntax element.

        Attributes:
            state: Supress writing EDITIT file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noedtt``.

            Parameters:
                state: Supress writing EDITIT file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOEDTT
            self.value = value

            self.state = value

    class Noadjm(DeterministicWeightWindowOption):
        """
        ``Noadjm`` represents INP noadjm deterministic weight window data card
        options.

        ``Noadjm`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP noadjm
        deterministic weight window data card option syntax element.

        Attributes:
            state: Suppress writing ADJMAC file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noadjm``.

            Parameters:
                state: Suppress writing ADJMAC file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOADJM
            self.value = value

            self.state = value

    class Lib(DeterministicWeightWindowOption):
        """
        ``Lib`` represents lib deterministic weight window datacell coptions.

        ``Lib`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Libents deterministic weight window data cell option
        syntax element.

        Attributes:
            name: Name/Form of corss-seciotn data file.
        """

        def __init__(self, name: str):
            """
            ``__init__`` initializes ``Lib``.

            Parameters:
                name: Name/Form of corss-seciotn data file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.LIB
            self.value = value

            self.name = value

    class Libname(DeterministicWeightWindowOption):
        """
        ``Libname`` represents INP libname deterministic weight window data
        card options.

        ``Libname`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP libname
        deterministic weight window data card option syntax element.

        Attributes:
            filename: Cross-section file name.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Libname``.

            Parameters:
                filename: Cross-section file name.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.LIBNAME
            self.value = value

            self.filename = value

    class Fissneut(DeterministicWeightWindowOption):
        """
        ``Fissneut`` represents INP fissneut deterministic weight window data
        card options.

        ``Fissneut`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP fissneut
        deterministic weight window data card option syntax element.

        Attributes:
            fission_neutron_flag: Fission neutron flag.
        """

        def __init__(self, fission_neutron_flag: int):
            """
            ``__init__`` initializes ``Fissneut``.

            Parameters:
                fission_neutron_flag: Fission neutron flag.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.FISSNEUT
            self.value = value

            self.fission_neutron_flag = value

    class Lng(DeterministicWeightWindowOption):
        """
        ``Lng`` represents lng deterministic weight window datacell coptions.

        ``Lng`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Lngents deterministic weight window datacell coption
        syntax element.

        Attributes:
            last_neutron_group_number: Number of the last neutron group.
        """

        def __init__(self, last_neutron_group_number: int):
            """
            ``__init__`` initializes ``Lng``.

            Parameters:
                last_neutron_group_number: Number of the last neutron group.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.LNG
            self.value = value

            self.last_neutron_group_number = value

    class Balxs(DeterministicWeightWindowOption):
        """
        ``Balxs`` represents INP balxs deterministic weight window data card
        options.

        ``Balxs`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP balxs deterministic weight window data card
        option syntax element.

        Attributes:
            cross_section_balance_control: Cross-section balance control.
        """

        def __init__(self, cross_section_balance_control: int):
            """
            ``__init__`` initializes ``Balxs``.

            Parameters:
                cross_section_balance_control: Cross-section balance control.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BALXS
            self.value = value

            self.cross_section_balance_control = value

    class Ntichi(DeterministicWeightWindowOption):
        """
        ``Ntichi`` represents INP ntichi deterministic weight window data card
        options.

        ``Ntichi`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ntichi
        deterministic weight window data card option syntax element.

        Attributes:
            mendf_fission_fraction: MENDF fission fraction to use.
        """

        def __init__(self, mendf_fission_fraction: int):
            """
            ``__init__`` initializes ``Ntichi``.

            Parameters:
                mendf_fission_fraction: MENDF fission fraction to use.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NTICHI
            self.value = value

            self.mendf_fission_fraction = value

    class Ievt(DeterministicWeightWindowOption):
        """
        ``Ievt`` represents INP ievt deterministic weight window data card
        options.

        ``Ievt`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP ievt deterministic weight window data card option
        syntax element.

        Attributes:
            calculation_type: Calculation type.
        """

        def __init__(self, calculation_type: int):
            """
            ``__init__`` initializes ``Ievt``.

            Parameters:
                calculation_type: Calculation type.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2, 3, 4}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IEVT
            self.value = value

            self.calculation_type = value

    class Isct(DeterministicWeightWindowOption):
        """
        ``Isct`` represents INP isct deterministic weight window data card
        options.

        ``Isct`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP isct deterministic weight window data card option
        syntax element.

        Attributes:
            legendre_order: Legendre order.
        """

        def __init__(self, legendre_order: int):
            """
            ``__init__`` initializes ``Isct``.

            Parameters:
                legendre_order: Legendre order.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.SCT
            self.value = value

            self.legendre_order = value

    class Ith(DeterministicWeightWindowOption):
        """
        ``Ith`` represents ith deterministic weight window datacell coptions.

        ``Ith`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Ithents deterministic weight window datacell coption
        syntax element.

        Attributes:
            calculation_state: Direct or adjoint calculation.
        """

        def __init__(self, calculation_state: int):
            """
            ``__init__`` initializes ``Ith``.

            Parameters:
                calculation_state: Direct or adjoint calculation.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ITH
            self.value = value

            self.calculation_state = value

    class Trcor(DeterministicWeightWindowOption):
        """
        ``Trcor`` represents INP trcor deterministic weight window data card
        options.

        ``Trcor`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP trcor deterministic weight window data card
        option syntax element.

        Attributes:
            trcor: trcor.
        """

        def __init__(self, trcor: str):
            """
            ``__init__`` initializes ``Trcor``.

            Parameters:
                trcor: trcor.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TRCOR
            self.value = value

            self.trcor = value

    class Ibl(DeterministicWeightWindowOption):
        """
        ``Ibl`` represents ibl deterministic weight window datacell coptions.

        ``Ibl`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Iblents deterministic weight window datacell coption
        syntax element.

        Attributes:
            left_boundary: Left boundary condition.
        """

        def __init__(self, left_boundary: int):
            """
            ``__init__`` initializes ``Ibl``.

            Parameters:
                left_boundary: Left boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBL
            self.value = value

            self.left_boundary = value

    class Ibr(DeterministicWeightWindowOption):
        """
        ``Ibr`` represents ibr deterministic weight window datacell coptions.

        ``Ibr`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Ibrents deterministic weight window datacell coption
        syntax element.

        Attributes:
            right_boundary: Right boundary condition.
        """

        def __init__(self, right_boundary: int):
            """
            ``__init__`` initializes ``Ibr``.

            Parameters:
                right_boundary: Right boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBR
            self.value = value

            self.right_boundary = value

    class Ibt(DeterministicWeightWindowOption):
        """
        ``Ibt`` represents ibt deterministic weight window datacell coptions.

        ``Ibt`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Ibtents deterministic weight window datacell coption
        syntax element.

        Attributes:
            top_boundary: Top boundary condition.
        """

        def __init__(self, top_boundary: int):
            """
            ``__init__`` initializes ``Ibt``.

            Parameters:
                top_boundary: Top boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBT
            self.value = value

            self.top_boundary = value

    class Ibb(DeterministicWeightWindowOption):
        """
        ``Ibb`` represents ibb deterministic weight window datacell coptions.

        ``Ibb`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Ibbents deterministic weight window datacell coption
        syntax element.

        Attributes:
            bottom_boundary: Bottom boundary condition.
        """

        def __init__(self, bottom_boundary: int):
            """
            ``__init__`` initializes ``Ibb``.

            Parameters:
                bottom_boundary: Bottom boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBB
            self.value = value

            self.bottom_boundary = value

    class Ibfrnt(DeterministicWeightWindowOption):
        """
        ``Ibfrnt`` represents INP ibfrnt deterministic weight window data card
        options.

        ``Ibfrnt`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ibfrnt
        deterministic weight window data card option syntax element.

        Attributes:
            front_boundary: Front boundary condition.
        """

        def __init__(self, front_boundary: int):
            """
            ``__init__`` initializes ``Ibfrnt``.

            Parameters:
                front_boundary: Front boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBFRNT
            self.value = value

            self.front_boundary = value

    class Ibback(DeterministicWeightWindowOption):
        """
        ``Ibback`` represents INP ibback deterministic weight window data card
        options.

        ``Ibback`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ibback
        deterministic weight window data card option syntax element.

        Attributes:
            back_boundary: Back boundary condition.
        """

        def __init__(self, back_boundary: int):
            """
            ``__init__`` initializes ``Ibback``.

            Parameters:
                back_boundary: Back boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BIBACK
            self.value = value

            self.back_boundary = value

    class Epsi(DeterministicWeightWindowOption):
        """
        ``Epsi`` represents INP epsi deterministic weight window data card
        options.

        ``Epsi`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP epsi deterministic weight window data card option
        syntax element.

        Attributes:
            Convergence percision: Convergence percision.
        """

        def __init__(self, convergence_percision: float):
            """
            ``__init__`` initializes ``Epsi``.

            Parameters:
                Convergence percision: Convergence percision.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.EPSI
            self.value = value

            self.convergence_percision = value

    class Oitm(DeterministicWeightWindowOption):
        """
        ``Oitm`` represents INP oitm deterministic weight window data card
        options.

        ``Oitm`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP oitm deterministic weight window data card option
        syntax element.

        Attributes:
            maximnum_outer_iteration: Maximum outer iteration count.
        """

        def __init__(self, maximum_outer_iteration: int):
            """
            ``__init__`` initializes ``Oitm``.

            Parameters:
                maximnum_outer_iteration: Maximum outer iteration count.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.OITM
            self.value = value

            self.maximum_outer_iteration = value

    class Nosigf(DeterministicWeightWindowOption):
        """
        ``Nosigf`` represents INP nosigf deterministic weight window data card
        options.

        ``Nosigf`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP nosigf
        deterministic weight window data card option syntax element.

        Attributes:
            state: Inhibit fission multiplication setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nosigf``.

            Parameters:
                state: Inhibit fission multiplication setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOSIGF
            self.value = value

            self.state = value

    class Srcacc(DeterministicWeightWindowOption):
        """
        ``Srcacc`` represents INP srcacc deterministic weight window data card
        options.

        ``Srcacc`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP srcacc
        deterministic weight window data card option syntax element.

        Attributes:
            transport_accelerations: Transport accelerations.
        """

        def __init__(self, transport_accelerations: str):
            """
            ``__init__`` initializes ``Srcacc``.

            Parameters:
                transport_accelerations: Transport accelerations.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.SRCACC
            self.value = value

            self.transport_accelerations = value

    class Diffsol(DeterministicWeightWindowOption):
        """
        ``Diffsol`` represents INP diffsol deterministic weight window data
        card options.

        ``Diffsol`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP diffsol
        deterministic weight window data card option syntax element.

        Attributes:
            diffusion_operator_solver: Diffusion operator solver.
        """

        def __init__(self, diffusion_operator_solver: str):
            """
            ``__init__`` initializes ``Diffsol``.

            Parameters:
                diffusion_operator_solver: Diffusion operator solver.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.DIFFSOL
            self.value = value

            self.diffusion_operator_solver = value

    class Tsasn(DeterministicWeightWindowOption):
        """
        ``Tsasn`` represents INP tsasn deterministic weight window data card
        options.

        ``Tsasn`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP tsasn deterministic weight window data card
        option syntax element.

        Attributes:
            sn_order: Sn order for low order TSA sweeps.
        """

        def __init__(self, sn_order: int):
            """
            ``__init__`` initializes ``Tsasn``.

            Parameters:
                sn_order: Sn order for low order TSA sweeps.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TSASN
            self.value = value

            self.sn_order = value

    class Tsaepsi(DeterministicWeightWindowOption):
        """
        ``Tsaepsi`` represents INP tsaepsi deterministic weight window data
        card options.

        ``Tsaepsi`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP tsaepsi
        deterministic weight window data card option syntax element.

        Attributes:
            convergence_criteria: Convergence criteria for TSA sweeps.
        """

        def __init__(self, convergence_criteria: float):
            """
            ``__init__`` initializes ``Tsaepsi``.

            Parameters:
                convergence_criteria: Convergence criteria for TSA sweeps.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TSAEPSI
            self.value = value

            self.convergence_criteria = value

    class Tsaits(DeterministicWeightWindowOption):
        """
        ``Tsaits`` represents INP tsaits deterministic weight window data card
        options.

        ``Tsaits`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP tsaits
        deterministic weight window data card option syntax element.

        Attributes:
            maximum_tsa_iteration: Maximmum TSA iteration count.
        """

        def __init__(self, maximum_tsa_iteration: int):
            """
            ``__init__`` initializes ``Tsaits``.

            Parameters:
                maximum_tsa_iteration: Maximmum TSA iteration count.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TSAITS
            self.value = value

            self.maximum_tsa_iteration = value

    class Tsabeta(DeterministicWeightWindowOption):
        """
        ``Tsabeta`` represents INP tsabeta deterministic weight window data
        card options.

        ``Tsabeta`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP tsabeta
        deterministic weight window data card option syntax element.

        Attributes:
            tsa_scattering_corss_section: Scatting cross-section reduction.
        """

        def __init__(self, tsa_scattering_cross_section: float):
            """
            ``__init__`` initializes ``Tsabeta``.

            Parameters:
                tsa_scattering_corss_section: Scatting cross-section reduction.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TSABETA
            self.value = value

            self.tsa_scattering_cross_section = value

    class Ptconv(DeterministicWeightWindowOption):
        """
        ``Ptconv`` represents INP ptconv deterministic weight window data card
        options.

        ``Ptconv`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ptconv
        deterministic weight window data card option syntax element.

        Attributes:
            state: Special criticality convergence scheme.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Ptconv``.

            Parameters:
                state: Special criticality convergence scheme.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.PTCONV
            self.value = value

            self.state = value

    class Norm(DeterministicWeightWindowOption):
        """
        ``Norm`` represents INP norm deterministic weight window data card
        options.

        ``Norm`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP norm deterministic weight window data card option
        syntax element.

        Attributes:
            norm: Norm.
        """

        def __init__(self, norm: float):
            """
            ``__init__`` initializes ``Norm``.

            Parameters:
                norm: Norm.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NORM
            self.value = value

            self.norm = value

    class Xesctp(DeterministicWeightWindowOption):
        """
        ``Xesctp`` represents INP xesctp deterministic weight window data card
        options.

        ``Xesctp`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP xesctp
        deterministic weight window data card option syntax element.

        Attributes:
            cross_section_print_flag: Corss-section print flag.
        """

        def __init__(self, cross_section_print_flag: int):
            """
            ``__init__`` initializes ``Xesctp``.

            Parameters:
                cross_section_print_flag: Corss-section print flag.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.XESCTP
            self.value = value

            self.cross_section_print_flag = value

    class Fissrp(DeterministicWeightWindowOption):
        """
        ``Fissrp`` represents INP fissrp deterministic weight window data card
        options.

        ``Fissrp`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP fissrp
        deterministic weight window data card option syntax element.

        Attributes:
            state: Print fission source rate.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Fissrp``.

            Parameters:
                state: Print fission source rate.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.FISSRP
            self.value = value

            self.state = value

    class Sourcp(DeterministicWeightWindowOption):
        """
        ``Sourcp`` represents INP sourcp deterministic weight window data card
        options.

        ``Sourcp`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP sourcp
        deterministic weight window data card option syntax element.

        Attributes:
           source_print_flag: Source print flag.
        """

        def __init__(self, source_print_flag: int):
            """
            ``__init__`` initializes ``Sourcp``.

            Parameters:
                ource_print_flag: Source print flag.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2, 3}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.SOURCP
            self.value = value

            self.source_print_flag = value

    class Angp(DeterministicWeightWindowOption):
        """
        ``Angp`` represents INP angp deterministic weight window data card
        options.

        ``Angp`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP angp deterministic weight window data card option
        syntax element.

        Attributes:
            state: Print angular flux setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Angp``.

            Parameters:
                state: Print angular flux setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ANGP
            self.value = value

            self.state = value

    class Balp(DeterministicWeightWindowOption):
        """
        ``Balp`` represents INP balp deterministic weight window data card
        options.

        ``Balp`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP balp deterministic weight window data card option
        syntax element.

        Attributes:
            state: Print coarse-mesh balance tables setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Balp``.

            Parameters:
                state: Print coarse-mesh balance tables setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BALP
            self.value = value

            self.state = value

    class Raflux(DeterministicWeightWindowOption):
        """
        ``Raflux`` represents INP raflux deterministic weight window data card
        options.

        ``Raflux`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP raflux
        deterministic weight window data card option syntax element.

        Attributes:
            state: Prepare angular flux file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Raflux``.

            Parameters:
                state: Prepare angular flux file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.RAFLUX
            self.value = value

            self.state = value

    class Rmflux(DeterministicWeightWindowOption):
        """
        ``Rmflux`` represents INP rmflux deterministic weight window data card
        options.

        ``Rmflux`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP rmflux
        deterministic weight window data card option syntax element.

        Attributes:
            state: Prepare flux moments file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Rmflux``.

            Parameters:
                state: Prepare flux moments file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.RMFLUX
            self.value = value

            self.state = value

    class Avatar(DeterministicWeightWindowOption):
        """
        ``Avatar`` represents INP avatar deterministic weight window data card
        options.

        ``Avatar`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP avatar
        deterministic weight window data card option syntax element.

        Attributes:
            state: Prepare special XMFLUXA file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Avatar``.

            Parameters:
                state: Prepare special XMFLUXA file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.AVATAR
            self.value = value

            self.state = value

    class Asleft(DeterministicWeightWindowOption):
        """
        ``Asleft`` represents INP asleft deterministic weight window data card
        options.

        ``Asleft`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asleft
        deterministic weight window data card option syntax element.

        Attributes:
            right_going_flux: Right-going flux at plane i.
        """

        def __init__(self, right_going_flux: int):
            """
            ``__init__`` initializes ``Asleft``.

            Parameters:
                right_going_flux: Right-going flux at plane i.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASLEFT
            self.value = value

            self.right_going_flux = value

    class Asrite(DeterministicWeightWindowOption):
        """
        ``Asrite`` represents INP asrite deterministic weight window data card
        options.

        ``Asrite`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asrite
        deterministic weight window data card option syntax element.

        Attributes:
            left_going_flux: Left-going flux at plane i.
        """

        def __init__(self, left_going_flux: int):
            """
            ``__init__`` initializes ``Asrite``.

            Parameters:
                left_going_flux: Left-going flux at plane i.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASRITE
            self.value = value

            self.left_going_flux = value

    class Asbott(DeterministicWeightWindowOption):
        """
        ``Asbott`` represents INP asbott deterministic weight window data card
        options.

        ``Asbott`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asbott
        deterministic weight window data card option syntax element.

        Attributes:
            top_going_flux: Top-going flux at plane j.
        """

        def __init__(self, top_going_flux: int):
            """
            ``__init__`` initializes ``Asbott``.

            Parameters:
                top_going_flux: Top-going flux at plane j.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASBOTT
            self.value = value

            self.top_going_flux = value

    class Astop(DeterministicWeightWindowOption):
        """
        ``Astop`` represents INP astop deterministic weight window data card
        options.

        ``Astop`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP astop deterministic weight window data card
        option syntax element.

        Attributes:
            bottom_going_flux: Bottom-going flux at plane j.
        """

        def __init__(self, bottom_going_flux: int):
            """
            ``__init__`` initializes ``Astop``.

            Parameters:
                bottom_going_flux: Bottom-going flux at plane j.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASTOP
            self.value = value

            self.bottom_going_flux = value

    class Asfrnt(DeterministicWeightWindowOption):
        """
        ``Asfrnt`` represents INP asfrnt deterministic weight window data card
        options.

        ``Asfrnt`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asfrnt
        deterministic weight window data card option syntax element.

        Attributes:
            back_going_flux: Back-going flux at plane k.
        """

        def __init__(self, back_going_flux: int):
            """
            ``__init__`` initializes ``Asfrnt``.

            Parameters:
                back_going_flux: Back-going flux at plane k.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASFRNT
            self.value = value

            self.back_going_flux = value

    class Asback(DeterministicWeightWindowOption):
        """
        ``Asback`` represents INP asback deterministic weight window data card
        options.

        ``Asback`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asback
        deterministic weight window data card option syntax element.

        Attributes:
            front_going_flux: Front-going flux at plane k.
        """

        def __init__(self, front_going_flux: int):
            """
            ``__init__`` initializes ``Asback``.

            Parameters:
                front_going_flux: Front-going flux at plane k.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASBACK
            self.value = value

            self.front_going_flux = value

    class Massed(DeterministicWeightWindowOption):
        """
        ``Massed`` represents INP massed deterministic weight window data card
        options.

        ``Massed`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP massed
        deterministic weight window data card option syntax element.

        Attributes:
            state: Mass edits setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Massed``.

            Parameters:
                state: Mass edits setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.MASSED
            self.value = value

            self.state = value

    class Pted(DeterministicWeightWindowOption):
        """
        ``Pted`` represents INP pted deterministic weight window data card
        options.

        ``Pted`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP pted deterministic weight window data card option
        syntax element.

        Attributes:
            state: Edits by fine mesh setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Pted``.

            Parameters:
                state: Edits by fine mesh setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.PTED
            self.value = value

            self.state = value

    class Zned(DeterministicWeightWindowOption):
        """
        ``Zned`` represents INP zned deterministic weight window data card
        options.

        ``Zned`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP zned deterministic weight window data card option
        syntax element.

        Attributes:
            state: Edits by zone setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Zned``.

            Parameters:
                state: Edits by zone setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ZNED
            self.value = value

            self.state = value

    class Rzflux(DeterministicWeightWindowOption):
        """
        ``Rzflux`` represents INP rzflux deterministic weight window data card
        options.

        ``Rzflux`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP rzflux
        deterministic weight window data card option syntax element.

        Attributes:
            state: Write a-flux file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Rzflux``.

            Parameters:
                state: Write a-flux file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.RZFLUX
            self.value = value

            self.state = value

    class Rzmflux(DeterministicWeightWindowOption):
        """
        ``Rzmflux`` represents INP rzmflux deterministic weight window data
        card options.

        ``Rzmflux`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP rzmflux
        deterministic weight window data card option syntax element.

        Attributes:
            state: Write b-flux file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Rzmflux``.

            Parameters:
                state: Write b-flux file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.RXMFLUX
            self.value = value

            self.state = value

    class Edoutf(DeterministicWeightWindowOption):
        """
        ``Edoutf`` represents INP edoutf deterministic weight window data card
        options.

        ``Edoutf`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP edoutf
        deterministic weight window data card option syntax element.

        Attributes:
            ascii_output_control: ASCII output file control.
        """

        def __init__(self, ascii_output_control: int):
            """
            ``__init__`` initializes ``Edoutf``.

            Parameters:
                ascii_output_control: ASCII output file control.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or not (-3 <= value <= 3):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.EDOUTF
            self.value = value

            self.ascii_output_control = value

    class Byvlop(DeterministicWeightWindowOption):
        """
        ``Byvlop`` represents INP byvlop deterministic weight window data card
        options.

        ``Byvlop`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP byvlop
        deterministic weight window data card option syntax element.

        Attributes:
            state: Printed point reaction rates scaled by mesh volume setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Byvlop``.

            Parameters:
                state: Printed point reaction rates scaled by mesh volume setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BYVLOP
            self.value = value

            self.state = value

    class Ajed(DeterministicWeightWindowOption):
        """
        ``Ajed`` represents INP ajed deterministic weight window data card
        options.

        ``Ajed`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP ajed deterministic weight window data card option
        syntax element.

        Attributes:
            state: Regular and adjoint edit setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Ajed``.

            Parameters:
                state: Regular and adjoint edit setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.AJED
            self.value = value

            self.state = value

    class Fluxone(DeterministicWeightWindowOption):
        """
        ``Fluxone`` represents INP fluxone deterministic weight window data
        card options.

        ``Fluxone`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP fluxone
        deterministic weight window data card option syntax element.

        Attributes:
            state: Flux override setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Fluxone``.

            Parameters:
                state: Flux override setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.FLUXONE
            self.value = value

            self.state = value

    def __init__(self, pairs: tuple[DeterministicWeightWindowOption]):
        """
        ``__init__`` initializes ``DeterministicWeightWindow``.

        Parameters:
            pairs: Tuple of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW
        self.parameters = pairs

        self.pairs = pairs


class EmbeddedGeometry(Datum):
    """
    ``EmbeddedGeometry`` represents INP deterministic embedded geometry data
    cards.

    ``EmbeddedGeometry`` inherits attributes from ``Datum``. It represents the
    INP embedded geometry data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
        suffix: Data card suffix.
    """

    class EmbeddedGeometryOption:
        """
        ``EmbeddedGeometryOption`` represents INP embedded geometry specification
        data card options.

        ``EmbeddedGeometryOption`` implements INP embedded geometry specification
        data card options. Its attributes store keywords and values, and its
        methods provide entry and endpoints for working with INP embedded
        geometry specification data card options. It represents the generic INP
        embedded geometry specification data card option syntax element, so
        ``EmbeddedGeometry`` depends on ``EmbeddedGeometryOption`` as a genric
        data structre and superclass.

        Attributes:
            keyword: INP embedded geometry specification option keyword.
            value: INP embedded geometry specification option value.
        """

        class EmbeddedGeometryKeyword(StrEnum):
            """
            ``EmbeddedGeometryKeyword`` represents INP embedded geometry
            specification data card option keywords.

            ``EmbeddedGeometryKeyword`` implements INP embedded geometry
            specification data card option keywords as a Python inner class. It
            enumerates MCNP keywords and provides methods for casting strings
            to ``EmbeddedGeometryKeyword`` instances. It represents the INP
            embedded geometry specification data card option keyword syntax
            element, so ``EmbeddedGeometry`` and ``EmbeddedGeometryOption``
            depend on ``EmbeddedGeometryKeyword`` as an enum.
            """

            MATCELL = "matcell"
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
            OVERLAP = "overlap"

            @staticmethod
            def from_mcnp(cls, source: str):
                """
                ``from_mcnp`` generates ``EmbeddedGeometryKeyword``
                objects from INP.

                ``from_mcnp`` constructs instances of
                ``EmbeddedGeometryKeyword`` from INP source strings,
                so it operates as a class constructor method and INP parser
                helper function.

                Parameters:
                    source: INP for embedded geometry option keyword.

                Returns:
                    ``EmbeddedGeometryKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
                """

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in EmbeddedGeometryKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

                return EmbeddedGeometryKeyword(source)

        def __init__(self, keyword: EmbeddedGeometryKeyword, value: any):
            """
            ``__init__`` initializes ``EmbeddedGeometryOption``.

            Parameters:
                keyword: Embedded geometry data card option keyword.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

            match keyword:
                case EmbeddedGeometryKeyword.MATCELL:
                    obj = EmbeddedGeometryOption.Matcell(keyword, value)
                case EmbeddedGeometryKeyword.MESHOGEO:
                    obj = EmbeddedGeometryOption.Meshgeo(keyword, value)
                case EmbeddedGeometryKeyword.MGEOIN:
                    obj = EmbeddedGeometryOption.Mgeoin(keyword, value)
                case EmbeddedGeometryKeyword.MEEOUT:
                    obj = EmbeddedGeometryOption.Meeout(keyword, value)
                case EmbeddedGeometryKeyword.MEEIN:
                    obj = EmbeddedGeometryOption.Meein(keyword, value)
                case EmbeddedGeometryKeyword.CALC_VOLS:
                    obj = EmbeddedGeometryOption.CalcVols(keyword, value)
                case EmbeddedGeometryKeyword.DEBUG:
                    obj = EmbeddedGeometryOption.Debug(keyword, value)
                case EmbeddedGeometryKeyword.FILETYPE:
                    obj = EmbeddedGeometryOption.Filetype(keyword, value)
                case EmbeddedGeometryKeyword.GMVFILE:
                    obj = EmbeddedGeometryOption.Gmvfile(keyword, value)
                case EmbeddedGeometryKeyword.LENGTH:
                    obj = EmbeddedGeometryOption.Length(keyword, value)
                case EmbeddedGeometryKeyword.MCNPUMFILE:
                    obj = EmbeddedGeometryOption.Mcnpumfile(keyword, value)
                case EmbeddedGeometryKeyword.OVERLAP:
                    obj = EmbeddedGeometryOption.Overlap(keyword, value)

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(cls, string: str):
            """
            ``from_mcnp`` generates ``EmbeddedGeometryOption`` objects from INP.

            ``from_mcnp`` constructs instances of ``EmbeddedGeometryOption``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function. Although defined on the
            superclass, it returns ``EmbeddedGeometryOption`` subclasses.

            Parameters:
                source: INP for embedded geometry specification option.

            Returns:
                ``EmbeddedGeometryOption`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
                MCNPSyntaxError: TOOFEW_DATUM_EMBED, TOOLONG_DATUM_EMBED.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_EMBED))

            keyword = EmbeddedGeometryOption.EmbeddedGeometryKeyword.from_mcnp(tokens.popl())

            match keyword:
                case EmbeddedGeometryKeyword.MATCELL:
                    assert False, "Unimplemented"
                case EmbeddedGeometryKeyword.MESHOGEO | EmbeddedGeometryKeyword.MGEOIN | EmbeddedGeometryKeyword.MEEOUT | EmbeddedGeometryKeyword.MEEIN | EmbeddedGeometryKeyword.CALC_VOLS | EmbeddedGeometryKeyword.DEBUG | EmbeddedGeometryKeyword.FILETYPE | EmbeddedGeometryKeyword.GMVFILE | EmbeddedGeometryKeyword.MCNPUMFILE:
                    value = tokens.popl()
                case EmbeddedGeometryKeyword.LENGTH:
                    value = types.cast_fortran_real(tokens.popl())
                case EmbeddedGeometryKeyword.OVERLAP:
                    assert False, "Unimplemented"
                case _:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_EMBED)

    class Meshgeo(EmbeddedGeometryOption):
        """
        ``Meshgeo`` represents INP meshgeo embedded geometry specification
        options.

        ``Meshgeo`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP meshgeo embedded geometry data card option sytnax
        element.

        Attributes:
            form: Format specification of the embedded mesh input file.
        """

        def __init__(self, form: str):
            """
            ``__init__`` initializes ``Meshgeo``.

            Parameters:
                form: Format specification of the embedded mesh input file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if form is None or form not in {"lnk3dnt", "abaqus", "mcnpum"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MESHOGEO
            self.value = value

            self.form = value

    class Mgeoin(EmbeddedGeometryOption):
        """
        ``Mgeoin`` represents INP mgeoin embedded geometry specification
        options.

        ``Mgeoin`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP mgeoin embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the input file with mesh description.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Mgeoin``.

            Parameters:
                filename: Name of the input file with mesh description.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filename is None or not filename:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MGEOIN
            self.value = value

            self.filename = value

    class Meeout(EmbeddedGeometryOption):
        """
        ``Meeout`` represents INP meeout embedded geometry specification
        options.

        ``Meeout`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP meeout embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name assigned to EEOUT, the elemental edit output file.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Meeout``.

            Parameters:
                filename: Name assigned to EEOUT, the elemental edit output file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MEEOUT
            self.value = value

            self.filename = value

    class Meein(EmbeddedGeometryOption):
        """
        ``Meein`` represents INP meein embedded geometry specification options.

        ``Meein`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP meein embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the EEOUT results file to read.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Meein``.

            Parameters:
                filename: Name of the EEOUT results file to read.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filename is None or not filename:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MEEIN
            self.value = filename

            self.filename = filename

    class CalcVols(EmbeddedGeometryOption):
        """
        ``CalcVols`` represents INP calc_vols embedded geometry specification
        options.

        ``CalcVols`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP calc_vols embedded geometry data card option sytnax
        element.

        Attributes:
            yes_no: Inferred geometry volume and masses calculation setting.
        """

        def __init__(self, yes_no: str):
            """
            ``__init__`` initializes ``CalcVols``.

            Parameters:
                yes_no: Inferred geometry volume and masses calculation setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if yes_no is None or yes_no not in {"yes", "no"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.CALC_VOLS
            self.value = yes_no

            self.yes_no = yes_no

    class Debug(EmbeddedGeometryOption):
        """
        ``Debug`` represents INP debug embedded geometry specification options.

        ``Debug`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP debug embedded geometry data card option sytnax
        element.

        Attributes:
            form: Write the embedded geometry parameters to the OUTP file.
        """

        def __init__(self, form: str):
            """
            ``__init__`` initializes ``Debug``.

            Parameters:
                form: Write the embedded geometry parameters to the OUTP file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if form is None or form not in {"echomesh"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.DEBUG
            self.value = form

            self.form = form

    class Filetype(EmbeddedGeometryOption):
        """
        ``Filetype`` represents INP filetype embedded geometry specification
        options.

        ``Filetype`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP filetype embedded geometry data card option sytnax
        element.

        Attributes:
            filetype: File type for the elemental edit output file.
        """

        def __init__(self, filetype: str):
            """
            ``__init__`` initializes ``Filetype``.

            Parameters:
                filetype: File type for the elemental edit output file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filetype is None or filetype not in {"ascii", "binary"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.FILETYPE
            self.value = filetype

            self.filetype = filetype

    class Gmvfile(EmbeddedGeometryOption):
        """
        ``Gmvfile`` represents INP gmvfile embedded geometry specification
        options.

        ``Gmvfile`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP gmvfile embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the GMV output file.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Gmvfile``.

            Parameters:
                filename: Name of the GMV output file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filename is None or not filename:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.GMVFILE
            self.value = filename

            self.filename = filename

    class Length(EmbeddedGeometryOption):
        """
        ``Length`` represents INP length embedded geometry specification
        options.

        ``Length`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP length embedded geometry data card option sytnax
        element.

        Attributes:
            factor: Multiplicative conversion factor to centimeters from mesh.
        """

        def __init__(self, factor: float):
            """
            ``__init__`` initializes ``Length``.

            Parameters:
                factor: Multiplicative conversion factor to centimeters from mesh.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if factor is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.LENGTH
            self.value = factor

            self.factor = factor

    class Mcnpumfile(EmbeddedGeometryOption):
        """
        ``Mcnpumfile `` represents INP mcnpumfile embedded geometry
        specification options.

        ``Mcnpumfile`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP mcnpumfile embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the MCNPUM output file.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Mcnpumfile``.

            Parameters:
                filename: Name of the MCNPUM output file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filename is None or not filename:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MCNPUMFILE
            self.value = filename

            self.filename = filename

    def __init__(self, pairs: tuple[EmbeddedGeometryOption], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedGeometry``.

        Parameters:
            pairs: Tuple of key-value pairs.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.EMBEDED_GEOMETRY
        self.parameters = pairs
        self.suffix: final[int] = suffix

        self.pairs = pairs


class EmbeddedControl(Datum):
    """
    ``EmbeddedControl`` represents INP embedded elemental edits control
    data cards.

    ``EmbeddedGeometry`` inherits attributes from ``Datum``. It represents the
    INP embedded elemental edits control data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
        suffix: Data card suffix.
        designator: Data card designator.
    """

    class EmbeddedControlOption:
        """
        ``EmbeddedControlOption`` represents INP embedded elemental
        edits control data card options.

        ``EmbeddedControlOption`` implements INP embedded elemental
        edits control data card options. Its attributes store keywords and
        values, and its methods provide entry and endpoints for working wit
        INP embedded elemental edits control data card options. It represents
        the generic INP embedded elemental edits control data card option
        syntax element, so ``EmbeddedControl`` depends on
        ``EmbeddedControlOption`` as a genric data structre and superclass.

        Attributes:
            keyword: INP embedded elemental control  option keyword.
            value: INP embedded elemental control option value.
        """

        class EmbeddedControlKeyword(StrEnum):
            """
            ``EmbeddedControlKeyword`` represents INP embedded elemental
            edits control data card option keywords.

            ``EmbeddedControlKeyword`` implements INP embedded elemental
            edits control data card option keywords as a Python inner class. It
            enumerates MCNP keywords and provides methods for casting strings
            to ``EmbeddedControlKeyword`` instances. It represents the
            INP embedded elemental edits control data card option keyword
            syntax element, so ``EmbeddedControl`` and
            ``EmbeddedControlOption`` depend on ``EmbeddedControlKeyword`` as
            an enum.
            """

            EMBED = "embed"
            ENERGY = "energy"
            TIME = "time"
            ATOM = "atom"
            FACTOR = "factor"
            LIST = "list"
            MAT = "mat"
            MTYPE = "mtype"

            @staticmethod
            def from_mcnp(cls, source: str):
                """
                ``from_mcnp`` generates ``EmbeddedControlKeyword``
                objects from INP.

                ``from_mcnp`` constructs instances of ``EmbeddedControlKeyword``
                from INP source strings, so it operates as a class constructor
                method and INP parser helper function.

                Parameters:
                    source: INP for embedded edits control option keyword.

                Returns:
                    ``EmbeddedControlKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
                """

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in EmbeddedControlKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

                return EmbeddedControlKeyword(source)

        def __init__(self, keyword: EmbeddedControlKeyword, value: any):
            """
            ``__init__`` initializes ``EmbeddedControlOption``.

            Parameters:
                keyword: Embedded edits control data card option keyword.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

            match mnemoinc:
                case EmbeddedControlOption.EmbeddedControlKeyword.EMBED:
                    obj = EmbeddedControlOption.Embed(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.ENERGY:
                    obj = EmbeddedControlOption.Energy(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.TIME:
                    obj = EmbeddedControlOption.Time(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.ATOM:
                    obj = EmbeddedControlOption.Atom(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.FACTOR:
                    obj = EmbeddedControlOption.Factor(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.LIST:
                    assert False, "Unimplemented"
                case EmbeddedControlOption.EmbeddedControlKeyword.MAT:
                    obj = EmbeddedControlOption.Mat(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.MTYPE:
                    obj = EmbeddedControlOption.Mtype(keyword, value)

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(string: str):
            """
            ``from_mcnp`` generates ``EmbeddedControlOption`` objects from INP.

            ``from_mcnp`` constructs instances of ``EmbeddedControlOption``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function. Although defined on the
            superclass, it returns ``EmbeddedControlOption`` subclasses.

            Parameters:
                source: INP for embedded elemental edits control option.

            Returns:
                ``EmbeddedControlOption`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
                MCNPSyntaxError: TOOFEW_DATUM_EMBEE, TOOLONG_DATUM_EMBEE.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_EMBEE))

            # Processing Keyword
            keyword = EmbeddedGeometryOption.EmbeddedGeometryKeyword.from_mcnp(tokens.peekl())

            # Processing Values
            match keyword:
                case EmbeddedGeometryKeyword.EMBED:
                    value = types.cast_fortran_integer(tokens.popl())
                case EmbeddedGeometryKeyword.ENERGY | EmbeddedGeometryKeyword.TIME | EmbeddedGeometryKeyword.FRACTOR:
                    value = types.cast_fortran_real(tokens.popl())
                case EmbeddedGeometryKeyword.ATOM | EmbeddedGeometryKeyword.MTYPE:
                    value = tokens.popl()
                case _:
                    errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_EMBEE)

            return EmbeddedControlOption(keyword, value)

    class Embed(EmbeddedControlOption):
        """
        ``Embed`` represents INP Embed embedded elemental edits control data
        card options.

        ``Embed`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Embed embedded elemental edits control data card
        option syntax element.

        Attributes:
            number: Embedded mesh universe number.
        """

        def __init__(self, number: int):
            """
            ``__init__`` initializes ``Embed``.

            Parameters:
                number: Embedded mesh universe number.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if number is None or not (1 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.EMBED
            self.value = number

            self.number = number

    class Energy(EmbeddedControlOption):
        """
        ``Energy`` represents INP Energy embedded elemental edits control data
        card options.

        ``Energy`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Energy embedded elemental edits control data card
        option syntax element.

        Attributes:
            factor: Conversion factor for all energy outputs.
        """

        def __init__(self, factor: float):
            """
            ``__init__`` initializes ``Energy``.

            Parameters:
                factor: Conversion factor for all energy outputs.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if factor is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.ENERGY
            self.value = factor

            self.factor = factor

    class Time(EmbeddedControlOption):
        """
        ``Time`` represents INP Time embedded elemental edits control data card
        options.

        ``Time`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Time embedded elemental edits control data card
        option syntax element.

        Attributes:
            factor: Conversion factor for all time-related outputs.
        """

        def __init__(self, factor: float):
            """
            ``__init__`` initializes ``Time``.

            Parameters:
                factor: Conversion factor for all time-related outputs.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if factor is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.TIME
            self.value = factor

            self.factor = factor

    class Atom(EmbeddedControlOption):
        """
        ``Atom`` represents INP Atom embedded elemental edits control data card
        options.

        ``Atom`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Atom embedded elemental edits control data card
        option syntax element.

        Attributes:
            yes_no: Flag to multiply by atom density.
        """

        def __init__(self, yes_no: str):
            """
            ``__init__`` initializes ``Atom``.

            Parameters:
                yes_no: Flag to multiply by atom density.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if yes_no is None or yes_no not in {"yes", "no"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.ATOM
            self.value = yes_no

            self.yes_no = yes_no

    class Factor(EmbeddedControlOption):
        """
        ``Factor`` represents INP Factor embedded elemental edits control data
        card options.

        ``Factor`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Factor embedded elemental edits control data card
        option syntax element.

        Attributes:
            factor: Multiplicative constant.
        """

        def __init__(self, factor: float):
            """
            ``__init__`` initializes ``Factor``.

            Parameters:
                factor: Multiplicative constant.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if factor is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.FACTOR
            self.value = factor

            self.factor = factor

    class Mat(EmbeddedControlOption):
        """
        ``Mat`` represents INP Mat embedded elemental edits control data card
        options.

        ``Mat`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Mat embedded elemental edits control data card option
        syntax element.

        Attributes:
            number: Material number.
        """

        def __init__(self, number: int):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                number: Material number.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if number is None or not (0 <= number <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.MAT
            self.value = number

            self.number = number

    class Mtype(EmbeddedControlOption):
        """
        ``Mtype`` represents INP Mtype embedded elemental edits control data
        card options.

        ``Mtype`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Mtype embedded elemental edits control data card
        option syntax element.

        Attributes:
            mtype: Multiplier type.
        """

        def __init__(self, mtype: str):
            """
            ``__init__`` initializes ``Mtype``.

            Parameters:
                mtype: Multiplier type.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if mtype is None or mtype not in {"flux", "isotopic", "population", "reaction", "source", "tracks"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.MTYPE
            self.value = mtype

            self.mtype = mtype

    def __init__(self, pairs: tuple[EmbeddedControlOption], suffix: int, designator: tuple[types.Designator]):
        """
        ``__init__`` initializes ``EmbeddedControl``.

        Parameters:
            pairs: Tuple of key-value pairs.
            suffix: Data card suffix.
            designator: Data card designator.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        for particle in designator:
            if particle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        self.mnemonic = Datum.DatumMnemonic.EMBEDED_CONTROL
        self.parameters = pairs
        self.suffix = suffix
        self.designator = designator

        self.pairs = pairs


class EmbeddedEnergyBoundaries(Datum):
    """
    ``EmbeddedEnergyBoundaries`` represents INP embedded elemental
    edits energy boundaries.

    ``EmbeddedEnergyBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits energy boundaries data
    card syntax element.

    Attributes:
        energies: Tuple of energy lower bounds.
        suffix: Data card suffix.
    """

    def __init__(self, energies: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedEnergyBoundaries``.

        Parameters:
            energies: Tuple of energy lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in energies:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.EMBEDED_ENERGY_BOUNDARIES
        self.parameters = energies
        self.suffix = suffix

        self.energies = energies


class EmbeddedEnergyMultipliers(Datum):
    """
    ``EmbeddedEnergyMultipliers`` represents INP embedded elemental
    edits energy multipliers.

    ``EmbeddedEnergyMultipliers`` inherits attributes from ``Datum``. It
    represents the INP embedded elemental edits energy multipliers data card
    syntax element.

    Attributes:
        multipliers: Tuple of energy multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedEnergyMultipliers``.

        Parameters:
            multipliers: Tuple of energy multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.EMBEDED_ENERGY_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers


class EmbeddedTimeBoundaries(Datum):
    """
    ``EmbeddedTimeBoundaries`` represents INP embedded elemental edits
    time boundaries.

    ``EmbeddedTimeBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits time boundaries data
    card syntax element.

    Attributes:
        times: Tuple of time lower bounds.
    """

    def __init__(self, times: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedTimeBoundaries``.

        Parameters:
            times: Tuple of time lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX
        """

        for parameter in times:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.EMBEDED_TIME_BOUNDARIES
        self.parameters = times
        self.suffix = suffix

        self.times = times


class EmbeddedTimeMultipliers(Datum):
    """
    ``EmbeddedTimeMultipliers`` represents INP embedded elemental
    edits time multipliers.

    ``EmbeddedTimeMultipliers`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits time multipliers data
    card syntax element.

    Attributes:
        multipliers: Tuple of time multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedTimeMultipliers``.

        Parameters:
            multipliers: Tuple of time multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.EMBEDED_TIME_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers


class EmbeddedDoseBoundaries(Datum):
    """
    ``EmbeddedDoseBoundaries`` represents INP embedded elemental edits
    dose boundaries.

    ``EmbeddedDoseBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits dose boundaries data
    card syntax element.

    Attributes:
        doses: Tuple of dose lower bounds.
    """

    def __init__(self, doses: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedDoseBoundaries``.

        Parameters:
            doses: Tuple of dose lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in doses:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.EMBEDED_DOSE_BOUNDARIES
        self.parameters = doses
        self.suffix = suffix

        self.doses = doses


class EmbeddedDoseMultipliers(Datum):
    """
    ``EmbeddedDoseMultipliers`` represents INP embedded elemental
    edits dose multipliers.

    ``EmbeddedDoseMultipliers`` iinherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits dose multipliers data
    card syntax element.

    Attributes:
        doses: Tuple of dose multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedDoseMultipliers``.

        Parameters:
            multipliers: Tuple of dose multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.EMBEDED_DOSE_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers


class Material(Datum):
    """
    ``Material`` represents INP matieral specification data cards.

    ``Material`` inherits attributes from ``Datum``. It represents the INP
    material data card syntax element.

    Attributes:
        substances: Tuple of substance specification.
        paris: Tuple of key-value pairs.
    """

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

        def __init__(self):
            """
            ``__init__`` initializes ``MaterialValue``.

            Parameters:
                zaid: Material value Zaid specifier.
                fraction: Material value fraction.

            Raises:
                MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            """

            self.zaid: types.Zaid = None
            self.fraction: float = None

        @staticmethod
        def from_mcnp(string: str):
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
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL))

            zaid = types.Zaid().cast_mcnp_zaid(tokens.popl())
            fraction = types.cast_fortran_real(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL)

            return MaterialValue(zaid, fraction)

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

        class MaterialKeyword(StrEnum):
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
            def from_mcnp(cls, string: str):
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
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD)

                return MaterialKeyword(source)

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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD)

            match keyword:
                case MaterialKeyword.GAS:
                    obj = MaterialOption.Gas(keyword, value)
                case MaterialKeyword.ESTEP:
                    obj = MaterialOption.Estep(keyword, value)
                case MaterialKeyword.HSTEP:
                    obj = MaterialOption.Hstep(keyword, value)
                case MaterialKeyword.NLIB:
                    obj = MaterialOption.Nlib(keyword, value)
                case MaterialKeyword.PLIB:
                    obj = MaterialOption.Plib(keyword, value)
                case MaterialKeyword.PNLIB:
                    obj = MaterialOption.Pnlib(keyword, value)
                case MaterialKeyword.ELIB:
                    obj = MaterialOption.Elib(keyword, value)
                case MaterialKeyword.HLIB:
                    obj = MaterialOption.Hlib(keyword, value)
                case MaterialKeyword.ALIB:
                    obj = MaterialOption.Alib(keyword, value)
                case MaterialKeyword.SLIB:
                    obj = MaterialOption.Slib(keyword, value)
                case MaterialKeyword.TLIB:
                    obj = MaterialOption.Tlib(keyword, value)
                case MaterialKeyword.DLIB:
                    obj = MaterialOption.Dlib(keyword, value)
                case MaterialKeyword.COND:
                    obj = MaterialOption.Cond(keyword, value)
                case MaterialKeyword.REFI:
                    obj = MaterialOption.Refi(keyword, value)
                case MaterialKeyword.REFC:
                    assert False, "Unimplemented"
                case MaterialKeyword.REFS:
                    assert False, "Unimplemented"

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(cls, string: str):
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
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL))

            # Processing Keyword
            keyword = EmbeddedGeometryOption.EmbeddedGeometryKeyword.from_mcnp(tokens.popl())

            # Processing Values
            match keyword:
                case EmbeddedGeometryOption.EmbeddedGeometryKeyword.GAS:
                    value = types.cast_fortran_integer(tokens.popl())

                case EmbeddedGeometryOption.EmbeddedGeometryKeyword.ESTEP | EmbeddedGeometryOption.EmbeddedGeometryKeyword.HSTEP | EmbeddedGeometryOption.EmbeddedGeometryKeyword.COND | EmbeddedGeometryOption.EmbeddedGeometryKeyword.REFI:
                    value = types.cast_fortran_real(tokens.popl())

                case EmbeddedGeometryOption.EmbeddedGeometryKeyword.NLIB | EmbeddedGeometryOption.EmbeddedGeometryKeyword.PLIB | EmbeddedGeometryOption.EmbeddedGeometryKeyword.PNLIB | EmbeddedGeometryOption.EmbeddedGeometryKeyword.ELIB | EmbeddedGeometryOption.EmbeddedGeometryKeyword.HLIB | EmbeddedGeometryOption.EmbeddedGeometryKeyword.ALIB | EmbeddedGeometryOption.EmbeddedGeometryKeyword.SLIB | EmbeddedGeometryOption.EmbeddedGeometryKeyword.TLIB | EmbeddedGeometryOption.EmbeddedGeometryKeyword.DLIB:
                    value = tokens.popl()

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL)

            return EmbeddedGeometryOption(keyword, value)

    class Gas(MaterialOption):
        """
        ``Gas`` represents INP Gas material data card options.

        ``Gas`` inherits attributes from ``MaterialOption``. It represents the
        INP Gas material data card option syntax element.

        Attributes:
            state: Flag for density-effect corection.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                state: Flag for density-effect corection.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if state is None or state not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.GAS
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

        def __init__(self, step: float):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                step: Energy step increment.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if step is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.ESTEP
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

        def __init__(self, step: float):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                step: Energy step increment.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if step is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.HSTEP
            self.value = step

            self.step = step

    class Nlib(MaterialOption):
        """
        ``Nlib`` represents INP Nlib material data card options.

        ``Nlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Nlib material data card option syntax element.

        Attributes:
            step: Energy step increment.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                step: Energy step increment.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if step is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.NLIB
            self.value = step

            self.abx = step

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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.PLIB
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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.PNLIB
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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.ELIB
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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.HLIB
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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.ALIB
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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.SLIB
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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.TLIB
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
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.DLIB
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

        def __init__(self, conducation_state: float):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                conducation_state: Conduction state of material for ELO3.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if conducation_state is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.COND
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

        def __init__(self, index: float):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                index: Constant refractive index.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = MaterialOption.MaterialKeyword.REFI
            self.value = value

            self.index = value

    def __init__(self):
        """
        ``__init__`` initializes ``Material``.

        Parameters:
            substances: Tuple of substance specification.
            paris: Tuple of key-value pairs.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in substances:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.paris = pairs
        self.substances = substances

        self.mnemonic = Datum.DatumMnemonic.MATERIAL
        self.parameters = tuple(list(substances) + list(pairs))
        self, suffix = suffix


class MaterialNeutronScattering(Datum):
    """
    ``MaterialNeutronScattering`` represents INP thermal neutron scattering
    data cards.

    ``MaterialNeutronScattering`` inherits attributes from ``Datum``. It
    represents the INP thermal neturon scattering data card syntax element.

    Attributes:
        identifiers: Tuple of material identifiers.
        suffix: Data card suffix.
    """

    def __init__(self, identifiers: tuple[str], suffix: int):
        """
        ``__init__`` initializes ``MaterialNeutronScattering``.

        Parameters:
            identifiers: Tuple of material identifiers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in identifiers:
            if parameter is None or not parmeter:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.THERMAL_NETURON_SCATTERING
        self.parameters = identifiers
        self.suffix = suffix

        self.identifiers = identifiers


class MaterialNuclideSubstitution(Datum):
    """
    ``MaterialNuclideSubstitution`` represents INP material nuclide
    substitution data cards.

    ``MaterialNuclideSubstitution`` inherits attributes from ``Datum``. It
    represents the INP material nuclide substitution data card syntax element.

    Attributes:
        zaids: Tuple of ZAID alias.
        suffix: Data card suffix.
        designator: Data card designator.
    """

    def __init__(self, zaids: tuple[types.Zaid], suffix: int, designator: tuple[types.Designator]):
        """
        ``__init__`` initializes ``MaterialNuclideSubstitution``.

        Parameters:
            zaids: Tuple of ZAID alias.
            suffix: Data card suffix.
            designator: Data card designator.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        for particle in designator:
            if particle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        self.mnemonic = Datum.DatumMnemonic.THERMAL_NETURON_SCATTERING
        self.parameters = zaids
        self.suffix = suffix
        self.designator = designator

        self.zaids = zaids


class OnTheFlyBroadening(Datum):
    """
    ``OnTheFlyBroadening`` represents INP on-the-fly broadening data cards.

    ``OnTheFlyBroadening`` inherits attributes from ``Datum``. It represents
    the INP on-the-fly boradening data card syntax element.

    Attributes:
        zaids: Tuple of ZAID alias.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``OnTheFlyBroadening``.

        Parameters:
            zaids: Tuple of ZAID alias.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.ONTHEFLY_BROADENING
        self.parameters = zaids

        self.zaids = zaids


class TotalFission(Datum):
    """
    ``OnTheFlyBroadening`` represents INP total fission data cards.

    ``OnTheFlyBroadening`` inherits attributes from ``Datum``. It represents
    the INP on-the-fly boradening data card syntax element.

    Attributes:
        has_no: No volume calculation option.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``TotalFission``.

        Parameters:
           has_no: No volume calculation option.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if has_no is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.TOTAL_FISSION
        self.parameters = (has_no,)

        self.states = has_no


class FissionTurnoff(Datum):
    """
    ``FissionTurnoff`` represents INP fission turnoff data cards.

    ``FissionTurnoff`` inherits attributes from ``Datum``. It represents
    the INP fission turnoff data card syntax element.

    Attributes:
        states: Tuple of fission turnoff settings.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``FissionTurnoff``.

        Parameters:
            states: Tuple of fission turnoff settings.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in states:
            if parameter is None or parameter not in {0, 1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.FISSION_TURNOFF
        self.parameters = states

        self.states = states


class AtomicWeight(Datum):
    """
    ``AtomicWeight`` represents INP atomic weight data cards.

    ``AtomicWeight`` inherits attributes from ``Datum``. It represents
    the INP atomic weight data card syntax element.

    Attributes:
        weight_ratios: Tuple of weight ratios.
    """

    class AtomicWeightValue:
        """
        ``AtomicWeightValue`` represents INP atomic weight data card entries.

        ``AtomicWeightValue`` implements INP material specifications as a
        Python inner class. Its attributes store different mateiral entries,
        and its methods provide entry points and endpoints for working with
        atomic weight entries. ``AtomicWeight`` depends on
        ``AtomicWeightValue`` as a data type.

        Attributes:
            zaid: Atomic weight value Zaid specifier.
            ratio: Atomic weight value weight ratio.
        """

        def __init__(self, zaid: types.Zaid, ratio: float):
            """
            ``__init__`` initializes ``AtomicWeightValue``.
            """

            if zaid is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if ratio is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.zaid: types.Zaid = zaid
            self.ratio: float = ratio

        @staticmethod
        def from_mcnp(string: str):
            """
            ``from_mcnp`` generates ``AtomicWeightValue`` objects from INP.

            ``from_mcnp`` constructs instances of ``AtomicWeightValue`` from
            INP source strings, so it operates as a class constructor method
            and INP parser helper function.

            Parameters:
                source: INP for atomic weight values.

            Returns:
                ``AtomicWeightValue`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_PARAMETERS.
                MCNPSyntaxError: TOOFEW_DATUM_WEIGHT, TOOLONG_DATUM_WEIGHT.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_WEIGHT))

            zaid = types.Zaid().cast_mcnp_zaid(tokens.popl())
            ratio = types.cast_fortran_real(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_WEIGHT)

            return AtomicWeightValue(zaid, ratio)

    def __init__(self, weight_ratios: tuple[AtomicWeightValue]):
        """
        ``__init__`` initializes ``AtomicWeight``.

        Parameters:
            weight_ratios: Tuple of weight ratios.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in weights:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.ATOMIC_WEIGHT
        self.parameters = weight_ratios

        self.weight_ratios = weight_ratios


class CrossSectionFile(Datum):
    """
    ``CrossSectionFile`` represents INP cross-section file data cards.

    ``CrossSectionFile`` inherits attributes from ``Datum``. It represents the
    INP cross-section file data card syntax element.

    Attributes:
        zaid: Cross-section file zaid.
        weight_ratio: Cross-section atomic weight ratio.
        entries: Tuple of file entries.
        suffix: Data card suffix.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CrossSectionFile``.

        Parameters:
            zaid: Cross-section file zaid.
            weight_ratio: Cross-section atomic weight ratio.
            entries: Tuple of file entries.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if zaid is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if weight_ratio is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for parameter in entries:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCOdes.INVALID_DATUM_SUFFIX)

        self.mnemonic = Datum.DatumMnemonic.CROSSSECTION_FILE
        self.parameters = (zaid, weight_ratio, entries)
        self.suffix = suffix

        self.zaid = zaid
        self.weight_ratio = weight_ratio
        self.entries = entries


class Void(Datum):
    """
    ``Void`` represents INP material void data cards.

    ``Void`` inherits attributes from ``Datum``. It represents the INP material
    void data card syntax element.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Void``.

        Parameters:
            numbers: Tuple of cell numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in numbers:
            if parameter is None or not (1 <= parameter <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.mnemonic = Datum.DatumMnemonic.VOID
        self.parameters = numbers

        self.numbers = numbers
