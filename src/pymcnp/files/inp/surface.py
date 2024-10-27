"""
``surface`` contains the class representing INP surface cards.

``surface`` packages the ``Surface`` class, providing an object-oriented,
importable interface for INP surface cards.
"""

import math
from typing import Final
from enum import Enum

from . import _card
from ..utils import _cadquery
from ..utils import _parser
from ..utils import errors
from ..utils import types


class Surface(_card.Card):
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

    class SurfaceMnemonic(str, Enum):
        """
        ``SurfaceMnemonic`` represents INP surface card mnemonics

        ``SurfaceMnemonic`` implements INP surface card mnemonics as a Python
        inner class. It enumerates MCNP mnemonics and provides methods for
        casting strings to ``SurfaceMnemonic`` instances. It represents the INP
        surface card mnemonics syntax element, so ``Surface`` depends on
        ``SurfaceMnemonic`` as an enum.
        """

        PLANEGENERAL = 'p'
        PLANENORMALX = 'px'
        PLANENORMALY = 'py'
        PLANENORMALZ = 'pz'
        SPHEREORIGIN = 'so'
        SPHEREGENERAL = 's'
        SPHERENORMALX = 'sx'
        SPHERENORMALY = 'sy'
        SPHERENORMALZ = 'sz'
        CYLINDERPARALLELX = 'c/x'
        CYLINDERPARALLELY = 'c/y'
        CYLINDERPARALLELZ = 'c/z'
        CYLINDERONX = 'cx'
        CYLINDERONY = 'cy'
        CYLINDERONZ = 'cz'
        CONEPARALLELX = 'k/x'
        CONEPARALLELY = 'k/y'
        CONEPARALLELZ = 'k/z'
        CONEONX = 'kx'
        CONEONY = 'ky'
        CONEONZ = 'kx'
        QUADRATICSPECIAL = 'sq'
        QUADRATICGENERAL = 'gq'
        TORUSPARALLELX = 'tx'
        TORUSPARALLELY = 'ty'
        TORUSPARALLELZ = 'tz'
        SURFACEX = 'x'
        SURFACEY = 'y'
        SURFACEZ = 'z'
        BOX = 'box'
        PARALLELEPIPED = 'rpp'
        SPHERE = 'sph'
        CYLINDERCIRCULAR = 'rcc'
        HEXAGONALPRISM = 'rhp'
        CYLINDERELLIPTICAL = 'rec'
        CONETRUNCATED = 'trc'
        ELLIPSOID = 'ell'
        WEDGE = 'wed'
        POLYHEDRON = 'arb'

        @staticmethod
        def from_mcnp(source: str):
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
            if source not in [enum.value for enum in Surface.SurfaceMnemonic]:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC, info=source
                )

            return Surface.SurfaceMnemonic(source)

        def to_mcnp(self) -> str:
            """
            ``to_mcnp`` generates INP from ``SurfaceMnemonic`` objects.

            ``to_mcnp`` creates INP source string from ``SurfaceMnemonic``
            objects, so it provides an MCNP endpoint.

            Returns:
                INP string for ``SurfaceMnemonic`` object.
            """

            return self.value

    def __init__(
        self,
        number: types.McnpInteger,
        mnemonic: SurfaceMnemonic,
        transform: types.McnpInteger,
        parameters: tuple[types.McnpReal],
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``Surface``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.
        """

        super().__init__(number.value)

        if mnemonic is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC)

        if parameters is None or not parameters:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        try:
            match mnemonic:
                case Surface.SurfaceMnemonic.PLANEGENERAL:
                    if len(parameters) == 4:
                        obj = PlaneGeneralEquation(
                            number,
                            transform,
                            *parameters,
                            is_whiteboundary=is_whiteboundary,
                            is_reflecting=is_reflecting,
                        )
                    else:
                        obj = PlaneGeneralPoint(
                            number,
                            transform,
                            *parameters,
                            is_whiteboundary=is_whiteboundary,
                            is_reflecting=is_reflecting,
                        )
                case Surface.SurfaceMnemonic.PLANENORMALX:
                    obj = PlaneNormalX(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.PLANENORMALY:
                    obj = PlaneNormalY(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.PLANENORMALZ:
                    obj = PlaneNormalZ(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SPHEREORIGIN:
                    obj = SphereOrigin(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SPHEREGENERAL:
                    obj = SphereGeneral(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SPHERENORMALX:
                    obj = SphereNormalX(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SPHERENORMALY:
                    obj = SphereNormalY(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SPHERENORMALZ:
                    obj = SphereNormalZ(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CYLINDERPARALLELX:
                    obj = CylinderParallelX(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CYLINDERPARALLELY:
                    obj = CylinderParallelY(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CYLINDERPARALLELZ:
                    obj = CylinderParallelZ(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CYLINDERONX:
                    obj = CylinderOnX(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CYLINDERONY:
                    obj = CylinderOnY(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CYLINDERONZ:
                    obj = CylinderOnZ(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CONEPARALLELX:
                    obj = ConeParallelX(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CONEPARALLELY:
                    obj = ConeParallelY(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CONEPARALLELZ:
                    obj = ConeParallelZ(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CONEONX:
                    obj = ConeOnX(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CONEONY:
                    obj = ConeOnY(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CONEONZ:
                    obj = ConeOnZ(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.QUADRATICSPECIAL:
                    obj = QuadraticSpecial(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.QUADRATICGENERAL:
                    obj = QuadraticGeneral(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.TORUSPARALLELX:
                    obj = TorusParallelX(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.TORUSPARALLELY:
                    obj = TorusParallelY(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.TORUSPARALLELZ:
                    obj = TorusParallelZ(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SURFACEX:
                    obj = SurfaceX(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SURFACEY:
                    obj = SurfaceY(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SURFACEZ:
                    obj = SurfaceZ(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.BOX:
                    obj = Box(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.PARALLELEPIPED:
                    obj = Parallelepiped(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.SPHERE:
                    obj = Sphere(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CYLINDERCIRCULAR:
                    obj = CylinderCircular(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.HEXAGONALPRISM:
                    obj = HexagonalPrism(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CYLINDERELLIPTICAL:
                    obj = CylinderElliptical(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.CONETRUNCATED:
                    obj = ConeTruncated(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.ELLIPSOID:
                    obj = Ellipsoid(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.WEDGE:
                    obj = Wedge(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case Surface.SurfaceMnemonic.POLYHEDRON:
                    obj = Polyhedron(
                        number,
                        transform,
                        *parameters,
                        is_whiteboundary=is_whiteboundary,
                        is_reflecting=is_reflecting,
                    )
                case _:
                    assert False, 'Impossible'

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        except TypeError:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES)

    @staticmethod
    def from_mcnp(source: str, line: int = None):
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

        # Processing Inline Comment
        comment = None
        if '$' in source:
            source, comment = source.split('$', maxsplit=1)

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE)
        )

        # Processing Reflecting Prefix
        if tokens.peekl()[0] == '+':
            is_whiteboundary = True
            is_reflecting = False
            tokens.pushl(tokens.popl()[1:])
        elif tokens.peekl()[0] == '*':
            is_whiteboundary = False
            is_reflecting = True
            tokens.pushl(tokens.popl()[1:])
        else:
            is_whiteboundary = False
            is_reflecting = False

        # Processing Number, Transform/Periodic, Mnemonic, Parameters
        number = types.McnpInteger.from_mcnp(tokens.popl())

        try:
            transform = types.McnpInteger.from_mcnp(tokens.peekl())
            tokens.popl()
        except Exception:
            transform = None

        mnemonic = Surface.SurfaceMnemonic.from_mcnp(tokens.popl())
        parameters = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        surface = Surface(
            number,
            mnemonic,
            transform,
            parameters,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
        surface.line = line
        surface.comment = comment

        return surface

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Surface`` objects.

        ``to_mcnp`` creates INP source string from ``Surface`` objects,
        so it provides an MCNP endpoint.

        Returns:
            INP string for ``Surface`` object.
        """

        number_str = self.number.to_mcnp()
        transform_str = self.transform.to_mcnp() if self.transform is not None else ' '
        parameter_str = ' '.join(
            str(parameter.value) if hasattr(parameter, 'to_mcnp') else str(parameter)
            for parameter in self.parameters
        )

        source = f'{number_str} {transform_str} {self.mnemonic.to_mcnp()} {parameter_str}'

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
            'j': self.number.to_mcnp(),
            '+': self.is_reflecting,
            '*': self.is_whiteboundary,
            'n': self.transform.to_mcnp() if self.transform is not None else None,
            'A': self.mnemonic.to_mcnp(),
            'list': tuple(
                [
                    parameter.to_mcnp() if hasattr(parameter, 'to_mcnp') else parameter
                    for parameter in self.parameters
                ]
            ),
        }


