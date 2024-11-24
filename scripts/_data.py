"""
Contains the ``CELL_OPTIONS`` ``SURFACE_CARDS``, and ``DATA_CARDS`` constants of INP metadata.,
"""

from typing import Final


class AttributeScheme:
    """
    Stores attribute metadata for metaprogramming.

    Attributes:
        name: Class attribute name.
        type: Class attribute type.
        descirption: Class attribute description for comments.
        restriction: Class attribute restriction from MCNP.
        error: Class attribute corresponding ``McnpError``.
    """

    def __init__(
        self,
        *,
        name: str = None,
        type: str = None,
        description: str = None,
        restriction: str = None,
        error: str = None,
    ):
        """
        Initializes ``AttributeScheme``.

        Parameters:
            name: Class attribute name.
            type: Class attribute type.
            descirption: Class attribute description for comments.
            restriction: Class attribute restriction from MCNP.
            error: Class attribute corresponding ``McnpError``.
        """

        self.name: Final[str] = name
        self.type: Final[str] = type
        self.description: Final[str] = description
        self.restriction: Final[str] = restriction
        self.error: Final[str] = error


class CellOptionScheme:
    """
    Stores ``CellOption`` metadata for metaprogramming.

    Attributes:
        name: ``CellOption`` subclass name.
        enum: ``CellOption`` subclass ``CellKeyword`` name.
        mnemonic: ``CellOption`` subclass ``CellKeyword`` value.
        attribute: ``CellOption`` subclass attribute.
    """

    def __init__(self, *, mnemonic: str = None, attributes: tuple[AttributeScheme] = None):
        """
        Initializes ``CellOptionScheme``.

        Parameters:
            mnemonic: ``CellOption`` subclass ``CellKeyword`` value.
            attributes: ``CellOption`` subclass attributes.
        """

        self.mnemonic: Final[str] = mnemonic
        self.attributes: Final[tuple[AttributeScheme]] = attributes

        self.name: Final[str] = mnemonic[0].upper() + mnemonic[1:]
        self.enum: Final[str] = mnemonic.upper()


