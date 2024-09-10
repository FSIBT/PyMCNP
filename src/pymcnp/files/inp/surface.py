"""
``surface`` contains the class representing INP surface cards.

``surface`` packages the ``Surface`` class, providing an object-oriented,
importable interface for INP surface cards.
"""


import numpy as np

import math
from typing import Callable
from enum import StrEnum

from . import card
from . import _cadquery
from ..utils import _parser
from ..utils import errors
from ..utils import types


class Surface(card.Card):
    """
    ``Surface`` represents INP cell cards.

    ``Surface`` implements INP cell cards as a Python class. Its attributes
    store INP surface card input parameters, and its methods provide entry
    points and endpoints for working with MCNP cells. It represents the INP
    surface card syntax element, and it inherits from the ``Card`` super class.

    Attributes:
        number: Surface card number.
        mnemonic: Surface card type identifier.
        transform: Surface card transformation number.
        periodic: Surface card periodic number.
        parameters: Surface parameter list based on mnemonic.
    """

    class SurfaceMnemonic(StrEnum):
        """
        ``SurfaceMnemonic`` represents INP surface card mnemonics

        ``SurfaceMnemonic`` implements INP surface card mnemonics as a Python
        inner class. It enumerates MCNP mnemonics and provides methods for
        casting strings to ``SurfaceMnemonic`` instances. It represents the INP
        surface card mnemonics syntax element, so ``Surface`` depends on
        ``SurfaceMnemonic`` as an enum.
        """

        PLANEGENERAL = "p"
        PLANENORMALX = "px"
        PLANENORMALY = "py"
        PLANENORMALZ = "pz"
        SPHEREORIGIN = "so"
        SPHEREGENERAL = "s"
        SPHERENORMALX = "sx"
        SPHERENORMALY = "sy"
        SPHERENORMALZ = "sz"
        CYLINDERPARALLELX = "c/x"
        CYLINDERPARALLELY = "c/y"
        CYLINDERPARALLELZ = "c/z"
        CYLINDERONX = "cx"
        CYLINDERONY = "cy"
        CYLINDERONZ = "cz"
        CONEPARALLELX = "k/x"
        CONEPARALLELY = "k/y"
        CONEPARALLELZ = "k/z"
        CONEONX = "kx"
        CONEONY = "ky"
        CONEONZ = "kx"
        QUADRATICSPECIAL = "sq"
        QUADRATICGENERAL = "gq"
        TORUSPARALLELX = "tx"
        TORUSPARALLELY = "ty"
        TORUSPARALLELZ = "tz"
        SURFACEX = "x"
        SURFACEY = "y"
        SURFACEZ = "z"
        BOX = "box"
        PARALLELEPIPED = "rpp"
        SPHERE = "sph"
        CYLINDERCIRCULAR = "rcc"
        HEXAGONALPRISM = "rhp"
        CYLINDERELLIPTICAL = "rec"
        CONETRUNCATED = "trc"
        ELLIPSOID = "ell"
        WEDGE = "wed"
        POLYHEDRON = "arb"

        @classmethod
        def from_mcnp(cls, source: str):
            """
            ``from_mcnp`` generates ``SurfaceMnemonic`` objects from INP.

            ``from_mcnp`` constructs instances of ``SurfaceMnemonic`` from INP
            source strings, so it operates as a class constructor method
            and INP parser helper function.

            Parameters:
                source: INP for surface card mnemonic.

            Returns:
                ``SurfaceMnemonic`` object.

            Raises:
                MCNPSemanticError: INVALID_SURFACE_MNEMONIC.
            """

            source = _parser.Preprocessor.process_inp(source)

            # Processing Mnemonic
            if source not in [enum.value for enum in cls]:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC)

            return cls(source)

    def __init__(self):
        """
        ``__init__`` initializes ``Surface``.
        """

        super().__init__()

        self.number: int = None
        self.mnemonic: str = None
        self.is_white_boundary: bool = False
        self.is_reflecting: bool = False
        self.transform: int = None
        self.periodic: int = None
        self.parameters: dict[str, float] = {}

    def set_number(self, number: int):
        """
        ``set_number`` stores INP surface card number.

        ``set_number`` checks given arguments before assigning the given value
        to ``Surface.number``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            number: Surface card number.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        self.number = number
        self.id = number

    def set_mnemonic(self, mnemonic: SurfaceMnemonic):
        """
        ``set_mnemonic`` stores INP surface card mnemonics.

        ``set_mnemonic`` checks given arguments before assigning the given
        value to ``Surface.mnemoinc``. If given an unrecognized argument, it
        raises semantic errors.

        Warnings:
            ``set_mnemonic`` reinitializes ``Surface`` instances since
            its attributes depend on the keyword. When the given keyword does
            not equal ``Surface.mnemonic``, all attributes reset.

        Parameters:
            mnemonic: Surface card mnemonic.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_MNEMONIC.
        """

        if mnemonic is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC)

        if mnemonic != self.mnemonic:
            is_white_boundary = self.is_white_boundary
            is_reflecting = self.is_reflecting
            transform = self.transform
            periodic = self.periodic
            number = self.number

            match mnemonic:
                case self.SurfaceMnemonic.PLANEGENERAL:
                    obj = PlaneGeneral()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.PLANENORMALX:
                    obj = PlaneNormalX()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.PLANENORMALY:
                    obj = PlaneNormalY()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.PLANENORMALZ:
                    obj = PlaneNormalZ()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SPHEREORIGIN:
                    obj = SphereOrigin()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SPHEREGENERAL:
                    obj = SphereGeneral()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SPHERENORMALX:
                    obj = SphereNormalX()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SPHERENORMALY:
                    obj = SphereNormalY()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SPHERENORMALZ:
                    obj = SphereNormalZ()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CYLINDERPARALLELX:
                    obj = CylinderParallelX()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CYLINDERPARALLELY:
                    obj = CylinderParallelY()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CYLINDERPARALLELZ:
                    obj = CylinderParallelZ()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CYLINDERONX:
                    obj = CylinderOnX()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CYLINDERONY:
                    obj = CylinderOnY()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CYLINDERONZ:
                    obj = CylinderOnZ()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CONEPARALLELX:
                    obj = ConeParallelX()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CONEPARALLELY:
                    obj = ConeParallelY()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CONEPARALLELZ:
                    obj = ConeParallelZ()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CONEONX:
                    obj = ConeOnX()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CONEONY:
                    obj = ConeOnY()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CONEONZ:
                    obj = ConeOnZ()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.QUADRATICSPECIAL:
                    obj = QuadraticSpecial()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.QUADRATICGENERAL:
                    obj = QuadraticGeneral()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.TORUSPARALLELX:
                    obj = TorusParallelX()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.TORUSPARALLELY:
                    obj = TorusParallelY()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.TORUSPARALLELZ:
                    obj = TorusParallelZ()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SURFACEX:
                    obj = SurfaceX()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SURFACEY:
                    obj = SurfaceY()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SURFACEZ:
                    obj = SurfaceZ()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.BOX:
                    obj = Box()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.PARALLELEPIPED:
                    obj = Parallelepiped()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.SPHERE:
                    obj = Sphere()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CYLINDERCIRCULAR:
                    obj = CylinderCircular()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.HEXAGONALPRISM:
                    obj = HexagonalPrism()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CYLINDERELLIPTICAL:
                    obj = CylinderElliptical()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.CONETRUNCATED:
                    obj = ConeTruncated()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.ELLIPSOID:
                    obj = Ellipsoid()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.WEDGE:
                    obj = Wedge()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__
                case self.SurfaceMnemonic.POLYHEDRON:
                    obj = Polyhedron()
                    self.__dict__ = obj.__dict__
                    self.__class__ = obj.__class__

            self.is_white_boundary = is_white_boundary
            self.is_reflecting = is_reflecting
            self.transform = transform
            self.periodic = periodic
            self.number = number

    def set_transform_periodic(self, transform_periodic: int):
        """
        ``set_transform_periodic`` stores INP surface card transform/periodic
        numbers.

        ``set_transform_periodic`` checks given arguments before assigning the
        given value to ``Surface.periodic`` and ``Surface.transform``. If given
        an unrecognized argument, it raises semantic errors.

        Parameters:
            transform_peridoic: Surface card transform/periodic number.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
        """

        if transform_periodic is None or not (-99_999_999 <= transform_periodic <= 999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC)

        if transform_periodic < 0:
            self.periodic = transform_periodic
            self.transform = None
        elif transform_periodic > 0:
            self.periodic = None
            self.transform = transform_periodic
        elif transform_periodic == 0:
            self.periodic = None
            self.transform = None
        else:
            assert False

    @classmethod
    def from_mcnp(cls, source: str, line: int = None):
        """
        ``from_mcnp`` generates ``Surface`` objects from INP.

        ``from_mcnp`` constructs instances of ``Surface`` from INP source
        strings, so it operates as a class constructor method and INP parser
        helper function.

        Parameters:
            source: INP for surface.
            line: Line number.

        Returns:
            ``Surface`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_SURFACE, TOOLONG_SURFACE.
        """

        surface = cls()

        # Processing Line Number
        surface.line = line

        # Processing Inline Comment
        if "$" in source:
            source, comment = source.split("$")
            surface.comment = comment

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE))

        # Processing Reflecting Prefix
        if tokens.peekl()[0] == "+":
            surface.is_white_boundary = True
            tokens.pushl(tokens.popl()[1:])
        elif tokens.peekl()[0] == "*":
            surface.is_reflecting_number = True
            tokens.pushl(tokens.popl()[1:])

        # Processing Card Number
        value = types.cast_fortran_integer(tokens.popl())
        surface.set_number(value)

        # Processing Transformation Number
        value = types.cast_fortran_integer(tokens.peekl())
        if value is not None:
            surface.set_transform_periodic(value)
            tokens.popl()

        # Processing Mnemonic
        value = cls.SurfaceMnemonic.from_mcnp(tokens.popl())
        surface.set_mnemonic(value)

        # Processing Parameters
        match surface.mnemonic:
            case "p":
                if len(tokens) not in {4, 9}:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                surface.__class__ = PlaneGeneral
                if len(tokens) == 4:
                    surface.set_parameters_equation(*tokens.deque)
                elif len(tokens) == 9:
                    surface.set_parameters_points(*tokens.deque)
                else:
                    assert False

            case "px":
                if len(tokens) > 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = PlaneNormalX
                surface.set_parameters(*tokens.deque)

            case "py":
                if len(tokens) > 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = PlaneNormalY
                surface.set_parameters(*tokens.deque)

            case "pz":
                if len(tokens) > 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = PlaneNormalZ
                surface.set_parameters(*tokens.deque)

            case "so":
                if len(tokens) > 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES).with_traceback(None) from None

                surface.__class__ = SphereOrigin
                surface.set_parameters(*tokens.deque)

            case "s":
                if len(tokens) > 4:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 4:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = SphereGeneral
                surface.set_parameters(*tokens.deque)

            case "sx":
                if len(tokens) > 2:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 2:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = SphereNormalX
                surface.set_parameters(*tokens.deque)

            case "sy":
                if len(tokens) > 2:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 2:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = SphereNormalY
                surface.set_parameters(*tokens.deque)

            case "sz":
                if len(tokens) > 2:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 2:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = SphereNormalZ
                surface.set_parameters(*tokens.deque)

            case "c/x":
                if len(tokens) > 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = CylinderParallelX
                surface.set_parameters(*tokens.deque)

            case "c/y":
                if len(tokens) > 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = CylinderParallelY
                surface.set_parameters(*tokens.deque)

            case "c/z":
                if len(tokens) > 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = CylinderParallelZ
                surface.set_parameters(*tokens.deque)

            case "cx":
                if len(tokens) > 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = CylinderOnX
                surface.set_parameters(*tokens.deque)

            case "cy":
                if len(tokens) > 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = CylinderOnY
                surface.set_parameters(*tokens.deque)

            case "cz":
                if len(tokens) > 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = CylinderOnZ
                surface.set_parameters(*tokens.deque)

            case "k/x":
                if len(tokens) > 5:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 5:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = ConeParallelX
                surface.set_parameters(*tokens.deque)

            case "k/y":
                if len(tokens) > 5:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 5:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = ConeParallelY
                surface.set_parameters(*tokens.deque)

            case "k/z":
                if len(tokens) > 5:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 5:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = ConeParallelZ
                surface.set_parameters(*tokens.deque)

            case "kx":
                if len(tokens) > 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = ConeOnX
                surface.set_parameters(*tokens.deque)

            case "ky":
                if len(tokens) > 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = ConeOnY
                surface.set_parameters(*tokens.deque)

            case "kx":
                if len(tokens) > 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 3:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = ConeOnZ
                surface.set_parameters(*tokens.deque)

            case "sq":
                if len(tokens) > 10:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 10:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = QuadraticSpecial
                surface.set_parameters(*tokens.deque)

            case "gq":
                if len(tokens) > 10:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 10:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = QuadraticGeneral
                surface.set_parameters(*tokens.deque)

            case "tx":
                if len(tokens) > 6:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 6:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = TorusParallelX
                surface.set_parameters(*tokens.deque)

            case "ty":
                if len(tokens) > 6:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 6:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = TorusParallelY
                surface.set_parameters(*tokens.deque)

            case "tz":
                if len(tokens) > 6:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 6:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = TorusParallelZ
                surface.set_parameters(*tokens.deque)

            case "x":
                if len(tokens) not in {2, 4, 6}:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                surface.__class__ = SurfaceX
                surface.set_parameters(*(list(tokens.deque) + [None] * (6 - len(tokens))))

            case "y":
                if len(tokens) not in {2, 4, 6}:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                surface.__class__ = SurfaceY
                surface.set_parameters(*(list(tokens.deque) + [None] * (6 - len(tokens))))

            case "z":
                if len(tokens) not in {2, 4, 6}:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                surface.__class__ = SurfaceZ
                surface.set_parameters(*(list(tokens.deque) + [None] * (6 - len(tokens))))

            case "box":
                if len(tokens) not in {12, 9}:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                surface.__class__ = Box
                surface.set_parameters(*(list(tokens.deque) + [None] * (12 - len(tokens))))

            case "rpp":
                if len(tokens) > 6:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 6:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = Parallelepiped
                surface.set_parameters(*tokens.deque)

            case "sph":
                if len(tokens) > 4:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 4:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = Sphere
                surface.set_parameters(*tokens.deque)

            case "rcc":
                if len(tokens) > 7:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 7:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = CylinderCircular
                surface.set_parameters(*tokens.deque)

            case "rhp" | "hex":
                if len(tokens) not in {15, 9}:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                surface.__class__ = HexagonalPrism
                surface.set_parameters(*(list(tokens.deque) + [None] * (15 - len(tokens))))

            case "rec":
                if len(tokens) not in {10, 12}:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                surface.__class__ = CylinderElliptical
                surface.set_parameters(*(list(tokens.deque) + [None] * (12 - len(tokens))))

            case "trc":
                if len(tokens) > 8:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 8:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = ConeTruncated
                surface.set_parameters(*tokens.deque)

            case "ell":
                if len(tokens) > 7:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 7:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = Ellipsoid
                surface.set_parameters(*tokens.deque)

            case "wed":
                if len(tokens) > 12:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 12:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = Wedge
                surface.set_parameters(*tokens.deque)

            case "arb":
                if len(tokens) > 30:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES)

                if len(tokens) < 30:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

                surface.__class__ = Polyhedron
                surface.set_parameters(*tokens.deque)

        return surface

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Surface`` objects.

        ``to_mcnp`` creates INP source string from ``Surface`` objects,
        so it provides an MCNP endpoint.

        Returns:
            INP string for ``Surface`` object.
        """

        parameters_str = " ".join([str(param) for _, param in self.parameters.items()])
        source = (
            f"{self.number}{' ' + {self.transform} + ' ' if self.transform is not None else ' '}"
            f"{self.mnemonic} {parameters_str}"
        )

        return _parser.Postprocessor.add_continuation_lines(source)

    def to_arguments(self) -> dict:
        """
        ``to_arguments`` makes dictionaries from ``Surface`` objects.

        ``to_arguments`` creates Python dictionaries from ``Surface`` objects,
        so it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual.

        Returns:
            Dictionary for ``Surface`` object.
        """

        return {
            "j": self.number,
            "n": self.transform,
            "A": self.mnemonic,
            "list": self.parameters,
        }


class PlaneGeneral(Surface):
    """
    ``PlaneGeneral`` represents INP general planes surface cards.

    ``PlaneGeneral`` inherits attributes from ``Surface``. It represents the
    INP general planes surface card syntax element.

    Attributes:
        a: Equation-defined general plane A coefficent.
        b: Equation-defined general plane B coefficent.
        c: Equation-defined general plane C coefficent.
        d: Equation-defined general plane D coefficent.
        x1: Point-defined general plane point #1 x component.
        y1: Point-defined general plane point #1 y component.
        z1: Point-defined general plane point #1 z component.
        x2: Point-defined general plane point #2 x component.
        y2: Point-defined general plane point #2 y component.
        z2: Point-defined general plane point #2 z component.
        x3: Point-defined general plane point #3 x component.
        y3: Point-defined general plane point #3 y component.
        z3: Point-defined general plane point #3 z component.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``PlaneGeneral``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.PLANEGENERAL

        self.a: float = None
        self.b: float = None
        self.c: float = None
        self.d: float = None
        self.x1: float = None
        self.y1: float = None
        self.z1: float = None
        self.x2: float = None
        self.y2: float = None
        self.z2: float = None
        self.x3: float = None
        self.y3: float = None
        self.z3: float = None

    def set_parameters_equation(self, a: float, b: float, c: float, d: float) -> None:
        """
        ``set_parameters_equation`` stores INP equation-defined general plane
        surface card parameters.

        ``set_parameters_equation`` checks given arguments before assigning the
        given values. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            a: Equation-defined general plane A coefficent.
            b: Equation-defined general plane B coefficent.
            c: Equation-defined general plane C coefficent.
            d: Equation-defined general plane D coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMAETER.
        """

        value = types.cast_fortran_real(a)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a = value
        self.parameters["a"] = value

        value = types.cast_fortran_real(b)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.b = value
        self.parameters["b"] = value

        value = types.cast_fortran_real(c)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.c = value
        self.parameters["c"] = value

        value = types.cast_fortran_real(d)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d = value
        self.parameters["d"] = value

        # Resetting point-defined parameters.
        self.x1 = None
        self.y1 = None
        self.z1 = None
        self.x2 = None
        self.y2 = None
        self.z2 = None
        self.x3 = None
        self.y3 = None
        self.z3 = None

    def set_parameters_points(
        self,
        x1: float,
        y1: float,
        z1: float,
        x2: float,
        y2: float,
        z2: float,
        x3: float,
        y3: float,
        z3: float,
    ) -> None:
        """
        ``set_parameters_points`` stores INP point-defined general plane
        surface card parameters.

        ``set_parameters_points`` checks given arguments before assigning the
        given values. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            x1: Point-defined general plane point #1 x component.
            y1: Point-defined general plane point #1 y component.
            z1: Point-defined general plane point #1 z component.
            x2: Point-defined general plane point #2 x component.
            y2: Point-defined general plane point #2 y component.
            z2: Point-defined general plane point #2 z component.
            x3: Point-defined general plane point #3 x component.
            y3: Point-defined general plane point #3 y component.
            z3: Point-defined general plane point #3 z component.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMAETER.
        """

        value = types.cast_fortran_real(x1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x1 = value
        self.parameters["x1"] = value

        value = types.cast_fortran_real(y1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y1 = value
        self.parameters["y1"] = value

        value = types.cast_fortran_real(z1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z1 = value
        self.parameters["z1"] = value

        value = types.cast_fortran_real(x2)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x2 = value
        self.parameters["x2"] = value

        value = types.cast_fortran_real(y2)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y2 = value
        self.parameters["y2"] = value

        value = types.cast_fortran_real(z2)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z2 = value
        self.parameters["z2"] = value

        value = types.cast_fortran_real(x3)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x3 = value
        self.parameters["x3"] = value

        value = types.cast_fortran_real(y3)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y3 = value
        self.parameters["y3"] = value

        value = types.cast_fortran_real(z3)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z3 = value
        self.parameters["z3"] = value

        # Resetting equation-defined parameters.
        self.a = None
        self.b = None
        self.c = None
        self.d = None


class PlaneNormalX(Surface):
    """
    ``PlaneNormalX`` represents INP normal-to-the-x-axis surface cards.

    ``PlaneGeneral`` inherits attributes from ``Surface``. It represents the
    INP normal-to-the-x-axis surface card syntax element.

    Attributes:
        d: Normal-to-the-x-axis plane D coefficent.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``PlaneNormalX``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.PLANENORMALX

        self.d: float = None

    def set_parameters(self, d: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            d: Normal-to-the-x-axis plane D coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(d)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d = value
        self.parameters["d"] = value


class PlaneNormalY(Surface):
    """
    ``PlaneNormalX`` represents INP normal-to-the-y-axis surface cards.

    ``PlaneGeneral`` inherits attributes from ``Surface``. It represents the
    INP normal-to-the-y-axis surface card syntax element.

    Attributes:
        d: Normal-to-the-y-axis plane D coefficent.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``PlaneNormalY``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.PLANENORMALY

        self.d: float = None

    def set_parameters(self, d: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            d: Normal-to-the-y-axis plane D coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(d)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d = value
        self.parameters["d"] = value


class PlaneNormalZ(Surface):
    """
    ``PlaneNormalX`` represents INP normal-to-the-z-axis surface cards.

    ``PlaneGeneral`` inherits attributes from ``Surface``. It represents the
    INP normal-to-the-z-axis surface card syntax element.

    Attributes:
        d: Normal-to-the-z-axis plane D coefficent.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``PlaneNormalZ``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.PLANENORMALZ

        self.d: float = None

    def set_parameters(self, d: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(d)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d = value
        self.parameters["d"] = value


class SphereOrigin(Surface):
    """
    ``SphereOrigin`` represents INP origin-centered sphere surface cards.

    ``SphereOrigin`` inherits attributes from ``Surface``. It represents the
    INP origin-centered sphere surface card syntax element.

    Attributes:
        r: Origin-centered sphere radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``SphereOrigin``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SPHEREORIGIN

        self.r: float = None

    def set_parameters(self, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            r: Origin-centered sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_sphere(self.r)

        return cadquery + "\n"


class SphereGeneral(Surface):
    """
    ``SphereGeneral`` represents INP general sphere surface cards.

    ``SphereGeneral`` inherits attributes from ``Surface``. It represents the
    INP general sphere surface card syntax element.

    Attributes:
        x: General sphere center x component.
        y: General sphere center y component.
        z: General sphere center z component.
        r: General sphere radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``SphereGeneral``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SPHEREGENERAL

        self.x: float = None
        self.y: float = None
        self.z: float = None
        self.r: float = None

    def set_parameters(self, x: float, y: float, z: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: General sphere center x component.
            y: General sphere center y component.
            z: General sphere center z component.
            r: General sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_sphere(self.r)
        cadquery += _cadquery.add_translation(self.x, self.y, self.z)

        return cadquery + "\n"


class SphereNormalX(Surface):
    """
    ``SphereNormalX`` represents INP on-x-axis sphere surface cards.

    ``SphereNormalX`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis sphere surface card syntax element.

    Attributes:
        x: On-x-axis sphere center x component.
        r: On-x-axis sphere radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``SphereNormalX``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SPHERENORMALX

        self.x: float = None
        self.r: float = None

    def set_parameters(self, x: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: On-x-axis sphere center x component.
            r: On-x-axis sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_sphere(self.r)
        cadquery += _cadquery.add_translation(self.x, 0, 0)

        return cadquery


class SphereNormalY(Surface):
    """
    ``SphereNormalY`` represents INP on-y-axis sphere surface cards.

    ``SphereNormalY`` inherits attributes from ``Surface``. It represents the
    INP on-y-axis sphere surface card syntax element.

    Attributes:
        y: On-y-axis sphere center y component.
        r: On-y-axis sphere radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``SphereNormalY``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SPHERENORMALY

        self.y: float = None
        self.r: float = None

    def set_parameters(self, y: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            y: On-y-axis sphere center y component.
            r: On-y-axis sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_sphere(self.r)
        cadquery += _cadquery.add_translation(0, self.y, 0)

        return cadquery


class SphereNormalZ(Surface):
    """
    ``SphereNormalZ`` represents INP on-z-axis sphere surface cards.

    ``SphereNormalZ`` inherits attributes from ``Surface``. It represents the
    INP on-z-axis sphere surface card syntax element.

    Attributes:
        z: On-z-axis sphere center z component.
        r: On-z-axis sphere radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``SphereNormalZ``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SPHERENORMALZ

        self.z: float = None
        self.r: float = None

    def set_parameters(self, z: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            z: On-z-axis sphere center z component.
            r: On-z-axis sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_sphere(self.r)
        cadquery += _cadquery.add_translation(0, 0, self.z)

        return cadquery


class CylinderParallelX(Surface):
    """
    ``CylinderParallelX`` represents INP parallel-to-x-axis cylinder surface
    cards.

    ``CylinderParallelX`` inherits attributes from ``Surface``. It represents
    the INP parallel-to-x-axis cylinder surface card syntax element.

    Attributes:
        y: Parallel-to-x-axis cylinder center y component.
        z: Parallel-to-x-axis cylinder center z component.
        r: Parallel-to-x-axis cylinder radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CylinderParallelX``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CYLINDERPARALLELX

        self.y: float = None
        self.z: float = None
        self.r: float = None

    def set_parameters(self, y: float, z: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            y: Parallel-to-x-axis cylinder center y component.
            z: Parallel-to-x-axis cylinder center z component.
            r: Parallel-to-x-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value


class CylinderParallelY(Surface):
    """
    ``CylinderParallelY`` represents INP parallel-to-y-axis cylinder surface
    cards.

    ``CylinderParallelY`` inherits attributes from ``Surface``. It represents
    the INP parallel-to-y-axis cylinder surface card syntax element.

    Attributes:
        x: Parallel-to-y-axis cylinder center x component.
        z: Parallel-to-y-axis cylinder center z component.
        r: Parallel-to-y-axis cylinder radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CylinderParallelY``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CYLINDERPARALLELY

        self.x: float = None
        self.z: float = None
        self.r: float = None

    def set_parameters(self, x: float, z: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-y-axis cylinder center x component.
            z: Parallel-to-y-axis cylinder center z component.
            r: Parallel-to-y-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value


class CylinderParallelZ(Surface):
    """
    ``CylinderParallelZ`` represents INP parallel-to-z-axis cylinder surface
    cards.

    ``CylinderParallelZ`` inherits attributes from ``Surface``. It represents
    the INP parallel-to-z-axis cylinder surface card syntax element.

    Attributes:
        x: Parallel-to-z-axis cylinder center x component.
        y: Parallel-to-z-axis cylinder center y component.
        r: Parallel-to-z-axis cylinder radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CylinderParallelZ``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CYLINDERPARALLELZ

        self.x: float = None
        self.y: float = None
        self.r: float = None

    def set_parameters(self, x: float, y: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-z-axis cylinder center x component.
            y: Parallel-to-z-axis cylinder center y component.
            r: Parallel-to-z-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value


class CylinderOnX(Surface):
    """
    ``CylinderOnX`` represents INP on-x-axis cylinder surface cards.

    ``CylinderOnX`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis surface card syntax element.

    Attributes:
        r: On-x-axis cylinder radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CylinderOnX``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CYLINDERONX

        self.r: float = None

    def set_parameters(self, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            r: On-x-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value


class CylinderOnY(Surface):
    """
    ``CylinderOnY`` represents INP on-y-axis cylinder surface cards.

    ``CylinderOnY`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis surface card syntax element.

    Attributes:
        r: On-y-axis cylinder radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CylinderOnY``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CYLINDERONY

        self.r: float = None

    def set_parameters(self, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            r: On-y-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value


class CylinderOnZ(Surface):
    """
    ``CylinderOnZ`` represents INP on-z-axis cylinder surface cards.

    ``CylinderOnZ`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis surface card syntax element.

    Attributes:
        r: On-z-axis cylinder radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CylinderOnZ``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CYLINDERONZ

        self.r: float = None

    def set_parameters(self, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            r: On-z-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value


class ConeParallelX(Surface):
    """
    ``ConeParallelX`` represents INP parallel-to-x-axis cone surface cards.

    ``ConeParallelX`` inherits attributes from ``Surface``. It represents the
    INP parallel-to-x-axis cone surface card syntax element.

    Attributes:
        x: Parallel-to-x-axis cone center x component.
        y: Parallel-to-x-axis cone center y component.
        z: Parallel-to-x-axis cone center z component.
        t_squared: Parallel-to-x-axis cone t^2 coefficent.
        plusminus_1: Parallel-to-x-axis cone sheet selector.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``ConeParallelX``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CONEPARALLELX

        self.x: float = None
        self.y: float = None
        self.z: float = None
        self.t_squared: float = None
        self.plusminus_1: float = None

    def set_parameters(self, x: float, y: float, z: float, t_squared: float, plusminus_1: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-x-axis cone center x component.
            y: Parallel-to-x-axis cone center y component.
            z: Parallel-to-x-axis cone center z component.
            t_squared: Parallel-to-x-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-x-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(t_squared)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.t_squared = value
        self.parameters["t_squared"] = value

        value = types.cast_fortran_real(plusminus_1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.plusminus_1 = value
        self.parameters["plusminus_1"] = value


class ConeParallelY(Surface):
    """
    ``ConeParallelY`` represents INP parallel-to-y-axis cone surface cards.

    ``ConeParallelY`` inherits attributes from ``Surface``. It represents the
    INP parallel-to-y-axis cone surface card syntax element.

    Attributes:
        x: Parallel-to-y-axis cone center x component.
        y: Parallel-to-y-axis cone center y component.
        z: Parallel-to-y-axis cone center z component.
        t_squared: Parallel-to-y-axis cone t^2 coefficent.
        plusminus_1: Parallel-to-y-axis cone sheet selector.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``ConeParallelY``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CONEPARALLELY

        self.x: float = None
        self.y: float = None
        self.z: float = None
        self.t_squared: float = None
        self.plusminus_1: float = None

    def set_parameters(self, x: float, y: float, z: float, t_squared: float, plusminus_1: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-y-axis cone center x component.
            y: Parallel-to-y-axis cone center y component.
            z: Parallel-to-y-axis cone center z component.
            t_squared: Parallel-to-y-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-y-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(t_squared)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.t_squared = value
        self.parameters["t_squared"] = value

        value = types.cast_fortran_real(plusminus_1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.plusminus_1 = value
        self.parameters["plusminus_1"] = value


class ConeParallelZ(Surface):
    """
    ``ConeParallelZ`` represents INP parallel-to-z-axis cone surface cards.

    ``ConeParallelZ`` inherits attributes from ``Surface``. It represents the
    INP parallel-to-z-axis cone surface card syntax element.

    Attributes:
        x: Parallel-to-z-axis cone center x component.
        y: Parallel-to-z-axis cone center y component.
        z: Parallel-to-z-axis cone center z component.
        t_squared: Parallel-to-z-axis cone t^2 coefficent.
        plusminus_1: Parallel-to-z-axis cone sheet selector.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``ConeParallelZ``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CONEPARALLELZ

        self.x: float = None
        self.y: float = None
        self.z: float = None
        self.t_squared: float = None
        self.plusminus_1: float = None

    def set_parameters(self, x: float, y: float, z: float, t_squared: float, plusminus_1: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-z-axis cone center x component.
            y: Parallel-to-z-axis cone center y component.
            z: Parallel-to-z-axis cone center z component.
            t_squared: Parallel-to-z-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-z-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(t_squared)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.t_squared = value
        self.parameters["t_squared"] = value

        value = types.cast_fortran_real(plusminus_1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.plusminus_1 = value
        self.parameters["plusminus_1"] = value


class ConeOnX(Surface):
    """
    ``ConeOnX`` represents INP on-x-axis cone surface cards.

    ``ConeOnX`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis cone surface card syntax element.

    Attributes:
        x: On-x-axis cone center x component.
        t_squared: On-x-axis cone t^2 coefficent.
        plusminus_1: On-x-axis cone sheet selector.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``ConeOnX``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CONEONX

        self.x: float = None
        self.t_squared: float = None
        self.plusminus_1: float = None

    def set_parameters(self, x: float, t_squared: float, plusminus_1: float) -> None:
        """
        'set_parameters' sets cones on x-axis parameters.

        'set_parameters' checks parameter entries are valid
        floating points. It raises errors if given None.

        Parameters:
            x: On-x-axis cone center x component.
            t_squared: On-x-axis cone t^2 coefficent.
            plusminus_1: On-x-axis cone sheet selector.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(t_squared)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.t_squared = value
        self.parameters["t_squared"] = value

        value = types.cast_fortran_real(plusminus_1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.plusminus_1 = value
        self.parameters["plusminus_1"] = value


class ConeOnY(Surface):
    """
    ``ConeOnY`` represents INP on-y-axis cone surface cards.

    ``ConeOnY`` inherits attributes from ``Surface``. It represents the
    INP on-y-axis cone surface card syntax element.

    Attributes:
        y: On-y-axis cone center y component.
        t_squared: On-y-axis cone t^2 coefficent.
        plusminus_1: On-y-axis cone sheet selector.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``ConeOnY``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CONEONY

        self.y: float = None
        self.t_squared: float = None
        self.plusminus_1: float = None

    def set_parameters(self, y: float, t_squared: float, plusminus_1: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            y: On-y-axis cone center y component.
            t_squared: On-y-axis cone t^2 coefficent.
            plusminus_1: On-y-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(t_squared)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.t_squared = value
        self.parameters["t_squared"] = value

        value = types.cast_fortran_real(plusminus_1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.plusminus_1 = value
        self.parameters["plusminus_1"] = value


class ConeOnZ(Surface):
    """
    ``ConeOnZ`` represents INP on-z-axis cone surface cards.

    ``ConeOnZ`` inherits attributes from ``Surface``. It represents the
    INP on-z-axis cone surface card syntax element.

    Attributes:
        z: On-z-axis cone center z component.
        t_squared: On-z-axis cone t^2 coefficent.
        plusminus_1: On-z-axis cone sheet selector.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``ConeOnZ``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CONEONZ

        self.z: float = None
        self.t_squared: float = None
        self.plusminus_1: float = None

    def set_parameters(self, z: float, t_squared: float, plusminus_1: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            z: On-z-axis cone center z component.
            t_squared: On-z-axis cone t^2 coefficent.
            plusminus_1: On-z-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(t_squared)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.t_squared = value
        self.parameters["t_squared"] = value

        value = types.cast_fortran_real(plusminus_1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.plusminus_1 = value
        self.parameters["plusminus_1"] = value


class QuadraticSpecial(Surface):
    """
    ``QuadraticSpecial`` represents INP oblique special quadratic surface cards.

    ``QuadraticSpecial`` inherits attributes from ``Surface``. It represents the
    INP oblique special quadratic surface card syntax element.

    Attributes:
        a: Oblique special quadratic A coefficent.
        b: Oblique special quadratic B coefficent.
        c: Oblique special quadratic C coefficent.
        d: Oblique special quadratic D coefficent.
        e: Oblique special quadratic E coefficent.
        f: Oblique special quadratic F coefficent.
        g: Oblique special quadratic G coefficent.
        x: Oblique special quadratic center x component.
        y: Oblique special quadratic center y component.
        z: Oblique special quadratic center z component.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``QuadraticSpecial``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.QUADRATICSPECIAL

        self.a: float = None
        self.b: float = None
        self.c: float = None
        self.d: float = None
        self.e: float = None
        self.f: float = None
        self.g: float = None
        self.x: float = None
        self.y: float = None
        self.z: float = None

    def set_parameters(
        self, a: float, b: float, c: float, d: float, e: float, f: float, g: float, x: float, y: float, z: float
    ) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            a: Oblique special quadratic A coefficent.
            b: Oblique special quadratic B coefficent.
            c: Oblique special quadratic C coefficent.
            d: Oblique special quadratic D coefficent.
            e: Oblique special quadratic E coefficent.
            f: Oblique special quadratic F coefficent.
            g: Oblique special quadratic G coefficent.
            x: Oblique special quadratic center x component.
            y: Oblique special quadratic center y component.
            z: Oblique special quadratic center z component.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(a)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a = value
        self.parameters["a"] = value

        value = types.cast_fortran_real(b)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.b = value
        self.parameters["b"] = value

        value = types.cast_fortran_real(c)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.c = value
        self.parameters["c"] = value

        value = types.cast_fortran_real(d)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d = value
        self.parameters["d"] = value

        value = types.cast_fortran_real(e)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.e = value
        self.parameters["e"] = value

        value = types.cast_fortran_real(f)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.f = value
        self.parameters["f"] = value

        value = types.cast_fortran_real(g)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.g = value
        self.parameters["g"] = value

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value


class QuadraticGeneral(Surface):
    """
    ``QuadraticGeneral`` represents INP parrallel-to-axis general quadratic
    surface cards.

    ``QuadraticGeneral`` inherits attributes from ``Surface``. It represents
    the INP parrallel-to-axis general quadratic surface card syntax element.

    Attributes:
        a: Oblique special quadratic A coefficent.
        b: Oblique special quadratic B coefficent.
        c: Oblique special quadratic C coefficent.
        d: Oblique special quadratic D coefficent.
        e: Oblique special quadratic E coefficent.
        f: Oblique special quadratic F coefficent.
        g: Oblique special quadratic G coefficent.
        h: Oblique special quadratic H coefficent.
        j: Oblique special quadratic J coefficent.
        k: Oblique special quadratic K coefficent.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``QuadraticGeneral``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.QUADRATICGENERAL

        self.a: float = None
        self.b: float = None
        self.c: float = None
        self.d: float = None
        self.e: float = None
        self.f: float = None
        self.g: float = None
        self.h: float = None
        self.j: float = None
        self.k: float = None

    def set_parameters(
        self, a: float, b: float, c: float, d: float, e: float, f: float, g: float, h: float, j: float, k: float
    ) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            a: Oblique special quadratic A coefficent.
            b: Oblique special quadratic B coefficent.
            c: Oblique special quadratic C coefficent.
            d: Oblique special quadratic D coefficent.
            e: Oblique special quadratic E coefficent.
            f: Oblique special quadratic F coefficent.
            g: Oblique special quadratic G coefficent.
            h: Oblique special quadratic H coefficent.
            j: Oblique special quadratic J coefficent.
            k: Oblique special quadratic K coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(a)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a = value
        self.parameters["a"] = value

        value = types.cast_fortran_real(b)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.b = value
        self.parameters["b"] = value

        value = types.cast_fortran_real(c)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.c = value
        self.parameters["c"] = value

        value = types.cast_fortran_real(d)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d = value
        self.parameters["d"] = value

        value = types.cast_fortran_real(e)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.e = value
        self.parameters["e"] = value

        value = types.cast_fortran_real(f)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.f = value
        self.parameters["f"] = value

        value = types.cast_fortran_real(g)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.g = value
        self.parameters["g"] = value

        value = types.cast_fortran_real(h)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.h = value
        self.parameters["h"] = value

        value = types.cast_fortran_real(j)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.j = value
        self.parameters["j"] = value

        value = types.cast_fortran_real(k)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.k = value
        self.parameters["k"] = value


class TorusParallelX(Surface):
    """
    ``TorusParallelX`` represents INP parallel-to-x-axis tori surface cards.

    ``TorusParallelX`` inherits attributes from ``Surface``. It represents the
    INP parallel-to-x-axis tori surface card syntax element.

    Attributes:
        x: Parallel-to-x-axis tori center x component.
        y: Parallel-to-x-axis tori center y component.
        z: Parallel-to-x-axis tori center z component.
        a: Parallel-to-x-axis tori A coefficent.
        b: Parallel-to-x-axis tori B coefficent.
        c: Parallel-to-x-axis tori C coefficent.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``TorusParallelX``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.TORUSPARALLELX

        self.x: float = None
        self.y: float = None
        self.z: float = None
        self.a: float = None
        self.b: float = None
        self.c: float = None

    def set_parameters(self, x: float, y: float, z: float, a: float, b: float, c: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-x-axis tori center x component.
            y: Parallel-to-x-axis tori center y component.
            z: Parallel-to-x-axis tori center z component.
            a: Parallel-to-x-axis tori A coefficent.
            b: Parallel-to-x-axis tori B coefficent.
            c: Parallel-to-x-axis tori C coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(a)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a = value
        self.parameters["a"] = value

        value = types.cast_fortran_real(b)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.b = value
        self.parameters["b"] = value

        value = types.cast_fortran_real(c)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.c = value
        self.parameters["c"] = value


class TorusParallelY(Surface):
    """
    ``TorusParallelY`` represents INP parallel-to-y-axis tori surface cards.

    ``TorusParallelY`` inherits attributes from ``Surface``. It represents the
    INP parallel-to-y-axis tori surface card syntax element.

    Attributes:
        x: Parallel-to-y-axis tori center x component.
        y: Parallel-to-y-axis tori center y component.
        z: Parallel-to-y-axis tori center z component.
        a: Parallel-to-y-axis tori A coefficent.
        b: Parallel-to-y-axis tori B coefficent.
        c: Parallel-to-y-axis tori C coefficent.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``TorusParallelY``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.TORUSPARALLELY

        self.x: float = None
        self.y: float = None
        self.z: float = None
        self.a: float = None
        self.b: float = None
        self.c: float = None

    def set_parameters(self, x: float, y: float, z: float, a: float, b: float, c: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-y-axis tori center x component.
            y: Parallel-to-y-axis tori center y component.
            z: Parallel-to-y-axis tori center z component.
            a: Parallel-to-y-axis tori A coefficent.
            b: Parallel-to-y-axis tori B coefficent.
            c: Parallel-to-y-axis tori C coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(a)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a = value
        self.parameters["a"] = value

        value = types.cast_fortran_real(b)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.b = value
        self.parameters["b"] = value

        value = types.cast_fortran_real(c)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.c = value
        self.parameters["c"] = value


class TorusParallelZ(Surface):
    """
    ``TorusParallelZ`` represents INP parallel-to-z-axis tori surface cards.

    ``TorusParallelZ`` inherits attributes from ``Surface``. It represents the
    INP parallel-to-z-axis tori surface card syntax element.

    Attributes:
        x: Parallel-to-z-axis tori center x component.
        y: Parallel-to-z-axis tori center y component.
        z: Parallel-to-z-axis tori center z component.
        a: Parallel-to-z-axis tori A coefficent.
        b: Parallel-to-z-axis tori B coefficent.
        c: Parallel-to-z-axis tori C coefficent.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``TorusParallelZ``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.TORUSPARALLELZ

        self.x: float = None
        self.y: float = None
        self.z: float = None
        self.a: float = None
        self.b: float = None
        self.c: float = None

    def set_parameters(self, x: float, y: float, z: float, a: float, b: float, c: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-z-axis tori center x component.
            y: Parallel-to-z-axis tori center y component.
            z: Parallel-to-z-axis tori center z component.
            a: Parallel-to-z-axis tori A coefficent.
            b: Parallel-to-z-axis tori B coefficent.
            c: Parallel-to-z-axis tori C coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x = value
        self.parameters["x"] = value

        value = types.cast_fortran_real(y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y = value
        self.parameters["y"] = value

        value = types.cast_fortran_real(z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z = value
        self.parameters["z"] = value

        value = types.cast_fortran_real(a)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a = value
        self.parameters["a"] = value

        value = types.cast_fortran_real(b)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.b = value
        self.parameters["b"] = value

        value = types.cast_fortran_real(c)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.c = value
        self.parameters["c"] = value


class SurfaceX(Surface):
    """
    ``SurfaceX`` represents INP x-axisymmetric point-defined surface cards.

    ``SurfaceX`` inherits attributes from ``Surface``. It represents the
    INP x-axisymmetric point-defined surface card syntax element.

    Attributes:
        x1: X-axisymmetric point-defined surface point #1 x component.
        r1: X-axisymmetric point-defined surface point #1 radius.
        x2: X-axisymmetric point-defined surface point #2 x component.
        r2: X-axisymmetric point-defined surface point #2 radius.
        x3: X-axisymmetric point-defined surface point #3 x component.
        r3: X-axisymmetric point-defined surface point #3 radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``SurfaceX``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SURFACEX

        self.x1: float = None
        self.r1: float = None
        self.x2: float = None
        self.r2: float = None
        self.x3: float = None
        self.r3: float = None

    def set_parameters(self, x1: float, r1: float, x2: float, r2: float, x3: float, r3: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            x1: X-axisymmetric point-defined surface point #1 x component.
            r1: X-axisymmetric point-defined surface point #1 radius.
            x2: X-axisymmetric point-defined surface point #2 x component.
            r2: X-axisymmetric point-defined surface point #2 radius.
            x3: X-axisymmetric point-defined surface point #3 x component.
            r3: X-axisymmetric point-defined surface point #3 radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(x1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x1 = value
        self.parameters["x1"] = value

        value = types.cast_fortran_real(r1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r1 = value
        self.parameters["r1"] = value

        if x2 is not None and r2 is not None:
            value = types.cast_fortran_real(x2)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.x2 = value
            self.parameters["x2"] = value

            value = types.cast_fortran_real(r2)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.r2 = value
            self.parameters["r2"] = value

            if x3 is not None and r3 is not None:
                value = types.cast_fortran_real(x3)
                if value is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

                self.x3 = value
                self.parameters["x3"] = value

                value = types.cast_fortran_real(r3)
                if value is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

                self.r3 = value
                self.parameters["r3"] = value


class SurfaceY(Surface):
    """
    ``SurfaceY`` represents INP y-axisymmetric point-defined surface cards.

    ``SurfaceY`` inherits attributes from ``Surface``. It represents the
    INP y-axisymmetric point-defined surface card syntax element.

    Attributes:
        y1: Y-axisymmetric point-defined surface point #1 y component.
        r1: Y-axisymmetric point-defined surface point #1 radius.
        y2: Y-axisymmetric point-defined surface point #2 y component.
        r2: Y-axisymmetric point-defined surface point #2 radius.
        y3: Y-axisymmetric point-defined surface point #3 y component.
        r3: Y-axisymmetric point-defined surface point #3 radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``SurfaceY``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SURFACEY

        self.y1: float = None
        self.r1: float = None
        self.y2: float = None
        self.r2: float = None
        self.y3: float = None
        self.r3: float = None

    def set_parameters(self, y1: float, r1: float, y2: float, r2: float, y3: float, r3: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            y1: Y-axisymmetric point-defined surface point #1 y component.
            r1: Y-axisymmetric point-defined surface point #1 radius.
            y2: Y-axisymmetric point-defined surface point #2 y component.
            r2: Y-axisymmetric point-defined surface point #2 radius.
            y3: Y-axisymmetric point-defined surface point #3 y component.
            r3: Y-axisymmetric point-defined surface point #3 radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(y1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y1 = value
        self.parameters["y1"] = value

        value = types.cast_fortran_real(r1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r1 = value
        self.parameters["r1"] = value

        if y2 is not None and r2 is not None:
            value = types.cast_fortran_real(y2)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.y2 = value
            self.parameters["y2"] = value

            value = types.cast_fortran_real(r2)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.r2 = value
            self.parameters["r2"] = value

            if y3 is not None and r3 is not None:
                value = types.cast_fortran_real(y3)
                if value is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

                self.y3 = value
                self.parameters["y3"] = value

                value = types.cast_fortran_real(r3)
                if value is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

                self.r3 = value
                self.parameters["r3"] = value


class SurfaceZ(Surface):
    """
    ``SurfaceZ`` represents INP z-axisymmetric point-defined surface cards.

    ``SurfaceZ`` inherits attributes from ``Surface``. It represents the
    INP z-axisymmetric point-defined surface card syntax element.

    Attributes:
        z1: Z-axisymmetric point-defined surface point #1 z component.
        r1: Z-axisymmetric point-defined surface point #1 radius.
        z2: Z-axisymmetric point-defined surface point #2 z component.
        r2: Z-axisymmetric point-defined surface point #2 radius.
        z3: Z-axisymmetric point-defined surface point #3 z component.
        r3: Z-axisymmetric point-defined surface point #3 radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``SurfaceZ``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SURFACEZ

        self.z1: float = None
        self.r1: float = None
        self.z2: float = None
        self.r2: float = None
        self.z3: float = None
        self.r3: float = None

    def set_parameters(self, z1: float, r1: float, z2: float, r2: float, z3: float, r3: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            z1: Z-axisymmetric point-defined surface point #1 z component.
            r1: Z-axisymmetric point-defined surface point #1 radius.
            z2: Z-axisymmetric point-defined surface point #2 z component.
            r2: Z-axisymmetric point-defined surface point #2 radius.
            z3: Z-axisymmetric point-defined surface point #3 z component.
            r3: Z-axisymmetric point-defined surface point #3 radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(z1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z1 = value
        self.parameters["z1"] = value

        value = types.cast_fortran_real(r1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r1 = value
        self.parameters["r1"] = value

        if z2 is not None and r2 is not None:
            value = types.cast_fortran_real(z2)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.z2 = value
            self.parameters["z2"] = value

            value = types.cast_fortran_real(r2)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.r2 = value
            self.parameters["r2"] = value

            if z3 is not None and r3 is not None:
                value = types.cast_fortran_real(z3)
                if value is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

                self.z3 = value
                self.parameters["z3"] = value

                value = types.cast_fortran_real(r3)
                if value is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

                self.r3 = value
                self.parameters["r3"] = value


class Box(Surface):
    """
    ``Box`` represents INP arbitrarily oriented orthogonal box macrobody
    surface cards.

    ``Box`` inherits attributes from ``Surface``. It represents the
    INP arbitrarily oriented orthogonal box macrobody surface card syntax
    element.

    Attributes:
        vx: Box macrobody position vector x component.
        vy: Box macrobody position vector y component.
        vz: Box macrobody position vector z component.
        a1x: Box macrobody vector #1 x component.
        a1y: Box macrobody vector #1 y component.
        a1z: Box macrobody vector #1 z component.
        a2x: Box macrobody vector #2 x component.
        a2y: Box macrobody vector #2 y component.
        a2z: Box macrobody vector #2 z component.
        a3x: Box macrobody vector #3 x component.
        a3y: Box macrobody vector #3 y component.
        a3z: Box macrobody vector #3 z component.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Box``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.BOX

        self.vx: float = None
        self.vy: float = None
        self.vz: float = None
        self.a1x: float = None
        self.a1y: float = None
        self.a1z: float = None
        self.a2x: float = None
        self.a2y: float = None
        self.a2z: float = None
        self.a3x: float = None
        self.a3y: float = None
        self.a3z: float = None

    def set_parameters(
        self,
        vx: float,
        vy: float,
        vz: float,
        a1x: float,
        a1y: float,
        a1z: float,
        a2x: float,
        a2y: float,
        a2z: float,
        a3x: float,
        a3y: float,
        a3z: float,
    ) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            vx: Box macrobody position vector x component.
            vy: Box macrobody position vector y component.
            vz: Box macrobody position vector z component.
            a1x: Box macrobody vector #1 x component.
            a1y: Box macrobody vector #1 y component.
            a1z: Box macrobody vector #1 z component.
            a2x: Box macrobody vector #2 x component.
            a2y: Box macrobody vector #2 y component.
            a2z: Box macrobody vector #2 z component.
            a3x: Box macrobody vector #3 x component.
            a3y: Box macrobody vector #3 y component.
            a3z: Box macrobody vector #3 z component.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(vx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx = value
        self.parameters["vx"] = value

        value = types.cast_fortran_real(vy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vy = value
        self.parameters["vy"] = value

        value = types.cast_fortran_real(vz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vz = value
        self.parameters["vz"] = value

        value = types.cast_fortran_real(a1x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a1x = value
        self.parameters["a1x"] = value

        value = types.cast_fortran_real(a1y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a1y = value
        self.parameters["a1y"] = value

        value = types.cast_fortran_real(a1z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a1z = value
        self.parameters["a1z"] = value

        value = types.cast_fortran_real(a2x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a2x = value
        self.parameters["a2x"] = value

        value = types.cast_fortran_real(a2y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a2y = value
        self.parameters["a2y"] = value

        value = types.cast_fortran_real(a2z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a2z = value
        self.parameters["a2z"] = value

        if a3x is not None and a3y is not None and a3z is not None:
            value = types.cast_fortran_real(a3x)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.a3x = value
            self.parameters["a3x"] = value

            value = types.cast_fortran_real(a3y)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.a3y = value
            self.parameters["a3y"] = value

            value = types.cast_fortran_real(a3z)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.a3z = value
            self.parameters["a3z"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        if len(self.parameters) == 12:
            v = _cadquery.cqVector(self.vx, self.vy, self.vz)
            a1 = _cadquery.cqVector(self.a1x, self.a1y, self.a1z)
            a2 = _cadquery.cqVector(self.a2x, self.a2y, self.a2z)
            a3 = _cadquery.cqVector(self.a3x, self.a3y, self.a3z)

            cadquery = "import cadquery as cq\n\n" if hasHeader else ""
            cadquery += f"surface_{self.number} = cq.Workplane()"
            cadquery += _cadquery.add_box(a1, a2, a3)
            cadquery += _cadquery.add_translation(v)

        return cadquery + "\n"


class Parallelepiped(Surface):
    """
    ``Parallelepiped`` represents INP rectangular parallelepiped macrobody
    surface cards.

    ``Parallelepiped`` inherits attributes from ``Surface``. It represents the
    INP rectangular parallelepiped macrobody surface card syntax element.

    Attributes:
        xmin: Parallelepiped x termini minimum.
        xmax: Parallelepiped x termini maximum.
        ymin: Parallelepiped y termini minimum.
        ymax: Parallelepiped y termini maximum.
        zmin: Parallelepiped z termini minimum.
        zmax: Parallelepiped z termini maximum.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Parallelepiped``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.PARALLELEPIPED

        self.xmin: float = None
        self.xmax: float = None
        self.ymin: float = None
        self.ymax: float = None
        self.zmin: float = None
        self.zmax: float = None

    def set_parameters(self, xmin: float, xmax: float, ymin: float, ymax: float, zmin: float, zmax: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            xmin: Parallelepiped x termini minimum.
            xmax: Parallelepiped x termini maximum.
            ymin: Parallelepiped y termini minimum.
            ymax: Parallelepiped y termini maximum.
            zmin: Parallelepiped z termini minimum.
            zmax: Parallelepiped z termini maximum.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(xmin)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.xmin = value
        self.parameters["xmin"] = value

        value = types.cast_fortran_real(xmax)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.xmax = value
        self.parameters["xmax"] = value

        value = types.cast_fortran_real(ymin)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.ymin = value
        self.parameters["ymin"] = value

        value = types.cast_fortran_real(ymax)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.ymax = value
        self.parameters["ymax"] = value

        value = types.cast_fortran_real(zmin)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.zmin = value
        self.parameters["zmin"] = value

        value = types.cast_fortran_real(zmax)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.zmax = value
        self.parameters["zmax"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        xlen, ylen, zlen = (
            math.fabs(self.xmax - self.xmin),
            math.fabs(self.ymax - self.ymin),
            math.fabs(self.zmax - self.zmin),
        )

        x = _cadquery.cqVector(xlen, 0, 0)
        y = _cadquery.cqVector(0, ylen, 0)
        z = _cadquery.cqVector(0, 0, zlen)
        v = _cadquery.cqVector(self.xmin + xlen / 2, self.ymin + ylen / 2, self.zmin + zlen / 2)

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_box(x, y, z)
        cadquery += _cadquery.add_translation(v)

        return cadquery + "\n"


class Sphere(Surface):
    """
    ``Sphere`` represents INP sphere macrobody surface cards.

    ``Sphere`` inherits attributes from ``Surface``. It represents the
    INP sphere macrobody surface card syntax element.

    Attributes:
        vx: Sphere macrobody position vector x component.
        vy: Sphere macrobody position vector y component.
        vz: Sphere macrobody position vector z component.
        r: Sphere macrobody radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Sphere``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.SPHERE

        self.vx: float = None
        self.vy: float = None
        self.vz: float = None
        self.r: float = None

    def set_parameters(self, vx: float, vy: float, vz: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            vx: Sphere macrobody position vector x component.
            vy: Sphere macrobody position vector y component.
            vz: Sphere macrobody position vector z component.
            r: Sphere macrobody radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(vx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx = value
        self.parameters["vx"] = value

        value = types.cast_fortran_real(vy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vy = value
        self.parameters["vy"] = value

        value = types.cast_fortran_real(vz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vz = value
        self.parameters["vz"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_sphere(self.r)
        cadquery += _cadquery.add_translation(self.vx, self.vy, self.vz)

        return cadquery


class CylinderCircular(Surface):
    """
    ``CylinderCircular`` represents INP right circular cylinder macrobody
    surface cards.

    ``CylinderCircular`` inherits attributes from ``Surface``. It represents
    the INP right circular cylinder surface card syntax element.

    Attributes:
        vx: Circular cylinder macrobody position vector x component.
        vy: Circular cylinder macrobody position vector y component.
        vz: Circular cylinder macrobody position vector z component.
        hx: Circular cylinder macrobody height vector x component.
        hy: Circular cylinder macrobody height vector y component.
        hz: Circular cylinder macrobody height vector z component.
        r: Circular cylinder macrobody radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CylinderCircular``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CYLINDERCIRCULAR

        self.vx: float = None
        self.vy: float = None
        self.vz: float = None
        self.hx: float = None
        self.hy: float = None
        self.hz: float = None
        self.r: float = None

    def set_parameters(self, vx: float, vy: float, vz: float, hx: float, hy: float, hz: float, r: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            vx: Circular cylinder macrobody position vector x component.
            vy: Circular cylinder macrobody position vector y component.
            vz: Circular cylinder macrobody position vector z component.
            hx: Circular cylinder macrobody height vector x component.
            hy: Circular cylinder macrobody height vector y component.
            hz: Circular cylinder macrobody height vector z component.
            r: Circular cylinder macrobody radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(vx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx = value
        self.parameters["vx"] = value

        value = types.cast_fortran_real(vy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vy = value
        self.parameters["vy"] = value

        value = types.cast_fortran_real(vz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vz = value
        self.parameters["vz"] = value

        value = types.cast_fortran_real(hx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hx = value
        self.parameters["hx"] = value

        value = types.cast_fortran_real(hy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hy = value
        self.parameters["hy"] = value

        value = types.cast_fortran_real(hz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hz = value
        self.parameters["hz"] = value

        value = types.cast_fortran_real(r)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r = value
        self.parameters["r"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        h = _cadquery.cqVector(self.hx, self.hy, self.hz)
        v = _cadquery.cqVector(self.vx, self.vy, self.vz / 2)
        k = _cadquery.cqVector(0, 0, 1)

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_cylinder_circle(h.norm(), self.r)

        if self.hx != 0 or self.hy != 0 or self.hz / self.hz != 1:
            cadquery += _cadquery.add_rotation(_cadquery.cqVector.cross(k, h), _cadquery.cqVector.angle(k, h))

        cadquery += _cadquery.add_translation(v)

        return cadquery


class HexagonalPrism(Surface):
    """
    ``HexagonalPrism`` represents INP right hexagonal prism macrobody surface
    cards.

    ``HexagonalPrism`` inherits attributes from ``Surface``. It represents the
    INP right hexagonal prism macrobody surface card syntax element.

    Attributes:
        vx: Hexagonal prism position vector x component.
        vy: Hexagonal prism position vector y component.
        vz: Hexagonal prism position vector z component.
        hx: Hexagonal prism height vector x component.
        hy: Hexagonal prism height vector y component.
        hz: Hexagonal prism height vector z component.
        r1: Hexagonal prism facet #1 vector x component.
        r2: Hexagonal prism facet #1 vector y component.
        r3: Hexagonal prism facet #1 vector z component.
        s1: Hexagonal prism facet #2 vector x component.
        s2: Hexagonal prism facet #2 vector y component.
        s3: Hexagonal prism facet #2 vector z component.
        t1: Hexagonal prism facet #3 vector x component.
        t2: Hexagonal prism facet #3 vector y component.
        t3: Hexagonal prism facet #3 vector z component.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``HexagonalPrism``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.HEXAGONALPRISM

        self.vx: float = None
        self.vy: float = None
        self.vz: float = None
        self.hx: float = None
        self.hy: float = None
        self.hz: float = None
        self.r1: float = None
        self.r2: float = None
        self.r3: float = None
        self.s1: float = None
        self.s2: float = None
        self.s3: float = None
        self.t1: float = None
        self.t2: float = None
        self.t3: float = None

    def set_parameters(
        self,
        vx: float,
        vy: float,
        vz: float,
        hx: float,
        hy: float,
        hz: float,
        r1: float,
        r2: float,
        r3: float,
        s1: float,
        s2: float,
        s3: float,
        t1: float,
        t2: float,
        t3: float,
    ) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            vx: Hexagonal prism position vector x component.
            vy: Hexagonal prism position vector y component.
            vz: Hexagonal prism position vector z component.
            hx: Hexagonal prism height vector x component.
            hy: Hexagonal prism height vector y component.
            hz: Hexagonal prism height vector z component.
            r1: Hexagonal prism facet #1 vector x component.
            r2: Hexagonal prism facet #1 vector y component.
            r3: Hexagonal prism facet #1 vector z component.
            s1: Hexagonal prism facet #2 vector x component.
            s2: Hexagonal prism facet #2 vector y component.
            s3: Hexagonal prism facet #2 vector z component.
            t1: Hexagonal prism facet #3 vector x component.
            t2: Hexagonal prism facet #3 vector y component.
            t3: Hexagonal prism facet #3 vector z component.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(vx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx = value
        self.parameters["vx"] = value

        value = types.cast_fortran_real(vy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vy = value
        self.parameters["vy"] = value

        value = types.cast_fortran_real(vz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vz = value
        self.parameters["vz"] = value

        value = types.cast_fortran_real(hx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hx = value
        self.parameters["hx"] = value

        value = types.cast_fortran_real(hy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hy = value
        self.parameters["hy"] = value

        value = types.cast_fortran_real(hz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hz = value
        self.parameters["hz"] = value

        value = types.cast_fortran_real(r1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r1 = value
        self.parameters["r1"] = value

        value = types.cast_fortran_real(r2)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r2 = value
        self.parameters["r2"] = value

        value = types.cast_fortran_real(r3)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r3 = value
        self.parameters["r3"] = value

        if s1 is not None and s2 is not None and s3 is not None and t1 is not None and t2 is not None and t3 is not None:
            value = types.cast_fortran_real(s1)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.s1 = value
            self.parameters["s1"] = value

            value = types.cast_fortran_real(s2)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.s2 = value
            self.parameters["s2"] = value

            value = types.cast_fortran_real(s3)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.s3 = value
            self.parameters["s3"] = value

            value = types.cast_fortran_real(t1)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.t1 = value
            self.parameters["t1"] = value

            value = types.cast_fortran_real(t2)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.t2 = value
            self.parameters["t2"] = value

            value = types.cast_fortran_real(t3)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.t3 = value
            self.parameters["t3"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        if len(self.parameters.items()) == 9:
            v = _cadquery.cqVector(self.vx, self.vy, self.vz)
            h = _cadquery.cqVector(self.hx, self.hy, self.hz)
            r = _cadquery.cqVector(self.r1, self.r2, self.r3)
            k = _cadquery.cqVector(0, 0, 1)

            cadquery = "import cadquery as cq\n\n" if hasHeader else ""
            cadquery += f"surface_{self.number} = cq.Workplane()"
            cadquery += _cadquery.add_prism_polygon(h.norm(), r.apothem())

            if self.hx != 0 or self.hy != 0 or self.hz / self.hz != 1:
                cadquery += _cadquery.add_rotation(_cadquery.cqVector.cross(k, h), _cadquery.cqVector.angle(k, h))

            cadquery += _cadquery.add_translation(v)

        return cadquery


class CylinderElliptical(Surface):
    """
    ``CylinderElliptical`` represents INP right elliptical cylinder macrobody
    surface cards.

    ``CylinderElliptical`` inherits attributes from ``Surface``. It represents
    the INP right elliptical cylinder macrobody surface card syntax element.

    Attributes:
        vx: Elliptical cylinder position vector x component.
        vy: Elliptical cylinder position vector y component.
        vz: Elliptical cylinder position vector z component.
        hx: Elliptical cylinder height vector x component.
        hy: Elliptical cylinder height vector y component.
        hz: Elliptical cylinder height vector z component.
        v1x: Elliptical cylinder major axis vector x component.
        v1y: Elliptical cylinder major axis vector y component.
        v1z: Elliptical cylinder major axis vector z component.
        v2x: Elliptical cylinder minor axis vector x component.
        v2y: Elliptical cylinder minor axis vector y component.
        v2z: Elliptical cylinder minor axis vector z component.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``CylinderElliptical``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CYLINDERELLIPTICAL

        self.vx: float = None
        self.vy: float = None
        self.vz: float = None
        self.hx: float = None
        self.hy: float = None
        self.hz: float = None
        self.v1x: float = None
        self.v1y: float = None
        self.v1z: float = None
        self.v2x: float = None
        self.v2y: float = None
        self.v2z: float = None

    def set_parameters(
        self,
        vx: float,
        vy: float,
        vz: float,
        hx: float,
        hy: float,
        hz: float,
        v1x: float,
        v1y: float,
        v1z: float,
        v2x: float,
        v2y: float,
        v2z: float,
    ) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            vx: Elliptical cylinder position vector x component.
            vy: Elliptical cylinder position vector y component.
            vz: Elliptical cylinder position vector z component.
            hx: Elliptical cylinder height vector x component.
            hy: Elliptical cylinder height vector y component.
            hz: Elliptical cylinder height vector z component.
            v1x: Elliptical cylinder major axis vector x component.
            v1y: Elliptical cylinder major axis vector y component.
            v1z: Elliptical cylinder major axis vector z component.
            v2x: Elliptical cylinder minor axis vector x component.
            v2y: Elliptical cylinder minor axis vector y component.
            v2z: Elliptical cylinder minor axis vector z component.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if vx is not None:
            value = types.cast_fortran_real(vx)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.vx = value
            self.parameters["vx"] = value

        if vy is not None:
            value = types.cast_fortran_real(vy)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.vy = value
            self.parameters["vy"] = value

        if vz is not None:
            value = types.cast_fortran_real(vz)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.vz = value
            self.parameters["vz"] = value

        if hx is not None:
            value = types.cast_fortran_real(hx)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.hx = value
            self.parameters["hx"] = value

        if hy is not None:
            value = types.cast_fortran_real(hy)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.hy = value
            self.parameters["hy"] = value

        if hz is not None:
            value = types.cast_fortran_real(hz)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.hz = value
            self.parameters["hz"] = value

        if v1x is not None:
            value = types.cast_fortran_real(v1x)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.v1x = value
            self.parameters["v1x"] = value

        if v1y is not None:
            value = types.cast_fortran_real(v1y)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.v1y = value
            self.parameters["v1y"] = value

        if v1z is not None:
            value = types.cast_fortran_real(v1z)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.v1z = value
            self.parameters["v1z"] = value

        if v2x is not None:
            value = types.cast_fortran_real(v2x)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.v2x = value
            self.parameters["v2x"] = value

        if v2y is not None:
            value = types.cast_fortran_real(v2y)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.v2y = value
            self.parameters["v2y"] = value

        if v2z is not None:
            value = types.cast_fortran_real(v2z)
            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            self.v2z = value
            self.parameters["v2z"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        k = _cadquery.cqVector(0, 0, 1)
        v = _cadquery.cqVector(self.vx, self.vy, self.vz)
        h = _cadquery.cqVector(self.hx, self.hy, self.hz)
        v1 = _cadquery.cqVector(self.v1x, self.v1y, self.v1z)
        v2 = _cadquery.cqVector(self.v2x, self.v2y, self.v2z)

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()."
        cadquery += _cadquery.add_cylinder_ellipse(h.norm(), v1.norm(), v2.norm())

        if self.hx != 0 or self.hy != 0 or self.hz / self.hz != 1:
            cadquery += _cadquery.add_rotation(_cadquery.cqVector.cross(k, h), _cadquery.cqVector.angle(k, h))

        cadquery += _cadquery.add_translation(v)

        return cadquery


class ConeTruncated(Surface):
    """
    ``ConeTruncated`` represents INP truncated right-angled cone macrobody
    urface cards.

    ``ConeTruncated`` inherits attributes from ``Surface``. It represents the
    INP truncated right-angled cone macrobody surface card syntax element.

    Attributes:
        vx: Truncated cone position vector x component.
        vy: Truncated cone position vector y component.
        vz: Truncated cone position vector z component.
        hx: Truncated cone height vector x component.
        hy: Truncated cone height vector y component.
        hz: Truncated cone height vector z component.
        r1: Truncated cone lower cone radius.
        r2: Truncated cone upper cone radius.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``ConeTruncated``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.CONETRUNCATED

        self.vx: float = None
        self.vy: float = None
        self.vz: float = None
        self.hx: float = None
        self.hy: float = None
        self.hz: float = None
        self.r1: float = None
        self.r2: float = None

    def set_parameters(self, vx: float, vy: float, vz: float, hx: float, hy: float, hz: float, r1: float, r2: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            vx: Truncated cone position vector x component.
            vy: Truncated cone position vector y component.
            vz: Truncated cone position vector z component.
            hx: Truncated cone height vector x component.
            hy: Truncated cone height vector y component.
            hz: Truncated cone height vector z component.
            r1: Truncated cone lower cone radius.
            r2: Truncated cone upper cone radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(vx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx = value
        self.parameters["vx"] = value

        value = types.cast_fortran_real(vy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vy = value
        self.parameters["vy"] = value

        value = types.cast_fortran_real(vz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vz = value
        self.parameters["vz"] = value

        value = types.cast_fortran_real(hx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hx = value
        self.parameters["hx"] = value

        value = types.cast_fortran_real(hy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hy = value
        self.parameters["hy"] = value

        value = types.cast_fortran_real(hz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hz = value
        self.parameters["hz"] = value

        value = types.cast_fortran_real(r1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r1 = value
        self.parameters["r1"] = value

        value = types.cast_fortran_real(r2)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r2 = value
        self.parameters["r2"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        k = _cadquery.cqVector(0, 0, 1)
        v = _cadquery.cqVector(self.vx, self.vy, self.vz)
        h = _cadquery.cqVector(self.hx, self.hy, self.hz)
        v1 = _cadquery.cqVector(self.v1x, self.v1y, self.v1z)
        v2 = _cadquery.cqVector(self.v2x, self.v2y, self.v2z)

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        cadquery += f"surface_{self.number} = cq.Workplane()"
        cadquery += _cadquery.add_cone_truncated(h.norm(), v1.norm(), v2.norm())

        if self.hx != 0 or self.hy != 0 or self.hz / self.hz != 1:
            cadquery += _cadquery.add_rotation(_cadquery.cqVector.cross(k, h), _cadquery.cqVector.angle(k, h))

        cadquery += _cadquery.add_translation(v)

        return cadquery


class Ellipsoid(Surface):
    """
    ``Ellipsoid`` represents INP ellipsoid surface cards.

    ``Ellipsoid`` inherits attributes from ``Surface``. It represents the
    INP ellipsoid surface card syntax element.

    Attributes:
        v1x: Ellipsoid focus #1 or center x component.
        v1y: Ellipsoid focus #1 or center y component.
        v1z: Ellipsoid focus #1 or center z component.
        v2x: Ellipsoid focus #2 or major axis x component.
        v2y: Ellipsoid focus #2 or major axis y component.
        v2z: Ellipsoid focus #2 or major axis z component.
        rm: Ellipsoid major/minor axis radius length.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Ellipsoid``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.ELLIPSOID

        self.v1x: float = None
        self.v1y: float = None
        self.v1z: float = None
        self.v2x: float = None
        self.v2y: float = None
        self.v2z: float = None
        self.rm: float = None

    def set_parameters(self, v1x: float, v1y: float, v1z: float, v2x: float, v2y: float, v2z: float, rm: float) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            v1x: Ellipsoid focus #1 or center x component.
            v1y: Ellipsoid focus #1 or center y component.
            v1z: Ellipsoid focus #1 or center z component.
            v2x: Ellipsoid focus #2 or major axis x component.
            v2y: Ellipsoid focus #2 or major axis y component.
            v2z: Ellipsoid focus #2 or major axis z component.
            rm: Ellipsoid major/minor axis radius length.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(v1x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v1x = value
        self.parameters["v1x"] = value

        value = types.cast_fortran_real(v1y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v1y = value
        self.parameters["v1y"] = value

        value = types.cast_fortran_real(v1z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v1z = value
        self.parameters["v1z"] = value

        value = types.cast_fortran_real(v2x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v2x = value
        self.parameters["v2x"] = value

        value = types.cast_fortran_real(v2y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v2y = value
        self.parameters["v2y"] = value

        value = types.cast_fortran_real(v2z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v2z = value
        self.parameters["v2z"] = value

        value = types.cast_fortran_real(rm)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.rm = value
        self.parameters["rm"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""

        if self.parameters["rm"] > 0:
            v2 = [self.v2x, self.v2y, self.v2z]

            a = self.parameters["rm"]
            b = math.sqrt(self.parameters["rm"] ** 2 - (np.linalg.norm(v2 - [self.v1x, self.v1y, self.v1z]) / 2) ** 2)

            vx, vy, vz = (v2 - [self.v1x, self.v1y, self.v1z]) / 2 + [
                self.v1x,
                self.v1y,
                self.v1z,
            ]
            ax, ay, az = np.cross(
                [0, 1, 0],
                [self.v2x, self.v2y, self.v2z] - [self.v1x, self.v1y, self.v1z],
            )
            angle = (
                np.arccos([self.v2x, self.v2y, self.v2z][1] / np.linalg.norm([self.v2x, self.v2y, self.v2z])) * 180 / math.pi
            )
            cadquery += (
                f"surface_{self.number} = cq.Workplane().ellipseArc({b}, {a}, -90, 90).close()"
                f".revolve(axisStart=(0, -{a}, 0), axisEnd=(0, {a}, 0)).translate(({vx}, {vy - a}, {vz}))"
                f".rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"
            )
        elif self.parameters["rm"] < 0:
            a = np.linalg.norm([self.v2x, self.v2y, self.v2z])
            b = math.fabs(self.parameters["rm"])
            vx, vy, vz = [self.v1x, self.v1y, self.v1z]
            ax, ay, az = np.cross([0, 1, 0], [self.v2x, self.v2y, self.v2z])
            angle = (
                np.arccos([self.v2x, self.v2y, self.v2z][1] / np.linalg.norm([self.v2x, self.v2y, self.v2z])) * 180 / math.pi
            )
            cadquery += (
                f"surface_{self.number} = cq.Workplane().ellipseArc({b}, {a}, -90, 90).close()"
                f".revolve(axisStart=(0, -{a}, 0), axisEnd=(0, {a}, 0)).translate(({vx}, {vy - a}, {vz}))"
                f".rotate(({vx - ax}, {vy - ay}, {vz - az}), ({vx + ax}, {vy + ay}, {vz + az}), {angle})\n"
            )

        return cadquery


class Wedge(Surface):
    """
    ``Wedge`` represents INP wedge surface cards.

    ``Wedge`` inherits attributes from ``Surface``. It represents the
    INP wedge surface card syntax element.

    Attributes:
        vx: Wedge position vector x component.
        vy: Wedge position vector y component.
        vz: Wedge position vector z component.
        v1x: Wedge side vector #1 x component.
        v1y: Wedge side vector #1 y component.
        v1z: Wedge side vector #1 z component.
        v2x: Wedge side vector #2 x component.
        v2y: Wedge side vector #2 y component.
        v2z: Wedge side vector #2 z component.
        v3x: Wedge height vector x component.
        v3y: Wedge height vector y component.
        v3z: Wedge height vector z component.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Wedge``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.WEDGE

        self.vx: float = None
        self.vy: float = None
        self.vz: float = None
        self.v1x: float = None
        self.v1y: float = None
        self.v1z: float = None
        self.v2x: float = None
        self.v2y: float = None
        self.v2z: float = None
        self.v3x: float = None
        self.v3y: float = None
        self.v3z: float = None

    def set_parameters(
        self,
        vx: float,
        vy: float,
        vz: float,
        v1x: float,
        v1y: float,
        v1z: float,
        v2x: float,
        v2y: float,
        v2z: float,
        v3x: float,
        v3y: float,
        v3z: float,
    ) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            vx: Wedge position vector x component.
            vy: Wedge position vector y component.
            vz: Wedge position vector z component.
            v1x: Wedge side vector #1 x component.
            v1y: Wedge side vector #1 y component.
            v1z: Wedge side vector #1 z component.
            v2x: Wedge side vector #2 x component.
            v2y: Wedge side vector #2 y component.
            v2z: Wedge side vector #2 z component.
            v3x: Wedge height vector x component.
            v3y: Wedge height vector y component.
            v3z: Wedge height vector z component.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(vx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx = value
        self.parameters["vx"] = value

        value = types.cast_fortran_real(vy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vy = value
        self.parameters["vy"] = value

        value = types.cast_fortran_real(vz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vz = value
        self.parameters["vz"] = value

        value = types.cast_fortran_real(v1x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v1x = value
        self.parameters["v1x"] = value

        value = types.cast_fortran_real(v1y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v1y = value
        self.parameters["v1y"] = value

        value = types.cast_fortran_real(v1z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v1z = value
        self.parameters["v1z"] = value

        value = types.cast_fortran_real(v2x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v2x = value
        self.parameters["v2x"] = value

        value = types.cast_fortran_real(v2y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v2y = value
        self.parameters["v2y"] = value

        value = types.cast_fortran_real(v2z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v2z = value
        self.parameters["v2z"] = value

        value = types.cast_fortran_real(v3x)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v3x = value
        self.parameters["v3x"] = value

        value = types.cast_fortran_real(v3y)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v3y = value
        self.parameters["v3y"] = value

        value = types.cast_fortran_real(v3z)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v3z = value
        self.parameters["v3z"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""

        # cadquery += f"surface_{self.number} = cq.Workplane().polyline(["
        #     f"({self.v1x}, {self.v1y}, {self.v1z}), "
        #     f"(0, 0, 0), "
        #     f"({self.v2x}, {self.v2y}, {self.v2z})]).close()"
        #     f".polyline(["
        #     f"({self.v1x + self.v3x}, {self.v1y + self.v3y}, {self.v1z + self.v3z}), "
        #     f"({self.v3x}, {self.v3y}, {self.v3z}), "
        #     f"({self.v2x + self.v3x}, {self.v2y + self.v3y}, {self.v2z + self.v3z})]).close()"
        #     f".loft().translate(({vx}, {vy}, {vz}))\n"

        return cadquery


class Polyhedron(Surface):
    """
    ``Polyhedron`` represents INP arbitrary polyhedron surface cards.

    ``Polyhedron`` inherits attributes from ``Surface``. It represents the
    INP arbitrary polyhedron surface card syntax element.

    Attributes:
        ax: Polyhedron corner #1 x component.
        ay: Polyhedron corner #1 y component.
        az: Polyhedron corner #1 z component.
        bx: Polyhedron corner #2 x component.
        by: Polyhedron corner #2 y component.
        bz: Polyhedron corner #2 z component.
        cx: Polyhedron corner #3 x component.
        cy: Polyhedron corner #3 y component.
        cz: Polyhedron corner #3 z component.
        dx: Polyhedron corner #4 x component.
        dy: Polyhedron corner #4 y component.
        dz: Polyhedron corner #4 z component.
        ex: Polyhedron corner #5 x component.
        ey: Polyhedron corner #5 y component.
        ez: Polyhedron corner #5 z component.
        fx: Polyhedron corner #6 x component.
        fy: Polyhedron corner #6 y component.
        fz: Polyhedron corner #6 z component.
        gx: Polyhedron corner #7 x component.
        gy: Polyhedron corner #7 y component.
        gz: Polyhedron corner #7 z component.
        hx: Polyhedron corner #8 x component.
        hy: Polyhedron corner #8 y component.
        hz: Polyhedron corner #8 z component.
        n1: Polyhedron four-digit side specificer #1.
        n2: Polyhedron four-digit side specificer #2.
        n3: Polyhedron four-digit side specificer #3.
        n4: Polyhedron four-digit side specificer #4.
        n5: Polyhedron four-digit side specificer #5.
        n6: Polyhedron four-digit side specificer #6.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Polyhedron``.
        """

        super().__init__()
        self.mnemonic = Surface.SurfaceMnemonic.POLYHEDRON

        self.ax: float = None
        self.ay: float = None
        self.az: float = None
        self.bx: float = None
        self.by: float = None
        self.bz: float = None
        self.cx: float = None
        self.cy: float = None
        self.cz: float = None
        self.dx: float = None
        self.dy: float = None
        self.dz: float = None
        self.ex: float = None
        self.ey: float = None
        self.ez: float = None
        self.fx: float = None
        self.fy: float = None
        self.fz: float = None
        self.gx: float = None
        self.gy: float = None
        self.gz: float = None
        self.hx: float = None
        self.hy: float = None
        self.hz: float = None
        self.n1: float = None
        self.n2: float = None
        self.n3: float = None
        self.n4: float = None
        self.n5: float = None
        self.n6: float = None

    def set_parameters(
        self,
        ax: float,
        ay: float,
        az: float,
        bx: float,
        by: float,
        bz: float,
        cx: float,
        cy: float,
        cz: float,
        dx: float,
        dy: float,
        dz: float,
        ex: float,
        ey: float,
        ez: float,
        fx: float,
        fy: float,
        fz: float,
        gx: float,
        gy: float,
        gz: float,
        hx: float,
        hy: float,
        hz: float,
        n1: float,
        n2: float,
        n3: float,
        n4: float,
        n5: float,
        n6: float,
    ) -> None:
        """
        ``set_parameters`` stores INP surface card parameters.

        ``set_parameters`` checks given arguments before assigning the given
        value. If given an unrecognized argument, it raises semantic errors.

        Parameters:
            ax: Polyhedron corner #1 x component.
            ay: Polyhedron corner #1 y component.
            az: Polyhedron corner #1 z component.
            bx: Polyhedron corner #2 x component.
            by: Polyhedron corner #2 y component.
            bz: Polyhedron corner #2 z component.
            cx: Polyhedron corner #3 x component.
            cy: Polyhedron corner #3 y component.
            cz: Polyhedron corner #3 z component.
            dx: Polyhedron corner #4 x component.
            dy: Polyhedron corner #4 y component.
            dz: Polyhedron corner #4 z component.
            ex: Polyhedron corner #5 x component.
            ey: Polyhedron corner #5 y component.
            ez: Polyhedron corner #5 z component.
            fx: Polyhedron corner #6 x component.
            fy: Polyhedron corner #6 y component.
            fz: Polyhedron corner #6 z component.
            gx: Polyhedron corner #7 x component.
            gy: Polyhedron corner #7 y component.
            gz: Polyhedron corner #7 z component.
            hx: Polyhedron corner #8 x component.
            hy: Polyhedron corner #8 y component.
            hz: Polyhedron corner #8 z component.
            n1: Polyhedron four-digit side specificer #1.
            n2: Polyhedron four-digit side specificer #2.
            n3: Polyhedron four-digit side specificer #3.
            n4: Polyhedron four-digit side specificer #4.
            n5: Polyhedron four-digit side specificer #5.
            n6: Polyhedron four-digit side specificer #6.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        value = types.cast_fortran_real(ax)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.ax = value
        self.parameters["ax"] = value

        value = types.cast_fortran_real(ay)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.ay = value
        self.parameters["ay"] = value

        value = types.cast_fortran_real(az)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.az = value
        self.parameters["az"] = value

        value = types.cast_fortran_real(bx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.bx = value
        self.parameters["bx"] = value

        value = types.cast_fortran_real(by)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.by = value
        self.parameters["by"] = value

        value = types.cast_fortran_real(bz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.bz = value
        self.parameters["bz"] = value

        value = types.cast_fortran_real(cx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.cx = value
        self.parameters["cx"] = value

        value = types.cast_fortran_real(cy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.cy = value
        self.parameters["cy"] = value

        value = types.cast_fortran_real(cz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.cz = value
        self.parameters["cz"] = value

        value = types.cast_fortran_real(dx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.dx = value
        self.parameters["dx"] = value

        value = types.cast_fortran_real(dy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.dy = value
        self.parameters["dy"] = value

        value = types.cast_fortran_real(dz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.dz = value
        self.parameters["dz"] = value

        value = types.cast_fortran_real(ex)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.ex = value
        self.parameters["ex"] = value

        value = types.cast_fortran_real(ey)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.ey = value
        self.parameters["ey"] = value

        value = types.cast_fortran_real(ez)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.ez = value
        self.parameters["ez"] = value

        value = types.cast_fortran_real(fx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.fx = value
        self.parameters["fx"] = value

        value = types.cast_fortran_real(fy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.fy = value
        self.parameters["fy"] = value

        value = types.cast_fortran_real(fz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.fz = value
        self.parameters["fz"] = value

        value = types.cast_fortran_real(gx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.gx = value
        self.parameters["gx"] = value

        value = types.cast_fortran_real(gy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.gy = value
        self.parameters["gy"] = value

        value = types.cast_fortran_real(gz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.gz = value
        self.parameters["gz"] = value

        value = types.cast_fortran_real(hx)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hx = value
        self.parameters["hx"] = value

        value = types.cast_fortran_real(hy)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hy = value
        self.parameters["hy"] = value

        value = types.cast_fortran_real(hz)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.hz = value
        self.parameters["hz"] = value

        value = types.cast_fortran_real(n1)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.n1 = value
        self.parameters["n1"] = value

        value = types.cast_fortran_real(n2)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.n2 = value
        self.parameters["n2"] = value

        value = types.cast_fortran_real(n3)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.n3 = value
        self.parameters["n3"] = value

        value = types.cast_fortran_real(n4)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.n4 = value
        self.parameters["n4"] = value

        value = types.cast_fortran_real(n5)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.n5 = value
        self.parameters["n5"] = value

        value = types.cast_fortran_real(n6)
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.n6 = value
        self.parameters["n6"] = value

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from INP surface card objects.

        ``to_cadquery`` provides a Cadquery endpoints for writing Cadquery
        source strings and later displaying geometries.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface card object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""

        return cadquery
