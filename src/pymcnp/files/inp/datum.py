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

        @classmethod
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

    def __init__(self):
        """
        ``__init__`` initializes ``Datum``.
        """

        super().__init__()

        self.mnemonic: DatumMnemonic = None
        self.parameters: tuple[any] = None

    def set_mnemonic(self, mnemonic: DatumMnemonic) -> None:
        """
        ``set_mnemonic`` stores INP data card mnemonic.

        ``set_mnemonic`` checks given arguments before assigning the given
        value to ``Datum.mnemonic``. If given an unrecognized argument, it
        raises semantic errors.

        Warnings:
            ``set_mnemonic`` reinitializes ``Datum`` instances since
            its attributes depend on the keyword. When the given keyword does
            not equal ``Datum.mnemonic``, all attributes reset.

        Parameters:
            number: Data card mnemonic.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MNEMONIC.
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
                    obj = EmbededGeometry()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_CONTROL:
                    obj = EmbededControl()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_ENERGY_BOUNDARIES:
                    obj = EmbededEnergyBoundaries()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_ENERGY_MULTIPLIERS:
                    obj = EmbededEnergyMultipliers()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_TIME_BOUNDARIES:
                    obj = EmbededTimeBoundaries()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_TIME_MULTIPLIERS:
                    obj = EmbededTimeMultipliers()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_DOSE_BOUNDARIES:
                    obj = EmbededDoseBoundaries
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.EMBEDED_DOSE_MULTIPLIERS:
                    obj = EmbededDoseMultipliers()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case cls.DatumMnemonic.MATERIAL:
                    obj = Material()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__

    @classmethod
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
                transformations = []
                while tokens:
                    source = " ".join([tokens.popl(), tokens.popl(), tokens.popl(), tokens.popl()])
                    transformations.append(StochasticGeometry.StochasticGeometryValue().from_mcnp(source))

                datum.set_parameters(*transformations)

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
                    paris.append(EmbededGeometry.EmbededGeometryOption.from_mcnp(tokens.popl()))

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
                    paris.append(EmbededControl.EmbededControlOption.from_mcnp(tokens.popl()))

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
            "mnemoinc": self.mnemonic,
            "m": self.suffix if hasattr(self.__class__, "suffix") else None,
            "n": self.designator if hasattr(self.__class__, "designator") else None,
            "parameters": self.parameters,
        }


class Datum_Designator(Datum):
    """
    ``Datum_Designator`` represents INP data card with designators.

    ``Datum_Designator`` extends ``Datum`` by adding attributes
    for storing and methods for parsing data card designators. It represents
    the generic INP data card syntax element with designators.

    Attributes:
        designator: Data card designator.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Datum_Designator``.
        """

        super().__init__()

        self.designator: tuple[types.Designator] = None

    def set_designator(self, designator: tuple[types.Designator]) -> None:
        """
        ``set_designator`` stores INP data card designators.

        ``set_designator`` checks for valid designators before assigning
        the given value to ``Datum_Designator.designator``. If given
        an unrecognized argument, it raises semantic errors.

        Parameters:
            designators: Data card designator.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        self.designator = designator