CELL_OPTIONS: Final[tuple[CellOptionScheme]] = (
    CellOptionScheme(
        mnemonic='imp',
        attributes=(
            AttributeScheme(
                name='importance',
                type='types.McnpReal',
                description='Particle(s) importance in cell',
                restriction='',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='designator',
                type='types.Designator',
                description='Cell option particle designator',
                restriction='',
                error='INVALID_CELL_OPTION_DESIGNATOR',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='vol',
        attributes=(
            AttributeScheme(
                name='volume',
                type='types.McnpReal',
                description='Cell volume',
                restriction='volume >= 0',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='pwt',
        attributes=(
            AttributeScheme(
                name='weight',
                type='types.McnpReal',
                description='Cell weight of photons produced at neutron collisions',
                restriction='',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='ext',
        attributes=(
            AttributeScheme(
                name='stretch',
                type='str',
                description='Cell exponential transform stretching specifier',
                restriction='',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='designator',
                type='types.Designator',
                description='Cell option particle designator',
                restriction='',
                error='INVALID_CELL_OPTION_DESIGNATOR',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='fcl',
        attributes=(
            AttributeScheme(
                name='control',
                type='types.McnpReal',
                description='Cell forced-collision control.',
                restriction='-1 <= control <= 1',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='designator',
                type='types.Designator',
                description='Cell option particle designator',
                restriction='',
                error='INVALID_CELL_OPTION_DESIGNATOR',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='wwn',
        attributes=(
            AttributeScheme(
                name='bound',
                type='types.McnpReal',
                description='Cell weight-window space, time, or energy lower bound.',
                restriction='bound == -1 or bound >= 0',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Cell option suffix',
                restriction='',
                error='INVALID_CELL_OPTION_SUFFIX',
            ),
            AttributeScheme(
                name='designator',
                type='types.Designator',
                description='Cell option particle designator',
                restriction='',
                error='INVALID_CELL_OPTION_DESIGNATOR',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='dxc',
        attributes=(
            AttributeScheme(
                name='probability',
                type='types.McnpReal',
                description='Cell probability of DXTRAN contribution.',
                restriction='0 <= probability <= 1',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Cell option suffix',
                restriction='',
                error='INVALID_CELL_OPTION_SUFFIX',
            ),
            AttributeScheme(
                name='designator',
                type='types.Designator',
                description='Cell option particle designator',
                restriction='',
                error='INVALID_CELL_OPTION_DESIGNATOR',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='nonu',
        attributes=(
            AttributeScheme(
                name='setting',
                type='types.McnpInteger',
                description='Cell fission setting.',
                restriction='setting in {0, 1, 2}',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='pd',
        attributes=(
            AttributeScheme(
                name='probability',
                type='types.McnpReal',
                description='Cell probability of DXTRAN contribution.',
                restriction='0 <= probability <= 1',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Cell option suffix',
                restriction='',
                error='INVALID_CELL_OPTION_SUFFIX',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='tmp',
        attributes=(
            AttributeScheme(
                name='temperature',
                type='types.McnpReal',
                description='Cell temperature at suffix time index.',
                restriction='temperature > 0',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Cell option suffix',
                restriction='',
                error='INVALID_CELL_OPTION_SUFFIX',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='u',
        attributes=(
            AttributeScheme(
                name='number',
                type='types.McnpInteger',
                description='Cell universe number.',
                restriction='-99_999_999 <= number <= 99_999_999',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='trcl',
        attributes=(
            AttributeScheme(
                name='value',
                type='int',
                description='Cell coordinate transformation option value(s).',
                restriction='1 <= value <= 999',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='lat',
        attributes=(
            AttributeScheme(
                name='shape',
                type='types.McnpInteger',
                description='Cell lattice shape.',
                restriction='shape in {1, 2}',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='fill',
        attributes=(
            AttributeScheme(
                name='numbers',
                type='tuple[types.McnpInteger]',
                description='Fill cell option value or value(s) tuple.',
                restriction='0 <= entry <= 99_999_999',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='elpt',
        attributes=(
            AttributeScheme(
                name='cutoff',
                type='types.McnpReal',
                description='Cell energy cutoff.',
                restriction='',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='designator',
                type='types.Designator',
                description='Cell option particle designator',
                restriction='',
                error='INVALID_CELL_OPTION_DESIGNATOR',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='cosy',
        attributes=(
            AttributeScheme(
                name='number',
                type='types.McnpInteger',
                description='Cell cosy map number.',
                restriction='number in {1, 2, 3, 4, 5, 6}',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='bflcl',
        attributes=(
            AttributeScheme(
                name='number',
                type='types.McnpInteger',
                description='Cell magnetic field number.',
                restriction='number >= 0',
                error='INVALID_CELL_OPTION_VALUE',
            ),
        ),
    ),
    CellOptionScheme(
        mnemonic='unc',
        attributes=(
            AttributeScheme(
                name='setting',
                type='types.McnpInteger',
                description='Cell uncollided secondaries setting.',
                restriction='setting in {0, 1}',
                error='INVALID_CELL_OPTION_VALUE',
            ),
            AttributeScheme(
                name='designator',
                type='types.Designator',
                description='Cell option particle designator',
                restriction='',
                error='INVALID_CELL_OPTION_DESIGNATOR',
            ),
        ),
    ),
)


class SurfaceScheme:
    """
    Stores ``Surface`` metadata for metaprogramming.

    Attributes:
        name: ``Surface`` subclass name.
        enum: ``Surface`` subclass ``SurfaceMnemonic`` name.
        mnemonic: ``Surface`` subclass ``SurfaceMnemonic`` value.
        attributes: ``Surface`` subclass attributes.
    """

    def __init__(self, *, mnemonic: str = None, attributes: tuple[AttributeScheme] = None):
        """
        Initializes ``SurfaceScheme``.

        Parameters:
            mnemonic: ``Surface`` subclass ``SurfaceMnemonic`` value.
            attributes: ``Surface`` subclass attributes.
        """

        self.mnemonic: Final[str] = mnemonic
        self.attributes: Final[tuple[AttributeScheme]] = attributes

        self.name: Final[str] = mnemonic[0].upper() + mnemonic[1:]
        self.enum: Final[str] = mnemonic.upper()

        self.name = self.name.replace('/', '_')
        self.enum = self.enum.replace('/', '_')


SURFACE_CARDS: Final[tuple[SurfaceScheme]] = (
    SurfaceScheme(
        mnemonic='p',
        attributes=[
            AttributeScheme(
                name='a',
                type='types.McnpReal',
                description='Equation-defined general plane A coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='b',
                type='types.McnpReal',
                description='Equation-defined general plane B coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='c',
                type='types.McnpReal',
                description='Equation-defined general plane C coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='d',
                type='types.McnpReal',
                description='Equation-defined general plane D coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='px',
        attributes=[
            AttributeScheme(
                name='d',
                type='types.McnpReal',
                description='Normal-to-the-x-axis plane D coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='py',
        attributes=[
            AttributeScheme(
                name='d',
                type='types.McnpReal',
                description='Normal-to-the-y-axis plane D coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='pz',
        attributes=[
            AttributeScheme(
                name='d',
                type='types.McnpReal',
                description='Normal-to-the-z-axis plane D coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='so',
        attributes=[
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='Origin-centered sphere radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='s',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='General sphere center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='General sphere center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='General sphere center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='General sphere radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='sx',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='On-x-axis sphere center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='On-x-axis sphere radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='sy',
        attributes=[
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='On-y-axis sphere center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='On-y-axis sphere radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='sz',
        attributes=[
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='On-z-axis sphere center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='On-z-axis sphere radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='c/x',
        attributes=[
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Parallel-to-x-axis cylinder center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Parallel-to-x-axis cylinder center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='Parallel-to-x-axis cylinder radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='c/y',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Parallel-to-y-axis cylinder center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Parallel-to-y-axis cylinder center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='Parallel-to-y-axis cylinder radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='c/z',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Parallel-to-z-axis cylinder center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Parallel-to-z-axis cylinder center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='Parallel-to-z-axis cylinder radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='cx',
        attributes=[
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='On-x-axis cylinder radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='cy',
        attributes=[
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='On-y-axis cylinder radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='cz',
        attributes=[
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='On-z-axis cylinder radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='k/x',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Parallel-to-x-axis cone center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Parallel-to-x-axis cone center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Parallel-to-x-axis cone center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t_squared',
                type='types.McnpReal',
                description='Parallel-to-x-axis cone t^2 coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='plusminus_1',
                type='types.McnpReal',
                description='Parallel-to-x-axis cone sheet selector',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='k/y',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Parallel-to-y-axis cone center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Parallel-to-y-axis cone center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Parallel-to-y-axis cone center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t_squared',
                type='types.McnpReal',
                description='Parallel-to-y-axis cone t^2 coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='plusminus_1',
                type='types.McnpReal',
                description='Parallel-to-y-axis cone sheet selector',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='k/z',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Parallel-to-z-axis cone center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Parallel-to-z-axis cone center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Parallel-to-z-axis cone center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t_squared',
                type='types.McnpReal',
                description='Parallel-to-z-axis cone t^2 coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='plusminus_1',
                type='types.McnpReal',
                description='Parallel-to-z-axis cone sheet selector',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='kx',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='On-x-axis cone center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t_squared',
                type='types.McnpReal',
                description='On-x-axis cone t^2 coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='plusminus_1',
                type='types.McnpReal',
                description='On-x-axis cone sheet selector',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='ky',
        attributes=[
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='On-y-axis cone center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t_squared',
                type='types.McnpReal',
                description='On-y-axis cone t^2 coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='plusminus_1',
                type='types.McnpReal',
                description='On-y-axis cone sheet selector',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='kz',
        attributes=[
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='On-z-axis cone center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t_squared',
                type='types.McnpReal',
                description='On-z-axis cone t^2 coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='plusminus_1',
                type='types.McnpReal',
                description='On-z-axis cone sheet selector',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='sq',
        attributes=[
            AttributeScheme(
                name='a',
                type='types.McnpReal',
                description='Oblique special quadratic A coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='b',
                type='types.McnpReal',
                description='Oblique special quadratic B coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='c',
                type='types.McnpReal',
                description='Oblique special quadratic C coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='d',
                type='types.McnpReal',
                description='Oblique special quadratic D coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='e',
                type='types.McnpReal',
                description='Oblique special quadratic E coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='f',
                type='types.McnpReal',
                description='Oblique special quadratic F coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='g',
                type='types.McnpReal',
                description='Oblique special quadratic G coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Oblique special quadratic center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Oblique special quadratic center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Oblique special quadratic center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='gq',
        attributes=[
            AttributeScheme(
                name='a',
                type='types.McnpReal',
                description='Oblique special quadratic A coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='b',
                type='types.McnpReal',
                description='Oblique special quadratic B coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='c',
                type='types.McnpReal',
                description='Oblique special quadratic C coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='d',
                type='types.McnpReal',
                description='Oblique special quadratic D coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='e',
                type='types.McnpReal',
                description='Oblique special quadratic E coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='f',
                type='types.McnpReal',
                description='Oblique special quadratic F coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='g',
                type='types.McnpReal',
                description='Oblique special quadratic G coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='h',
                type='types.McnpReal',
                description='Oblique special quadratic H coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='j',
                type='types.McnpReal',
                description='Oblique special quadratic J coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='k',
                type='types.McnpReal',
                description='Oblique special quadratic K coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='tx',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Parallel-to-x-axis tori center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Parallel-to-x-axis tori center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Parallel-to-x-axis tori center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a',
                type='types.McnpReal',
                description='Parallel-to-x-axis tori A coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='b',
                type='types.McnpReal',
                description='Parallel-to-x-axis tori B coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='c',
                type='types.McnpReal',
                description='Parallel-to-x-axis tori C coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='ty',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Parallel-to-y-axis tori center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Parallel-to-y-axis tori center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Parallel-to-y-axis tori center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a',
                type='types.McnpReal',
                description='Parallel-to-y-axis tori A coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='b',
                type='types.McnpReal',
                description='Parallel-to-y-axis tori B coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='c',
                type='types.McnpReal',
                description='Parallel-to-y-axis tori C coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='tz',
        attributes=[
            AttributeScheme(
                name='x',
                type='types.McnpReal',
                description='Parallel-to-z-axis tori center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y',
                type='types.McnpReal',
                description='Parallel-to-z-axis tori center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z',
                type='types.McnpReal',
                description='Parallel-to-z-axis tori center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a',
                type='types.McnpReal',
                description='Parallel-to-z-axis tori A coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='b',
                type='types.McnpReal',
                description='Parallel-to-z-axis tori B coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='c',
                type='types.McnpReal',
                description='Parallel-to-z-axis tori C coefficent',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='x',
        attributes=[
            AttributeScheme(
                name='x1',
                type='types.McnpReal',
                description='X-axisymmetric point-defined surface point #1 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r1',
                type='types.McnpReal',
                description='X-axisymmetric point-defined surface point #1 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='x2',
                type='types.McnpReal',
                description='X-axisymmetric point-defined surface point #2 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r2',
                type='types.McnpReal',
                description='X-axisymmetric point-defined surface point #2 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='x3',
                type='types.McnpReal',
                description='X-axisymmetric point-defined surface point #3 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r3',
                type='types.McnpReal',
                description='X-axisymmetric point-defined surface point #3 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='y',
        attributes=[
            AttributeScheme(
                name='y1',
                type='types.McnpReal',
                description='Y-axisymmetric point-defined surface point #1 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r1',
                type='types.McnpReal',
                description='Y-axisymmetric point-defined surface point #1 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y2',
                type='types.McnpReal',
                description='Y-axisymmetric point-defined surface point #2 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r2',
                type='types.McnpReal',
                description='Y-axisymmetric point-defined surface point #2 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='y3',
                type='types.McnpReal',
                description='Y-axisymmetric point-defined surface point #3 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r3',
                type='types.McnpReal',
                description='Y-axisymmetric point-defined surface point #3 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='z',
        attributes=[
            AttributeScheme(
                name='z1',
                type='types.McnpReal',
                description='Z-axisymmetric point-defined surface point #1 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r1',
                type='types.McnpReal',
                description='Z-axisymmetric point-defined surface point #1 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z2',
                type='types.McnpReal',
                description='Z-axisymmetric point-defined surface point #2 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r2',
                type='types.McnpReal',
                description='Z-axisymmetric point-defined surface point #2 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='z3',
                type='types.McnpReal',
                description='Z-axisymmetric point-defined surface point #3 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r3',
                type='types.McnpReal',
                description='Z-axisymmetric point-defined surface point #3 radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='box',
        attributes=[
            AttributeScheme(
                name='vx',
                type='types.McnpReal',
                description='Box macrobody position vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vy',
                type='types.McnpReal',
                description='Box macrobody position vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vz',
                type='types.McnpReal',
                description='Box macrobody position vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a1x',
                type='types.McnpReal',
                description='Box macrobody vector #1 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a1y',
                type='types.McnpReal',
                description='Box macrobody vector #1 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a1z',
                type='types.McnpReal',
                description='Box macrobody vector #1 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a2x',
                type='types.McnpReal',
                description='Box macrobody vector #2 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a2y',
                type='types.McnpReal',
                description='Box macrobody vector #2 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a2z',
                type='types.McnpReal',
                description='Box macrobody vector #2 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a3x',
                type='types.McnpReal',
                description='Box macrobody vector #3 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a3y',
                type='types.McnpReal',
                description='Box macrobody vector #3 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='a3z',
                type='types.McnpReal',
                description='Box macrobody vector #3 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='rpp',
        attributes=[
            AttributeScheme(
                name='xmin',
                type='types.McnpReal',
                description='Parallelepiped x termini minimum',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='xmax',
                type='types.McnpReal',
                description='Parallelepiped x termini maximum',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='ymin',
                type='types.McnpReal',
                description='Parallelepiped y termini minimum',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='ymax',
                type='types.McnpReal',
                description='Parallelepiped y termini maximum',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='zmin',
                type='types.McnpReal',
                description='Parallelepiped z termini minimum',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='zmax',
                type='types.McnpReal',
                description='Parallelepiped z termini maximum',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='sph',
        attributes=[
            AttributeScheme(
                name='vx',
                type='types.McnpReal',
                description='Sphere macrobody position vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vy',
                type='types.McnpReal',
                description='Sphere macrobody position vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vz',
                type='types.McnpReal',
                description='Sphere macrobody position vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='Sphere macrobody radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='rcc',
        attributes=[
            AttributeScheme(
                name='vx',
                type='types.McnpReal',
                description='Circular cylinder macrobody position vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vy',
                type='types.McnpReal',
                description='Circular cylinder macrobody position vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vz',
                type='types.McnpReal',
                description='Circular cylinder macrobody position vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hx',
                type='types.McnpReal',
                description='Circular cylinder macrobody height vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hy',
                type='types.McnpReal',
                description='Circular cylinder macrobody height vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hz',
                type='types.McnpReal',
                description='Circular cylinder macrobody height vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r',
                type='types.McnpReal',
                description='Circular cylinder macrobody radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='rhp',
        attributes=[
            AttributeScheme(
                name='vx',
                type='types.McnpReal',
                description='Hexagonal prism position vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vy',
                type='types.McnpReal',
                description='Hexagonal prism position vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vz',
                type='types.McnpReal',
                description='Hexagonal prism position vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hx',
                type='types.McnpReal',
                description='Hexagonal prism height vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hy',
                type='types.McnpReal',
                description='Hexagonal prism height vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hz',
                type='types.McnpReal',
                description='Hexagonal prism height vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r1',
                type='types.McnpReal',
                description='Hexagonal prism facet #1 vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r2',
                type='types.McnpReal',
                description='Hexagonal prism facet #1 vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r3',
                type='types.McnpReal',
                description='Hexagonal prism facet #1 vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='s1',
                type='types.McnpReal',
                description='Hexagonal prism facet #2 vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='s2',
                type='types.McnpReal',
                description='Hexagonal prism facet #2 vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='s3',
                type='types.McnpReal',
                description='Hexagonal prism facet #2 vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t1',
                type='types.McnpReal',
                description='Hexagonal prism facet #3 vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t2',
                type='types.McnpReal',
                description='Hexagonal prism facet #3 vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='t3',
                type='types.McnpReal',
                description='Hexagonal prism facet #3 vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='rec',
        attributes=[
            AttributeScheme(
                name='vx',
                type='types.McnpReal',
                description='Elliptical cylinder position vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vy',
                type='types.McnpReal',
                description='Elliptical cylinder position vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vz',
                type='types.McnpReal',
                description='Elliptical cylinder position vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hx',
                type='types.McnpReal',
                description='Elliptical cylinder height vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hy',
                type='types.McnpReal',
                description='Elliptical cylinder height vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hz',
                type='types.McnpReal',
                description='Elliptical cylinder height vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v1x',
                type='types.McnpReal',
                description='Elliptical cylinder major axis vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v1y',
                type='types.McnpReal',
                description='Elliptical cylinder major axis vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v1z',
                type='types.McnpReal',
                description='Elliptical cylinder major axis vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2x',
                type='types.McnpReal',
                description='Elliptical cylinder minor axis vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2y',
                type='types.McnpReal',
                description='Elliptical cylinder minor axis vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2z',
                type='types.McnpReal',
                description='Elliptical cylinder minor axis vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='trc',
        attributes=[
            AttributeScheme(
                name='vx',
                type='types.McnpReal',
                description='Truncated cone position vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vy',
                type='types.McnpReal',
                description='Truncated cone position vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vz',
                type='types.McnpReal',
                description='Truncated cone position vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hx',
                type='types.McnpReal',
                description='Truncated cone height vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hy',
                type='types.McnpReal',
                description='Truncated cone height vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hz',
                type='types.McnpReal',
                description='Truncated cone height vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r1',
                type='types.McnpReal',
                description='Truncated cone lower cone radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='r2',
                type='types.McnpReal',
                description='Truncated cone upper cone radius',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='ell',
        attributes=[
            AttributeScheme(
                name='v1x',
                type='types.McnpReal',
                description='Ellipsoid focus #1 or center x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v1y',
                type='types.McnpReal',
                description='Ellipsoid focus #1 or center y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v1z',
                type='types.McnpReal',
                description='Ellipsoid focus #1 or center z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2x',
                type='types.McnpReal',
                description='Ellipsoid focus #2 or major axis x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2y',
                type='types.McnpReal',
                description='Ellipsoid focus #2 or major axis y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2z',
                type='types.McnpReal',
                description='Ellipsoid focus #2 or major axis z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='rm',
                type='types.McnpReal',
                description='Ellipsoid major/minor axis radius length',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='wed',
        attributes=[
            AttributeScheme(
                name='vx',
                type='types.McnpReal',
                description='Wedge position vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vy',
                type='types.McnpReal',
                description='Wedge position vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='vz',
                type='types.McnpReal',
                description='Wedge position vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v1x',
                type='types.McnpReal',
                description='Wedge side vector #1 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v1y',
                type='types.McnpReal',
                description='Wedge side vector #1 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v1z',
                type='types.McnpReal',
                description='Wedge side vector #1 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2x',
                type='types.McnpReal',
                description='Wedge side vector #2 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2y',
                type='types.McnpReal',
                description='Wedge side vector #2 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v2z',
                type='types.McnpReal',
                description='Wedge side vector #2 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v3x',
                type='types.McnpReal',
                description='Wedge height vector x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v3y',
                type='types.McnpReal',
                description='Wedge height vector y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='v3z',
                type='types.McnpReal',
                description='Wedge height vector z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
    SurfaceScheme(
        mnemonic='arb',
        attributes=[
            AttributeScheme(
                name='ax',
                type='types.McnpReal',
                description='Polyhedron corner #1 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='ay',
                type='types.McnpReal',
                description='Polyhedron corner #1 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='az',
                type='types.McnpReal',
                description='Polyhedron corner #1 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='bx',
                type='types.McnpReal',
                description='Polyhedron corner #2 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='by',
                type='types.McnpReal',
                description='Polyhedron corner #2 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='bz',
                type='types.McnpReal',
                description='Polyhedron corner #2 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='cx',
                type='types.McnpReal',
                description='Polyhedron corner #3 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='cy',
                type='types.McnpReal',
                description='Polyhedron corner #3 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='cz',
                type='types.McnpReal',
                description='Polyhedron corner #3 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='dx',
                type='types.McnpReal',
                description='Polyhedron corner #4 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='dy',
                type='types.McnpReal',
                description='Polyhedron corner #4 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='dz',
                type='types.McnpReal',
                description='Polyhedron corner #4 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='ex',
                type='types.McnpReal',
                description='Polyhedron corner #5 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='ey',
                type='types.McnpReal',
                description='Polyhedron corner #5 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='ez',
                type='types.McnpReal',
                description='Polyhedron corner #5 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='fx',
                type='types.McnpReal',
                description='Polyhedron corner #6 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='fy',
                type='types.McnpReal',
                description='Polyhedron corner #6 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='fz',
                type='types.McnpReal',
                description='Polyhedron corner #6 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='gx',
                type='types.McnpReal',
                description='Polyhedron corner #7 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='gy',
                type='types.McnpReal',
                description='Polyhedron corner #7 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='gz',
                type='types.McnpReal',
                description='Polyhedron corner #7 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hx',
                type='types.McnpReal',
                description='Polyhedron corner #8 x component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hy',
                type='types.McnpReal',
                description='Polyhedron corner #8 y component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='hz',
                type='types.McnpReal',
                description='Polyhedron corner #8 z component',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='n1',
                type='types.McnpReal',
                description='Polyhedron four-digit side specificer #1',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='n2',
                type='types.McnpReal',
                description='Polyhedron four-digit side specificer #2',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='n3',
                type='types.McnpReal',
                description='Polyhedron four-digit side specificer #3',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='n4',
                type='types.McnpReal',
                description='Polyhedron four-digit side specificer #4',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='n5',
                type='types.McnpReal',
                description='Polyhedron four-digit side specificer #5',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
            AttributeScheme(
                name='n6',
                type='types.McnpReal',
                description='Polyhedron four-digit side specificer #6',
                restriction='',
                error='INVALID_SURFACE_PARAMETER',
            ),
        ],
    ),
)


class DataEntryScheme:
    """
    Stores ``DataEntry`` metadata for metaprogramming.

    Attributes:
        name: ``DataEntry`` subclass name.
        enum: ``DataEntry`` subclass ``DataKeyword`` name.
        mnemonic: ``DataEntry`` subclass ``DataKeyword`` value.
        attributes: ``DataEntry`` subclass attributes.
    """

    def __init__(
        self, *, name: str = None, mnemonic: str = None, attributes: tuple[AttributeScheme] = None
    ):
        """
        Initializes ``DataEntryScheme``.

        Parameters:
            mnemonic: ``DataEntry`` subclass ``DataKeyword`` value.
            attributes: ``DataEntry`` subclass attributes.
        """

        self.mnemonic: Final[str] = mnemonic
        self.attributes: Final[tuple[AttributeScheme]] = attributes

        self.name: Final[str] = mnemonic[0].upper() + mnemonic[1:]
        self.enum: Final[str] = mnemonic.upper()


class DataOptionScheme:
    """
    Stores ``DataOption`` metadata for metaprogramming.

    Attributes:
        name: ``DataOption`` subclass name.
        enum: ``DataOption`` subclass ``DataKeyword`` name.
        mnemonic: ``DataOption`` subclass ``DataKeyword`` value.
        attribute: ``DataOption`` subclass attribute.
    """

    def __init__(self, *, mnemonic: str = None, attribute: AttributeScheme = None):
        """
        Initializes ``DataOptionScheme``.

        Parameters:
            mnemonic: ``DataOption`` subclass ``DataKeyword`` value.
            attribute: ``DataOption`` subclass attribute.
        """

        self.mnemonic: Final[str] = mnemonic
        self.attribute: Final[AttributeScheme] = attribute

        self.name: Final[str] = mnemonic[0].upper() + mnemonic[1:]
        self.enum: Final[str] = mnemonic.upper()


class DataScheme:
    """
    Stores ``Data`` metadata for metaprogramming.

    Attributes:
        name: ``Data`` subclass name.
        enum: ``Data`` subclass ``DataMnemonic`` name.
        mnemonic: ``Data`` subclass ``DataMnemonic`` value.
        entries: ``Data`` subclass entries.
        options: ``Data`` subclass options.
        attributes: ``Data`` subclass attributes.
    """

    def __init__(
        self,
        *,
        mnemonic: str = None,
        entries: list[DataEntryScheme],
        options: list[DataOptionScheme],
        attributes: list[AttributeScheme] = None,
    ):
        """
        Initializes ``DataScheme``.

        Parameters:
            mnemonic: ``Data`` subclass ``DataMnemonic`` value.
            entries: ``Data`` subclass entries.
            options: ``Data`` subclass options.
            attributes: ``Data`` subclass attributes.
        """

        self.mnemonic: Final[str] = mnemonic
        self.entries: Final[tuple[DataEntryScheme]] = tuple(entries)
        self.options: Final[tuple[DataOptionScheme]] = tuple(options)
        self.attributes: Final[tuple[AttributeScheme]] = tuple(attributes)

        self.name: Final[str] = mnemonic[0].upper() + mnemonic[1:]
        self.enum: Final[str] = mnemonic.upper()


DATA_CARDS: Final[tuple[DataScheme]] = (
    DataScheme(
        mnemonic='area',
        attributes=[
            AttributeScheme(
                name='areas',
                type='tuple[types.McnpReal]',
                description='Tuple of surface areas',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='tr',
        attributes=[
            AttributeScheme(
                name='displacement',
                type='TrDisplacementEntry',
                description='Tuple for displacement vector',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='rotation',
                type='TrRotationEntry',
                description='Tuple for rotation matrix',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='system',
                type='types.McnpInteger',
                description='Coordinate system setting',
                restriction='system == -1 or system == 1',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[
            DataEntryScheme(
                mnemonic='TrDisplacement',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.McnpReal',
                        description='Displacement vector x component',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.McnpReal',
                        description='Displacement vector y component',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.McnpReal',
                        description='Displacement vector z component',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                ],
            ),
            DataEntryScheme(
                mnemonic='TrRotation',
                attributes=[
                    AttributeScheme(
                        name='xx',
                        type='types.McnpReal',
                        description="Rotation matrix xx' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='xy',
                        type='types.McnpReal',
                        description="Rotation matrix xy' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='xz',
                        type='types.McnpReal',
                        description="Rotation matrix xz' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='yx',
                        type='types.McnpReal',
                        description="Rotation matrix yx' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='yy',
                        type='types.McnpReal',
                        description="Rotation matrix yy' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='yz',
                        type='types.McnpReal',
                        description="Rotation matrix yz' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='zx',
                        type='types.McnpReal',
                        description="Rotation matrix zx' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='zy',
                        type='types.McnpReal',
                        description="Rotation matrix zy' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='zz',
                        type='types.McnpReal',
                        description="Rotation matrix zz' component",
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                ],
            ),
        ],
        options=[],
    ),
    DataScheme(
        mnemonic='u',
        attributes=[
            AttributeScheme(
                name='numbers',
                type='tuple[types.McnpInteger]',
                description='Tuple of cell numbers',
                restriction='1 <= entry <= 99_999_999',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='lat',
        attributes=[
            AttributeScheme(
                name='types',
                type='tuple[types.McnpInteger]',
                description='Tuple of lattice types',
                restriction='entry == 1 or entry == 2',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='fill',
        attributes=[
            AttributeScheme(
                name='numbers',
                type='tuple[types.McnpInteger]',
                description='Tuple of universe numbers',
                restriction='0 <= entry <= 99_999_999',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='uran',
        attributes=[
            AttributeScheme(
                name='transformations',
                type='tuple[UranEntry]',
                description='Tuple of stochastic transformations',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[
            DataEntryScheme(
                mnemonic='uran',
                attributes=[
                    AttributeScheme(
                        name='number',
                        type='types.McnpInteger',
                        description='Universe number for transformation',
                        restriction='0 <= number <= 99_999_999',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='maximum_x',
                        type='types.McnpReal',
                        description='Maximum displacement in the x direction',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='maximum_y',
                        type='types.McnpReal',
                        description='Maximum displacement in the y direction',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='maximum_z',
                        type='types.McnpReal',
                        description='Maximum displacement in the z direction',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                ],
            )
        ],
        options=[],
    ),
    DataScheme(
        mnemonic='dm',
        attributes=[
            AttributeScheme(
                name='zaids',
                type='tuple[types.Zaid]',
                description='Tuple of ZAID aliases',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='embed',
        attributes=[
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='background',
                attribute=AttributeScheme(
                    name='number',
                    type='types.McnpInteger',
                    description='Background pseudo-cell number',
                    restriction='1 <= number <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='meshgeo',
                attribute=AttributeScheme(
                    name='form',
                    type='str',
                    description='Format specification of the embedded mesh input file',
                    restriction='form in {"lnk3dnt", "abaqu", "mcnpum"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='mgeoin',
                attribute=AttributeScheme(
                    name='filename',
                    type='str',
                    description='Name of the input file containing the mesh description',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='meeout',
                attribute=AttributeScheme(
                    name='filename',
                    type='str',
                    description='Name assigned to EEOUT, the elemental edit output file',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='meein',
                attribute=AttributeScheme(
                    name='filename',
                    type='str',
                    description='Name of the EEOUT results file to read',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='calcvols',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Yes/no calculate the inferred geometry cell information',
                    restriction='setting in {"yes", "no"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='debug',
                attribute=AttributeScheme(
                    name='parameter',
                    type='str',
                    description='Debug parameter',
                    restriction='parameter in {"echomesh"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='filetype',
                attribute=AttributeScheme(
                    name='kind',
                    type='str',
                    description='File type for the elemental edit output file',
                    restriction='type in {"ascii", "binary"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='gmvfile',
                attribute=AttributeScheme(
                    name='filename',
                    type='str',
                    description='Name of the GMV output file',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='length',
                attribute=AttributeScheme(
                    name='factor',
                    type='types.McnpReal',
                    description='Conversion factor to centimeters for all mesh dimentions',
                    restriction='factor > 0',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='mcnpumfile',
                attribute=AttributeScheme(
                    name='filename',
                    type='str',
                    description='Name of the MCNPUM output file',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='embee',
        attributes=[
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='embed',
                attribute=AttributeScheme(
                    name='number',
                    type='types.McnpInteger',
                    description='Embedded mesh universe number',
                    restriction='0 <= number <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='energy',
                attribute=AttributeScheme(
                    name='factor',
                    type='types.McnpReal',
                    description='Multiplicative conversion factor for energy-related output',
                    restriction='factor > 0',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='time',
                attribute=AttributeScheme(
                    name='factor',
                    type='types.McnpReal',
                    description='Multiplicative conversion factor for time-related output',
                    restriction='factor > 0',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='atom',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Flag to multiply by atom density',
                    restriction='setting in {"yes", "no"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='factor',
                attribute=AttributeScheme(
                    name='constant',
                    type='types.McnpReal',
                    description='Multiplicative constant',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='mat',
                attribute=AttributeScheme(
                    name='number',
                    type='types.McnpInteger',
                    description='Material number',
                    restriction='0 <= number <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='mtype',
                attribute=AttributeScheme(
                    name='kind',
                    type='str',
                    description='Multiplier type',
                    restriction='type in {"flux", "isotropic", "population", "reaction", "source", "track"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='embeb',
        attributes=[
            AttributeScheme(
                name='bounds',
                type='tuple[types.McnpReal]',
                description='Tuple of upper energy bounds',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='embem',
        attributes=[
            AttributeScheme(
                name='multipliers',
                type='tuple[types.McnpReal]',
                description='Tuple of energy multipliers',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='embtb',
        attributes=[
            AttributeScheme(
                name='bounds',
                type='tuple[types.McnpReal]',
                description='Tuple of upper time bounds',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='embtm',
        attributes=[
            AttributeScheme(
                name='multipliers',
                type='tuple[types.McnpReal]',
                description='Tuple of time multipliers',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='embdb',
        attributes=[
            AttributeScheme(
                name='bounds',
                type='tuple[types.McnpReal]',
                description='Tuple of upper dose energy bounds',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='embdf',
        attributes=[
            AttributeScheme(
                name='multipliers',
                type='tuple[types.McnpReal]',
                description='Tuple of dose energy multipliers',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='m',
        attributes=[
            AttributeScheme(
                name='substances',
                type='tuple[MEntry]',
                description='Tuple of material constituents',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[
            DataEntryScheme(
                mnemonic='m',
                attributes=[
                    AttributeScheme(
                        name='zaid',
                        type='types.Zaid',
                        description='Substance ZAID alias',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='fraction',
                        type='types.McnpReal',
                        description='Substance fraction',
                        restriction='-1 <= fraction <= 1',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                ],
            ),
        ],
        options=[
            DataOptionScheme(
                mnemonic='gas',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Flag for density-effect correction to electron stopping power',
                    restriction='setting in {"yes", "no"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='estep',
                attribute=AttributeScheme(
                    name='step',
                    type='types.McnpInteger',
                    description='Number of electron sub-step per energy step',
                    restriction='step >= 0',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='hstep',
                attribute=AttributeScheme(
                    name='step',
                    type='types.McnpInteger',
                    description='Number of proton sub-step per energy step',
                    restriction='step >= 0',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='nlib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default neutron table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='plib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default photoatomic table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='pnlib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default photonuclear table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='elib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default electron table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='hlib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default proton table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='alib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default alpha table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='slib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default helion table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='tlib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default triton table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='dlib',
                attribute=AttributeScheme(
                    name='abx',
                    type='str',
                    description='Default deuteron table identifier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='cond',
                attribute=AttributeScheme(
                    name='setting',
                    type='types.McnpReal',
                    description='Conduction state for EL03 electron-transport evaluation',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='refi',
                attribute=AttributeScheme(
                    name='refractive_index',
                    type='types.McnpReal',
                    description='Refractive index constant',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='refc',
                attribute=AttributeScheme(
                    name='coefficents',
                    type='tuple[types.McnpReal]',
                    description='Cauchy coefficents',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='refs',
                attribute=AttributeScheme(
                    name='coefficents',
                    type='tuple[types.McnpReal]',
                    description='Sellmeier coefficents',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='mt',
        attributes=[
            AttributeScheme(
                name='identifier',
                type='str',
                description='Corresponding S(α,β) identifier',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='otfdb',
        attributes=[
            AttributeScheme(
                name='zaids',
                type='tuple[types.Zaid]',
                description='Identifiers for the broadening tables',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='nonu',
        attributes=[
            AttributeScheme(
                name='settings',
                type='tuple[types.McnpInteger]',
                description='Tuple of fission settings',
                restriction='entry == 0 or entry == 1 or entry == 2',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='awtab',
        attributes=[
            AttributeScheme(
                name='weight_ratios',
                type='tuple[AwtabEntry]',
                description='Tuple of atomic weight ratios',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[
            DataEntryScheme(
                mnemonic='awtab',
                attributes=[
                    AttributeScheme(
                        name='zaid',
                        type='types.Zaid',
                        description='Zaid alias for nuclide',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='weight_ratio',
                        type='types.McnpReal',
                        description='Atomic weight ratios',
                        restriction='weight_ratio > 0',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                ],
            ),
        ],
        options=[],
    ),
    DataScheme(
        mnemonic='xs',
        attributes=[
            AttributeScheme(
                name='weight_ratios',
                type='tuple[XsEntry]',
                description='Tuple of atomic weight ratios',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[
            DataEntryScheme(
                mnemonic='xs',
                attributes=[
                    AttributeScheme(
                        name='zaid',
                        type='types.Zaid',
                        description='Zaid alias for nuclide',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='weight_ratio',
                        type='types.McnpReal',
                        description='Atomic weight ratios',
                        restriction='weight_ratio > 0',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                ],
            ),
        ],
        options=[],
    ),
    DataScheme(
        mnemonic='void',
        attributes=[
            AttributeScheme(
                name='numbers',
                type='tuple[types.McnpInteger]',
                description='Tuple of cell numbers',
                restriction='1 <= entry <= 99_999_999',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='mgopt',
        attributes=[
            AttributeScheme(
                name='mcal',
                type='str',
                description='Problem type setting',
                restriction='mcal in {"f", "a"}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='igm',
                type='types.McnpInteger',
                description='Total number of energy groups for all kinds of particle',
                restriction='igm >= 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='iplt',
                type='types.McnpInteger',
                description='Weight windows usage indicator',
                restriction='iplt == 0 or iplt == 1 or iplt == 2',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='iab',
                type='types.McnpInteger',
                description='Adjoint biasing for adjoint problems contorls',
                restriction='iab == 0 or iab == 1 or iab == 2',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='icw',
                type='types.McnpInteger',
                description='Name of the reference cell for generated weight windows',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='fnw',
                type='types.McnpReal',
                description='Normalization value for generated weight windows',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='rim',
                type='types.McnpReal',
                description='Generated weight windows compression limit',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='drxs',
        attributes=[
            AttributeScheme(
                name='zaids',
                type='tuple[types.Zaid]',
                description='Tuple of ZAID aliases',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='mode',
        attributes=[
            AttributeScheme(
                name='particles',
                type='tuple[types.Designator]',
                description='Tuple of particle designators',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='act',
        attributes=[
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            )
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='fission',
                attribute=AttributeScheme(
                    name='kind',
                    type='str',
                    description='Type of delayed particle(s) to be produced from residuals created by fission',
                    restriction='type in {"none", "n,p,e,f,a", "all"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='nonfiss',
                attribute=AttributeScheme(
                    name='kind',
                    type='str',
                    description='Type of delayed particle(s) to be produced by simple multi-particle reaction',
                    restriction='type in {"none", "n,p,e,f,a", "all"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='dn',
                attribute=AttributeScheme(
                    name='source',
                    type='str',
                    description='Delayed neutron data source',
                    restriction='source in {"model", "library", "both", "prompt"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='dg',
                attribute=AttributeScheme(
                    name='source',
                    type='str',
                    description='Delayed gamma data source',
                    restriction='source in {"line", "mg", "none"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='thresh',
                attribute=AttributeScheme(
                    name='fraction',
                    type='types.McnpReal',
                    description='Fraction of highest-amplitude discrete delayed-gamma lines retained',
                    restriction='0 <= fraction, <= 1',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='dnbais',
                attribute=AttributeScheme(
                    name='count',
                    type='types.McnpInteger',
                    description='Maximum number of neutrons generated per reaction',
                    restriction='0 <= count <= 10',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='nap',
                attribute=AttributeScheme(
                    name='count',
                    type='types.McnpInteger',
                    description='Number of activation products',
                    restriction='0 <= count',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='pecut',
                attribute=AttributeScheme(
                    name='cutoff',
                    type='types.McnpReal',
                    description='Delayed-gamma energy cutoff',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='hlcut',
                attribute=AttributeScheme(
                    name='cutoff',
                    type='types.McnpReal',
                    description='Spontaneous-decay half-life threshold',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='sample',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Flag for correlated or uncorrelated',
                    restriction='setting in {"correlate", "nonfiss_cor"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='cut',
        attributes=[
            AttributeScheme(
                name='time_cutoff',
                type='types.McnpReal',
                description='Time cutoff in shakes',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='energy_cutoff',
                type='types.McnpReal',
                description='Lower energy cutoff',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='weight_cutoff1',
                type='types.McnpReal',
                description='Weight cutoff #1',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='weight_cutoff2',
                type='types.McnpReal',
                description='Weight cutoff #2',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='source_weight',
                type='types.McnpReal',
                description='Minimum source weight',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='elpt',
        attributes=[
            AttributeScheme(
                name='cutoffs',
                type='tuple[types.McnpReal]',
                description='Tuple of cell lower energy cutoffs',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='thtme',
        attributes=[
            AttributeScheme(
                name='times',
                type='tuple[types.McnpReal]',
                description='Tuple of times when thermal temperatures are specified',
                restriction='entry <= 99',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='lca',
        attributes=[
            AttributeScheme(
                name='ielas',
                type='types.McnpInteger',
                description='Elastic scattering controls',
                restriction='ielas == 0 or ielas == 1 or ielas == 2',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ipreg',
                type='types.McnpInteger',
                description='pre-equilibrium model',
                restriction='ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='iexisa',
                type='types.McnpInteger',
                description='Model choice controls',
                restriction='iexisa == 0 or iexisa == 1 or iexisa == 2',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ichoic',
                type='types.McnpInteger',
                description='ISABEL intranuclear cascade model control',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='jcoul',
                type='types.McnpInteger',
                description='Coulomb barrier for incident charged particle controls',
                restriction='jcoul == 0 or jcoul == 1',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='nexite',
                type='types.McnpInteger',
                description='Subtract nuclear recoil energy to get excitation energy',
                restriction='nexite == 0 or nexite == 1',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='npidk',
                type='types.McnpInteger',
                description='Cutoff interact/terminate control',
                restriction='npidk == 0 or npidk == 1',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='noact',
                type='types.McnpInteger',
                description='Particle transport settings',
                restriction='noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='icem',
                type='types.McnpInteger',
                description='Choose alternative physics model',
                restriction='icem == 0 or icem == 1 or icem == 2',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ilaq',
                type='types.McnpInteger',
                description='Choose light ion and nucleon physics modules',
                restriction='ilaq == 0 or ilaq == 1',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='nevtype',
                type='types.McnpInteger',
                description='Choose number of evaporation particles for GEM2',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='lcb',
        attributes=[
            AttributeScheme(
                name='flenb1',
                type='types.McnpReal',
                description='Kinetic energy for nucleons CEM/Bertini/INCL',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='flenb2',
                type='types.McnpReal',
                description='Kinetic energy for nucleons LAQGSM03.03',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='flenb3',
                type='types.McnpReal',
                description='Kinetic energy for pions CEM/Bertini/INCL',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='flenb4',
                type='types.McnpReal',
                description='Kinetic energy for pions LAQGSM03.03',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='flenb5',
                type='types.McnpReal',
                description='Kinetic energy for nucleons ISABEL',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='flenb6',
                type='types.McnpReal',
                description='Kinetic energy for appropriate model',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='cotfe',
                type='types.McnpReal',
                description='Cutoff kinetic energy for particle escape',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='film0',
                type='types.McnpReal',
                description='Maximum correction allowed for masss-energy balancing',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='lcc',
        attributes=[
            AttributeScheme(
                name='stincl',
                type='types.McnpReal',
                description='Rescaling factor of the cascade duration',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='v0incl',
                type='types.McnpReal',
                description='Potential depth',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='xfoisaincl',
                type='types.McnpReal',
                description='Maximum impact parameter for Pauli blocking',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='npaulincl',
                type='types.McnpInteger',
                description='Pauli blocking parameter setting',
                restriction='npaulincl == 0 or npaulincl == -1 or npaulincl == 1',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='nosurfincl',
                type='types.McnpInteger',
                description='Difuse nuclear surface based on Wood-Saxon density setting',
                restriction='xfoisaincl == -2 or xfoisaincl == -1 or xfoisaincl == 0 or xfoisaincl == 1',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ecutincl',
                type='types.McnpReal',
                description='Bertini model energy below this energy',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ebankincl',
                type='types.McnpReal',
                description='INCL bank particles below this energy',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ebankabia',
                type='types.McnpReal',
                description='ABLA bank particles below this energy',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='lae',
        attributes=[
            AttributeScheme(
                name='ipht',
                type='types.McnpInteger',
                description='Generation of de-excitation photons setting',
                restriction='ipht.value in {0, 1}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='icc',
                type='types.McnpInteger',
                description='Level of physics for PHT physics setting',
                restriction='icc.value in {0, 1, 2, 3, 4}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='nobalc',
                type='types.McnpInteger',
                description='Mass-energy balancing in cascade setting',
                restriction='nobalc.value in {0, 1}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='nobale',
                type='types.McnpInteger',
                description='Mass-energy balancing in evaporation setting',
                restriction='nobale.value in {0, 1}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ifbrk',
                type='types.McnpInteger',
                description='Mass-energy balancing in Fermi-breakup setting',
                restriction='ifbrk.value in {0, 1}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ilvden',
                type='types.McnpInteger',
                description='Level-density model setting',
                restriction='ilvden.value in {0, 1, -1}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ievap',
                type='types.McnpInteger',
                description='Evaporation and fission model setting',
                restriction='ievap.value in {0, 1, -1, 2}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='nofis',
                type='types.McnpInteger',
                description='Fission setting',
                restriction='nofis.value in {0, 1}',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='leb',
        attributes=[
            AttributeScheme(
                name='yzere',
                type='types.McnpReal',
                description='Y0 parameter in level-density formula for Z≤70',
                restriction='yzere > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='bzere',
                type='types.McnpReal',
                description='B0 parameter in level-density formula for Z≤70',
                restriction='bzere > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='yzero',
                type='types.McnpReal',
                description='Y0 parameter in level-density formula for Z≥71',
                restriction='yzero > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='bzero',
                type='types.McnpReal',
                description='B0 parameter in level-density formula for Z≥70',
                restriction='bzero > 0',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='fmult',
        attributes=[
            AttributeScheme(
                name='zaid',
                type='types.Zaid',
                description='Nuclide for which data are entered',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='sfnu',
                attribute=AttributeScheme(
                    name='nu',
                    type='types.McnpReal',
                    description='V bar for sampling spontaneous fission',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='width',
                attribute=AttributeScheme(
                    name='width',
                    type='types.McnpReal',
                    description='Width for sampling spontaneous fission',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='sfyield',
                attribute=AttributeScheme(
                    name='fission_yield',
                    type='types.McnpReal',
                    description='Spontaneous fission yield',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='method',
                attribute=AttributeScheme(
                    name='setting',
                    type='types.McnpInteger',
                    description='Gaussian sampling algorithm setting',
                    restriction='setting.value in {0, 1, 3, 5, 6, 7}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='shift',
                attribute=AttributeScheme(
                    name='setting',
                    type='types.McnpInteger',
                    description='Shift method setting',
                    restriction='setting.value in {0, 1, 2, 3, 4}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='tropt',
        attributes=[
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='mcscat',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Multiple coulomb scattering setting',
                    restriction='setting in {"off", "fnal1", "gaussian", "fnal2"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='eloss',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Slowing down energy losses setting',
                    restriction='setting in {"off", "strag1", "csda"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='nreact',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Nuclear reactions setting',
                    restriction='setting in {"off", "on", "atten", "remove"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='nescat',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Nuclear elastic scattering setting',
                    restriction='setting in {"off", "on"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='unc',
        attributes=[
            AttributeScheme(
                name='settings',
                type='tuple[types.McnpInteger]',
                description='Tuple of uncollided secondary settings',
                restriction='entry.value in {0, 1}',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='cosyp',
        attributes=[
            AttributeScheme(
                name='prefix',
                type='types.McnpInteger',
                description='Prefix number of the COSY map files',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='axsh',
                type='types.McnpInteger',
                description='Horiztonal axis orientation',
                restriction='axsh.value in {1, 2, 3}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='axsv',
                type='types.McnpInteger',
                description='Vertical axis orientation',
                restriction='axsv.value in {1, 2, 3}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='emaps',
                type='tuple[types.McnpReal]',
                description='Tuple of operating beam energies',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='cosy',
        attributes=[
            AttributeScheme(
                name='numbers',
                type='tuple[types.McnpInteger]',
                description='Tuple of COSY map numbers',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='bfld',
        attributes=[
            AttributeScheme(
                name='kind',
                type='str',
                description='Magnetic field type',
                restriction='type in {"const", "quad", "quadff"}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='field',
                attribute=AttributeScheme(
                    name='strength_gradient',
                    type='types.McnpReal',
                    description='Magnetic field strength/gradient',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='vec',
                attribute=AttributeScheme(
                    name='vector',
                    type='tuple[types.McnpReal]',
                    description='Direction of mangentic field or plane corresponding to the x-axis of the quadrapole',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='maxdeflc',
                attribute=AttributeScheme(
                    name='angle',
                    type='types.McnpReal',
                    description='Maximum deflection angles',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='maxstep',
                attribute=AttributeScheme(
                    name='size',
                    type='types.McnpReal',
                    description='Maximum step size',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='axs',
                attribute=AttributeScheme(
                    name='vector',
                    type='tuple[types.McnpReal]',
                    description='Direction of the cosines of the quadropole beam axis',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='ffedges',
                attribute=AttributeScheme(
                    name='numbers',
                    type='tuple[types.McnpReal]',
                    description='Surface numbers to apply field fringe edges',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='refpnt',
                attribute=AttributeScheme(
                    name='point',
                    type='tuple[types.McnpReal]',
                    description='Point anywhere on the quadrapole beam',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='bflcl',
        attributes=[
            AttributeScheme(
                name='numbers',
                type='tuple[types.McnpInteger]',
                description='Tuple of BFLD map numbers',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='sdef',
        attributes=[
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='cel',
                attribute=AttributeScheme(
                    name='number',
                    type='types.McnpInteger',
                    description='Cell number',
                    restriction='0 <= number <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='sur',
                attribute=AttributeScheme(
                    name='number',
                    type='types.McnpInteger',
                    description='Surface number',
                    restriction='0 <= number <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='erg',
                attribute=AttributeScheme(
                    name='energy',
                    type='types.McnpReal',
                    description='Kinetic energy',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='tme',
                attribute=AttributeScheme(
                    name='time',
                    type='Union[types.McnpReal, types.EmbeddedDistributionNumber]',
                    description='Time in shakes',
                    restriction='time >= 0',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='dir',
                attribute=AttributeScheme(
                    name='cosine',
                    type='types.McnpReal',
                    description='Cosine of the angle between VEC and particle',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='vec',
                attribute=AttributeScheme(
                    name='vector',
                    type='tuple[types.McnpReal]',
                    description='Reference vector for DIR',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='nrm',
                attribute=AttributeScheme(
                    name='sign',
                    type='types.McnpInteger',
                    description='Sign of the surface normal',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='pos',
                attribute=AttributeScheme(
                    name='vector',
                    type='tuple[types.McnpReal]',
                    description='Reference point for position sampling in vector notation',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='rad',
                attribute=AttributeScheme(
                    name='radial_distance',
                    type='types.McnpReal',
                    description='Radial distance fo the position from POS or AXS',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='ext',
                attribute=AttributeScheme(
                    name='distance_cosine',
                    type='types.McnpReal',
                    description='Distance for POS along AXS or Cosine of angle from AXS',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='axs',
                attribute=AttributeScheme(
                    name='vector',
                    type='tuple[types.McnpReal]',
                    description='Reference vector for EXT and RAD',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='x',
                attribute=AttributeScheme(
                    name='x_coordinate',
                    type='types.McnpReal',
                    description='X-cordinate of position',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='y',
                attribute=AttributeScheme(
                    name='y_coordinate',
                    type='types.McnpReal',
                    description='Y-cordinate of position',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='z',
                attribute=AttributeScheme(
                    name='z_coordinate',
                    type='types.McnpReal',
                    description='Z-cordinate of position',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='ccc',
                attribute=AttributeScheme(
                    name='number',
                    type='types.McnpInteger',
                    description='Cookie-cutter cell number',
                    restriction='0 <= number <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='ara',
                attribute=AttributeScheme(
                    name='area',
                    type='types.McnpReal',
                    description='Area of surface',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='wgt',
                attribute=AttributeScheme(
                    name='weight',
                    type='types.McnpReal',
                    description='Particle weight',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='eff',
                attribute=AttributeScheme(
                    name='criterion',
                    type='types.McnpReal',
                    description='Rejection efficiency criterion for position sampling',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='par',
                attribute=AttributeScheme(
                    name='kind',
                    type='str',
                    description='Source particle type',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='sc',
        attributes=[
            AttributeScheme(
                name='comment',
                type='tuple[str]',
                description='source comment',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='suffix',
                type='types.McnpInteger',
                description='Data card suffix.',
                restriction='',
                error='INVALID_DATA_OPTION_SUFFIX',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='ssr',
        attributes=[
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            )
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='old',
                attribute=AttributeScheme(
                    name='numbers',
                    type='tuple[types.McnpInteger]',
                    description='Tuple of surface numbers from subset of surfaces on SSW card',
                    restriction='1 <= entry <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='cel',
                attribute=AttributeScheme(
                    name='numbers',
                    type='tuple[types.McnpInteger]',
                    description='Tuple of cell from subset of cells on SSW card',
                    restriction='1 <= entry <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='new',
                attribute=AttributeScheme(
                    name='numbers',
                    type='tuple[types.McnpInteger]',
                    description='Tuple of surface numbers to start run',
                    restriction='1 <= entry <= 99_999_999',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='pty',
                attribute=AttributeScheme(
                    name='particles',
                    type='tuple[types.Designator]',
                    description='Tuple of designators',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='col',
                attribute=AttributeScheme(
                    name='setting',
                    type='types.McnpInteger',
                    description='Collision option setting',
                    restriction='setting.value in {-1, 0, 1}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='wgt',
                attribute=AttributeScheme(
                    name='constant',
                    type='types.McnpReal',
                    description='Particle weight multiplier',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='axs',
                attribute=AttributeScheme(
                    name='cosines',
                    type='tuple[types.McnpReal]',
                    description='Direction cosines defining',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='ext',
                attribute=AttributeScheme(
                    name='number',
                    type='types.DistributionNumber',
                    description='Distribution number for baising sampling',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='poa',
                attribute=AttributeScheme(
                    name='angle',
                    type='types.McnpReal',
                    description='Angle within which particles accepeted for transport',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='kcode',
        attributes=[
            AttributeScheme(
                name='nsrck',
                type='types.McnpInteger',
                description='Number of source histories per cycle',
                restriction='nsrck >= 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='rkk',
                type='types.McnpReal',
                description='Initial guess of keff',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='ikz',
                type='types.McnpInteger',
                description='Number of cycles to be skipped before beginning tally accumulation',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='kct',
                type='types.McnpInteger',
                description='Total number of cycles to be done',
                restriction='kct > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='msrk',
                type='types.McnpInteger',
                description='Number of source points to allocate for.',
                restriction='msrk < 40 * nsrck',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='knrm',
                type='types.McnpInteger',
                description='Normalization of tallies setting',
                restriction='knrm.value in {0, 1}',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='mrkp',
                type='types.McnpInteger',
                description='Maximum number of cycle values on MCTAL or RUNTPE files',
                restriction='mrkp > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='kc8',
                type='types.McnpInteger',
                description='Number of cylces for average setting',
                restriction='kc8.value in {0, 1}',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='ksrc',
        attributes=[
            AttributeScheme(
                name='locations',
                type='tuple[KsrcEntry]',
                description='Tuple of inital source points',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[
            DataEntryScheme(
                mnemonic='ksrc',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.McnpReal',
                        description='Location x-coordinate',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.McnpReal',
                        description='Location y-coordinate',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.McnpReal',
                        description='Location z-coordinate',
                        restriction='',
                        error='INVALID_DATA_ENTRY_PARAMETER',
                    ),
                ],
            ),
        ],
        options=[],
    ),
    DataScheme(
        mnemonic='kopts',
        attributes=[
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='blocksize',
                attribute=AttributeScheme(
                    name='ncy',
                    type='types.McnpInteger',
                    description='Number of cycles in every outer iteration',
                    restriction='ncy >= 2',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='kinetics',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Yes/No calculate point-kinetics parameters',
                    restriction='setting in {"yes", "no"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='precursor',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Yes/No detailed precursor information',
                    restriction='setting in {"yes", "no"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='ksental',
                attribute=AttributeScheme(
                    name='fileopt',
                    type='str',
                    description='Format of sensity profiles output file',
                    restriction='fileopt in {",mctal"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmat',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='Yes/No FMAT',
                    restriction='setting in {"yes", "no"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmatskpt',
                attribute=AttributeScheme(
                    name='fmat_skip',
                    type='types.McnpReal',
                    description='fmat_skip',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmatncyc',
                attribute=AttributeScheme(
                    name='fmat_ncyc',
                    type='types.McnpReal',
                    description='fmat_ncyc',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmatspace',
                attribute=AttributeScheme(
                    name='fmat_space',
                    type='types.McnpReal',
                    description='fmat_space',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmataccel',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='fmataccel',
                    restriction='setting in {"yes", "no"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmatreduce',
                attribute=AttributeScheme(
                    name='setting',
                    type='str',
                    description='fmatreduce',
                    restriction='setting in {"yes", "no"}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmatnx',
                attribute=AttributeScheme(
                    name='fmat_nx',
                    type='types.McnpReal',
                    description='fmat_nx',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmatny',
                attribute=AttributeScheme(
                    name='fmat_ny',
                    type='types.McnpReal',
                    description='fmat_ny',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='fmatnz',
                attribute=AttributeScheme(
                    name='fmat_nz',
                    type='types.McnpReal',
                    description='fmat_nz',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
    DataScheme(
        mnemonic='hsrc',
        attributes=[
            AttributeScheme(
                name='x_number',
                type='types.McnpInteger',
                description='Number of mesh intervals in x direction',
                restriction='x_number > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='x_minimum',
                type='types.McnpReal',
                description='Minimum x-value for mesh.',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='x_maximum',
                type='types.McnpReal',
                description='Maximum x-value for mesh.',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='y_number',
                type='types.McnpInteger',
                description='Number of mesh intervals in y direction',
                restriction='y_number > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='y_minimum',
                type='types.McnpReal',
                description='Minimum y-value for mesh.',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='y_maximum',
                type='types.McnpReal',
                description='Maximum y-value for mesh.',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='z_number',
                type='types.McnpInteger',
                description='Number of mesh intervals in z direction',
                restriction='z_number > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='z_minimum',
                type='types.McnpReal',
                description='Minimum z-value for mesh.',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='z_maximum',
                type='types.McnpReal',
                description='Maximum z-value for mesh.',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='nps',
        attributes=[
            AttributeScheme(
                name='npp',
                type='types.McnpInteger',
                description='Total number of histories to run',
                restriction='npp > 0',
                error='INVALID_DATA_PARAMETER',
            ),
            AttributeScheme(
                name='npsmg',
                type='types.McnpInteger',
                description='Number of history with direct source contributions',
                restriction='npsmg > 0',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[],
    ),
    DataScheme(
        mnemonic='rand',
        attributes=[
            AttributeScheme(
                name='pairs',
                type='dict[DataOption]',
                description='Dictionary of options',
                restriction='',
                error='INVALID_DATA_PARAMETER',
            ),
        ],
        entries=[],
        options=[
            DataOptionScheme(
                mnemonic='gen',
                attribute=AttributeScheme(
                    name='setting',
                    type='types.McnpInteger',
                    description='Type of pseudorandom number generator',
                    restriction='setting.value in {1, 2, 3, 4}',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='seed',
                attribute=AttributeScheme(
                    name='seed',
                    type='types.McnpInteger',
                    description='Random number generator seed',
                    restriction='seed.value % 2 == 1',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='stride',
                attribute=AttributeScheme(
                    name='stride',
                    type='types.McnpInteger',
                    description='Number of random numbers between source particle',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
            DataOptionScheme(
                mnemonic='hist',
                attribute=AttributeScheme(
                    name='hist',
                    type='types.McnpInteger',
                    description='Starting pseudorandom number',
                    restriction='',
                    error='INVALID_DATA_OPTION_VALUE',
                ),
            ),
        ],
    ),
)