class PlaneGeneralPoint(Surface):
    """
    ``PlaneGeneralPoint`` represents INP general planes surface cards.

    ``PlaneGeneralPoint`` inherits attributes from ``Surface``. It
    represents the INP general planes surface card syntax element.

    Attributes:
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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x1: types.McnpReal,
        y1: types.McnpReal,
        z1: types.McnpReal,
        x2: types.McnpReal,
        y2: types.McnpReal,
        z2: types.McnpReal,
        x3: types.McnpReal,
        y3: types.McnpReal,
        z3: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``PlaneGeneral``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.PLANEGENERAL
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if x2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if x3 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y3 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z3 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x1: Final[types.McnpReal] = x1
        self.y1: Final[types.McnpReal] = y1
        self.z1: Final[types.McnpReal] = z1
        self.x2: Final[types.McnpReal] = x2
        self.y2: Final[types.McnpReal] = y2
        self.z2: Final[types.McnpReal] = z2
        self.x3: Final[types.McnpReal] = x3
        self.y3: Final[types.McnpReal] = y3
        self.z3: Final[types.McnpReal] = z3

        self.parameters: Final[tuple[types.McnpReal]] = (x1, y1, z1, x2, y2, z2, x3, y3, z3)


class PlaneGeneralEquation(Surface):
    """
    ``PlaneGeneralEquation`` represents INP general planes surface cards.

    ``PlaneGeneralEquation`` inherits attributes from ``Surface``. It
    represents the INP general planes surface card syntax element.

    Attributes:
        a: Equation-defined general plane A coefficent.
        b: Equation-defined general plane B coefficent.
        c: Equation-defined general plane C coefficent.
        d: Equation-defined general plane D coefficent.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        d: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``PlaneGeneral``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            a: Equation-defined general plane A coefficent.
            b: Equation-defined general plane B coefficent.
            c: Equation-defined general plane C coefficent.
            d: Equation-defined general plane D coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.PLANEGENERAL
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if a is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if b is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if c is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if d is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c
        self.d: Final[types.McnpReal] = d

        self.parameters: Final[tuple[types.McnpReal]] = (a, b, c, d)