class Datum_Suffix(Datum):
    """
    ``Datum_Suffix`` represents INP data card with suffixes.

    ``Datum_Suffix`` extends ``Datum`` by adding attributes for
    storing and methods for parsing data card suffixes. It represents the
    generic INP cell card option syntax element with suffixes.

    Attributes:
        suffix: Data card suffix.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Datum_Suffix``.
        """

        super().__init__()

        self.suffix: int = None

    def set_suffix(self, suffix: int) -> None:
        """
        ``set_suffix`` stores INP cell option suffixes.

        ``set_suffix`` checks for valid suffixes before assigning the given
        value to ``Datum_Suffix.suffix``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.suffix = suffix


class Volume(Datum):
    """
    ``Volume`` represents INP volume data cards.

    ``Volume`` inherits attributes from ``Datum``. It represents the INP volume
    data card syntax element.

    Attributes:
        has_no: No volume calculation option.
        volumes: Iterable of cell volumes.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Volume``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.VOLUME

        self.has_no: bool = None
        self.volumes: tuple[float] = None

    def set_parameters(self, has_no: bool, *volumes: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``Volume.volumes``, ``Volume.has_no``, and
        ``Volume.parameters``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            has_no: No volume calculation option.
            *volumes: Iterable of cell volumes.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        self.has_no = has_no

        for parameter in volumes:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = volumes
        self.volumes = volumes


class Area(Datum):
    """
    ``Area`` represents INP area data cards.

    ``Area`` inherits attributes from ``Datum``. It represents the INP area
    data card syntax element.

    Attributes:
        areas: Iterable of cell areas.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Area``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.AREA

        self.areas: tuple[float] = None

    def set_parameters(self, *areas: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``Area.areas`` and ``Area.parameters``. If given an
        unrecognized argument, it raises semantic errors.

        Parameters:
            *areas: Iterable of cell areas.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in areas:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = areas
        self.areas = areas


class Transformation(Datum_Suffix):
    """
    ``Transformation`` represents INP transformation data cards.

    ``Transformation`` inherits attributes from ``Datum_Suffix``, i.e.
    ``Datum`` with suffix support. It represents the INP transformation data
    card syntax element.

    Attributes:
        displacement: Transformation displacement vector.
        rotation: Transformation rotation matrix.
        system: Transformation coordinate system setting.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Transformation``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.TRANSFORMATION

        self.displacement: tuple[float] = None
        self.rotation: tuple[tuple[float]] = None
        self.system: int = None

    def set_parameters(self, displacement: tuple[float], rotation: tuple[tuple[float]], system: int) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``Transformation.displacement``, ``Transformation.rotation``,
        ``Transformation.system``, and ``Transformation.parameters``. If given
        an unrecognized argument, it raises semantic errors.

        Parameters:
            displacement: Transformation displacement vector.
            rotation: Transformation rotation matrix.
            system: Transformation coordinate system setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        # Processing displacement
        for entry in displacement:
            if entry is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.displacement = displacement

        # Processing rotation
        parameters = []
        for row in rotation:
            for entry in row:
                if entry is None:
                    parameters.append(entry)
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.rotation = rotation

        # Processing system
        if system is None or system not in {-1, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.system = system

        self.parameters = tuple([number] + list(displacement) + parameters + [system])


class Universe(Datum):
    """
    ``Universe`` represents INP universe data cards.

    ``Universe`` inherits attributes from ``Datum``. It represents the INP
    universe data card syntax element.

    Attributes:
        universes: Iterable of cell universe numbers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Universe``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.UNIVERSE

        self.unvierses: tuple[int] = None

    def set_parameters(self, *unvierses: int) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``Universe.universes`` and ``Universe.parameters``. If given
        an unrecognized argument, it raises semantic errors.

        Parameters:
            *universes: Iterable of cell universe numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in unvierses:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = unvierses
        self.universes = unvierses


class Lattice(Datum):
    """
    ``Lattice`` represents INP lattice data cards.

    ``Lattice`` inherits attributes from ``Datum``. It represents the INP
    lattice data card syntax element.

    Attributes:
        lattices: Iterable of cell lattice numbers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Lattice``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.LATTICE

        self.lattices: tuple[int] = None

    def set_parameters(self, *lattices: int) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``Lattice.lattices`` and ``Lattice.parameters``. If given
        an unrecognized argument, it raises semantic errors.

        Parameters:
            *lattices: Iterable of cell lattice numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in lattices:
            if parameter is None or parameter not in {1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = lattices
        self.lattices = lattices


class Fill(Datum):
    """
    ``Fill`` represents INP fill data cards.

    ``Fill`` inherits attributes from ``Datum``. It represents the INP
    universe data card syntax element.

    Attributes:
        fills: Iterable of universe numbers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Fill``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.FILL

        self.fills: tuple[int] = None

    def set_parameters(self, *fills: int) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``Fill.fills`` and ``Fill.parameters``. If given
        an unrecognized argument, it raises semantic errors.

        Parameters:
            *fills: Iterable of universe numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in fills:
            if parameter is None or not (parameter >= 0 and parameter <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = fills
        self.fills = fills


class StochasticGeometry(Datum):
    """
    ``StochasticGeometry`` represents INP stochastic geometry data cards.

    ``StochasticGeometry`` inherits attributes from ``Datum``. It represents
    the INP universe data card syntax element.

    Attributes:
        transformations: Iterable of stochastric geometry transformations.
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

        def __init__(self):
            """
            ``__init__`` initializes ``StochasticGeometryValue``.
            """

            self.number: int = None
            self.maximum_x: float = None
            self.maximum_y: float = None
            self.maximum_z: float = None

        @classmethod
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
                MCNPSemanticError: INVALID_DATUM_PARAMETERS.
                MCNPSyntaxError: TOOFEW_DATUM_URAN, TOOLONG_DATUM_URAN.
            """

            entry = cls()

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_URAN))

            # Parsing Universe Number
            value = types.cast_fortran_integer(tokens.popl())
            if value is None or not (1 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            entry.number = value

            # Parsing Maximum Translations
            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            entry.maximum_x = value

            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            entry.maximum_y = value

            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            entry.maximum_z = value

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_URAN)

            return entry

    def __init__(self):
        """
        ``__init__`` initializes ``StochasticGeometry``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.STOCHASTIC_GEOMETRY

        self.transformations: tuple[StochasticGeometryValue] = None

    def set_parameters(self, *transformations: StochasticGeometryValue) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``StochasticGeometry.transformations`` and
        ``StochasticGeometry.parameters``. If given an unrecognized argument,
        it raises semantic errors.

        Parameters:
            *transformations: Iterable of stochastric geometry transformations.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in transformations:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = transformations
        self.transformations = transformations


class DeterministicMaterials(Datum):
    """
    ``DeterministicMaterials`` represents INP deterministic materials data
    cards.

    ``DeterministicMaterials`` inherits attributes from ``Datum``. It
    represents the INP deterministic materials data card syntax element.

    Attributes:
        materials: Iterable of Zaids.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``DeterministicMaterials``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.DETERMINISTIC_MATERIALS

        self.materials: tuple[types.Zaid] = None

    def set_parameters(self, *materials: types.Zaid) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``DeterministicMaterials.matierals`` and
        ``DeterministicMaterials.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *materials: Iterable of ZAID aliases.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in materials:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = materials
        self.materials = materials


class DeterministicWeightWindow(Datum):
    """
    ``DeterministicWeightWindow`` represents INP deterministic weight window
    data cards.

    ``DeterministicWeightWindow`` inherits attributes from ``Datum``. It
    represents the INP deterministic weight window data card syntax element.

    Attributes:
        pairs: Iterable of key-value pairs.
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

            @classmethod
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

                keyword = cls()

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in cls]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

                return cls(source)

        def __init__(self):
            """
            ``__init__`` initializes ``DeterministicWeightWindowOption``.
            """

            self.keyword: self.DeterministicWeightWindowKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: DeterministicWeightWindowKeyword) -> None:
            """
            ``set_keyword`` stores INP deterministic weight window option
            keywords.

            ``set_keyword`` checks given arguments before assigning the
            given value to``DeterministicWeightWindowOption.keyword``. If
            given an unrecognized argument, it raises semantic errors.

            Warnings:
                ``set_keyword`` reinitializes
                ``DeterministicWeightWindowOption`` instances sincee its
                attributes depend on the keyword. When the given keyword does
                not equal ``DeterministicWeightWindowOption.keyword``, all
                attributes reset.

            Parameters:
                keyword: Deterministic weight window data card option keyword.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

            if self.keyword != keyword:
                match keyword:
                    case DeterministicWeightWindowKeyword.POINTS:
                        obj = DeterministicWeightWindow.Points()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.XSEC:
                        obj = DeterministicWeightWindow.Xsec()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.TALLY:
                        obj = DeterministicWeightWindow.Tally()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.BLOCK:
                        obj = DeterministicWeightWindow.Block()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NGROUP:
                        obj = DeterministicWeightWindow.Ngroup()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ISN:
                        obj = DeterministicWeightWindow.Isn()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NISO:
                        obj = DeterministicWeightWindow.Niso()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.MT:
                        obj = DeterministicWeightWindow.Mt()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.IQUAD:
                        obj = DeterministicWeightWindow.Iquad()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.FMMIX:
                        obj = DeterministicWeightWindow.Fmmix()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOSOLV:
                        obj = DeterministicWeightWindow.Nosolv()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOEDIT:
                        obj = DeterministicWeightWindow.Noedit()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOGEOD:
                        obj = DeterministicWeightWindow.Nogeod()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOMIX:
                        obj = DeterministicWeightWindow.Nomix()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOASG:
                        obj = DeterministicWeightWindow.Noasg()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOMACR:
                        obj = DeterministicWeightWindow.Nomacr()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOSLNP:
                        obj = DeterministicWeightWindow.Noslnp()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOEDTT:
                        obj = DeterministicWeightWindow.Noedtt()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOADJM:
                        obj = DeterministicWeightWindow.Noadjm()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.LIB:
                        obj = DeterministicWeightWindow.Lib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.LIBNAME:
                        obj = DeterministicWeightWindow.Libname()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.FISSNEUT:
                        obj = DeterministicWeightWindow.Fissneut()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.LNG:
                        obj = DeterministicWeightWindow.Lng()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.BALXS:
                        obj = DeterministicWeightWindow.Balxs()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NTICHI:
                        obj = DeterministicWeightWindow.Ntichi()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.IEVT:
                        obj = DeterministicWeightWindow.Ievt()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.SCT:
                        obj = DeterministicWeightWindow.Isct()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ITH:
                        obj = DeterministicWeightWindow.Ith()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.TRCOR:
                        obj = DeterministicWeightWindow.Trcor()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.IBL:
                        obj = DeterministicWeightWindow.Ibl()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.IBR:
                        obj = DeterministicWeightWindow.Ibr()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.IBT:
                        obj = DeterministicWeightWindow.Ibt()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.IBB:
                        obj = DeterministicWeightWindow.Ibb()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.IBFRNT:
                        obj = DeterministicWeightWindow.Ibfrnt()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.BIBACK:
                        obj = DeterministicWeightWindow.Ibback()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.EPSI:
                        obj = DeterministicWeightWindow.Epsi()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.OITM:
                        obj = DeterministicWeightWindow.Oitm()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NOSIGF:
                        obj = DeterministicWeightWindow.Nosigf()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.SRCACC:
                        obj = DeterministicWeightWindow.Srcacc()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.DIFFSOL:
                        obj = DeterministicWeightWindow.Diffsol()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.TSASN:
                        obj = DeterministicWeightWindow.Tsasn()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.TSAEPSI:
                        obj = DeterministicWeightWindow.Tsaepsi()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.TSAITS:
                        obj = DeterministicWeightWindow.Tsaits()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.TSABETA:
                        obj = DeterministicWeightWindow.Tsabeta()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.PTCONV:
                        obj = DeterministicWeightWindow.Ptconv()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.NORM:
                        obj = DeterministicWeightWindow.Norm()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.XESCTP:
                        obj = DeterministicWeightWindow.Xesctp()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.FISSRP:
                        obj = DeterministicWeightWindow.Fissrp()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.SOURCP:
                        obj = DeterministicWeightWindow.Sourcp()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ANGP:
                        obj = DeterministicWeightWindow.Angp()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.BALP:
                        obj = DeterministicWeightWindow.Balp()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.RAFLUX:
                        obj = DeterministicWeightWindow.Raflux()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.RMFLUX:
                        obj = DeterministicWeightWindow.Rmflux()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.AVATAR:
                        obj = DeterministicWeightWindow.Avatar()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ASLEFT:
                        obj = DeterministicWeightWindow.Asleft()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ASRITE:
                        obj = DeterministicWeightWindow.Asrite()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ASBOTT:
                        obj = DeterministicWeightWindow.Asbott()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ASTOP:
                        obj = DeterministicWeightWindow.Astop()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ASFRNT:
                        obj = DeterministicWeightWindow.Asfrnt()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ASBACK:
                        obj = DeterministicWeightWindow.Asback()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.MASSED:
                        obj = DeterministicWeightWindow.Massed()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.PTED:
                        obj = DeterministicWeightWindow.Pted()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.ZNED:
                        obj = DeterministicWeightWindow.Zned()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.RZFLUX:
                        obj = DeterministicWeightWindow.Rzflux()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.RXMFLUX:
                        obj = DeterministicWeightWindow.Rzmflux()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.EDOUTF:
                        obj = DeterministicWeightWindow.Edoutf()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.BYVLOP:
                        obj = DeterministicWeightWindow.Byvlop()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.AJED:
                        obj = DeterministicWeightWindow.Ajed()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case DeterministicWeightWindowKeyword.FLUXONE:
                        obj = DeterministicWeightWindow.Fluxone()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__

        @classmethod
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
                MCNPSyntaxError: TOOFEW_DATUM_DAWWG, TOOLONG_DATUM_DAWWG.
            """

            parameter = cls()

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_DAWWG))

            # Processing Keyword
            keyword = cls.DeterministicWeightWindowKeyword.cast_keyword(tokens.peekl())
            parameter.set_keyword(keyword)

            # Processing Values
            match tokens.popl():
                case "points" | "block" | "ngroup" | "isn" | "niso" | "mt" | "iquad" | "fmmix" | "nosolv" | "noedit" | "nogeod" | "nomix" | "noasg" | "nomacr" | "noslnp" | "noedtt" | "noadjm" | "fissneut" | "lng" | "balxs" | "ntichi" | "ievt" | "sct" | "ith" | "ibl" | "ibr" | "ibt" | "ibb" | "ibfrnt" | "biback" | "oitm" | "nosigf" | "tsasn" | "tsaits" | "ptconv" | "xesctp" | "fissrp" | "sourcp" | "angp" | "balp" | "raflux" | "rmflux" | "avatar" | "asleft" | "asrite" | "asbott" | "astop" | "asfrnt" | "asback" | "massed" | "pted" | "zned" | "rzflux" | "rxmflux" | "edoutf" | "byvlop" | "ajed" | "fluxone":
                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "epsi" | "tsaepsi" | "tsabeta" | "norm":
                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "lib" | "libname" | "trcor" | "srcacc" | "diffsol":
                    parameter.set_value(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_DAWWG)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Points``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.POINTS

            self.point: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Block``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.BLOCK

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {1, 3, 5, 6}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ngroup``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NGROUP

            self.energy_group_number: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Isn``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ISN

            self.sn_order: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Niso``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NISO

            self.isotopes_number: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Mt``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.MT

            self.materials_number: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Iquad``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.IQUAD

            self.quadrature: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {1, 3, 4, 5, 6, 7, 8, 9}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Fmmix``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.FMMIX

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Nosolv``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOSOLV

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Noedit``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOEDIT

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Nogeod``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOGEOD

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Nomix``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOMIX

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Noasg``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOASG

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Nomacr``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOMACR

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Noslnp``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOSLNP

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Noedtt``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOEDTT

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Noadjm``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOADJM

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Lib``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.LIB

            self.name: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Libname``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.LIBNAME

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Fissneut``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.FISSNEUT

            self.fission_neutron_flag: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Lng``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.LNG

            self.last_neutron_group_number: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Balxs``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.BALXS

            self.cross_section_balance_control: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ntichi``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NTICHI

            self.mendf_fission_fraction: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ievt``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.IEVT

            self.calculation_type: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2, 3, 4}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Isct``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.SCT

            self.legendre_order: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ith``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ITH

            self.calculation_state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Trcor``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.TRCOR

            self.trcor: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ibl``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.IBL

            self.left_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ibr``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.IBR

            self.right_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ibt``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.IBT

            self.top_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ibb``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.IBB

            self.bottom_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ibfrnt``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.IBFRNT

            self.front_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ibback``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.BIBACK

            self.back_boundary: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Epsi``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.EPSI

            self.convergence_percision: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Oitm``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.OITM

            self.maximum_outer_iteration: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Nosigf``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NOSIGF

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Srcacc``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.SRCACC

            self.transport_accelerations: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Diffsol``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.DIFFSOL

            self.diffusion_operator_solver: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Tsasn``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.TSASN

            self.sn_order: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Tsaepsi``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.TSAEPSI

            self.convergence_criteria: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Tsaits``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.TSAITS

            self.maximum_tsa_iteration: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Tsabeta``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.TSABETA

            self.tsa_scattering_cross_section: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ptconv``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.PTCONV

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Norm``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.NORM

            self.norm: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Xesctp``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.XESCTP

            self.cross_section_print_flag: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Fissrp``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.FISSRP

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Sourcp``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.SOURCP

            self.source_print_flag: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2, 3}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Angp``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ANGP

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Balp``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.BALP

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Raflux``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.RAFLUX

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Rmflux``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.RMFLUX

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Avatar``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.AVATAR

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Asleft``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ASLEFT

            self.right_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Asrite``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ASRITE

            self.left_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Asbott``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ASBOTT

            self.top_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Astop``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ASTOP

            self.bottom_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Asfrnt``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ASFRNT

            self.back_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Asback``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ASBACK

            self.front_going_flux: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Massed``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.MASSED

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Pted``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.PTED

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Zned``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.ZNED

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Rzflux``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.RZFLUX

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Rzmflux``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.RXMFLUX

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Edoutf``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.EDOUTF

            self.ascii_output_control: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or not (-3 <= value <= 3):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Byvlop``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.BYVLOP

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Ajed``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.AJED

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

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

        def __init__(self):
            """
            ``__init__`` initializes ``Fluxone``.
            """

            super().__init__()
            self.keyword = DeterministicWeightWindowKeyword.FLUXONE

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP deterministic weight window data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``DeterministicWeightWindowOption.value``. If given an
            unrecognized arguments, it raises semantic errors.

            Parameters:
                value: Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.value = value
            self.state = value

    def __init__(self):
        """
        ``__init__`` initializes ``DeterministicWeightWindow``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW

        self.pairs: tuple[self.DeterministicWeightWindowOption] = None

    def set_parameters(self, *pairs: DeterministicWeightWindowOption) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``DeterministicWeightWindow.pairs`` and
        ``DeterministicWeightWindow.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *pairs: Iterable of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.pairs = pairs
        self.parameters = pairs


class EmbededGeometry(Datum_Suffix):
    """
    ``EmbededGeometry`` represents INP deterministic embeded geometry data
    cards.

    ``EmbededGeometry`` inherits attributes from ``Datum_Suffix``, i.e.
    ``Datum`` with suffix support. It represents the INP embeded geometry data
    card syntax element.

    Attributes:
        pairs: Iterable of key-value pairs.
    """

    class EmbededGeometryOption:
        """
        ``EmbededGeometryOption`` represents INP embeded geometry specification
        data card options.

        ``EmbededGeometryOption`` implements INP embeded geometry specification
        data card options. Its attributes store keywords and values, and its
        methods provide entry and endpoints for working with INP embeded
        geometry specification data card options. It represents the generic INP
        embeded geometry specification data card option syntax element, so
        ``EmbededGeometry`` depends on ``EmbededGeometryOption`` as a genric
        data structre and superclass.

        Attributes:
            keyword: INP embeded geometry specification option keyword.
            value: INP embeded geometry specification option value.
        """

        class EmbededGeometryKeyword(StrEnum):
            """
            ``EmbededGeometryKeyword`` represents INP embeded geometry
            specification data card option keywords.

            ``EmbededGeometryKeyword`` implements INP embeded geometry
            specification data card option keywords as a Python inner class. It
            enumerates MCNP keywords and provides methods for casting strings
            to ``EmbededGeometryKeyword`` instances. It represents the INP
            embeded geometry specification data card option keyword syntax
            element, so ``EmbededGeometry`` and ``EmbededGeometryOption``
            depend on ``EmbededGeometryKeyword`` as an enum.
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

            @classmethod
            def from_mcnp(cls, source: str):
                """
                ``from_mcnp`` generates ``EmbededGeometryKeyword``
                objects from INP.

                ``from_mcnp`` constructs instances of
                ``EmbededGeometryKeyword`` from INP source strings,
                so it operates as a class constructor method and INP parser
                helper function.

                Parameters:
                    source: INP for embeded geometry option keyword.

                Returns:
                    ``EmbededGeometryKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
                """

                keyword = cls()

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in cls]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

                return cls(source)

        def __init__(self):
            """
            ``__init__`` initializes ``EmbededGeometryOption``.
            """

            self.keyword: self.EmbededGeometryKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: EmbededGeometryKeyword) -> None:
            """
            ``set_keyword`` stores INP embeded geometry option keywords.

            ``set_keyword`` checks given arguments before assigning the
            given value to``EmbededGeometryOption.keyword``. If given an
            unrecognized argument, it raises semantic errors.

            Warnings:
                ``set_keyword`` reinitializes
                ``EmbededGeometryKeyword`` instances sincee its attributes
                depend on the keyword. When the given keyword does not equal
                ``EmbededGeometryOption.keyword``, all attributes reset.

            Parameters:
                keyword: Embeded geometry data card option keyword.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

            if self.keyword != keyword:
                match keyword:
                    case EmbededGeometryKeyword.MATCELL:
                        obj = EmbededGeometryOption.Matcell()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.MESHOGEO:
                        obj = EmbededGeometryOption.Meshgeo()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.MGEOIN:
                        obj = EmbededGeometryOption.Mgeoin()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.MEEOUT:
                        obj = EmbededGeometryOption.Meeout()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.MEEIN:
                        obj = EmbededGeometryOption.Meein()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.CALC_VOLS:
                        obj = EmbededGeometryOption.CalcVols()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.DEBUG:
                        obj = EmbededGeometryOption.Debug()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.FILETYPE:
                        obj = EmbededGeometryOption.Filetype()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.GMVFILE:
                        obj = EmbededGeometryOption.Gmvfile()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.LENGTH:
                        obj = EmbededGeometryOption.Length()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.MCNPUMFILE:
                        obj = EmbededGeometryOption.Mcnpumfile()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case EmbededGeometryKeyword.OVERLAP:
                        obj = EmbededGeometryOption.Overlap()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__

        @classmethod
        def from_mcnp(cls, string: str):
            """
            ``from_mcnp`` generates ``EmbededGeometryOption`` objects from INP.

            ``from_mcnp`` constructs instances of ``EmbededGeometryOption``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function. Although defined on the
            superclass, it returns ``EmbededGeometryOption`` subclasses.

            Parameters:
                source: INP for embeded geometry specification option.

            Returns:
                ``EmbededGeometryOption`` object.

            Raises:
                MCNPSyntaxError: TOOFEW_DATUM_EMBED, TOOLONG_DATUM_EMBED.
            """

            parameter = cls()

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_EMBED))

            # Processing Keyword
            keyword = cls.EmbededGeometryKeyword.from_mcnp(tokens.peekl())
            parameter.set_keyword(keyword)

            # Processing Values
            match tokens.popl():
                case "matcell":
                    parameter.__class__ = EmbededGeometry.Matcell

                    parameter.set_parameter(tokens.popl())

                case "meshgeo" | "mgeoin" | "meeout" | "meein" | "calc_vols" | "debug" | "filetype" | "gmvfile" | "mcnpumfile":
                    parameter.__class__ = EmbededGeometry.Gmvfile

                    parameter.set_parameter(tokens.popl())

                case "length":
                    parameter.__class__ = EmbededGeometry.Length

                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_parameter(value)

                case "overlap":
                    parameter.__class__ = EmbededGeometry.Overlap

                    parameter.set_parameter(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_EMBED)

    class Meshgeo(EmbededGeometryOption):
        """
        ``Meshgeo`` represents INP meshgeo embeded geometry specification
        options.

        ``Meshgeo`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP meshgeo embeded geometry data card option sytnax
        element.

        Attributes:
            format: Format specification of the embedded mesh input file.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Meshgeo``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.MESHOGEO

            self.format: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or value not in {"lnk3dnt", "abaqus", "mcnpum"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.format = value

    class Mgeoin(EmbededGeometryOption):
        """
        ``Mgeoin`` represents INP mgeoin embeded geometry specification
        options.

        ``Mgeoin`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP mgeoin embeded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the input file with mesh description.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mgeoin``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.MGEOIN

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.filename = value

    class Meeout(EmbededGeometryOption):
        """
        ``Meeout`` represents INP meeout embeded geometry specification
        options.

        ``Meeout`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP meeout embeded geometry data card option sytnax
        element.

        Attributes:
            filename: Name assigned to EEOUT, the elemental edit output file.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Meeout``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.MEEOUT

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.filename = value

    class Meein(EmbededGeometryOption):
        """
        ``Meein`` represents INP meein embeded geometry specification options.

        ``Meein`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP meein embeded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the EEOUT results file to read.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Meein``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.MEEIN

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.filename = value

    class CalcVols(EmbededGeometryOption):
        """
        ``CalcVols`` represents INP calc_vols embeded geometry specification
        options.

        ``CalcVols`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP calc_vols embeded geometry data card option sytnax
        element.

        Attributes:
            yes_no: Inferred geometry volume and masses calculation setting.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``CalcVols``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.CALC_VOLS

            self.yes_no: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or value not in {"yes", "no"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.yes_no = value

    class Debug(EmbededGeometryOption):
        """
        ``Debug`` represents INP debug embeded geometry specification options.

        ``Debug`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP debug embeded geometry data card option sytnax
        element.

        Attributes:
            format: Write the embedded geometry parameters to the OUTP file.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Debug``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.DEBUG

            self.format: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or value not in {"echomesh"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.format = value

    class Filetype(EmbededGeometryOption):
        """
        ``Filetype`` represents INP filetype embeded geometry specification
        options.

        ``Filetype`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP filetype embeded geometry data card option sytnax
        element.

        Attributes:
            type: File tpye for the elemental edit output file.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Filetype``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.FILETYPE

            self.type: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or value not in {"ascii", "binary"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self._ = value

    class Gmvfile(EmbededGeometryOption):
        """
        ``Gmvfile`` represents INP gmvfile embeded geometry specification
        options.

        ``Gmvfile`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP gmvfile embeded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the GMV output file.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Gmvfile``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.GMVFILE

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.filename = value

    class Length(EmbededGeometryOption):
        """
        ``Length`` represents INP length embeded geometry specification
        options.

        ``Length`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP length embeded geometry data card option sytnax
        element.

        Attributes:
            factor: Multiplicative conversion factor to centimeters from mesh.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Length``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.LENGTH

            self.factor: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.factor = value

    class Mcnpumfile(EmbededGeometryOption):
        """
        ``Mcnpumfile `` represents INP mcnpumfile embeded geometry
        specification options.

        ``Mcnpumfile`` inherits attributes from ``EmbededGeometryOption``. It
        represents the INP mcnpumfile embeded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the MCNPUM output file.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mcnpumfile``.
            """

            super().__init__()
            self.keyword = EmbededGeometryKeyword.MCNPUMFILE

            self.filename: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded geometry data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededGeometryOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded geomtry data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.value = value
            self.filename = value

    def __init__(self):
        """
        ``__init__`` initializes ``EmbededGeometry``.
        """

        super().__init__()
        self.keyword = EmbededGeometryKeyword.OVERLAP
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_GEOMETRY

        self.pairs: tuple[types.Zaid] = None

    def set_parameters(self, *pairs: EmbededGeometryOption) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``EmbededGeometry.pairs`` and ``EmbededGeometry.parameters``.
        If given an unrecognized argument, it raises semantic errors.

        Parameters:
            *pairs: Iterable of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.pairs = pairs
        self.parameters = pairs


class EmbededControl(Datum_Suffix, Datum_Designator):
    """
    ``EmbededControl`` represents INP embeded elemental edits control
    data cards.

    ``EmbededGeometry`` inherits attributes from ``Datum_Suffix``, i.e.
    ``Datum`` with suffix support, and ``Datum_Designator`` with designator
    support. It represents the INP embeded elemental edits control data card
    syntax element.

    Attributes:
        pairs: Iterable of key-value pairs.
    """

    class EmbededControlOption:
        """
        ``EmbededControlOption`` represents INP embeded elemental
        edits control data card options.

        ``EmbededControlOption`` implements INP embeded elemental
        edits control data card options. Its attributes store keywords and
        values, and its methods provide entry and endpoints for working wit
        INP embeded elemental edits control data card options. It represents
        the generic INP embeded elemental edits control data card option syntax
        element, so ``EmbededControl`` depends on ``EmbededControlOptoin`` as a
        genric data structre and superclass.

        Attributes:
            keyword: INP embeded elemental control  option keyword.
            value: INP embeded elemental control option value.
        """

        class EmbededControlKeyword(StrEnum):
            """
            ``EmbededControlKeyword`` represents INP embeded elemental
            edits control data card option keywords.

            ``EmbededControlKeyword`` implements INP embeded elemental
            edits control data card option keywords as a Python inner class. It
            enumerates MCNP keywords and provides methods for casting strings
            to ``EmbededControlKeyword`` instances. It represents the
            INP embeded elemental edits control data card option keyword syntax
            element, so ``EmbededControl`` and ``EmbededControlOption`` depend
            on ``EmbededControlKeyword`` as an enum.
            """

            EMBED = "embed"
            ENERGY = "energy"
            TIME = "time"
            ATOM = "atom"
            FACTOR = "factor"
            REACTION_LIST = "list"
            MAT = "mat"
            MTYPE = "mtype"

            @classmethod
            def from_mcnp(cls, source: str):
                """
                ``from_mcnp`` generates ``EmbededControlKeyword``
                objects from INP.

                ``from_mcnp`` constructs instances of ``EmbededControlKeyword``
                from INP source strings, so it operates as a class constructor
                method and INP parser helper function.

                Parameters:
                    source: INP for embeded edits control option keyword.

                Returns:
                    ``EmbededControlKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
                """

                keyword = cls()

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in cls]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

                return cls(source)

        def __init__(self):
            """
            ``__init__`` initializes ``EmbededControlOption``.
            """

            self.keyword: self.EmbededControlKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: EmbededControlKeyword) -> None:
            """
            ``set_keyword`` stores INP embeded elemental edits control data
            card option keywords.

            ``set_keyword`` checks given arguments before assigning the
            given value to``EmbededControlOption.keyword``. If given an
            unrecognized argument, it raises semantic errors.

            Warnings:
                ``set_keyword`` reinitializes
                ``EmbededControlKeyword`` instances sincee its attributes
                depend on the keyword. When the given keyword does not equal
                ``EmbededControlOption.keyword``, all attributes reset.

            Parameters:
                keyword: Embeded edits control data card option keyword.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

            if mnemonic != self.mnemonic:
                match mnemoinc:
                    case cls.EmbededControlKeyword.EMBED:
                        obj = EmbededControlOption.Embed()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case cls.EmbededControlKeyword.ENERGY:
                        obj = EmbededControlOption.Energy()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case cls.EmbededControlKeyword.TIME:
                        obj = EmbededControlOption.Time()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case cls.EmbededControlKeyword.ATOM:
                        obj = EmbededControlOption.Atom()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case cls.EmbededControlKeyword.FACTOR:
                        obj = EmbededControlOption.Factor()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case cls.EmbededControlKeyword.MAT:
                        obj = EmbededControlOption.Mat()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case cls.EmbededControlKeyword.MTYPE:
                        obj = EmbededControlOption.Mtype()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__

        @classmethod
        def from_mcnp(cls, string: str):
            """
            ``from_mcnp`` generates ``EmbededControlOption`` objects from INP.

            ``from_mcnp`` constructs instances of ``EmbededControlOption``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function. Although defined on the
            superclass, it returns ``EmbededControlOption`` subclasses.

            Parameters:
                source: INP for embeded elemental edits control option.

            Returns:
                ``EmbededControlOption`` object.

            Raises:
                MCNPSyntaxError: TOOFEW_DATUM_EMBEE, TOOLONG_DATUM_EMBEE.
            """

            parameter = cls()

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_EMBEE))

            # Processing Keyword
            keyword = cls.EmbededGeometryKeyword.from_mcnp(tokens.peekl())
            parameter.set_keyword(keyword)

            # Processing Values
            match tokens.popl():
                case "embded" | "mat":
                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)
                case "engery" | "time" | "factor":
                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)
                case "atom" | "mtype":
                    parameter.set_valie(tokens.popL())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_EMBEE)

    class Embed(EmbededControlOption):
        """
        ``Embed`` represents INP Embed embeded elemental edits control data
        card options.

        ``Embed`` inherits attributes from ``EmbededControlOption``. It
        represents the INP Embed embeded elemental edits control data card
        option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Embed``.
            """

            super().__init__()
            self.keyword = EmbededControlKeyword.EMBED

            self.number: any = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP embeded elemental edits control data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededControlOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded elemental edits control data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if value is None or not (1 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.value = value
            self.number = value

    class Energy(EmbededControlOption):
        """
        ``Energy`` represents INP Energy embeded elemental edits control data
        card options.

        ``Energy`` inherits attributes from ``EmbededControlOption``. It
        represents the INP Energy embeded elemental edits control data card
        option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Energy``.
            """

            super().__init__()
            self.keyword = EmbededControlKeyword.ENERGY

            self.factor: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP embeded elemental edits control data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededControlOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded elemental edits control data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.value = value
            self.factor = value

    class Time(EmbededControlOption):
        """
        ``Time`` represents INP Time embeded elemental edits control data card
        options.

        ``Time`` inherits attributes from ``EmbededControlOption``. It
        represents the INP Time embeded elemental edits control data card
        option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Time``.
            """

            super().__init__()
            self.keyword = EmbededControlKeyword.TIME

            self.factor: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP embeded elemental edits control data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededControlOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded elemental edits control data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.value = value
            self.factor = value

    class Atom(EmbededControlOption):
        """
        ``Atom`` represents INP Atom embeded elemental edits control data card
        options.

        ``Atom`` inherits attributes from ``EmbededControlOption``. It
        represents the INP Atom embeded elemental edits control data card
        option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Atom``.
            """

            super().__init__()
            self.keyword = EmbededControlKeyword.ATOM

            self.yes_no: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded elemental edits control data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededControlOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded elemental edits control data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if value is None or value not in {"yes", "no"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.value = value
            self.yes_no = value

    class Factor(EmbededControlOption):
        """
        ``Factor`` represents INP Factor embeded elemental edits control data
        card options.

        ``Factor`` inherits attributes from ``EmbededControlOption``. It
        represents the INP Factor embeded elemental edits control data card
        option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Factor``.
            """

            super().__init__()
            self.keyword = EmbededControlKeyword.FACTOR

            self.factor: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP embeded elemental edits control data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededControlOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded elemental edits control data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.value = value
            self.factor = value

    class Mat(EmbededControlOption):
        """
        ``Mat`` represents INP Mat embeded elemental edits control data card
        options.

        ``Mat`` inherits attributes from ``EmbededControlOption``. It
        represents the INP Mat embeded elemental edits control data card option
        syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()
            self.keyword = EmbededControlKeyword.MAT

            self.number: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP embeded elemental edits control data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededControlOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded elemental edits control data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if value is None or not (0 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.value = value
            self.number = value

    class Mtype(EmbededControlOption):
        """
        ``Mtype`` represents INP Mtype embeded elemental edits control data
        card options.

        ``Mtype`` inherits attributes from ``EmbededControlOption``. It
        represents the INP Mtype embeded elemental edits control data card
        option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mtype``.
            """

            super().__init__()
            self.keyword = EmbededControlKeyword.MTYPE

            self.type: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP embeded elemental edits control data card
            option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``EmbededControlOptoin.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Embeded elemental edits control data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if value is None or value not in {
                "flux",
                "isotopic",
                "population",
                "reaction",
                "source",
                "tracks",
            }:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.value = value
            self.type = value

    def __init__(self):
        """
        ``__init__`` initializes ``EmbededControl``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_CONTROL

        self.pairs: tuple[types.Zaid] = None

    def set_parameters(self, *pairs: EmbededControlOption) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``EmbededControl.pairs`` and ``EmbededControl.parameters``.
        If given an unrecognized argument, it raises semantic errors.

        Parameters:
            *pairs: Iterable of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.pairs = pairs
        self.parameters = pairs


class EmbededEnergyBoundaries(Datum_Suffix):
    """
    ``EmbededEnergyBoundaries`` represents INP embeded elemental
    edits energy boundaries.

    ``EmbededEnergyBoundaries`` inherits attributes from
    ``Datum_Suffix``, i.e. ``Datum`` with suffix support. It represents the INP
    embeded embeded elemental edits energy boundaries data card syntax element.

    Attributes:
        energies: Iterable of energy lower bounds.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``EmbededEnergyBoundaries``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_ENERGY_BOUNDARIES

        self.energies: tuple[float] = None

    def set_parameters(self, *energies: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``EmbededEnergyBoundaries.pairs`` and
        ``EmbededEnergyBoundaries.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *energies: Iterable of energy lower bounds.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in energies:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = energies
        self.energies = energies


class EmbededEnergyMultipliers(Datum_Suffix):
    """
    ``EmbededEnergyMultipliers`` represents INP embeded elemental
    edits energy multipliers.

    ``EmbededEnergyMultipliers`` inherits attributes from ``Datum_Suffix``,
    i.e. ``Datum`` with suffix support. It represents the INP embeded elemental
    edits energy multipliers data card syntax element.

    Attributes:
        multipliers: Iterable of energy multipliers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``EmbededEnergyMultipliers``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_ENERGY_MULTIPLIERS

        self.multipliers: tuple[float] = None

    def set_parameters(self, *multipliers: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``EmbededEnergyMultipliers.pairs`` and
        ``EmbededEnergyMultipliers.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *multipliers: Iterable of energy multipliers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = multipliers
        self.multipliers = multipliers


class EmbededTimeBoundaries(Datum_Suffix):
    """
    ``EmbededTimeBoundaries`` represents INP embeded elemental edits
    time boundaries.

    ``EmbededTimeBoundaries`` inherits attributes from
    ``Datum_Suffix``, i.e. ``Datum`` with suffix support. It represents the INP
    embeded embeded elemental edits time boundaries data card syntax element.

    Attributes:
        times: Iterable of time lower bounds.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``EmbededTimeBoundaries``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_TIME_BOUNDARIES

        self.times: tuple[float] = None

    def set_parameters(self, *times: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``EmbededTimeBoundaries.pairs`` and
        ``EmbededTimeBoundaries.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *times: Iterable of time lower bounds.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in times:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = times
        self.times = times


class EmbededTimeMultipliers(Datum_Suffix):
    """
    ``EmbededTimeMultipliers`` represents INP embeded elemental
    edits time multipliers.

    ``EmbededTimeMultipliers`` inherits attributes from
    ``Datum_Suffix``, i.e. ``Datum`` with suffix support. It represents the INP
    embeded embeded elemental edits time multipliers data card syntax element.

    Attributes:
        times: Iterable of time multipliers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``EmbededTimeMultipliers``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_TIME_MULTIPLIERS

        self.multipliers: tuple[float] = None

    def set_parameters(self, *multipliers: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``EmbededTimeMultipliers.pairs`` and
        ``EmbededTimeMultipliers.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *multipliers: Iterable of time multipliers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = multipliers
        self.multipliers = multipliers


class EmbededDoseBoundaries(Datum_Suffix):
    """
    ``EmbededDoseBoundaries`` represents INP embeded elemental edits
    dose boundaries.

    ``EmbededDoseBoundaries`` inherits attributes from
    ``Datum_Suffix``, i.e. ``Datum`` with suffix support. It represents the INP
    embeded embeded elemental edits dose boundaries data card syntax element.

    Attributes:
        doses: Iterable of dose lower bounds.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``EmbededDoseBoundaries``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_DOSE_BOUNDARIES

        self.doses: tuple[float] = None

    def set_parameters(self, *doses: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``EmbededDoseBoundaries.pairs`` and
        ``EmbededDoseBoundaries.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *doses: Iterable of dose lower bounds.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in doses:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = doses
        self.doses = doses


class EmbededDoseMultipliers(Datum_Suffix):
    """
    ``EmbededDoseMultipliers`` represents INP embeded elemental
    edits dose multipliers.

    ``EmbededDoseMultipliers`` inherits attributes from
    ``Datum_Suffix``, i.e. ``Datum`` with suffix support. It represents the INP
    embeded embeded elemental edits dose multipliers data card syntax element.

    Attributes:
        doses: Iterable of dose multipliers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``EmbededDoseMultipliers``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.EMBEDED_DOSE_MULTIPLIERS

        self.multipliers: tuple[float] = None

    def set_parameters(self, *multipliers: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``EmbededDoseMultipliers.pairs`` and
        ``EmbededDoseMultipliers.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *multipliers: Iterable of dose multipliers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = multipliers
        self.multipliers = multipliers


class Material(Datum_Suffix):
    """
    ``Material`` represents INP matieral specification data cards.

    ``Material`` inherits attributes from ``Datum_Suffix``, i.e. ``Datum`` with
    suffix support. It represents the INP material data card
    syntax element.

    Attributes:
        substances: Iterable of substance specification.
        paris: Iterable of key-value pairs.
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
            """

            self.zaid: types.Zaid = None
            self.fraction: float = None

        @classmethod
        def from_mcnp(cls, string: str):
            """
            ``from_mcnp`` generates ``MaterialValue`` objects from
            INP.

            ``from_mcnp`` constructs instances of ``MaterialValue`` from INP
            source strings, so it operates as a class constructor method and
            INP parser helper function.

            Parameters:
                source: INP for mateiral values.

            Returns:
                ``MaterialValue`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_PARAMETERS.
                MCNPSyntaxError: TOOFEW_DATUM_MATERIAL, TOOLONG_DATUM_MATERIAL.
            """

            entry = cls()

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL))

            # Parsing zaid
            value = types.Zaid().cast_mcnp_zaid(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.zaid = value

            # Parsing fraction
            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.fraction = value

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL)

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

            @classmethod
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

                keyword = cls()

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in cls]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD)

                return cls(source)

        def __init__(self):
            """
            ``__init__`` initializes ``MaterialOption``.
            """

            self.keyword: MaterialKeyword = None
            self.value: any = None

        def set_keyword(self, keyword: MaterialKeyword) -> None:
            """
            ``set_keyword`` stores INP material data card option
            keywords.

            ``set_keyword`` checks given arguments before assigning the
            given value to``MaterialOption.keyword``. If given an unrecognized
            argument, it raises semantic errors.

            Warnings:
                ``set_keyword`` reinitializes
                ``MaterialKeyword`` instances sincee its attributes depend on
                the keyword. When the given keyword does not equal
                ``MaterialOption.keyword``, all attributes reset.

            Parameters:
                keyword: Material specification data card option keyword.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD)

            self.keyword = keyword

            if keyword != self.keyword:
                match keyword:
                    case MaterialKeyword.GAS:
                        obj = MaterialOption.Gas()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.ESTEP:
                        obj = MaterialOption.Estep()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.HSTEP:
                        obj = MaterialOption.Hstep()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.NLIB:
                        obj = MaterialOption.Nlib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.PLIB:
                        obj = MaterialOption.Plib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.PNLIB:
                        obj = MaterialOption.Pnlib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.ELIB:
                        obj = MaterialOption.Elib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.HLIB:
                        obj = MaterialOption.Hlib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.ALIB:
                        obj = MaterialOption.Alib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.SLIB:
                        obj = MaterialOption.Slib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.TLIB:
                        obj = MaterialOption.Tlib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.DLIB:
                        obj = MaterialOption.Dlib()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.COND:
                        obj = MaterialOption.Cond()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__
                    case MaterialKeyword.REFI:
                        obj = MaterialOption.Refi()
                        self.__dict__ = obj.__dict__
                        self.__class__ = obj.__class__

        @classmethod
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

            parameter = cls()

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL))

            # Processing Keyword
            value = cls.EmbededGeometryKeyword.cast_keyword(tokens.peekl())
            parameter.set_keyword(value)

            # Processing Values
            match tokens.popl():
                case "gas":
                    value = types.cast_fortran_integer(tokens.popl())
                    parameter.set_value(value)

                case "estep" | "hstep" | "cond" | "refi":
                    value = types.cast_fortran_real(tokens.popl())
                    parameter.set_value(value)

                case "nlib" | "plib" | "pnlib" | "elib" | "hlib" | "alib" | "slib" | "tlib" | "dlib":
                    parameter.set_value(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL)

    class Gas(MaterialOption):
        """
        ``Gas`` represents INP Gas material data card options.

        ``Gas`` inherits attributes from ``MaterialOption``. It represents the
        INP Gas material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.state: int = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.state = value

    class Estep(MaterialOption):
        """
        ``Estep`` represents INP Estep material data card options.

        ``Estep`` inherits attributes from ``MaterialOption``. It represents the
        INP Estep material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.step: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.step = value

    class Hstep(MaterialOption):
        """
        ``Hstep`` represents INP Hstep material data card options.

        ``Hstep`` inherits attributes from ``MaterialOption``. It represents the
        INP Hstep material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.step: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.step = value

    class Nlib(MaterialOption):
        """
        ``Nlib`` represents INP Nlib material data card options.

        ``Nlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Nlib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.abx = value

    class Plib(MaterialOption):
        """
        ``Plib`` represents INP Plib material data card options.

        ``Plib`` inherits attributes from ``MaterialOption``. It represents the
        INP Plib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self._ = value

    class Pnlib(MaterialOption):
        """
        ``Pnlib`` represents INP Pnlib material data card options.

        ``Pnlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Pnlib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.abx = value

    class Elib(MaterialOption):
        """
        ``Elib`` represents INP Elib material data card options.

        ``Elib`` inherits attributes from ``MaterialOption``. It represents the
        INP Elib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: int) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.abx = value

    class Hlib(MaterialOption):
        """
        ``Hlib`` represents INP Hlib material data card options.

        ``Hlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Hlib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.abx = value

    class Alib(MaterialOption):
        """
        ``Alib`` represents INP Alib material data card options.

        ``Alib`` inherits attributes from ``MaterialOption``. It represents the
        INP Alib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.abx = value

    class Slib(MaterialOption):
        """
        ``Slib`` represents INP Slib material data card options.

        ``Slib`` inherits attributes from ``MaterialOption``. It represents the
        INP Slib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.abx = value

    class Tlib(MaterialOption):
        """
        ``Tlib`` represents INP Tlib material data card options.

        ``Tlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Tlib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.abx = value

    class Dlib(MaterialOption):
        """
        ``Dlib`` represents INP Dlib material data card options.

        ``Dlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Dlib material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.abx: str = None

        def set_value(self, value: str) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.abx = value

    class Cond(MaterialOption):
        """
        ``Cond`` represents INP Cond material data card options.

        ``Cond`` inherits attributes from ``MaterialOption``. It represents the
        INP Cond material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.conducation_state: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.conducation_state = value

    class Refi(MaterialOption):
        """
        ``Refi`` represents INP Refi material data card options.

        ``Refi`` inherits attributes from ``MaterialOption``. It represents the
        INP Refi material data card option syntax element.
        """

        def __init__(self):
            """
            ``__init__`` initializes ``Mat``.
            """

            super().__init__()

            self.constant_refracive_index: float = None

        def set_value(self, value: float) -> None:
            """
            ``set_value`` stores INP material data card option values.

            ``set_value`` checks given arguments before assigning the given
            value to ``MaterialOption.value``. If given an unrecognized
            arguments, it raises semantic errors.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.value = value
            self.constant_refracive_index = value

    def __init__(self):
        """
        ``__init__`` initializes ``Material``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.MATERIAL

        self.substances: tuple[MaterialValue] = None
        self.paris: tuple[MaterialOption] = None

    def set_parameters(self, substances: tuple[MaterialValue], pairs: tuple[MaterialOption]) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``Material.pairs``, ``Mateiral.substances``, and
        ``Material.parameters``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            substances: Iterable of substance specification.
            paris: Iterable of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in substances:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.substances = substances

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.paris = pairs

        self.parameters = tuple(list(substances) + list(pairs))


