"""
Contains classes representing INP surface cards.
"""

from . import _card
from . import _factory
from ..utils import types  # noqa
from ..utils import errors
from ..utils import _parser


class SurfaceMnemonic(_card.CardMnemonic):
    """
    Represents INP surface card mnemonics.

    ``SurfaceMnemonic`` implements ``_card.CardMnemonic``.
    """

    P = 'p'
    PX = 'px'
    PY = 'py'
    PZ = 'pz'
    SO = 'so'
    S = 's'
    SX = 'sx'
    SY = 'sy'
    SZ = 'sz'
    C_X = 'c/x'
    C_Y = 'c/y'
    C_Z = 'c/z'
    CX = 'cx'
    CY = 'cy'
    CZ = 'cz'
    K_X = 'k/x'
    K_Y = 'k/y'
    K_Z = 'k/z'
    KX = 'kx'
    KY = 'ky'
    KZ = 'kz'
    SQ = 'sq'
    GQ = 'gq'
    TX = 'tx'
    TY = 'ty'
    TZ = 'tz'
    X = 'x'
    Y = 'y'
    Z = 'z'
    BOX = 'box'
    RPP = 'rpp'
    SPH = 'sph'
    RCC = 'rcc'
    RHP = 'rhp'
    REC = 'rec'
    TRC = 'trc'
    ELL = 'ell'
    WED = 'wed'
    ARB = 'arb'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceMnemonic`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``SurfaceMnemonic``.

        Returns:
            ``SurfaceMnemonic`` object.

        Raises:
            McnpError: INVALID_SURFACE_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return SurfaceMnemonic(source)
        except ValueError:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_MNEMONIC)


class Surface(_card.Card):
    """
    Represents INP data cards.

    ``Surface`` extends the ``_card.Card`` abstract class.

    Attributes:
        ident: Card identifier.
        line_number: Card line number.
        comment: Card inline comment.
        number: Surface card number.
        mnemonic: Surface card type identifier.
        transform: Surface card transformation number.
        periodic: Surface card periodic number.
        parameters: Surface parameter list.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Surface``.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Surface``.
        """

        number_str = self.number.to_mcnp()
        transform_str = self.transform.to_mcnp() if self.transform is not None else ' '
        parameter_str = ' '.join(
            str(parameter.value) if hasattr(parameter, 'to_mcnp') else str(parameter)
            for parameter in self.parameters
        )

        source = f'{number_str} {transform_str} {self.mnemonic.to_mcnp()} {parameter_str}'

        return _parser.Postprocessor.add_continuation_lines(source)


_SurfacePFactory = _factory.SurfaceFactory(
    'p',
    [
        _factory.AttributeFactory(
            'a', 'types.McnpReal', 'Equation-defined general plane A coefficent', ''
        ),
        _factory.AttributeFactory(
            'b', 'types.McnpReal', 'Equation-defined general plane B coefficent', ''
        ),
        _factory.AttributeFactory(
            'c', 'types.McnpReal', 'Equation-defined general plane C coefficent', ''
        ),
        _factory.AttributeFactory(
            'd', 'types.McnpReal', 'Equation-defined general plane D coefficent', ''
        ),
    ],
)

_SurfacePxFactory = _factory.SurfaceFactory(
    'px',
    [
        _factory.AttributeFactory(
            'd', 'types.McnpReal', 'Normal-to-the-x-axis plane D coefficent', ''
        ),
    ],
)

_SurfacePyFactory = _factory.SurfaceFactory(
    'py',
    [
        _factory.AttributeFactory(
            'd', 'types.McnpReal', 'Normal-to-the-y-axis plane D coefficent', ''
        ),
    ],
)

_SurfacePzFactory = _factory.SurfaceFactory(
    'pz',
    [
        _factory.AttributeFactory(
            'd', 'types.McnpReal', 'Normal-to-the-z-axis plane D coefficent', ''
        ),
    ],
)

_SurfaceSoFactory = _factory.SurfaceFactory(
    'so',
    [
        _factory.AttributeFactory('r', 'types.McnpReal', 'Origin-centered sphere radius', ''),
    ],
)

_SurfaceSFactory = _factory.SurfaceFactory(
    's',
    [
        _factory.AttributeFactory('x', 'types.McnpReal', 'General sphere center x component', ''),
        _factory.AttributeFactory('y', 'types.McnpReal', 'General sphere center y component', ''),
        _factory.AttributeFactory('z', 'types.McnpReal', 'General sphere center z component', ''),
        _factory.AttributeFactory('r', 'types.McnpReal', 'General sphere radius', ''),
    ],
)

_SurfaceSxFactory = _factory.SurfaceFactory(
    'sx',
    [
        _factory.AttributeFactory('x', 'types.McnpReal', 'On-x-axis sphere center x component', ''),
        _factory.AttributeFactory('r', 'types.McnpReal', 'On-x-axis sphere radius', ''),
    ],
)

_SurfaceSyFactory = _factory.SurfaceFactory(
    'sy',
    [
        _factory.AttributeFactory('y', 'types.McnpReal', 'On-y-axis sphere center y component', ''),
        _factory.AttributeFactory('r', 'types.McnpReal', 'On-y-axis sphere radius', ''),
    ],
)

_SurfaceSzFactory = _factory.SurfaceFactory(
    'sz',
    [
        _factory.AttributeFactory('z', 'types.McnpReal', 'On-z-axis sphere center z component', ''),
        _factory.AttributeFactory('r', 'types.McnpReal', 'On-z-axis sphere radius', ''),
    ],
)

_SurfaceC_xFactory = _factory.SurfaceFactory(
    'c/x',
    [
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Parallel-to-x-axis cylinder center y component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Parallel-to-x-axis cylinder center z component', ''
        ),
        _factory.AttributeFactory('r', 'types.McnpReal', 'Parallel-to-x-axis cylinder radius', ''),
    ],
)

_SurfaceC_yFactory = _factory.SurfaceFactory(
    'c/y',
    [
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Parallel-to-y-axis cylinder center x component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Parallel-to-y-axis cylinder center z component', ''
        ),
        _factory.AttributeFactory('r', 'types.McnpReal', 'Parallel-to-y-axis cylinder radius', ''),
    ],
)

_SurfaceC_zFactory = _factory.SurfaceFactory(
    'c/z',
    [
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Parallel-to-z-axis cylinder center x component', ''
        ),
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Parallel-to-z-axis cylinder center y component', ''
        ),
        _factory.AttributeFactory('r', 'types.McnpReal', 'Parallel-to-z-axis cylinder radius', ''),
    ],
)

_SurfaceCxFactory = _factory.SurfaceFactory(
    'cx',
    [
        _factory.AttributeFactory('r', 'types.McnpReal', 'On-x-axis cylinder radius', ''),
    ],
)

_SurfaceCyFactory = _factory.SurfaceFactory(
    'cy',
    [
        _factory.AttributeFactory('r', 'types.McnpReal', 'On-y-axis cylinder radius', ''),
    ],
)

_SurfaceCzFactory = _factory.SurfaceFactory(
    'cz',
    [
        _factory.AttributeFactory('r', 'types.McnpReal', 'On-z-axis cylinder radius', ''),
    ],
)

_SurfaceK_xFactory = _factory.SurfaceFactory(
    'k/x',
    [
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Parallel-to-x-axis cone center x component', ''
        ),
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Parallel-to-x-axis cone center y component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Parallel-to-x-axis cone center z component', ''
        ),
        _factory.AttributeFactory(
            't_squared', 'types.McnpReal', 'Parallel-to-x-axis cone t^2 coefficent', ''
        ),
        _factory.AttributeFactory(
            'plusminus_1', 'types.McnpReal', 'Parallel-to-x-axis cone sheet selector', ''
        ),
    ],
)

_SurfaceK_yFactory = _factory.SurfaceFactory(
    'k/y',
    [
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Parallel-to-y-axis cone center x component', ''
        ),
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Parallel-to-y-axis cone center y component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Parallel-to-y-axis cone center z component', ''
        ),
        _factory.AttributeFactory(
            't_squared', 'types.McnpReal', 'Parallel-to-y-axis cone t^2 coefficent', ''
        ),
        _factory.AttributeFactory(
            'plusminus_1', 'types.McnpReal', 'Parallel-to-y-axis cone sheet selector', ''
        ),
    ],
)

_SurfaceK_zFactory = _factory.SurfaceFactory(
    'k/z',
    [
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Parallel-to-z-axis cone center x component', ''
        ),
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Parallel-to-z-axis cone center y component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Parallel-to-z-axis cone center z component', ''
        ),
        _factory.AttributeFactory(
            't_squared', 'types.McnpReal', 'Parallel-to-z-axis cone t^2 coefficent', ''
        ),
        _factory.AttributeFactory(
            'plusminus_1', 'types.McnpReal', 'Parallel-to-z-axis cone sheet selector', ''
        ),
    ],
)

_SurfaceKxFactory = _factory.SurfaceFactory(
    'kx',
    [
        _factory.AttributeFactory('x', 'types.McnpReal', 'On-x-axis cone center x component', ''),
        _factory.AttributeFactory(
            't_squared', 'types.McnpReal', 'On-x-axis cone t^2 coefficent', ''
        ),
        _factory.AttributeFactory(
            'plusminus_1', 'types.McnpReal', 'On-x-axis cone sheet selector', ''
        ),
    ],
)

_SurfaceKyFactory = _factory.SurfaceFactory(
    'ky',
    [
        _factory.AttributeFactory('y', 'types.McnpReal', 'On-y-axis cone center y component', ''),
        _factory.AttributeFactory(
            't_squared', 'types.McnpReal', 'On-y-axis cone t^2 coefficent', ''
        ),
        _factory.AttributeFactory(
            'plusminus_1', 'types.McnpReal', 'On-y-axis cone sheet selector', ''
        ),
    ],
)

_SurfaceKzFactory = _factory.SurfaceFactory(
    'kz',
    [
        _factory.AttributeFactory('z', 'types.McnpReal', 'On-z-axis cone center z component', ''),
        _factory.AttributeFactory(
            't_squared', 'types.McnpReal', 'On-z-axis cone t^2 coefficent', ''
        ),
        _factory.AttributeFactory(
            'plusminus_1', 'types.McnpReal', 'On-z-axis cone sheet selector', ''
        ),
    ],
)

_SurfaceSqFactory = _factory.SurfaceFactory(
    'sq',
    [
        _factory.AttributeFactory(
            'a', 'types.McnpReal', 'Oblique special quadratic A coefficent', ''
        ),
        _factory.AttributeFactory(
            'b', 'types.McnpReal', 'Oblique special quadratic B coefficent', ''
        ),
        _factory.AttributeFactory(
            'c', 'types.McnpReal', 'Oblique special quadratic C coefficent', ''
        ),
        _factory.AttributeFactory(
            'd', 'types.McnpReal', 'Oblique special quadratic D coefficent', ''
        ),
        _factory.AttributeFactory(
            'e', 'types.McnpReal', 'Oblique special quadratic E coefficent', ''
        ),
        _factory.AttributeFactory(
            'f', 'types.McnpReal', 'Oblique special quadratic F coefficent', ''
        ),
        _factory.AttributeFactory(
            'g', 'types.McnpReal', 'Oblique special quadratic G coefficent', ''
        ),
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Oblique special quadratic center x component', ''
        ),
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Oblique special quadratic center y component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Oblique special quadratic center z component', ''
        ),
    ],
)

_SurfaceGqFactory = _factory.SurfaceFactory(
    'gq',
    [
        _factory.AttributeFactory(
            'a', 'types.McnpReal', 'Oblique special quadratic A coefficent', ''
        ),
        _factory.AttributeFactory(
            'b', 'types.McnpReal', 'Oblique special quadratic B coefficent', ''
        ),
        _factory.AttributeFactory(
            'c', 'types.McnpReal', 'Oblique special quadratic C coefficent', ''
        ),
        _factory.AttributeFactory(
            'd', 'types.McnpReal', 'Oblique special quadratic D coefficent', ''
        ),
        _factory.AttributeFactory(
            'e', 'types.McnpReal', 'Oblique special quadratic E coefficent', ''
        ),
        _factory.AttributeFactory(
            'f', 'types.McnpReal', 'Oblique special quadratic F coefficent', ''
        ),
        _factory.AttributeFactory(
            'g', 'types.McnpReal', 'Oblique special quadratic G coefficent', ''
        ),
        _factory.AttributeFactory(
            'h', 'types.McnpReal', 'Oblique special quadratic H coefficent', ''
        ),
        _factory.AttributeFactory(
            'j', 'types.McnpReal', 'Oblique special quadratic J coefficent', ''
        ),
        _factory.AttributeFactory(
            'k', 'types.McnpReal', 'Oblique special quadratic K coefficent', ''
        ),
    ],
)

_SurfaceTxFactory = _factory.SurfaceFactory(
    'tx',
    [
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Parallel-to-x-axis tori center x component', ''
        ),
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Parallel-to-x-axis tori center y component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Parallel-to-x-axis tori center z component', ''
        ),
        _factory.AttributeFactory(
            'a', 'types.McnpReal', 'Parallel-to-x-axis tori A coefficent', ''
        ),
        _factory.AttributeFactory(
            'b', 'types.McnpReal', 'Parallel-to-x-axis tori B coefficent', ''
        ),
        _factory.AttributeFactory(
            'c', 'types.McnpReal', 'Parallel-to-x-axis tori C coefficent', ''
        ),
    ],
)

_SurfaceTyFactory = _factory.SurfaceFactory(
    'ty',
    [
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Parallel-to-y-axis tori center x component', ''
        ),
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Parallel-to-y-axis tori center y component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Parallel-to-y-axis tori center z component', ''
        ),
        _factory.AttributeFactory(
            'a', 'types.McnpReal', 'Parallel-to-y-axis tori A coefficent', ''
        ),
        _factory.AttributeFactory(
            'b', 'types.McnpReal', 'Parallel-to-y-axis tori B coefficent', ''
        ),
        _factory.AttributeFactory(
            'c', 'types.McnpReal', 'Parallel-to-y-axis tori C coefficent', ''
        ),
    ],
)

_SurfaceTzFactory = _factory.SurfaceFactory(
    'tz',
    [
        _factory.AttributeFactory(
            'x', 'types.McnpReal', 'Parallel-to-z-axis tori center x component', ''
        ),
        _factory.AttributeFactory(
            'y', 'types.McnpReal', 'Parallel-to-z-axis tori center y component', ''
        ),
        _factory.AttributeFactory(
            'z', 'types.McnpReal', 'Parallel-to-z-axis tori center z component', ''
        ),
        _factory.AttributeFactory(
            'a', 'types.McnpReal', 'Parallel-to-z-axis tori A coefficent', ''
        ),
        _factory.AttributeFactory(
            'b', 'types.McnpReal', 'Parallel-to-z-axis tori B coefficent', ''
        ),
        _factory.AttributeFactory(
            'c', 'types.McnpReal', 'Parallel-to-z-axis tori C coefficent', ''
        ),
    ],
)

_SurfaceXFactory = _factory.SurfaceFactory(
    'x',
    [
        _factory.AttributeFactory(
            'x1',
            'types.McnpReal',
            'X-axisymmetric point-defined surface point #1 x component',
            '',
        ),
        _factory.AttributeFactory(
            'r1', 'types.McnpReal', 'X-axisymmetric point-defined surface point #1 radius', ''
        ),
        _factory.AttributeFactory(
            'x2',
            'types.McnpReal',
            'X-axisymmetric point-defined surface point #2 x component',
            '',
        ),
        _factory.AttributeFactory(
            'r2', 'types.McnpReal', 'X-axisymmetric point-defined surface point #2 radius', ''
        ),
        _factory.AttributeFactory(
            'x3',
            'types.McnpReal',
            'X-axisymmetric point-defined surface point #3 x component',
            '',
        ),
        _factory.AttributeFactory(
            'r3', 'types.McnpReal', 'X-axisymmetric point-defined surface point #3 radius', ''
        ),
    ],
)

_SurfaceYFactory = _factory.SurfaceFactory(
    'y',
    [
        _factory.AttributeFactory(
            'y1',
            'types.McnpReal',
            'Y-axisymmetric point-defined surface point #1 y component',
            '',
        ),
        _factory.AttributeFactory(
            'r1', 'types.McnpReal', 'Y-axisymmetric point-defined surface point #1 radius', ''
        ),
        _factory.AttributeFactory(
            'y2',
            'types.McnpReal',
            'Y-axisymmetric point-defined surface point #2 y component',
            '',
        ),
        _factory.AttributeFactory(
            'r2', 'types.McnpReal', 'Y-axisymmetric point-defined surface point #2 radius', ''
        ),
        _factory.AttributeFactory(
            'y3',
            'types.McnpReal',
            'Y-axisymmetric point-defined surface point #3 y component',
            '',
        ),
        _factory.AttributeFactory(
            'r3', 'types.McnpReal', 'Y-axisymmetric point-defined surface point #3 radius', ''
        ),
    ],
)

_SurfaceZFactory = _factory.SurfaceFactory(
    'z',
    [
        _factory.AttributeFactory(
            'z1',
            'types.McnpReal',
            'Z-axisymmetric point-defined surface point #1 z component',
            '',
        ),
        _factory.AttributeFactory(
            'r1', 'types.McnpReal', 'Z-axisymmetric point-defined surface point #1 radius', ''
        ),
        _factory.AttributeFactory(
            'z2',
            'types.McnpReal',
            'Z-axisymmetric point-defined surface point #2 z component',
            '',
        ),
        _factory.AttributeFactory(
            'r2', 'types.McnpReal', 'Z-axisymmetric point-defined surface point #2 radius', ''
        ),
        _factory.AttributeFactory(
            'z3',
            'types.McnpReal',
            'Z-axisymmetric point-defined surface point #3 z component',
            '',
        ),
        _factory.AttributeFactory(
            'r3', 'types.McnpReal', 'Z-axisymmetric point-defined surface point #3 radius', ''
        ),
    ],
)

_SurfaceBoxFactory = _factory.SurfaceFactory(
    'box',
    [
        _factory.AttributeFactory(
            'vx', 'types.McnpReal', 'Box macrobody position vector x component', ''
        ),
        _factory.AttributeFactory(
            'vy', 'types.McnpReal', 'Box macrobody position vector y component', ''
        ),
        _factory.AttributeFactory(
            'vz', 'types.McnpReal', 'Box macrobody position vector z component', ''
        ),
        _factory.AttributeFactory(
            'a1x', 'types.McnpReal', 'Box macrobody vector #1 x component', ''
        ),
        _factory.AttributeFactory(
            'a1y', 'types.McnpReal', 'Box macrobody vector #1 y component', ''
        ),
        _factory.AttributeFactory(
            'a1z', 'types.McnpReal', 'Box macrobody vector #1 z component', ''
        ),
        _factory.AttributeFactory(
            'a2x', 'types.McnpReal', 'Box macrobody vector #2 x component', ''
        ),
        _factory.AttributeFactory(
            'a2y', 'types.McnpReal', 'Box macrobody vector #2 y component', ''
        ),
        _factory.AttributeFactory(
            'a2z', 'types.McnpReal', 'Box macrobody vector #2 z component', ''
        ),
        _factory.AttributeFactory(
            'a3x', 'types.McnpReal', 'Box macrobody vector #3 x component', ''
        ),
        _factory.AttributeFactory(
            'a3y', 'types.McnpReal', 'Box macrobody vector #3 y component', ''
        ),
        _factory.AttributeFactory(
            'a3z', 'types.McnpReal', 'Box macrobody vector #3 z component', ''
        ),
    ],
)

_SurfaceRppFactory = _factory.SurfaceFactory(
    'rpp',
    [
        _factory.AttributeFactory('xmin', 'types.McnpReal', 'Parallelepiped x termini minimum', ''),
        _factory.AttributeFactory('xmax', 'types.McnpReal', 'Parallelepiped x termini maximum', ''),
        _factory.AttributeFactory('ymin', 'types.McnpReal', 'Parallelepiped y termini minimum', ''),
        _factory.AttributeFactory('ymax', 'types.McnpReal', 'Parallelepiped y termini maximum', ''),
        _factory.AttributeFactory('zmin', 'types.McnpReal', 'Parallelepiped z termini minimum', ''),
        _factory.AttributeFactory('zmax', 'types.McnpReal', 'Parallelepiped z termini maximum', ''),
    ],
)

_SurfaceSphFactory = _factory.SurfaceFactory(
    'sph',
    [
        _factory.AttributeFactory(
            'vx', 'types.McnpReal', 'Sphere macrobody position vector x component', ''
        ),
        _factory.AttributeFactory(
            'vy', 'types.McnpReal', 'Sphere macrobody position vector y component', ''
        ),
        _factory.AttributeFactory(
            'vz', 'types.McnpReal', 'Sphere macrobody position vector z component', ''
        ),
        _factory.AttributeFactory('r', 'types.McnpReal', 'Sphere macrobody radius', ''),
    ],
)

_SurfaceRccFactory = _factory.SurfaceFactory(
    'rcc',
    [
        _factory.AttributeFactory(
            'vx',
            'types.McnpReal',
            'Circular cylinder macrobody position vector x component',
            '',
        ),
        _factory.AttributeFactory(
            'vy',
            'types.McnpReal',
            'Circular cylinder macrobody position vector y component',
            '',
        ),
        _factory.AttributeFactory(
            'vz',
            'types.McnpReal',
            'Circular cylinder macrobody position vector z component',
            '',
        ),
        _factory.AttributeFactory(
            'hx', 'types.McnpReal', 'Circular cylinder macrobody height vector x component', ''
        ),
        _factory.AttributeFactory(
            'hy', 'types.McnpReal', 'Circular cylinder macrobody height vector y component', ''
        ),
        _factory.AttributeFactory(
            'hz', 'types.McnpReal', 'Circular cylinder macrobody height vector z component', ''
        ),
        _factory.AttributeFactory('r', 'types.McnpReal', 'Circular cylinder macrobody radius', ''),
    ],
)

_SurfaceRhpFactory = _factory.SurfaceFactory(
    'rhp',
    [
        _factory.AttributeFactory(
            'vx', 'types.McnpReal', 'Hexagonal prism position vector x component', ''
        ),
        _factory.AttributeFactory(
            'vy', 'types.McnpReal', 'Hexagonal prism position vector y component', ''
        ),
        _factory.AttributeFactory(
            'vz', 'types.McnpReal', 'Hexagonal prism position vector z component', ''
        ),
        _factory.AttributeFactory(
            'hx', 'types.McnpReal', 'Hexagonal prism height vector x component', ''
        ),
        _factory.AttributeFactory(
            'hy', 'types.McnpReal', 'Hexagonal prism height vector y component', ''
        ),
        _factory.AttributeFactory(
            'hz', 'types.McnpReal', 'Hexagonal prism height vector z component', ''
        ),
        _factory.AttributeFactory(
            'r1', 'types.McnpReal', 'Hexagonal prism facet #1 vector x component', ''
        ),
        _factory.AttributeFactory(
            'r2', 'types.McnpReal', 'Hexagonal prism facet #1 vector y component', ''
        ),
        _factory.AttributeFactory(
            'r3', 'types.McnpReal', 'Hexagonal prism facet #1 vector z component', ''
        ),
        _factory.AttributeFactory(
            's1', 'types.McnpReal', 'Hexagonal prism facet #2 vector x component', ''
        ),
        _factory.AttributeFactory(
            's2', 'types.McnpReal', 'Hexagonal prism facet #2 vector y component', ''
        ),
        _factory.AttributeFactory(
            's3', 'types.McnpReal', 'Hexagonal prism facet #2 vector z component', ''
        ),
        _factory.AttributeFactory(
            't1', 'types.McnpReal', 'Hexagonal prism facet #3 vector x component', ''
        ),
        _factory.AttributeFactory(
            't2', 'types.McnpReal', 'Hexagonal prism facet #3 vector y component', ''
        ),
        _factory.AttributeFactory(
            't3', 'types.McnpReal', 'Hexagonal prism facet #3 vector z component', ''
        ),
    ],
)

_SurfaceRecFactory = _factory.SurfaceFactory(
    'rec',
    [
        _factory.AttributeFactory(
            'vx', 'types.McnpReal', 'Elliptical cylinder position vector x component', ''
        ),
        _factory.AttributeFactory(
            'vy', 'types.McnpReal', 'Elliptical cylinder position vector y component', ''
        ),
        _factory.AttributeFactory(
            'vz', 'types.McnpReal', 'Elliptical cylinder position vector z component', ''
        ),
        _factory.AttributeFactory(
            'hx', 'types.McnpReal', 'Elliptical cylinder height vector x component', ''
        ),
        _factory.AttributeFactory(
            'hy', 'types.McnpReal', 'Elliptical cylinder height vector y component', ''
        ),
        _factory.AttributeFactory(
            'hz', 'types.McnpReal', 'Elliptical cylinder height vector z component', ''
        ),
        _factory.AttributeFactory(
            'v1x', 'types.McnpReal', 'Elliptical cylinder major axis vector x component', ''
        ),
        _factory.AttributeFactory(
            'v1y', 'types.McnpReal', 'Elliptical cylinder major axis vector y component', ''
        ),
        _factory.AttributeFactory(
            'v1z', 'types.McnpReal', 'Elliptical cylinder major axis vector z component', ''
        ),
        _factory.AttributeFactory(
            'v2x', 'types.McnpReal', 'Elliptical cylinder minor axis vector x component', ''
        ),
        _factory.AttributeFactory(
            'v2y', 'types.McnpReal', 'Elliptical cylinder minor axis vector y component', ''
        ),
        _factory.AttributeFactory(
            'v2z', 'types.McnpReal', 'Elliptical cylinder minor axis vector z component', ''
        ),
    ],
)

_SurfaceTrcFactory = _factory.SurfaceFactory(
    'trc',
    [
        _factory.AttributeFactory(
            'vx', 'types.McnpReal', 'Truncated cone position vector x component', ''
        ),
        _factory.AttributeFactory(
            'vy', 'types.McnpReal', 'Truncated cone position vector y component', ''
        ),
        _factory.AttributeFactory(
            'vz', 'types.McnpReal', 'Truncated cone position vector z component', ''
        ),
        _factory.AttributeFactory(
            'hx', 'types.McnpReal', 'Truncated cone height vector x component', ''
        ),
        _factory.AttributeFactory(
            'hy', 'types.McnpReal', 'Truncated cone height vector y component', ''
        ),
        _factory.AttributeFactory(
            'hz', 'types.McnpReal', 'Truncated cone height vector z component', ''
        ),
        _factory.AttributeFactory('r1', 'types.McnpReal', 'Truncated cone lower cone radius', ''),
        _factory.AttributeFactory('r2', 'types.McnpReal', 'Truncated cone upper cone radius', ''),
    ],
)

_SurfaceEllFactory = _factory.SurfaceFactory(
    'ell',
    [
        _factory.AttributeFactory(
            'v1x', 'types.McnpReal', 'Ellipsoid focus #1 or center x component', ''
        ),
        _factory.AttributeFactory(
            'v1y', 'types.McnpReal', 'Ellipsoid focus #1 or center y component', ''
        ),
        _factory.AttributeFactory(
            'v1z', 'types.McnpReal', 'Ellipsoid focus #1 or center z component', ''
        ),
        _factory.AttributeFactory(
            'v2x', 'types.McnpReal', 'Ellipsoid focus #2 or major axis x component', ''
        ),
        _factory.AttributeFactory(
            'v2y', 'types.McnpReal', 'Ellipsoid focus #2 or major axis y component', ''
        ),
        _factory.AttributeFactory(
            'v2z', 'types.McnpReal', 'Ellipsoid focus #2 or major axis z component', ''
        ),
        _factory.AttributeFactory(
            'rm', 'types.McnpReal', 'Ellipsoid major/minor axis radius length', ''
        ),
    ],
)

_SurfaceWedFactory = _factory.SurfaceFactory(
    'wed',
    [
        _factory.AttributeFactory('vx', 'types.McnpReal', 'Wedge position vector x component', ''),
        _factory.AttributeFactory('vy', 'types.McnpReal', 'Wedge position vector y component', ''),
        _factory.AttributeFactory('vz', 'types.McnpReal', 'Wedge position vector z component', ''),
        _factory.AttributeFactory('v1x', 'types.McnpReal', 'Wedge side vector #1 x component', ''),
        _factory.AttributeFactory('v1y', 'types.McnpReal', 'Wedge side vector #1 y component', ''),
        _factory.AttributeFactory('v1z', 'types.McnpReal', 'Wedge side vector #1 z component', ''),
        _factory.AttributeFactory('v2x', 'types.McnpReal', 'Wedge side vector #2 x component', ''),
        _factory.AttributeFactory('v2y', 'types.McnpReal', 'Wedge side vector #2 y component', ''),
        _factory.AttributeFactory('v2z', 'types.McnpReal', 'Wedge side vector #2 z component', ''),
        _factory.AttributeFactory('v3x', 'types.McnpReal', 'Wedge height vector x component', ''),
        _factory.AttributeFactory('v3y', 'types.McnpReal', 'Wedge height vector y component', ''),
        _factory.AttributeFactory('v3z', 'types.McnpReal', 'Wedge height vector z component', ''),
    ],
)

_SurfaceArbFactory = _factory.SurfaceFactory(
    'arb',
    [
        _factory.AttributeFactory('ax', 'types.McnpReal', 'Polyhedron corner #1 x component', ''),
        _factory.AttributeFactory('ay', 'types.McnpReal', 'Polyhedron corner #1 y component', ''),
        _factory.AttributeFactory('az', 'types.McnpReal', 'Polyhedron corner #1 z component', ''),
        _factory.AttributeFactory('bx', 'types.McnpReal', 'Polyhedron corner #2 x component', ''),
        _factory.AttributeFactory('by', 'types.McnpReal', 'Polyhedron corner #2 y component', ''),
        _factory.AttributeFactory('bz', 'types.McnpReal', 'Polyhedron corner #2 z component', ''),
        _factory.AttributeFactory('cx', 'types.McnpReal', 'Polyhedron corner #3 x component', ''),
        _factory.AttributeFactory('cy', 'types.McnpReal', 'Polyhedron corner #3 y component', ''),
        _factory.AttributeFactory('cz', 'types.McnpReal', 'Polyhedron corner #3 z component', ''),
        _factory.AttributeFactory('dx', 'types.McnpReal', 'Polyhedron corner #4 x component', ''),
        _factory.AttributeFactory('dy', 'types.McnpReal', 'Polyhedron corner #4 y component', ''),
        _factory.AttributeFactory('dz', 'types.McnpReal', 'Polyhedron corner #4 z component', ''),
        _factory.AttributeFactory('ex', 'types.McnpReal', 'Polyhedron corner #5 x component', ''),
        _factory.AttributeFactory('ey', 'types.McnpReal', 'Polyhedron corner #5 y component', ''),
        _factory.AttributeFactory('ez', 'types.McnpReal', 'Polyhedron corner #5 z component', ''),
        _factory.AttributeFactory('fx', 'types.McnpReal', 'Polyhedron corner #6 x component', ''),
        _factory.AttributeFactory('fy', 'types.McnpReal', 'Polyhedron corner #6 y component', ''),
        _factory.AttributeFactory('fz', 'types.McnpReal', 'Polyhedron corner #6 z component', ''),
        _factory.AttributeFactory('gx', 'types.McnpReal', 'Polyhedron corner #7 x component', ''),
        _factory.AttributeFactory('gy', 'types.McnpReal', 'Polyhedron corner #7 y component', ''),
        _factory.AttributeFactory('gz', 'types.McnpReal', 'Polyhedron corner #7 z component', ''),
        _factory.AttributeFactory('hx', 'types.McnpReal', 'Polyhedron corner #8 x component', ''),
        _factory.AttributeFactory('hy', 'types.McnpReal', 'Polyhedron corner #8 y component', ''),
        _factory.AttributeFactory('hz', 'types.McnpReal', 'Polyhedron corner #8 z component', ''),
        _factory.AttributeFactory(
            'n1', 'types.McnpReal', 'Polyhedron four-digit side specificer #1', ''
        ),
        _factory.AttributeFactory(
            'n2', 'types.McnpReal', 'Polyhedron four-digit side specificer #2', ''
        ),
        _factory.AttributeFactory(
            'n3', 'types.McnpReal', 'Polyhedron four-digit side specificer #3', ''
        ),
        _factory.AttributeFactory(
            'n4', 'types.McnpReal', 'Polyhedron four-digit side specificer #4', ''
        ),
        _factory.AttributeFactory(
            'n5', 'types.McnpReal', 'Polyhedron four-digit side specificer #5', ''
        ),
        _factory.AttributeFactory(
            'n6', 'types.McnpReal', 'Polyhedron four-digit side specificer #6', ''
        ),
    ],
)

exec(_SurfacePFactory.build())
exec(_SurfacePxFactory.build())
exec(_SurfacePyFactory.build())
exec(_SurfacePzFactory.build())
exec(_SurfaceSoFactory.build())
exec(_SurfaceSFactory.build())
exec(_SurfaceSxFactory.build())
exec(_SurfaceSyFactory.build())
exec(_SurfaceSzFactory.build())
exec(_SurfaceC_xFactory.build())
exec(_SurfaceC_yFactory.build())
exec(_SurfaceC_zFactory.build())
exec(_SurfaceCxFactory.build())
exec(_SurfaceCyFactory.build())
exec(_SurfaceCzFactory.build())
exec(_SurfaceK_xFactory.build())
exec(_SurfaceK_yFactory.build())
exec(_SurfaceK_zFactory.build())
exec(_SurfaceKxFactory.build())
exec(_SurfaceKyFactory.build())
exec(_SurfaceKzFactory.build())
exec(_SurfaceSqFactory.build())
exec(_SurfaceGqFactory.build())
exec(_SurfaceTxFactory.build())
exec(_SurfaceTyFactory.build())
exec(_SurfaceTzFactory.build())
exec(_SurfaceXFactory.build())
exec(_SurfaceYFactory.build())
exec(_SurfaceZFactory.build())
exec(_SurfaceBoxFactory.build())
exec(_SurfaceRppFactory.build())
exec(_SurfaceSphFactory.build())
exec(_SurfaceRccFactory.build())
exec(_SurfaceRhpFactory.build())
exec(_SurfaceRecFactory.build())
exec(_SurfaceTrcFactory.build())
exec(_SurfaceEllFactory.build())
exec(_SurfaceWedFactory.build())
exec(_SurfaceArbFactory.build())