class PlaneNormalX(Surface):
    """
    ``PlaneNormalX`` represents INP normal-to-the-x-axis surface cards.

    ``PlaneNormalX`` inherits attributes from ``Surface``. It represents the
    INP normal-to-the-x-axis surface card syntax element.

    Attributes:
        d: Normal-to-the-x-axis plane D coefficent.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        d: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``PlaneNormalX``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            d: Normal-to-the-x-axis plane D coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.PLANENORMALX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if d is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d: Final[types.McnpReal] = d

        self.parameters: Final[tuple[types.McnpReal]] = (d,)


class PlaneNormalY(Surface):
    """
    ``PlaneNormalY`` represents INP normal-to-the-y-axis surface cards.

    ``PlaneNormalY`` inherits attributes from ``Surface``. It represents the
    INP normal-to-the-y-axis surface card syntax element.

    Attributes:
        d: Normal-to-the-y-axis plane D coefficent.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        d: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``PlaneNormalY``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            d: Normal-to-the-y-axis plane D coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.PLANENORMALY
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if d is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d: Final[types.McnpReal] = d

        self.parameters: Final[tuple[types.McnpReal]] = (d,)


class PlaneNormalZ(Surface):
    """
    ``PlaneNormalZ`` represents INP normal-to-the-z-axis surface cards.

    ``PlaneNormalZ`` inherits attributes from ``Surface``. It represents the
    INP normal-to-the-z-axis surface card syntax element.

    Attributes:
        d: Normal-to-the-z-axis plane D coefficent.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        d: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``PlaneNormalZ``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.PLANENORMALZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if d is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.d: Final[types.McnpReal] = d

        self.parameters: Final[tuple[types.McnpReal]] = (d,)


class SphereOrigin(Surface):
    """
    ``SphereOrigin`` represents INP origin-centered sphere surface cards.

    ``SphereOrigin`` inherits attributes from ``Surface``. It represents the
    INP origin-centered sphere surface card syntax element.

    Attributes:
        r: Origin-centered sphere radius.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``SphereOrigin``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            r: Origin-centered sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SPHEREORIGIN
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (r,)

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

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_sphere(self.r.value)

        return cadquery + '\n'


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``SphereGeneral``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: General sphere center x component.
            y: General sphere center y component.
            z: General sphere center z component.
            r: General sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SPHEREGENERAL
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (x, y, z, r)

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

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_sphere(self.r.value)
        cadquery += _cadquery.add_translation(self.x.value, self.y.value, self.z.value)

        return cadquery + '\n'


class SphereNormalX(Surface):
    """
    ``SphereNormalX`` represents INP on-x-axis sphere surface cards.

    ``SphereNormalX`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis sphere surface card syntax element.

    Attributes:
        x: On-x-axis sphere center x component.
        r: On-x-axis sphere radius.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``SphereNormalX``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: On-x-axis sphere center x component.
            r: On-x-axis sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SPHERENORMALX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (x, r)

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

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_sphere(self.r.value)
        cadquery += _cadquery.add_translation(self.x.value, 0, 0)

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        y: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``SphereNormalY``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            y: On-y-axis sphere center y component.
            r: On-y-axis sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SPHERENORMALY
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y: Final[types.McnpReal] = y
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (y, r)

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

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_sphere(self.r.value)
        cadquery += _cadquery.add_translation(0, self.y.value, 0)

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        z: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``SphereNormalZ``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            z: On-z-axis sphere center z component.
            r: On-z-axis sphere radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SPHERENORMALZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z: Final[types.McnpReal] = z
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (z, r)

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

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_sphere(self.r.value)
        cadquery += _cadquery.add_translation(0, 0, self.z.value)

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        y: types.McnpReal,
        z: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``CylinderParallelX``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            y: Parallel-to-x-axis cylinder center y component.
            z: Parallel-to-x-axis cylinder center z component.
            r: Parallel-to-x-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CYLINDERPARALLELX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (y, z, r)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        z: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``CylinderParallelY``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-y-axis cylinder center x component.
            z: Parallel-to-y-axis cylinder center z component.
            r: Parallel-to-y-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CYLINDERPARALLELY
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.z: Final[types.McnpReal] = z
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (x, z, r)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``CylinderParallelZ``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-z-axis cylinder center x component.
            y: Parallel-to-z-axis cylinder center y component.
            r: Parallel-to-z-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CYLINDERPARALLELZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (x, y, r)


class CylinderOnX(Surface):
    """
    ``CylinderOnX`` represents INP on-x-axis cylinder surface cards.

    ``CylinderOnX`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis surface card syntax element.

    Attributes:
        r: On-x-axis cylinder radius.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``CylinderOnX``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            r: On-x-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CYLINDERONX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (r,)


class CylinderOnY(Surface):
    """
    ``CylinderOnY`` represents INP on-y-axis cylinder surface cards.

    ``CylinderOnY`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis surface card syntax element.

    Attributes:
        r: On-y-axis cylinder radius.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``CylinderOnY``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            r: On-y-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CYLINDERONY
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (r,)