#    @classmethod
#    def from_formula(cls, formulas: dict[str, float]):
#        """
#        'from_formula'
#        """
#
#        material = cls()
#
#        elements = {}
#        for formula, fraction in formulas.items():
#            tokens = _parser.Parser(types.ELEMENTS_PATTERN.findall(formula), SyntaxError)
#
#            atoms = {}
#            while tokens:
#                # Checking first token is not numeric.
#                if tokens.peekl() not in types.ELEMENTS:
#                    raise SyntaxError
#
#                element = tokens.popl()
#
#                if not tokens or tokens.peekl() in types.ELEMENTS:
#                    # Adding symbol without subscript
#                    atoms[element] = 1
#                elif types.cast_fortran_integer(tokens.peekl()) is not None:
#                    # Adding symbol with subscript
#                    atoms[element] = types.cast_fortran_integer(tokens.popl())
#                else:
#                    raise SyntaxError
#
#            total = sum(atoms.values())
#
#            # Adding current forumla elements to dictionary.
#            for atom, count in atoms.items():
#                if atom not in elements:
#                    elements[atom] = fraction * (count / total)
#                else:
#                    elements[atom] += fraction * (count / total)
#
#        substances = []
#        for element, fraction in elements.items():
#            zaid = types.Zaid()
#            zaid.z = types.ELEMENTS[element]
#            zaid.a = 0
#
#            substance = cls.MaterialValue()
#            substance.zaid = zaid
#            substance.fraction = fraction
#
#            substances.append(substance)
#
#        material.set_parameters(tuple(substances), ())
#
#        return material


class MaterialNeutronScattering(Datum_Suffix):
    """
    ``MaterialNeutronScattering`` represents INP thermal neutron scattering
    data cards.

    ``MaterialNeutronScattering`` inherits attributes from ``Datum_Suffix``,
    i.e. ``Datum`` with suffix support. It represents the INP thermal neturon
    scattering data card syntax element.

    Attributes:
        identifiers: Iterable of material identifiers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``MaterialNeutronScattering``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.THERMAL_NETURON_SCATTERING

        self.identifiers: tuple[str] = None

    def set_parameters(self, *identifiers: str) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``MaterialNeutronScattering.identifiers`` and
        ``MaterialNeutronScattering.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *identifiers: Iterable of material identifiers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in identifiers:
            if parameter is None or not parmeter:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = identifiers
        self.identifiers = identifiers


class MaterialNuclideSubstitution(Datum_Suffix, Datum_Designator):
    """
    ``MaterialNuclideSubstitution`` represents INP material nuclide
    substitution data cards.

    ``MaterialNuclideSubstitution`` inherits attributes from ``Datum_Suffix``,
    i.e. ``Datum`` with suffix support, and ``Datum_Designator`` with
    designator support. It represents the INP material nuclide substitution
    data card syntax element.

    Attributes:
        Zaids: Iterable of ZAID alias.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``MaterialNuclideSubstitution``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.THERMAL_NETURON_SCATTERING

        self.zaids: tuple[types.Zaid] = None

    def set_parameters(self, *zaids: types.Zaid) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``MaterialNuclideSubstitution.zaids`` and
        ``MaterialNuclideSubstitution.parameters``. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            *zaids: Iterable of ZAID alias.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = zaids
        self.zaids = zaids