class CylinderOnZ(Surface):
    """
    ``CylinderOnZ`` represents INP on-z-axis cylinder surface cards.

    ``CylinderOnZ`` inherits attributes from ``Surface``. It represents the
    INP on-x-axis surface card syntax element.

    Attributes:
        r: On-z-axis cylinder radius.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``CylinderOnZ``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            r: On-z-axis cylinder radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CYLINDERONZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (r,)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        t_squared: types.McnpReal,
        plusminus_1: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``ConeParallelX``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-x-axis cone center x component.
            y: Parallel-to-x-axis cone center y component.
            z: Parallel-to-x-axis cone center z component.
            t_squared: Parallel-to-x-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-x-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CONEPARALLELX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.t_squared: Final[types.McnpReal] = t_squared
        self.plusminus_1: Final[types.McnpReal] = plusminus_1

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if t_squared is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if plusminus_1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.parameters: Final[tuple[types.McnpReal]] = (x, y, z, t_squared, plusminus_1)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        t_squared: types.McnpReal,
        plusminus_1: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``ConeParallelY``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-y-axis cone center x component.
            y: Parallel-to-y-axis cone center y component.
            z: Parallel-to-y-axis cone center z component.
            t_squared: Parallel-to-y-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-y-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CONEPARALLELY
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if t_squared is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if plusminus_1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.t_squared: Final[types.McnpReal] = t_squared
        self.plusminus_1: Final[types.McnpReal] = plusminus_1

        self.parameters: Final[tuple[types.McnpReal]] = (x, y, z, t_squared, plusminus_1)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        t_squared: types.McnpReal,
        plusminus_1: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``ConeParallelZ``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-z-axis cone center x component.
            y: Parallel-to-z-axis cone center y component.
            z: Parallel-to-z-axis cone center z component.
            t_squared: Parallel-to-z-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-z-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CONEPARALLELZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if t_squared is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if plusminus_1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.t_squared: Final[types.McnpReal] = t_squared
        self.plusminus_1: Final[types.McnpReal] = plusminus_1

        self.parameters: Final[tuple[types.McnpReal]] = (x, y, z, t_squared, plusminus_1)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        t_squared: types.McnpReal,
        plusminus_1: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``ConeOnX``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: On-x-axis cone center x component.
            t_squared: On-x-axis cone t^2 coefficent.
            plusminus_1: On-x-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CONEONX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if t_squared is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if plusminus_1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.t_squared: Final[types.McnpReal] = t_squared
        self.plusminus_1: Final[types.McnpReal] = plusminus_1

        self.parameters: Final[tuple[types.McnpReal]] = (x, t_squared, plusminus_1)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        y: types.McnpReal,
        t_squared: types.McnpReal,
        plusminus_1: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``ConeOnY``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            y: On-y-axis cone center y component.
            t_squared: On-y-axis cone t^2 coefficent.
            plusminus_1: On-y-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CONEONY
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if t_squared is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if plusminus_1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.y: Final[types.McnpReal] = y
        self.t_squared: Final[types.McnpReal] = t_squared
        self.plusminus_1: Final[types.McnpReal] = plusminus_1

        self.parameters: Final[tuple[types.McnpReal]] = (y, t_squared, plusminus_1)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        z: types.McnpReal,
        t_squared: types.McnpReal,
        plusminus_1: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``ConeOnZ``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            z: On-z-axis cone center z component.
            t_squared: On-z-axis cone t^2 coefficent.
            plusminus_1: On-z-axis cone sheet selector.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CONEONZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if t_squared is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if plusminus_1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.z: Final[types.McnpReal] = z
        self.t_squared: Final[types.McnpReal] = t_squared
        self.plusminus_1: Final[types.McnpReal] = plusminus_1

        self.parameters: Final[tuple[types.McnpReal]] = (z, t_squared, plusminus_1)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        d: types.McnpReal,
        e: types.McnpReal,
        f: types.McnpReal,
        g: types.McnpReal,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``QuadraticSpecial``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.QUADRATICSPECIAL
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if a is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if b is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if c is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if d is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if e is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if f is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if g is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c
        self.d: Final[types.McnpReal] = d
        self.e: Final[types.McnpReal] = e
        self.f: Final[types.McnpReal] = f
        self.g: Final[types.McnpReal] = g
        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z

        self.parameters: Final[tuple[types.McnpReal]] = (a, b, c, d, e, f, g, x, y, z)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        d: types.McnpReal,
        e: types.McnpReal,
        f: types.McnpReal,
        g: types.McnpReal,
        h: types.McnpReal,
        j: types.McnpReal,
        k: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``QuadraticGeneral``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.QUADRATICGENERAL
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if a is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if b is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if c is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if d is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if e is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if f is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if g is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if h is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if j is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if k is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c
        self.d: Final[types.McnpReal] = d
        self.e: Final[types.McnpReal] = e
        self.f: Final[types.McnpReal] = f
        self.g: Final[types.McnpReal] = g
        self.h: Final[types.McnpReal] = h
        self.j: Final[types.McnpReal] = j
        self.k: Final[types.McnpReal] = k

        self.parameters: Final[tuple[types.McnpReal]] = (a, b, c, d, e, f, g, h, j, k)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``TorusParallelX``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-x-axis tori center x component.
            y: Parallel-to-x-axis tori center y component.
            z: Parallel-to-x-axis tori center z component.
            a: Parallel-to-x-axis tori A coefficent.
            b: Parallel-to-x-axis tori B coefficent.
            c: Parallel-to-x-axis tori C coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.TORUSPARALLELX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if b is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if c is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c

        self.parameters: Final[tuple[types.McnpReal]] = (x, y, z, a, b, c)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``TorusParallelY``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-y-axis tori center x component.
            y: Parallel-to-y-axis tori center y component.
            z: Parallel-to-y-axis tori center z component.
            a: Parallel-to-y-axis tori A coefficent.
            b: Parallel-to-y-axis tori B coefficent.
            c: Parallel-to-y-axis tori C coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.TORUSPARALLELY
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if b is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if c is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c

        self.parameters: Final[tuple[types.McnpReal]] = (x, y, z, a, b, c)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``TorusParallelZ``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x: Parallel-to-z-axis tori center x component.
            y: Parallel-to-z-axis tori center y component.
            z: Parallel-to-z-axis tori center z component.
            a: Parallel-to-z-axis tori A coefficent.
            b: Parallel-to-z-axis tori B coefficent.
            c: Parallel-to-z-axis tori C coefficent.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.TORUSPARALLELZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if b is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if c is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c

        self.parameters: Final[tuple[types.McnpReal]] = (x, y, z, a, b, c)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x1: types.McnpReal,
        r1: types.McnpReal,
        x2: types.McnpReal = None,
        r2: types.McnpReal = None,
        x3: types.McnpReal = None,
        r3: types.McnpReal = None,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``SurfaceX``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            x1: X-axisymmetric point-defined surface point #1 x component.
            r1: X-axisymmetric point-defined surface point #1 radius.
            x2: X-axisymmetric point-defined surface point #2 x component.
            r2: X-axisymmetric point-defined surface point #2 radius.
            x3: X-axisymmetric point-defined surface point #3 x component.
            r3: X-axisymmetric point-defined surface point #3 radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SURFACEX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if x1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if x2 is not None and r2 is not None:
            if x2 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if r2 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if x3 is not None and r3 is not None:
                if x3 is None:
                    raise errors.MCNPSemanticError(
                        errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER
                    )

                if r3 is None:
                    raise errors.MCNPSemanticError(
                        errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER
                    )

        self.x1: Final[types.McnpReal] = x1
        self.r1: Final[types.McnpReal] = r1
        self.x2: Final[types.McnpReal] = x2 if x2 is not None else None
        self.r2: Final[types.McnpReal] = r2 if r2 is not None else None
        self.x3: Final[types.McnpReal] = x3 if x3 is not None else None
        self.r3: Final[types.McnpReal] = r3 if r3 is not None else None

        self.parameters = (x1, r1, x2, r2, x3, r3)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        y1: types.McnpReal,
        r1: types.McnpReal,
        y2: types.McnpReal = None,
        r2: types.McnpReal = None,
        y3: types.McnpReal = None,
        r3: types.McnpReal = None,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``SurfaceY``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            y1: Y-axisymmetric point-defined surface point #1 y component.
            r1: Y-axisymmetric point-defined surface point #1 radius.
            y2: Y-axisymmetric point-defined surface point #2 y component.
            r2: Y-axisymmetric point-defined surface point #2 radius.
            y3: Y-axisymmetric point-defined surface point #3 y component.
            r3: Y-axisymmetric point-defined surface point #3 radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SURFACEY
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if y1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if y2 is not None and r2 is not None:
            if y2 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if r2 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if y3 is not None and r3 is not None:
                if y3 is None:
                    raise errors.MCNPSemanticError(
                        errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER
                    )

                if r3 is None:
                    raise errors.MCNPSemanticError(
                        errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER
                    )

        self.y1: Final[types.McnpReal] = y1
        self.r1: Final[types.McnpReal] = r1
        self.y2: Final[types.McnpReal] = y2 if y2 is not None else None
        self.r2: Final[types.McnpReal] = r2 if r2 is not None else None
        self.y3: Final[types.McnpReal] = y3 if y3 is not None else None
        self.r3: Final[types.McnpReal] = r3 if r3 is not None else None

        self.parameters: Final[tuple[types.McnpReal]] = (y1, r1, y2, r2, y3, r3)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        z1: types.McnpReal,
        r1: types.McnpReal,
        z2: types.McnpReal = None,
        r2: types.McnpReal = None,
        z3: types.McnpReal = None,
        r3: types.McnpReal = None,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``SurfaceZ``.

        Parameters:
            z1: Z-axisymmetric point-defined surface point #1 z component.
            r1: Z-axisymmetric point-defined surface point #1 radius.
            z2: Z-axisymmetric point-defined surface point #2 z component.
            r2: Z-axisymmetric point-defined surface point #2 radius.
            z3: Z-axisymmetric point-defined surface point #3 z component.
            r3: Z-axisymmetric point-defined surface point #3 radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SURFACEZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if z1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if z2 is not None and r2 is not None:
            if z2 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if r2 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if z3 is not None and r3 is not None:
                if z3 is None:
                    raise errors.MCNPSemanticError(
                        errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER
                    )

                if r3 is None:
                    raise errors.MCNPSemanticError(
                        errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER
                    )

        self.z1: Final[types.McnpReal] = z1
        self.r1: Final[types.McnpReal] = r1
        self.z2: Final[types.McnpReal] = z2 if z2 is not None else None
        self.r2: Final[types.McnpReal] = r2 if r2 is not None else None
        self.z3: Final[types.McnpReal] = z3 if z3 is not None else None
        self.r3: Final[types.McnpReal] = r3 if r3 is not None else None

        self.parameters: Final[tuple[types.McnpReal]] = (z1, r1, z2, r2, z3, r3)


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        a1x: types.McnpReal,
        a1y: types.McnpReal,
        a1z: types.McnpReal,
        a2x: types.McnpReal,
        a2y: types.McnpReal,
        a2z: types.McnpReal,
        a3x: types.McnpReal = None,
        a3y: types.McnpReal = None,
        a3z: types.McnpReal = None,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``Box``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.BOX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if vx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a1x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a1y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a1z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a2x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a2y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a2z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if a3x is not None or a3y is not None or a3z is not None:
            if a3x is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if a3y is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if a3z is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.a1x: Final[types.McnpReal] = a1x
        self.a1y: Final[types.McnpReal] = a1y
        self.a1z: Final[types.McnpReal] = a1z
        self.a2x: Final[types.McnpReal] = a2x
        self.a2y: Final[types.McnpReal] = a2y
        self.a2z: Final[types.McnpReal] = a2z
        self.a3x: Final[types.McnpReal] = a3x if a3x is not None else None
        self.a3y: Final[types.McnpReal] = a3y if a3y is not None else None
        self.a3z: Final[types.McnpReal] = a3z if a3z is not None else None

        self.parameters: Final[tuple[types.McnpReal]] = (
            vx,
            vy,
            vz,
            a1x,
            a1y,
            a1z,
            a2x,
            a2y,
            a2z,
            a3x,
            a3y,
            a3z,
        )

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

        v = _cadquery.CqVector(self.vx.value, self.vy.value, self.vz.value)
        a1 = _cadquery.CqVector(self.a1x.value, self.a1y.value, self.a1z.value)
        a2 = _cadquery.CqVector(self.a2x.value, self.a2y.value, self.a2z.value)
        a3 = _cadquery.CqVector(self.a3x.value, self.a3y.value, self.a3z.value)

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_box(a1, a2, a3)
        cadquery += _cadquery.add_translation(v)

        return cadquery + '\n'


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        xmin: types.McnpReal,
        xmax: types.McnpReal,
        ymin: types.McnpReal,
        ymax: types.McnpReal,
        zmin: types.McnpReal,
        zmax: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``Parallelepiped``.

        Parameters:
            xmin: Parallelepiped x termini minimum.
            xmax: Parallelepiped x termini maximum.
            ymin: Parallelepiped y termini minimum.
            ymax: Parallelepiped y termini maximum.
            zmin: Parallelepiped z termini minimum.
            zmax: Parallelepiped z termini maximum.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.PARALLELEPIPED
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if xmin is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if xmax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if ymin is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if ymax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if zmin is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if zmax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.xmin: Final[types.McnpReal] = xmin
        self.xmax: Final[types.McnpReal] = xmax
        self.ymin: Final[types.McnpReal] = ymin
        self.ymax: Final[types.McnpReal] = ymax
        self.zmin: Final[types.McnpReal] = zmin
        self.zmax: Final[types.McnpReal] = zmax

        self.parameters: Final[tuple[types.McnpReal]] = (xmin, xmax, ymin, ymax, zmin, zmax)

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
            math.fabs(self.xmax.value - self.xmin.value),
            math.fabs(self.ymax.value - self.ymin.value),
            math.fabs(self.zmax.value - self.zmin.value),
        )

        x = _cadquery.CqVector(xlen, 0, 0)
        y = _cadquery.CqVector(0, ylen, 0)
        z = _cadquery.CqVector(0, 0, zlen)
        v = _cadquery.CqVector(
            self.xmin.value + xlen / 2, self.ymin.value + ylen / 2, self.zmin.value + zlen / 2
        )

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_box(x, y, z)
        cadquery += _cadquery.add_translation(v)

        return cadquery + '\n'


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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``Sphere``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            vx: Sphere macrobody position vector x component.
            vy: Sphere macrobody position vector y component.
            vz: Sphere macrobody position vector z component.
            r: Sphere macrobody radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.SPHERE
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if vx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (vx, vy, vz, r)

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

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_sphere(self.r.value)
        cadquery += _cadquery.add_translation(self.vx.value, self.vy.value, self.vz.value)

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        hx: types.McnpReal,
        hy: types.McnpReal,
        hz: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``CylinderCircular``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            vx: Circular cylinder macrobody position vector x component.
            vy: Circular cylinder macrobody position vector y component.
            vz: Circular cylinder macrobody position vector z component.
            hx: Circular cylinder macrobody height vector x component.
            hy: Circular cylinder macrobody height vector y component.
            hz: Circular cylinder macrobody height vector z component.
            r: Circular cylinder macrobody radius.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CYLINDERCIRCULAR
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if vx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.hx: Final[types.McnpReal] = hx
        self.hy: Final[types.McnpReal] = hy
        self.hz: Final[types.McnpReal] = hz
        self.r: Final[types.McnpReal] = r

        self.parameters: Final[tuple[types.McnpReal]] = (vx, vy, vz, hx, hy, hz, r)

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

        h = _cadquery.CqVector(self.hx.value, self.hy.value, self.hz.value)
        v = _cadquery.CqVector(self.vx.value, self.vy.value, self.vz.value / 2)
        k = _cadquery.CqVector(0, 0, 1)

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_cylinder_circle(h.norm(), self.r.value)

        if self.hx.value != 0 or self.hy.value != 0 or self.hz.value / self.hz.value != 1:
            cadquery += _cadquery.add_rotation(
                _cadquery.CqVector.cross(k, h), _cadquery.CqVector.angle(k, h)
            )

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        hx: types.McnpReal,
        hy: types.McnpReal,
        hz: types.McnpReal,
        r1: types.McnpReal,
        r2: types.McnpReal,
        r3: types.McnpReal,
        s1: types.McnpReal = None,
        s2: types.McnpReal = None,
        s3: types.McnpReal = None,
        t1: types.McnpReal = None,
        t2: types.McnpReal = None,
        t3: types.McnpReal = None,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``HexagonalPrism``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.HEXAGONALPRISM
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if vx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r3 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if (
            s1 is not None
            or s2 is not None
            or s3 is not None
            or t1 is not None
            or t2 is not None
            or t3 is not None
        ):
            if s1 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if s2 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if s3 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if t1 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if t2 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if t3 is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.hx: Final[types.McnpReal] = hx
        self.hy: Final[types.McnpReal] = hy
        self.hz: Final[types.McnpReal] = hz
        self.r1: Final[types.McnpReal] = r1
        self.r2: Final[types.McnpReal] = r2
        self.r3: Final[types.McnpReal] = r3
        self.s1: Final[types.McnpReal] = s1 if s1 is not None else None
        self.s2: Final[types.McnpReal] = s2 if s2 is not None else None
        self.s3: Final[types.McnpReal] = s3 if s3 is not None else None
        self.t1: Final[types.McnpReal] = t1 if t1 is not None else None
        self.t2: Final[types.McnpReal] = t2 if t2 is not None else None
        self.t3: Final[types.McnpReal] = t3 if t3 is not None else None

        self.parameters: Final[tuple[types.McnpReal]] = (
            vx,
            vy,
            vz,
            hx,
            hy,
            hz,
            r1,
            r2,
            r3,
            s1,
            s2,
            s3,
            t1,
            t2,
            t3,
        )

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

        v = _cadquery.CqVector(self.vx.value, self.vy.value, self.vz.value)
        h = _cadquery.CqVector(self.hx.value, self.hy.value, self.hz.value)
        r = _cadquery.CqVector(self.r1.value, self.r2.value, self.r3.value)
        k = _cadquery.CqVector(0, 0, 1)

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_prism_polygon(h.norm(), r.apothem())

        if self.hx.value != 0 or self.hy.value != 0 or self.hz.value / self.hz.value != 1:
            cadquery += _cadquery.add_rotation(
                _cadquery.CqVector.cross(k, h), _cadquery.CqVector.angle(k, h)
            )

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        hx: types.McnpReal,
        hy: types.McnpReal,
        hz: types.McnpReal,
        v1x: types.McnpReal,
        v1y: types.McnpReal,
        v1z: types.McnpReal,
        v2x: types.McnpReal,
        v2y: types.McnpReal = None,
        v2z: types.McnpReal = None,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``CylinderElliptical``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CYLINDERELLIPTICAL
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if vx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v1x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v1y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v1z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v2x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v2y is not None or v2z is not None:
            if v2y is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

            if v2z is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.hx: Final[types.McnpReal] = hx
        self.hy: Final[types.McnpReal] = hy
        self.hz: Final[types.McnpReal] = hz
        self.v1x: Final[types.McnpReal] = v1x
        self.v1y: Final[types.McnpReal] = v1y
        self.v1z: Final[types.McnpReal] = v1z
        self.v2x: Final[types.McnpReal] = v2x

        self.v2y: Final[types.McnpReal] = v2y
        self.v2z: Final[types.McnpReal] = v2z

        self.parameters: Final[tuple[types.McnpReal]] = (
            vx,
            vy,
            vz,
            hx,
            hy,
            hz,
            v1x,
            v1y,
            v1z,
            v2x,
            v2y,
            v2z,
        )

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

        k = _cadquery.CqVector(0, 0, 1)
        v = _cadquery.CqVector(self.vx.value, self.vy.value, self.vz.value)
        h = _cadquery.CqVector(self.hx.value, self.hy.value, self.hz.value)
        v1 = _cadquery.CqVector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _cadquery.CqVector(self.v2x.value, self.v2y.value, self.v2z.value)

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane().'
        cadquery += _cadquery.add_cylinder_ellipse(h.norm(), v1.norm(), v2.norm())

        if self.hx.value != 0 or self.hy.value != 0 or self.hz.value / self.hz.value != 1:
            cadquery += _cadquery.add_rotation(
                _cadquery.CqVector.cross(k, h), _cadquery.CqVector.angle(k, h)
            )

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        hx: types.McnpReal,
        hy: types.McnpReal,
        hz: types.McnpReal,
        r1: types.McnpReal,
        r2: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``ConeTruncated``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.CONETRUNCATED
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if vx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if r2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.hx: Final[types.McnpReal] = hx
        self.hy: Final[types.McnpReal] = hy
        self.hz: Final[types.McnpReal] = hz
        self.r1: Final[types.McnpReal] = r1
        self.r2: Final[types.McnpReal] = r2

        self.parameters: Final[tuple[types.McnpReal]] = (vx, vy, vz, hx, hy, hz, r1, r2)

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

        k = _cadquery.CqVector(0, 0, 1)
        v = _cadquery.CqVector(self.vx.value, self.vy.value, self.vz.value)
        h = _cadquery.CqVector(self.hx.value, self.hy.value, self.hz.value)
        v1 = _cadquery.CqVector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _cadquery.CqVector(self.v2x.value, self.v2y.value, self.v2z.value)

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_cone_truncated(h.norm(), v1.norm(), v2.norm())

        if self.hx.value != 0 or self.hy.value != 0 or self.hz.value / self.hz.value != 1:
            cadquery += _cadquery.add_rotation(
                _cadquery.CqVector.cross(k, h), _cadquery.CqVector.angle(k, h)
            )

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        v1x: types.McnpReal,
        v1y: types.McnpReal,
        v1z: types.McnpReal,
        v2x: types.McnpReal,
        v2y: types.McnpReal,
        v2z: types.McnpReal,
        rm: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``Ellipsoid``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            v1x: Ellipsoid focus #1 or center x component.
            v1y: Ellipsoid focus #1 or center y component.
            v1z: Ellipsoid focus #1 or center z component.
            v2x: Ellipsoid focus #2 or major axis x component.
            v2y: Ellipsoid focus #2 or major axis y component.
            v2z: Ellipsoid focus #2 or major axis z component.
            rm: Ellipsoid major/minor axis radius length.

        Raises:
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.ELLIPSOID
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if v1x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v1y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v1z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v2x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v2y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v2z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if rm is None or (rm == 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.v1x: Final[types.McnpReal] = v1x
        self.v1y: Final[types.McnpReal] = v1y
        self.v1z: Final[types.McnpReal] = v1z
        self.v2x: Final[types.McnpReal] = v2x
        self.v2y: Final[types.McnpReal] = v2y
        self.v2z: Final[types.McnpReal] = v2z
        self.rm: Final[types.McnpReal] = rm

        self.parameters: Final[tuple[types.McnpReal]] = (v1x, v1y, v1z, v2x, v2y, v2z, rm)

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

        j = _cadquery.CqVector(0, 1, 0)
        v1 = _cadquery.CqVector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _cadquery.CqVector(self.v2x.value, self.v2y.value, self.v2z.value)

        if self.rm.value > 0:
            a = _cadquery.CqVector.cross(j, v2 - v1)
            angle = _cadquery.CqVector.angle(j, v2 - v1)
            v = (
                _cadquery.CqVector(
                    (self.v2x.value - self.v1x.value) / 2,
                    (self.v2y.value - self.v1y.value) / 2 - a,
                    (self.v2z.value - self.v1z.value) / 2,
                )
                + v1
            )
        else:
            a = _cadquery.CqVector.cross(j, v2)
            angle = _cadquery.CqVector.angle(j, v2)
            v = _cadquery.CqVector(v1.x, v1.y - a.y, v1.z)

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += f'surface_{self.number.value} = cq.Workplane()'
        cadquery += _cadquery.add_ellipsoid(a.norm(), self.rm.value)
        cadquery += _cadquery.add_rotation(a, angle)
        cadquery += _cadquery.add_translation(v)

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        v1x: types.McnpReal,
        v1y: types.McnpReal,
        v1z: types.McnpReal,
        v2x: types.McnpReal,
        v2y: types.McnpReal,
        v2z: types.McnpReal,
        v3x: types.McnpReal,
        v3y: types.McnpReal,
        v3z: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``Wedge``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.WEDGE
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if vx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if vz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v1x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v1y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v1z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v2x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v2y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v2z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v3x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v3y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if v3z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.v1x: Final[types.McnpReal] = v1x
        self.v1y: Final[types.McnpReal] = v1y
        self.v1z: Final[types.McnpReal] = v1z
        self.v2x: Final[types.McnpReal] = v2x
        self.v2y: Final[types.McnpReal] = v2y
        self.v2z: Final[types.McnpReal] = v2z
        self.v3x: Final[types.McnpReal] = v3x
        self.v3y: Final[types.McnpReal] = v3y
        self.v3z: Final[types.McnpReal] = v3z

        self.parameters: Final[tuple[types.McnpReal]] = (
            vx,
            vy,
            vz,
            v1x,
            v1y,
            v1z,
            v2x,
            v2y,
            v2z,
            v3x,
            v3y,
            v3z,
        )

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

        v = _cadquery.CqVectro(self.vx, self.vy, self.vz)
        v1 = _cadquery.CqVector(self.v1x, self.v1y, self.v1z)
        v2 = _cadquery.CqVector(self.v2x, self.v2y, self.v2z)
        v3 = _cadquery.CqVector(self.v3x, self.v3y, self.v3z)

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        cadquery += _cadquery.add_wedge(v1, v2, v3)
        cadquery += _cadquery.add_translation(v)

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        ax: types.McnpReal,
        ay: types.McnpReal,
        az: types.McnpReal,
        bx: types.McnpReal,
        by: types.McnpReal,
        bz: types.McnpReal,
        cx: types.McnpReal,
        cy: types.McnpReal,
        cz: types.McnpReal,
        dx: types.McnpReal,
        dy: types.McnpReal,
        dz: types.McnpReal,
        ex: types.McnpReal,
        ey: types.McnpReal,
        ez: types.McnpReal,
        fx: types.McnpReal,
        fy: types.McnpReal,
        fz: types.McnpReal,
        gx: types.McnpReal,
        gy: types.McnpReal,
        gz: types.McnpReal,
        hx: types.McnpReal,
        hy: types.McnpReal,
        hz: types.McnpReal,
        n1: types.McnpReal,
        n2: types.McnpReal,
        n3: types.McnpReal,
        n4: types.McnpReal,
        n5: types.McnpReal,
        n6: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        ``__init__`` initializes ``Polyhedron``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

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
            MCNPSemanticError: INVALID_SURFACE_NUMBER.
            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.
            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.
            MCNPSemanticError: INVALID_SURFACE_REFLECTING.
            MCNPSemanticError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC
            )

        if is_whiteboundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)

        _card.Card.__init__(self, number.value)
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[Surface.SurfaceMnemonic] = Surface.SurfaceMnemonic.POLYHEDRON
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        if ax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if ay is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if az is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if bx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if by is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if bz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if cx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if cy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if cz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if dx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if dy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if dz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if ex is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if ey is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if ez is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if fx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if fy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if fz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if gx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if gy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if gz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if hz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if n1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if n2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if n3 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if n4 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if n5 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        if n6 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)

        self.ax: Final[types.McnpReal] = ax
        self.ay: Final[types.McnpReal] = ay
        self.az: Final[types.McnpReal] = az
        self.bx: Final[types.McnpReal] = bx
        self.by: Final[types.McnpReal] = by
        self.bz: Final[types.McnpReal] = bz
        self.cx: Final[types.McnpReal] = cx
        self.cy: Final[types.McnpReal] = cy
        self.cz: Final[types.McnpReal] = cz
        self.dx: Final[types.McnpReal] = dx
        self.dy: Final[types.McnpReal] = dy
        self.dz: Final[types.McnpReal] = dz
        self.ex: Final[types.McnpReal] = ex
        self.ey: Final[types.McnpReal] = ey
        self.ez: Final[types.McnpReal] = ez
        self.fx: Final[types.McnpReal] = fx
        self.fy: Final[types.McnpReal] = fy
        self.fz: Final[types.McnpReal] = fz
        self.gx: Final[types.McnpReal] = gx
        self.gy: Final[types.McnpReal] = gy
        self.gz: Final[types.McnpReal] = gz
        self.hx: Final[types.McnpReal] = hx
        self.hy: Final[types.McnpReal] = hy
        self.hz: Final[types.McnpReal] = hz
        self.n1: Final[types.McnpReal] = n1
        self.n2: Final[types.McnpReal] = n2
        self.n3: Final[types.McnpReal] = n3
        self.n4: Final[types.McnpReal] = n4
        self.n5: Final[types.McnpReal] = n5
        self.n6: Final[types.McnpReal] = n6

        self.parameters: Final[tuple[types.McnpReal]] = (
            ax,
            ay,
            az,
            bx,
            by,
            bz,
            cx,
            cy,
            cz,
            dx,
            dy,
            dz,
            ex,
            ey,
            ez,
            fx,
            fy,
            fz,
            gx,
            gy,
            gz,
            hx,
            hy,
            hz,
            n1,
            n2,
            n3,
            n4,
            n5,
            n6,
        )