class OnTheFlyBroadening(Datum):
    """
    ``OnTheFlyBroadening`` represents INP on-the-fly broadening data cards.

    ``OnTheFlyBroadening`` inherits attributes from ``Datum``. It represents
    the INP on-the-fly boradening data card syntax element.

    Attributes:
        zaids: Iterable of ZAID alias.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``OnTheFlyBroadening``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.ONTHEFLY_BROADENING

        self.zaids: tuple[types.Zaid] = None

    def set_parameters(self, *zaids: types.Zaid) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``OnTheFlyBroadening.zaids`` and
        ``OnTheFlyBroadening.parameters``. If given an unrecognized argument,
        it raises semantic errors.

        Parameters:
            *zaids: Iterable of ZAID alias.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

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
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.TOTAL_FISSION

        self.has_no: bool = None

    def set_parameters(self, has_no: bool) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``TotalFission.has_no`` and ``TotalFission.parameters``. If
        given an unrecognized argument, it raises semantic errors.

        Parameters:
           has_no: No volume calculation option.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if has_no is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = tuple(has_no)
        self.states = has_no


class FissionTurnoff(Datum):
    """
    ``FissionTurnoff`` represents INP fission turnoff data cards.

    ``FissionTurnoff`` inherits attributes from ``Datum``. It represents
    the INP fission turnoff data card syntax element.

    Attributes:
        states: Iterable of fission turnoff settings.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``FissionTurnoff``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.FISSION_TURNOFF

        self.states: tuple[int] = None

    def set_parameters(self, *states: int) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``FissionTurnoff.states`` and ``FissionTurnoff.parameters``.
        If given an unrecognized argument, it raises semantic errors.

        Parameters:
            *states: Iterable of fission turnoff settings.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in states:
            if parameter is None or parameter not in {0, 1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = states
        self.states = states


class AtomicWeight(Datum):
    """
    ``AtomicWeight`` represents INP atomic weight data cards.

    ``AtomicWeight`` inherits attributes from ``Datum``. It represents
    the INP atomic weight data card syntax element.

    Attributes:
        weight_ratios: Iterable of weight ratios.
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

        def __init__(self):
            """
            ``__init__`` initializes ``AtomicWeightValue``.
            """

            self.zaid: types.Zaid = None
            self.ratio: float = None

        @classmethod
        def from_mcnp(cls, string: str):
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

            entry = cls()

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_WEIGHT))

            # Parsing zzzaaa
            value = types.Zaid().cast_mcnp_zaid(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.zaid = value

            # Parsing atomic weight
            value = types.cast_fortran_real(tokens.popl())
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.weight = value

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_WEIGHT)

    def __init__(self):
        """
        ``__init__`` initializes ``AtomicWeight``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.ATOMIC_WEIGHT

        self.weight_ratios: tuple[AtomicWeightValue] = None

    def set_parameters(self, *weight_ratios: AtomicWeightValue) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``AtomicWeight.weight_ratios`` and
        ``AtomicWeight.parameters``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            *weight_ratios: Iterable of weight ratios.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in weights:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = weight_ratios
        self.weight_ratios = weight_ratios


class CrossSectionFile(Datum_Suffix):
    """
    ``CrossSectionFile`` represents INP cross-section file data cards.

    ``CrossSectionFile`` inherits attributes from ``Datum_Suffix``, i.e.
    ``Datum`` with suffix support. It represents the INP cross-section file
    data card syntax element.

    Attributes:
        zaid: Cross-section file zaid.
        weight_ratio: Cross-section atomic weight ratio.
        entries: Iterable of file entries.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CrossSectionFile``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.CROSSSECTION_FILE

        self.zaid: types.Zaid = None
        self.weight_ratio: float = None

    def set_parameters(self, zaid: types.Zaid, weight_ratio: float, *entries: str) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``CrossSectionFile.zaid``, ``CrossSectionFile.weight_ratio``,
        ``CrossSectionFile.entries``, and ``CrossSectionFile.parameters``. If
        given an unrecognized argument, it raises semantic errors.

        Parameters:
            zaid: Cross-section file zaid.
            weight_ratio: Cross-section atomic weight ratio.
            *entries: Iterable of file entries.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if zaid is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.zaid = zaid

        if weight_ratio is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.weight_ratio = weight_ratio

        for parameter in entries:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.entries = entries
        self.parameters = tuple([zaid, weight_ratio] + list(entries))


class Void(Datum):
    """
    ``Void`` represents INP material void data cards.

    ``Void`` inherits attributes from ``Datum``. It represents the INP material
    void data card syntax element.

    Attributes:
        numbers: Iterable of cell numbers.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Void``.
        """

        super().__init__()
        self.mnemonic = Datum.DatumMnemonic.VOID

        self.numbers: tuple[int] = None

    def set_parameters(self, *numbers: float) -> None:
        """
        ``set_parameters`` stores INP data card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value to ``Void.numbers`` and ``Void.parameters``. If given an
        unrecognized argument, it raises semantic errors.

        Parameters:
            *numbers: Iterable of cell numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in numbers:
            if parameter is None or not (1 <= parameter <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.parameters = numbers
        self.numbers = numbers
