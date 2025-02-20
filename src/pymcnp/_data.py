import typing


GET = {}


class AttributeScheme:
    """
    Stores INP attribute metadata.

    Attributes:
        name: INP attribute name.
        type: INP attribute type.
        descirption: INP attribute comment description.
        restriction: INP attribute restriction.
        error: INP attribute ``InpError``.
        optional: INP attribute optional setting.
    """

    def __init__(
        self,
        *,
        name: str,
        type: str,
        description: str,
        restriction: str,
        optional: bool = False,
    ):
        """
        Initializes ``AttributeScheme``.

        Parameters:
            name: INP attribute name.
            type: INP attribute type.
            descirption: INP attribute comment description.
            restriction: INP attribute restriction.
            error: INP attribute ``InpError``.
            optional: INP attribute optional setting.

        Returns:
            ``AttributeScheme``.
        """

        self.name: typing.Final[str] = name
        self.type: typing.Final[str] = type
        self.description: typing.Final[str] = description
        self.restriction: typing.Final[str] = restriction
        self.optional: typing.Final[bool] = optional

        GET[name] = self


class EntryScheme:
    """
    Stores INP entry metadata.

    Attributes:
        name: INP entry name.
        attributes: INP entry attributes.
    """

    def __init__(
        self,
        *,
        name: str,
        attributes: tuple[AttributeScheme],
        entries: tuple[any] = None,
        options: tuple[any] = None,
        extra: str = '',
    ):
        """
        Initializes ``EntryScheme``.

        Parameters:
            name: INP entry name.
            attributes: INP entry attributes.
            options: INP entry options.
            entries: INP entry entries.
            extra: Python to append.

        Returns:
            ``EntryScheme``.
        """

        self.name: typing.Final[str] = name
        self.attributes: typing.Final[tuple[AttributeScheme]] = attributes
        self.entries: typing.Final[tuple[EntryScheme]] = entries
        self.options: typing.Final[tuple[OptionScheme]] = options
        self.extra: typing.Final[str] = extra

        GET[name] = self


class OptionScheme:
    """
    Stores INP option metadata.

    Attributes:
        name: INP option name.
        attributes: INP option attributes.
        options: INP option options.
        entries: INP option entries.
        extra: Python to append.
    """

    def __init__(
        self,
        *,
        name: str,
        mnemonic: str,
        attributes: tuple[AttributeScheme],
        options: tuple[any] = None,
        entries: tuple[EntryScheme] = None,
        extra: str = '',
    ):
        """
        Initializes ``OptionScheme``.

        Parameters:
            name: INP option name.
            mnemonic: INP option mnemonic.
            attributes: INP option attributes.
            options: INP option options.
            entries: INP option entries.

        Returns:
            ``OptionScheme``.
        """

        self.name: typing.Final[str] = name
        self.mnemonic: typing.Final[str] = mnemonic
        self.attributes: typing.Final[tuple[AttributeScheme]] = attributes
        self.options: typing.Final[tuple[OptionScheme]] = options
        self.entries: typing.Final[tuple[EntryScheme]] = entries
        self.extra: typing.Final[str] = extra


class CardScheme:
    """
    Stores INP card metadata.

    Attributes:
        name: INP card mnemonic.
        attributes: INP card attributes.
        options: INP card options.
        entries: INP card entries.
    """

    def __init__(
        self,
        *,
        name: str,
        attributes: tuple[AttributeScheme],
        options: tuple[any] = None,
        entries: tuple[EntryScheme] = None,
    ):
        """
        Initializes ``CardScheme``.

        Parameters:
            name: INP card mnemonic.
            attributes: INP card attributes.
            options: INP card options.
            entries: INP card entries.

        Returns:
            ``CardScheme``.
        """

        self.name: typing.Final[str] = name
        self.attributes: typing.Final[tuple[AttributeScheme]] = attributes
        self.options: typing.Final[tuple[OptionScheme]] = options
        self.entries: typing.Final[tuple[EntryScheme]] = entries


CARDS = (
    CardScheme(
        name='cell',
        attributes=[
            AttributeScheme(
                name='options',
                type='tuple[cell_.CellOption_]',
                description='Help Me!',
                restriction='',
                optional=True,
            ),
        ],
        entries=[
            EntryScheme(
                name='geometry',
                attributes=[
                    AttributeScheme(
                        name='infix',
                        type='types.String',
                        description='Cell geometry infix formula',
                        restriction='',
                    ),
                ],
                options='',
                entries='',
            ),
        ],
        options=[
            OptionScheme(
                name='imp',
                mnemonic='imp',
                attributes=(
                    AttributeScheme(
                        name='importance',
                        type='types.Real',
                        description='Cell particle importance',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Particle designator',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='vol',
                mnemonic='vol',
                attributes=(
                    AttributeScheme(
                        name='volume',
                        type='types.Real',
                        description='Cell volume',
                        restriction='volume >= 0',
                    ),
                ),
            ),
            OptionScheme(
                name='pwt',
                mnemonic='pwt',
                attributes=(
                    AttributeScheme(
                        name='weight',
                        type='types.Real',
                        description='Cell weight of photons produced at neutron collisions',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='ext',
                mnemonic='ext',
                attributes=(
                    AttributeScheme(
                        name='stretch',
                        type='str',
                        description='Cell exponential transform stretching specifier',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Cell particle designator',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='fcl',
                mnemonic='fcl',
                attributes=(
                    AttributeScheme(
                        name='control',
                        type='types.Real',
                        description='Cell forced-collision control',
                        restriction='-1 <= control <= 1',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Cell particle designator',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='wwn',
                mnemonic='wwn',
                attributes=(
                    AttributeScheme(
                        name='bound',
                        type='types.Real',
                        description='Cell weight-window space, time, or energy lower bound',
                        restriction='bound == -1 or bound >= 0',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Cell option suffix',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Cell particle designator',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='dxc',
                mnemonic='dxc',
                attributes=(
                    AttributeScheme(
                        name='probability',
                        type='types.Real',
                        description='Cell probability of DXTRAN contribution',
                        restriction='0 <= probability <= 1',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Cell option suffix',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Cell particle designator',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='nonu',
                mnemonic='nonu',
                attributes=(
                    AttributeScheme(
                        name='setting',
                        type='types.Integer',
                        description='Cell fission setting',
                        restriction='setting.value in {0, 1, 2}',
                    ),
                ),
            ),
            OptionScheme(
                name='pd',
                mnemonic='pd',
                attributes=(
                    AttributeScheme(
                        name='probability',
                        type='types.Real',
                        description='Cell probability of DXTRAN contribution',
                        restriction='0 <= probability <= 1',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Cell option suffix',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='tmp',
                mnemonic='tmp',
                attributes=(
                    AttributeScheme(
                        name='temperature',
                        type='types.Real',
                        description='Cell temperature at suffix time index',
                        restriction='temperature > 0',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Cell option suffix',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='u',
                mnemonic='u',
                attributes=(
                    AttributeScheme(
                        name='number',
                        type='types.Integer',
                        description='Cell universe number',
                        restriction='-99_999_999 <= number <= 99_999_999',
                    ),
                ),
            ),
            OptionScheme(
                name='trcl_0',
                mnemonic='trcl',
                attributes=(
                    AttributeScheme(
                        name='transformation',
                        type='types.Integer',
                        description='Cell transformation number',
                        restriction='1 <= transformation <= 999',
                    ),
                ),
            ),
            OptionScheme(
                name='trcl_1',
                mnemonic='trcl',
                attributes=[
                    AttributeScheme(
                        name='transformation',
                        type='trcl_1_.Trcl1Entry_Transformation',
                        description='Cell transformation.',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='transformation',
                        attributes=[
                            AttributeScheme(
                                name='o1',
                                type='types.Real',
                                description='Transformation displacement vector x-coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='o2',
                                type='types.Real',
                                description='Transformation displacement vector y-coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='o3',
                                type='types.Real',
                                description='Transformation displacement vector z-coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='xx',
                                type='types.Real',
                                description='Transformation rotation matrix xx-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='xy',
                                type='types.Real',
                                description='Transformation rotation matrix xy-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='xz',
                                type='types.Real',
                                description='Transformation rotation matrix xz-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='yx',
                                type='types.Real',
                                description='Transformation rotation matrix yx-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='yy',
                                type='types.Real',
                                description='Transformation rotation matrix yy-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='yz',
                                type='types.Real',
                                description='Transformation rotation matrix yz-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='zx',
                                type='types.Real',
                                description='Transformation rotation matrix zx-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='zy',
                                type='types.Real',
                                description='Transformation rotation matrix zy-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='zz',
                                type='types.Real',
                                description='Transformation rotation matrix zz-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='m',
                                type='types.Real',
                                description='Transformation coordinate system setting',
                                restriction='m in {-1, 1}',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='lat',
                mnemonic='lat',
                attributes=(
                    AttributeScheme(
                        name='shape',
                        type='types.Integer',
                        description='Cell lattice shape',
                        restriction='shape.value in {1, 2}',
                    ),
                ),
            ),
            OptionScheme(
                name='fill_0',
                mnemonic='fill',
                attributes=(
                    AttributeScheme(
                        name='universe',
                        type='types.Integer',
                        description='Cell fill universe number',
                        restriction='0 <= universe <= 99_999_999',
                    ),
                    AttributeScheme(
                        name='transformation',
                        type='types.Integer',
                        description='Cell fill transformation number',
                        restriction='0 <= transformation <= 999',
                        optional=True,
                    ),
                ),
            ),
            OptionScheme(
                name='fill_1',
                mnemonic='fill',
                attributes=[
                    AttributeScheme(
                        name='universe',
                        type='types.Integer',
                        description='Cell fill universe number',
                        restriction='0 <= universe <= 99_999_999',
                    ),
                    AttributeScheme(
                        name='transformation',
                        type='fill_1_.Fill1Entry_Transformation',
                        description='Cell fill transformation',
                        restriction='',
                        optional=True,
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='transformation',
                        attributes=[
                            AttributeScheme(
                                name='o1',
                                type='types.Real',
                                description='Fill displacement vector x-coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='o2',
                                type='types.Real',
                                description='Fill displacement vector y-coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='o3',
                                type='types.Real',
                                description='Fill displacement vector z-coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='xx',
                                type='types.Real',
                                description='Fill rotation matrix xx-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='xy',
                                type='types.Real',
                                description='Fill rotation matrix xy-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='xz',
                                type='types.Real',
                                description='Fill rotation matrix xz-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='yx',
                                type='types.Real',
                                description='Fill rotation matrix yx-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='yy',
                                type='types.Real',
                                description='Fill rotation matrix yy-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='yz',
                                type='types.Real',
                                description='Fill rotation matrix yz-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='zx',
                                type='types.Real',
                                description='Fill rotation matrix zx-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='zy',
                                type='types.Real',
                                description='Fill rotation matrix zy-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='zz',
                                type='types.Real',
                                description='Fill rotation matrix zz-entry',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='m',
                                type='types.Real',
                                description='Fill coordinate system setting',
                                restriction='m in {-1, 1}',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='elpt',
                mnemonic='elpt',
                attributes=(
                    AttributeScheme(
                        name='cutoff',
                        type='types.Real',
                        description='Cell energy cutoff',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Cell particle designator',
                        restriction='',
                    ),
                ),
            ),
            OptionScheme(
                name='cosy',
                mnemonic='cosy',
                attributes=(
                    AttributeScheme(
                        name='number',
                        type='types.Integer',
                        description='Cell cosy map number',
                        restriction='number.value in {1, 2, 3, 4, 5, 6}',
                    ),
                ),
            ),
            OptionScheme(
                name='bflcl',
                mnemonic='bflcl',
                attributes=(
                    AttributeScheme(
                        name='number',
                        type='types.Integer',
                        description='Cell magnetic field number',
                        restriction='number >= 0',
                    ),
                ),
            ),
            OptionScheme(
                name='unc',
                mnemonic='unc',
                attributes=(
                    AttributeScheme(
                        name='setting',
                        type='types.Integer',
                        description='Cell uncollided secondaries setting',
                        restriction='setting.value in {0, 1}',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Cell particle designator',
                        restriction='',
                    ),
                ),
            ),
        ],
    ),
    CardScheme(
        name='surface',
        attributes=[
            AttributeScheme(
                name='options',
                type='surface_.SurfaceOption_',
                description='Help Me!',
                restriction='',
            ),
        ],
        options=[
            OptionScheme(
                name='p_0',
                mnemonic='p',
                attributes=[
                    AttributeScheme(
                        name='a',
                        type='types.Real',
                        description='Equation-defined general plane A coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='b',
                        type='types.Real',
                        description='Equation-defined general plane B coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='c',
                        type='types.Real',
                        description='Equation-defined general plane C coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='d',
                        type='types.Real',
                        description='Equation-defined general plane D coefficent',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Px``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Px``
        """

        vis = _visualization.McnpVisualization.get_plane(
            self.a.value, self.b.value, self.c.value, self.d.value
        )

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='p_1',
                mnemonic='p',
                attributes=[
                    AttributeScheme(
                        name='x1',
                        type='types.Real',
                        description='point-defined general plane x-coordinate #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y1',
                        type='types.Real',
                        description='point-defined general plane y-coordinate #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z1',
                        type='types.Real',
                        description='point-defined general plane z-coordinate #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x2',
                        type='types.Real',
                        description='point-defined general plane x-coordinate #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y2',
                        type='types.Real',
                        description='point-defined general plane y-coordinate #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z2',
                        type='types.Real',
                        description='point-defined general plane z-coordinate #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x3',
                        type='types.Real',
                        description='point-defined general plane x-coordinate #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y3',
                        type='types.Real',
                        description='point-defined general plane y-coordinate #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z3',
                        type='types.Real',
                        description='point-defined general plane z-coordinate #3',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_P0``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_P1``
        """

        a = _visualization.Vector(self.x2 - self.x1, self.y2 - self.y1, self.z2 - self.z1)
        b = _visualization.Vector(self.x3 - self.x1, self.y3 - self.y1, self.z3 - self.z1)
        n = a * b

        vis = _visualization.McnpVisualization.get_plane(
            n.x, n.y, n.z, n.x * self.x1 + n.y * self.y1 + n.z * self.z1
        )

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='px',
                mnemonic='px',
                attributes=[
                    AttributeScheme(
                        name='d',
                        type='types.Real',
                        description='Normal-to-the-x-axis plane D coefficent',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Px``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Px``
        """

        vis = _visualization.McnpVisualization.get_plane(1, 0, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='py',
                mnemonic='py',
                attributes=[
                    AttributeScheme(
                        name='d',
                        type='types.Real',
                        description='Normal-to-the-y-axis plane D coefficent',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Py``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Py``
        """

        vis = _visualization.McnpVisualization.get_plane(0, 1, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='pz',
                mnemonic='pz',
                attributes=[
                    AttributeScheme(
                        name='d',
                        type='types.Real',
                        description='Normal-to-the-z-axis plane D coefficent',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Pz``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Pz``
        """

        vis = _visualization.McnpVisualization.get_plane(0, 0, 1, self.d.value)

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='so',
                mnemonic='so',
                attributes=[
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='Origin-centered sphere radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_So``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_So``
        """

        vis = _visualization.McnpVisualization.get_sphere(self.r.value)

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='s',
                mnemonic='s',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='General sphere center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='General sphere center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='General sphere center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='General sphere radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_S``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_S``
        """

        vis = _visualization.McnpVisualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='sx',
                mnemonic='sx',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='On-x-axis sphere center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='On-x-axis sphere radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Sx``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Sx``
        """

        vis = _visualization.McnpVisualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='sy',
                mnemonic='sy',
                attributes=[
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='On-y-axis sphere center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='On-y-axis sphere radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Sy``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Sy``
        """

        vis = _visualization.McnpVisualization.get_sphere(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='sz',
                mnemonic='sz',
                attributes=[
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='On-z-axis sphere center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='On-z-axis sphere radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Sz``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Sz``
        """

        vis = _visualization.McnpVisualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='c/x',
                mnemonic='c/x',
                attributes=[
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Parallel-to-x-axis cylinder center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Parallel-to-x-axis cylinder center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='Parallel-to-x-axis cylinder radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_C_x``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_C_x``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='c/y',
                mnemonic='c/y',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Parallel-to-y-axis cylinder center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Parallel-to-y-axis cylinder center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='Parallel-to-y-axis cylinder radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_C_y``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_C_y``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, self.z.value))

        return vis.data
''',
            ),
            OptionScheme(
                name='c/z',
                mnemonic='c/z',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Parallel-to-z-axis cylinder center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Parallel-to-z-axis cylinder center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='Parallel-to-z-axis cylinder radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_C_z``.
        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_C_z``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, 0))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='cx',
                mnemonic='cx',
                attributes=[
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='On-x-axis cylinder radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Cx``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Cx``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='cy',
                mnemonic='cy',
                attributes=[
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='On-y-axis cylinder radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Cy``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Cy``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis.data
''',
            ),
            OptionScheme(
                name='cz',
                mnemonic='cz',
                attributes=[
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='On-z-axis cylinder radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Cz``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Cz``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)

        return vis.data
''',
            ),
            OptionScheme(
                name='k/x',
                mnemonic='k/x',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Parallel-to-x-axis cone center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Parallel-to-x-axis cone center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Parallel-to-x-axis cone center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t_squared',
                        type='types.Real',
                        description='Parallel-to-x-axis cone t^2 coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='plusminus_1',
                        type='types.Real',
                        description='Parallel-to-x-axis cone sheet selector',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_K_x``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_K_x``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='k/y',
                mnemonic='k/y',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Parallel-to-y-axis cone center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Parallel-to-y-axis cone center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Parallel-to-y-axis cone center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t_squared',
                        type='types.Real',
                        description='Parallel-to-y-axis cone t^2 coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='plusminus_1',
                        type='types.Real',
                        description='Parallel-to-y-axis cone sheet selector',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_K_y``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_K_y``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='k/z',
                mnemonic='k/z',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Parallel-to-z-axis cone center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Parallel-to-z-axis cone center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Parallel-to-z-axis cone center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t_squared',
                        type='types.Real',
                        description='Parallel-to-z-axis cone t^2 coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='plusminus_1',
                        type='types.Real',
                        description='Parallel-to-z-axis cone sheet selector',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_K_z``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_K_z``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='kx',
                mnemonic='kx',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='On-x-axis cone center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t_squared',
                        type='types.Real',
                        description='On-x-axis cone t^2 coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='plusminus_1',
                        type='types.Real',
                        description='On-x-axis cone sheet selector',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Kx``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Kx``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='ky',
                mnemonic='ky',
                attributes=[
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='On-y-axis cone center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t_squared',
                        type='types.Real',
                        description='On-y-axis cone t^2 coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='plusminus_1',
                        type='types.Real',
                        description='On-y-axis cone sheet selector',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Ky``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Ky``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='kz',
                mnemonic='kz',
                attributes=[
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='On-z-axis cone center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t_squared',
                        type='types.Real',
                        description='On-z-axis cone t^2 coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='plusminus_1',
                        type='types.Real',
                        description='On-z-axis cone sheet selector',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Kz``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Kz``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='sq',
                mnemonic='sq',
                attributes=[
                    AttributeScheme(
                        name='a',
                        type='types.Real',
                        description='Oblique special quadratic A coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='b',
                        type='types.Real',
                        description='Oblique special quadratic B coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='c',
                        type='types.Real',
                        description='Oblique special quadratic C coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='d',
                        type='types.Real',
                        description='Oblique special quadratic D coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='e',
                        type='types.Real',
                        description='Oblique special quadratic E coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='f',
                        type='types.Real',
                        description='Oblique special quadratic F coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='g',
                        type='types.Real',
                        description='Oblique special quadratic G coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Oblique special quadratic center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Oblique special quadratic center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Oblique special quadratic center z component',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='gq',
                mnemonic='gq',
                attributes=[
                    AttributeScheme(
                        name='a',
                        type='types.Real',
                        description='Oblique special quadratic A coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='b',
                        type='types.Real',
                        description='Oblique special quadratic B coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='c',
                        type='types.Real',
                        description='Oblique special quadratic C coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='d',
                        type='types.Real',
                        description='Oblique special quadratic D coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='e',
                        type='types.Real',
                        description='Oblique special quadratic E coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='f',
                        type='types.Real',
                        description='Oblique special quadratic F coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='g',
                        type='types.Real',
                        description='Oblique special quadratic G coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='h',
                        type='types.Real',
                        description='Oblique special quadratic H coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='j',
                        type='types.Real',
                        description='Oblique special quadratic J coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='k',
                        type='types.Real',
                        description='Oblique special quadratic K coefficent',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='tx',
                mnemonic='tx',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Parallel-to-x-axis tori center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Parallel-to-x-axis tori center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Parallel-to-x-axis tori center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a',
                        type='types.Real',
                        description='Parallel-to-x-axis tori A coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='b',
                        type='types.Real',
                        description='Parallel-to-x-axis tori B coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='c',
                        type='types.Real',
                        description='Parallel-to-x-axis tori C coefficent',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Tx``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Tx``
        """

        vis = _visualization.McnpVisualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='ty',
                mnemonic='ty',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Parallel-to-y-axis tori center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Parallel-to-y-axis tori center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Parallel-to-y-axis tori center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a',
                        type='types.Real',
                        description='Parallel-to-y-axis tori A coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='b',
                        type='types.Real',
                        description='Parallel-to-y-axis tori B coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='c',
                        type='types.Real',
                        description='Parallel-to-y-axis tori C coefficent',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Ty``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Ty``
        """

        vis = _visualization.McnpVisualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='tz',
                mnemonic='tz',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Parallel-to-z-axis tori center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Parallel-to-z-axis tori center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Parallel-to-z-axis tori center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a',
                        type='types.Real',
                        description='Parallel-to-z-axis tori A coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='b',
                        type='types.Real',
                        description='Parallel-to-z-axis tori B coefficent',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='c',
                        type='types.Real',
                        description='Parallel-to-z-axis tori C coefficent',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Tz``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Tz``
        """

        vis = _visualization.McnpVisualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='x',
                mnemonic='x',
                attributes=[
                    AttributeScheme(
                        name='x1',
                        type='types.Real',
                        description='X-axisymmetric point-defined surface point #1 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r1',
                        type='types.Real',
                        description='X-axisymmetric point-defined surface point #1 radius',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x2',
                        type='types.Real',
                        description='X-axisymmetric point-defined surface point #2 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r2',
                        type='types.Real',
                        description='X-axisymmetric point-defined surface point #2 radius',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x3',
                        type='types.Real',
                        description='X-axisymmetric point-defined surface point #3 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r3',
                        type='types.Real',
                        description='X-axisymmetric point-defined surface point #3 radius',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='y',
                mnemonic='y',
                attributes=[
                    AttributeScheme(
                        name='y1',
                        type='types.Real',
                        description='Y-axisymmetric point-defined surface point #1 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r1',
                        type='types.Real',
                        description='Y-axisymmetric point-defined surface point #1 radius',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y2',
                        type='types.Real',
                        description='Y-axisymmetric point-defined surface point #2 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r2',
                        type='types.Real',
                        description='Y-axisymmetric point-defined surface point #2 radius',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y3',
                        type='types.Real',
                        description='Y-axisymmetric point-defined surface point #3 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r3',
                        type='types.Real',
                        description='Y-axisymmetric point-defined surface point #3 radius',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='z',
                mnemonic='z',
                attributes=[
                    AttributeScheme(
                        name='z1',
                        type='types.Real',
                        description='Z-axisymmetric point-defined surface point #1 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r1',
                        type='types.Real',
                        description='Z-axisymmetric point-defined surface point #1 radius',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z2',
                        type='types.Real',
                        description='Z-axisymmetric point-defined surface point #2 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r2',
                        type='types.Real',
                        description='Z-axisymmetric point-defined surface point #2 radius',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z3',
                        type='types.Real',
                        description='Z-axisymmetric point-defined surface point #3 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r3',
                        type='types.Real',
                        description='Z-axisymmetric point-defined surface point #3 radius',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='box',
                mnemonic='box',
                attributes=[
                    AttributeScheme(
                        name='vx',
                        type='types.Real',
                        description='Box macrobody position vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vy',
                        type='types.Real',
                        description='Box macrobody position vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vz',
                        type='types.Real',
                        description='Box macrobody position vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a1x',
                        type='types.Real',
                        description='Box macrobody vector #1 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a1y',
                        type='types.Real',
                        description='Box macrobody vector #1 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a1z',
                        type='types.Real',
                        description='Box macrobody vector #1 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a2x',
                        type='types.Real',
                        description='Box macrobody vector #2 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a2y',
                        type='types.Real',
                        description='Box macrobody vector #2 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a2z',
                        type='types.Real',
                        description='Box macrobody vector #2 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a3x',
                        type='types.Real',
                        description='Box macrobody vector #3 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a3y',
                        type='types.Real',
                        description='Box macrobody vector #3 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='a3z',
                        type='types.Real',
                        description='Box macrobody vector #3 z component',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Box``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Box``.
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        a1 = _visualization.Vector(self.a1x.value, self.a1y.value, self.a1z.value)
        a2 = _visualization.Vector(self.a2x.value, self.a2y.value, self.a2z.value)
        a3 = _visualization.Vector(self.a3x.value, self.a3y.value, self.a3z.value)
        cross = _visualization.Vector(1, 0, 0) * a1
        angle = _visualization.Vector(1, 0, 0) & a1

        vis = _visualization.McnpVisualization.get_box(a1.norm(), a2.norm(), a3.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis.data
''',
            ),
            OptionScheme(
                name='rpp',
                mnemonic='rpp',
                attributes=[
                    AttributeScheme(
                        name='xmin',
                        type='types.Real',
                        description='Parallelepiped x termini minimum',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='xmax',
                        type='types.Real',
                        description='Parallelepiped x termini maximum',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ymin',
                        type='types.Real',
                        description='Parallelepiped y termini minimum',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ymax',
                        type='types.Real',
                        description='Parallelepiped y termini maximum',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='zmin',
                        type='types.Real',
                        description='Parallelepiped z termini minimum',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='zmax',
                        type='types.Real',
                        description='Parallelepiped z termini maximum',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Rpp``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Rpp``
        """

        vis = _visualization.McnpVisualization.get_parallelipiped(
            self.xmin.value,
            self.xmax.value,
            self.ymin.value,
            self.ymax.value,
            self.zmin.value,
            self.zmax.value,
        )

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='sph',
                mnemonic='sph',
                attributes=[
                    AttributeScheme(
                        name='vx',
                        type='types.Real',
                        description='Sphere macrobody position vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vy',
                        type='types.Real',
                        description='Sphere macrobody position vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vz',
                        type='types.Real',
                        description='Sphere macrobody position vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='Sphere macrobody radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Sph``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Sph``
        """

        vis = _visualization.McnpVisualization.get_sphere(self.r.value)
        vis = vis.add_translation(
            _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        )

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='rcc',
                mnemonic='rcc',
                attributes=[
                    AttributeScheme(
                        name='vx',
                        type='types.Real',
                        description='Circular cylinder macrobody position vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vy',
                        type='types.Real',
                        description='Circular cylinder macrobody position vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vz',
                        type='types.Real',
                        description='Circular cylinder macrobody position vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hx',
                        type='types.Real',
                        description='Circular cylinder macrobody height vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hy',
                        type='types.Real',
                        description='Circular cylinder macrobody height vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hz',
                        type='types.Real',
                        description='Circular cylinder macrobody height vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r',
                        type='types.Real',
                        description='Circular cylinder macrobody radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Rcc``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Rcc``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.McnpVisualization.get_cylinder_circle(h.norm(), self.r.value)
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='rhp',
                mnemonic='rhp',
                attributes=[
                    AttributeScheme(
                        name='vx',
                        type='types.Real',
                        description='Hexagonal prism position vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vy',
                        type='types.Real',
                        description='Hexagonal prism position vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vz',
                        type='types.Real',
                        description='Hexagonal prism position vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hx',
                        type='types.Real',
                        description='Hexagonal prism height vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hy',
                        type='types.Real',
                        description='Hexagonal prism height vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hz',
                        type='types.Real',
                        description='Hexagonal prism height vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r1',
                        type='types.Real',
                        description='Hexagonal prism facet #1 vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r2',
                        type='types.Real',
                        description='Hexagonal prism facet #1 vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r3',
                        type='types.Real',
                        description='Hexagonal prism facet #1 vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='s1',
                        type='types.Real',
                        description='Hexagonal prism facet #2 vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='s2',
                        type='types.Real',
                        description='Hexagonal prism facet #2 vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='s3',
                        type='types.Real',
                        description='Hexagonal prism facet #2 vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t1',
                        type='types.Real',
                        description='Hexagonal prism facet #3 vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t2',
                        type='types.Real',
                        description='Hexagonal prism facet #3 vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='t3',
                        type='types.Real',
                        description='Hexagonal prism facet #3 vector z component',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Rhp``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Rhp``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)
        r = _visualization.Vector(self.r1.value, self.r2.value, self.r3.value)
        s = _visualization.Vector(self.s1.value, self.s2.value, self.s3.value)
        t = _visualization.Vector(self.t1.value, self.t2.value, self.t3.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.McnpVisualization.get_cylinder_hexagon(
            h.norm(), r.apothem(), s.apothem(), t.apothem()
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='rec',
                mnemonic='rec',
                attributes=[
                    AttributeScheme(
                        name='vx',
                        type='types.Real',
                        description='Elliptical cylinder position vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vy',
                        type='types.Real',
                        description='Elliptical cylinder position vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vz',
                        type='types.Real',
                        description='Elliptical cylinder position vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hx',
                        type='types.Real',
                        description='Elliptical cylinder height vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hy',
                        type='types.Real',
                        description='Elliptical cylinder height vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hz',
                        type='types.Real',
                        description='Elliptical cylinder height vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v1x',
                        type='types.Real',
                        description='Elliptical cylinder major axis vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v1y',
                        type='types.Real',
                        description='Elliptical cylinder major axis vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v1z',
                        type='types.Real',
                        description='Elliptical cylinder major axis vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2x',
                        type='types.Real',
                        description='Elliptical cylinder minor axis vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2y',
                        type='types.Real',
                        description='Elliptical cylinder minor axis vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2z',
                        type='types.Real',
                        description='Elliptical cylinder minor axis vector z component',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Rec``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Rec``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)
        v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.McnpVisualization.get_cylinder_ellipse(h.norm(), v1.norm(), v2.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='trc',
                mnemonic='trc',
                attributes=[
                    AttributeScheme(
                        name='vx',
                        type='types.Real',
                        description='Truncated cone position vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vy',
                        type='types.Real',
                        description='Truncated cone position vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vz',
                        type='types.Real',
                        description='Truncated cone position vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hx',
                        type='types.Real',
                        description='Truncated cone height vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hy',
                        type='types.Real',
                        description='Truncated cone height vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hz',
                        type='types.Real',
                        description='Truncated cone height vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r1',
                        type='types.Real',
                        description='Truncated cone lower cone radius',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='r2',
                        type='types.Real',
                        description='Truncated cone upper cone radius',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Trc``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Trc``
        """

        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)

        cross = h * _visualization.Vector(0, 0, 1)
        angle = h & _visualization.Vector(0, 0, 1)

        vis = _visualization.McnpVisualization.get_cone_truncated(
            h.norm(), self.r1.value, self.r2.value
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(
            _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        )

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='ell',
                mnemonic='ell',
                attributes=[
                    AttributeScheme(
                        name='v1x',
                        type='types.Real',
                        description='Ellipsoid focus #1 or center x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v1y',
                        type='types.Real',
                        description='Ellipsoid focus #1 or center y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v1z',
                        type='types.Real',
                        description='Ellipsoid focus #1 or center z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2x',
                        type='types.Real',
                        description='Ellipsoid focus #2 or major axis x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2y',
                        type='types.Real',
                        description='Ellipsoid focus #2 or major axis y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2z',
                        type='types.Real',
                        description='Ellipsoid focus #2 or major axis z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='rm',
                        type='types.Real',
                        description='Ellipsoid major/minor axis radius length',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Ell``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Ell``.
        """

        v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)

        if self.rm > 0:
            center = _visualization.Vector(
                (v2 - v1).x / 2 + v1.x, (v2 - v1).y / 2 + v1.y, (v2 - v1).z / 2 + v1.z
            )
            major_length = self.rm.value
            minor_length = 2 * (((major_length / 2) ** 2 - ((v2 - v1).norm() / 2) ** 2) ** 0.5)
            cross = (v2 - v1) * _visualization.Vector(1, 0, 0)
            angle = (v2 - v1) & _visualization.Vector(1, 0, 0)
        elif self.rm < 0:
            center = v1
            major_length = v2.norm()
            minor_length = -self.rm.value
            cross = v2 * _visualization.Vector(1, 0, 0)
            angle = v2 & _visualization.Vector(1, 0, 0)

        vis = _visualization.McnpVisualization.get_ellipsoid(major_length, minor_length)
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(center)

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='wed',
                mnemonic='wed',
                attributes=[
                    AttributeScheme(
                        name='vx',
                        type='types.Real',
                        description='Wedge position vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vy',
                        type='types.Real',
                        description='Wedge position vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='vz',
                        type='types.Real',
                        description='Wedge position vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v1x',
                        type='types.Real',
                        description='Wedge side vector #1 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v1y',
                        type='types.Real',
                        description='Wedge side vector #1 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v1z',
                        type='types.Real',
                        description='Wedge side vector #1 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2x',
                        type='types.Real',
                        description='Wedge side vector #2 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2y',
                        type='types.Real',
                        description='Wedge side vector #2 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v2z',
                        type='types.Real',
                        description='Wedge side vector #2 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v3x',
                        type='types.Real',
                        description='Wedge height vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v3y',
                        type='types.Real',
                        description='Wedge height vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v3z',
                        type='types.Real',
                        description='Wedge height vector z component',
                        restriction='',
                    ),
                ],
                extra='''
def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Wed``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Wed``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)
        v3 = _visualization.Vector(self.v3x.value, self.v3y.value, self.v3z.value)

        cross = _visualization.Vector(1, 0, 0) * v1
        angle = _visualization.Vector(1, 0, 0) & v1

        vis = _visualization.McnpVisualization.get_wedge(v1.norm(), v2.norm(), v3.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis.data
'''[1:-1],
            ),
            OptionScheme(
                name='arb',
                mnemonic='arb',
                attributes=[
                    AttributeScheme(
                        name='ax',
                        type='types.Real',
                        description='Polyhedron corner #1 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ay',
                        type='types.Real',
                        description='Polyhedron corner #1 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='az',
                        type='types.Real',
                        description='Polyhedron corner #1 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bx',
                        type='types.Real',
                        description='Polyhedron corner #2 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='by',
                        type='types.Real',
                        description='Polyhedron corner #2 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bz',
                        type='types.Real',
                        description='Polyhedron corner #2 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='cx',
                        type='types.Real',
                        description='Polyhedron corner #3 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='cy',
                        type='types.Real',
                        description='Polyhedron corner #3 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='cz',
                        type='types.Real',
                        description='Polyhedron corner #3 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='dx',
                        type='types.Real',
                        description='Polyhedron corner #4 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='dy',
                        type='types.Real',
                        description='Polyhedron corner #4 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='dz',
                        type='types.Real',
                        description='Polyhedron corner #4 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ex',
                        type='types.Real',
                        description='Polyhedron corner #5 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ey',
                        type='types.Real',
                        description='Polyhedron corner #5 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ez',
                        type='types.Real',
                        description='Polyhedron corner #5 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='fx',
                        type='types.Real',
                        description='Polyhedron corner #6 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='fy',
                        type='types.Real',
                        description='Polyhedron corner #6 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='fz',
                        type='types.Real',
                        description='Polyhedron corner #6 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='gx',
                        type='types.Real',
                        description='Polyhedron corner #7 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='gy',
                        type='types.Real',
                        description='Polyhedron corner #7 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='gz',
                        type='types.Real',
                        description='Polyhedron corner #7 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hx',
                        type='types.Real',
                        description='Polyhedron corner #8 x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hy',
                        type='types.Real',
                        description='Polyhedron corner #8 y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='hz',
                        type='types.Real',
                        description='Polyhedron corner #8 z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='n1',
                        type='types.Real',
                        description='Polyhedron four-digit side specificer #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='n2',
                        type='types.Real',
                        description='Polyhedron four-digit side specificer #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='n3',
                        type='types.Real',
                        description='Polyhedron four-digit side specificer #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='n4',
                        type='types.Real',
                        description='Polyhedron four-digit side specificer #4',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='n5',
                        type='types.Real',
                        description='Polyhedron four-digit side specificer #5',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='n6',
                        type='types.Real',
                        description='Polyhedron four-digit side specificer #6',
                        restriction='',
                    ),
                ],
            ),
        ],
    ),
    CardScheme(
        name='data',
        attributes=[
            AttributeScheme(
                name='options',
                type='data_.DataOption_',
                description='Help Me!',
                restriction='',
            ),
        ],
        options=[
            OptionScheme(
                name='vol',
                mnemonic='vol',
                attributes=[
                    AttributeScheme(
                        name='no',
                        type='types.String',
                        description='Calculation on/off',
                        restriction='no == "no"',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='volumes',
                        type='tuple[types.Real]',
                        description='Tuple of cell volumes',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='area',
                mnemonic='area',
                attributes=[
                    AttributeScheme(
                        name='areas',
                        type='tuple[types.Real]',
                        description='Tuple of surface areas',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='tr',
                mnemonic='tr',
                attributes=[
                    AttributeScheme(
                        name='x',
                        type='types.Real',
                        description='Displacement vector x component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y',
                        type='types.Real',
                        description='Displacement vector y component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z',
                        type='types.Real',
                        description='Displacement vector z component',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='xx',
                        type='types.Real',
                        description="Rotation matrix xx' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='xy',
                        type='types.Real',
                        description="Rotation matrix xy' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='xz',
                        type='types.Real',
                        description="Rotation matrix xz' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='yx',
                        type='types.Real',
                        description="Rotation matrix yx' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='yy',
                        type='types.Real',
                        description="Rotation matrix yy' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='yz',
                        type='types.Real',
                        description="Rotation matrix yz' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='zx',
                        type='types.Real',
                        description="Rotation matrix zx' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='zy',
                        type='types.Real',
                        description="Rotation matrix zy' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='zz',
                        type='types.Real',
                        description="Rotation matrix zz' component",
                        restriction='',
                    ),
                    AttributeScheme(
                        name='system',
                        type='types.Integer',
                        description='Coordinate system setting',
                        restriction='system == -1 or system == 1',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='1 <= suffix <= 999',
                    ),
                ],
            ),
            OptionScheme(
                name='u',
                mnemonic='u',
                attributes=[
                    AttributeScheme(
                        name='numbers',
                        type='tuple[types.Integer]',
                        description='Tuple of cell numbers',
                        restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                    ),
                ],
            ),
            OptionScheme(
                name='lat',
                mnemonic='lat',
                attributes=[
                    AttributeScheme(
                        name='type',
                        type='tuple[types.Integer]',
                        description='Tuple of lattice types',
                        restriction='filter(lambda entry: not (entry == 1 or entry == 2), type)',
                    ),
                ],
            ),
            OptionScheme(
                name='fill',
                mnemonic='fill',
                attributes=[
                    AttributeScheme(
                        name='numbers',
                        type='tuple[types.Integer]',
                        description='Tuple of universe numbers',
                        restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)',
                    ),
                ],
            ),
            OptionScheme(
                name='uran',
                mnemonic='uran',
                attributes=[
                    AttributeScheme(
                        name='transformations',
                        type='tuple[uran_.UranEntry_Transformation]',
                        description='Tuple of stochastic transformations',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='transformation',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Universe number for transformation',
                                restriction='0 <= number <= 99_999_999',
                            ),
                            AttributeScheme(
                                name='maximum_x',
                                type='types.Real',
                                description='Maximum displacement in the x direction',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='maximum_y',
                                type='types.Real',
                                description='Maximum displacement in the y direction',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='maximum_z',
                                type='types.Real',
                                description='Maximum displacement in the z direction',
                                restriction='',
                            ),
                        ],
                    )
                ],
            ),
            OptionScheme(
                name='dm',
                mnemonic='dm',
                attributes=[
                    AttributeScheme(
                        name='zaids',
                        type='tuple[types.Zaid]',
                        description='Tuple of ZAID aliases',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='dawwg',
                mnemonic='dawwg',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[dawwg_.DawwgOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='points',
                        mnemonic='points',
                        attributes=[
                            AttributeScheme(
                                name='name',
                                type='types.String',
                                description='Cross section library',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='xsec',
                        mnemonic='xsec',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='Number of sample points for each direction in each mesh',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='block',
                        mnemonic='block',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Integer',
                                description='Destination of key-value pairs',
                                restriction='setting.value in {1, 3, 5, 6}',
                            ),
                            AttributeScheme(
                                name='options',
                                type='tuple[block_.BlockOption_]',
                                description='Dictionary of dawwg block options',
                                restriction='',
                                optional=True,
                            ),
                        ],
                        options=[
                            OptionScheme(
                                name='ngroup',
                                mnemonic='ngroup',
                                attributes=[
                                    AttributeScheme(
                                        name='value',
                                        type='types.Integer',
                                        description='Number of energy groups',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='isn',
                                mnemonic='isn',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Sn order',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='niso',
                                mnemonic='niso',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Number of isotopes',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='mt',
                                mnemonic='mt',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Number of materials',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='iquad',
                                mnemonic='iquad',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Quadrature',
                                        restriction='setting.value in {1, 2, 3, 4, 5, 6, 7, 8, 9}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='fmmix',
                                mnemonic='fmmix',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Read composition from LNK3DNT on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='nosolv',
                                mnemonic='nosolv',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress solver module on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='noedit',
                                mnemonic='noedit',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress edit module on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='nogeod',
                                mnemonic='nogeod',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress writing GEODST on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='nomix',
                                mnemonic='nomix',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress writing mixing on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='noasg',
                                mnemonic='noasg',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress writing ASGMAT on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='nomacr',
                                mnemonic='nomacr',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress writing MACRXS on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='noslnp',
                                mnemonic='noslnp',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress writing SOLINP on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='noedtt',
                                mnemonic='noedtt',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress writing EDITIT on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='noadjm',
                                mnemonic='noadjm',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Suppress writing ADJMAC on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='lib',
                                mnemonic='lib',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.String',
                                        description='Name of cross-section file',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='libname',
                                mnemonic='libname',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.String',
                                        description='Cross-section file name',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='fissneut',
                                mnemonic='fissneut',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Fission neutron flag',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='lng',
                                mnemonic='lng',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Number of the last neutron group',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='balxs',
                                mnemonic='balxs',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Cross-section balance control',
                                        restriction='setting.value in {-1, 0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ntichi',
                                mnemonic='ntichi',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='MENDF fission fraction',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ievt',
                                mnemonic='ievt',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Calculation type',
                                        restriction='setting in {0, 1, 2, 3, 4}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='isct',
                                mnemonic='isct',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Legendre order',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ith',
                                mnemonic='ith',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Direction/adjoint calculation control',
                                        restriction='setting in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='trcor',
                                mnemonic='trcor',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.String',
                                        description='Trcor',
                                        restriction='setting in {"diag"}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ibl',
                                mnemonic='ibl',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Left boundary condition',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ibr',
                                mnemonic='ibr',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Right boudary condition',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ibt',
                                mnemonic='ibt',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Top boudary condition',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ibb',
                                mnemonic='ibb',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Bottom  boudary condition',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ibfrnt',
                                mnemonic='ibfrnt',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Front boudary condition',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ibback',
                                mnemonic='ibback',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Back boudary condition',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='epsi',
                                mnemonic='epsi',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Real',
                                        description='Convergence precision',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='oitm',
                                mnemonic='oitm',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Maximum outer iteration count',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='nosigf',
                                mnemonic='nosigf',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Inhibit fission multiplication on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='srcacc',
                                mnemonic='srcacc',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.String',
                                        description='Transport accelerations',
                                        restriction='setting in {"dsa", "tsa", "no"}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='diffsol',
                                mnemonic='diffsol',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.String',
                                        description='Diffusion operator solver',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='tsasn',
                                mnemonic='tsasn',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Sn order for lower order TSA sweeps',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='tsaepsi',
                                mnemonic='tsaepsi',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Real',
                                        description='Convergence criteria for TSA sweeps',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='tsaits',
                                mnemonic='tsaits',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Maximum TSA iteration count',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='tsabeta',
                                mnemonic='tsabeta',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Real',
                                        description='Scattering cross-section reduction for TSA',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ptconv',
                                mnemonic='ptconv',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Special criticality convergence scheme on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='norm',
                                mnemonic='norm',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Real',
                                        description='Norm',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='xsectp',
                                mnemonic='xsectp',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Cross-section print flag',
                                        restriction='setting in {0, 1, 2}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='fissrp',
                                mnemonic='fissrp',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Print fission source rate on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='sourcp',
                                mnemonic='sourcp',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Source print flag',
                                        restriction='setting in {0, 1, 2, 3}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='angp',
                                mnemonic='angp',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Print angular flux on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='balp',
                                mnemonic='balp',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Print coarse-mesh balance tables on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='raflux',
                                mnemonic='raflux',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Prepare angular flux file on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='rmflux',
                                mnemonic='rmflux',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Prepare flux moments file on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='avatar',
                                mnemonic='avatar',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Prepare special XMFLUXA file on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='asleft',
                                mnemonic='asleft',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Right-going flux at plane i',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='asrite',
                                mnemonic='asrite',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Left-going flux at plane i',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='asbott',
                                mnemonic='asbott',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Top-going flux at plane j',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='astop',
                                mnemonic='astop',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Bottom-going flux at plane j',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='asfrnt',
                                mnemonic='asfrnt',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Back-going flux at plane k',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='asback',
                                mnemonic='asback',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Front-going flux at plane k',
                                        restriction='',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='massed',
                                mnemonic='massed',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Mass edits on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='pted',
                                mnemonic='pted',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Edits by fine mesh on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='zned',
                                mnemonic='zned',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Edits by zone on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='rzflux',
                                mnemonic='rzflux',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Write a-flux file on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='rzmflux',
                                mnemonic='rzmflux',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Write b-flux file on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='edoutf',
                                mnemonic='edoutf',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='ASCII output files control',
                                        restriction='setting in {-3, -2, -1, 0, 1, 2, 3}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='byvolp',
                                mnemonic='byvolp',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Printed point reactions rates on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='ajed',
                                mnemonic='ajed',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Regular/adjoint edits control',
                                        restriction='setting in {0, 1}',
                                    ),
                                ],
                            ),
                            OptionScheme(
                                name='fluxone',
                                mnemonic='fluxone',
                                attributes=[
                                    AttributeScheme(
                                        name='setting',
                                        type='types.Integer',
                                        description='Flux override on/off',
                                        restriction='setting.value in {0, 1}',
                                    ),
                                ],
                            ),
                        ],
                        entries=[],
                    ),
                ],
            ),
            OptionScheme(
                name='embed',
                mnemonic='embed',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[embed_.EmbedOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='background',
                        mnemonic='background',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Background pseudo-cell number',
                                restriction='1 <= number <= 99_999_999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='meshgeo',
                        mnemonic='meshgeo',
                        attributes=[
                            AttributeScheme(
                                name='form',
                                type='types.String',
                                description='Format specification of the embedded mesh input file',
                                restriction='form in {"lnk3dnt", "abaqu", "mcnpum"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='mgeoin',
                        mnemonic='mgeoin',
                        attributes=[
                            AttributeScheme(
                                name='filename',
                                type='types.String',
                                description='Name of the input file containing the mesh description',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='meeout',
                        mnemonic='meeout',
                        attributes=[
                            AttributeScheme(
                                name='filename',
                                type='types.String',
                                description='Name assigned to EEOUT, the elemental edit output file',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='meein',
                        mnemonic='meein',
                        attributes=[
                            AttributeScheme(
                                name='filename',
                                type='types.String',
                                description='Name of the EEOUT results file to read',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='calcvols',
                        mnemonic='calcvols',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Yes/no calculate the inferred geometry cell information',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='debug',
                        mnemonic='debug',
                        attributes=[
                            AttributeScheme(
                                name='parameter',
                                type='types.String',
                                description='Debug parameter',
                                restriction='parameter in {"echomesh"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='filetype',
                        mnemonic='filetype',
                        attributes=[
                            AttributeScheme(
                                name='kind',
                                type='types.String',
                                description='File type for the elemental edit output file',
                                restriction='type in {"ascii", "binary"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='gmvfile',
                        mnemonic='gmvfile',
                        attributes=[
                            AttributeScheme(
                                name='filename',
                                type='types.String',
                                description='Name of the GMV output file',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='length',
                        mnemonic='length',
                        attributes=[
                            AttributeScheme(
                                name='factor',
                                type='types.Real',
                                description='Conversion factor to centimeters for all mesh dimentions',
                                restriction='factor > 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='mcnpumfile',
                        mnemonic='mcnpumfile',
                        attributes=[
                            AttributeScheme(
                                name='filename',
                                type='types.String',
                                description='Name of the MCNPUM output file',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='embee',
                mnemonic='embee',
                attributes=[
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='options',
                        type='tuple[embee_.EmbeeOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='embed',
                        mnemonic='embed',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Embedded mesh universe number',
                                restriction='0 <= number <= 99_999_999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='energy',
                        mnemonic='energy',
                        attributes=[
                            AttributeScheme(
                                name='factor',
                                type='types.Real',
                                description='Multiplicative conversion factor for energy-related output',
                                restriction='factor > 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='time',
                        mnemonic='time',
                        attributes=[
                            AttributeScheme(
                                name='factor',
                                type='types.Real',
                                description='Multiplicative conversion factor for time-related output',
                                restriction='factor > 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='atom',
                        mnemonic='atom',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Flag to multiply by atom density',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='factor',
                        mnemonic='factor',
                        attributes=[
                            AttributeScheme(
                                name='constant',
                                type='types.Real',
                                description='Multiplicative constant',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='list',
                        mnemonic='list',
                        attributes=[
                            AttributeScheme(
                                name='reactions',
                                type='types.Real',
                                description='List of reactions',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='mat',
                        mnemonic='mat',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Material number',
                                restriction='0 <= number <= 99_999_999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='mtype',
                        mnemonic='mtype',
                        attributes=[
                            AttributeScheme(
                                name='kind',
                                type='types.String',
                                description='Multiplier type',
                                restriction='type in {"flux", "isotropic", "population", "reaction", "source", "track"}',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='embeb',
                mnemonic='embeb',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Tuple of upper energy bounds',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='embem',
                mnemonic='embem',
                attributes=[
                    AttributeScheme(
                        name='multipliers',
                        type='tuple[types.Real]',
                        description='Tuple of energy multipliers',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='embtb',
                mnemonic='embtb',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Tuple of upper time bounds',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='embtm',
                mnemonic='embtm',
                attributes=[
                    AttributeScheme(
                        name='multipliers',
                        type='tuple[types.Real]',
                        description='Tuple of time multipliers',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='embdb',
                mnemonic='embdb',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Tuple of upper dose energy bounds',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='embdf',
                mnemonic='embdf',
                attributes=[
                    AttributeScheme(
                        name='multipliers',
                        type='tuple[types.Real]',
                        description='Tuple of dose energy multipliers',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='m',
                mnemonic='m',
                attributes=[
                    AttributeScheme(
                        name='substances',
                        type='tuple[m_.MEntry_Substance]',
                        description='Tuple of material constituents',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='options',
                        type='tuple[m_.MOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='substance',
                        attributes=[
                            AttributeScheme(
                                name='zaid',
                                type='types.Zaid',
                                description='Substance ZAID alias',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='fraction',
                                type='types.Real',
                                description='Substance fraction',
                                restriction='-1 <= fraction <= 1',
                            ),
                        ],
                    ),
                ],
                options=[
                    OptionScheme(
                        name='gas',
                        mnemonic='gas',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Flag for density-effect correction to electron stopping power',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='estep',
                        mnemonic='estep',
                        attributes=[
                            AttributeScheme(
                                name='step',
                                type='types.Integer',
                                description='Number of electron sub-step per energy step',
                                restriction='step >= 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='hstep',
                        mnemonic='hstep',
                        attributes=[
                            AttributeScheme(
                                name='step',
                                type='types.Integer',
                                description='Number of proton sub-step per energy step',
                                restriction='step >= 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='nlib',
                        mnemonic='nlib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default neutron table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='plib',
                        mnemonic='plib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default photoatomic table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='pnlib',
                        mnemonic='pnlib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default photonuclear table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='elib',
                        mnemonic='elib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default electron table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='hlib',
                        mnemonic='hlib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default proton table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='alib',
                        mnemonic='alib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default alpha table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='slib',
                        mnemonic='slib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default helion table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='tlib',
                        mnemonic='tlib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default triton table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='dlib',
                        mnemonic='dlib',
                        attributes=[
                            AttributeScheme(
                                name='abx',
                                type='types.String',
                                description='Default deuteron table identifier',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='cond',
                        mnemonic='cond',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Real',
                                description='Conduction state for EL03 electron-transport evaluation',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='refi',
                        mnemonic='refi',
                        attributes=[
                            AttributeScheme(
                                name='refractive_index',
                                type='types.Real',
                                description='Refractive index constant',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='refc',
                        mnemonic='refc',
                        attributes=[
                            AttributeScheme(
                                name='coefficents',
                                type='tuple[types.Real]',
                                description='Cauchy coefficents',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='refs',
                        mnemonic='refs',
                        attributes=[
                            AttributeScheme(
                                name='coefficents',
                                type='tuple[types.Real]',
                                description='Sellmeier coefficents',
                                restriction='',
                            ),
                        ],
                    ),
                ],
                extra='''
@staticmethod
    def from_formula(number: int, formulas: dict[str, float], atomic_or_weight: bool = True):
        """
        Generates ``DataOption_M`` from INP.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            atomic_or_weight: Atomtic/Weight fraction true/false flag.

        Returns:
            ``DataOption_M`` object.
        """

        substances = []
        comments = []
        for formula, mixture_fraction in formulas.items():
            formula = molmass.Formula(formula)

            composition = formula.composition()
            for element in composition:
                compound_fraction = (
                    composition[element].fraction
                    if atomic_or_weight
                    else composition[element].mass / formula.mass
                )

                zaids = [
                    (
                        types.Zaid(_elements.ELEMENTS[element]['z'], a),
                        isotropic_fraction,
                    )
                    for a, isotropic_fraction in _elements.ELEMENTS[element]['fraction'].items()
                ]
                subcomments = [f"{element}-{zaid.a:03}" for zaid, _ in zaids]
                entries = [
                    m.MEntry_Substance(
                        zaid,
                        types.Real(
                            (-1 if atomic_or_weight else 1)
                            * mixture_fraction
                            * compound_fraction
                            * isotropic_fraction
                        ),
                    )
                    for zaid, isotropic_fraction in zaids
                ]

                comments += subcomments
                substances += entries

        material = DataOption_M(substances, types.Integer(number), [])
        material.comment = tuple(comments)

        return material
'''[1:-1],
            ),
            OptionScheme(
                name='mt',
                mnemonic='mt',
                attributes=[
                    AttributeScheme(
                        name='identifier',
                        type='types.String',
                        description='Corresponding S(α,β) identifier',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='mx',
                mnemonic='mx',
                attributes=[
                    AttributeScheme(
                        name='zaids',
                        type='tuple[types.Zaid]',
                        description='Zaid substitutions for particles',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='otfdb',
                mnemonic='otfdb',
                attributes=[
                    AttributeScheme(
                        name='zaids',
                        type='tuple[types.Zaid]',
                        description='Identifiers for the broadening tables',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='totnu',
                mnemonic='totnu',
                attributes=[
                    AttributeScheme(
                        name='no',
                        type='types.String',
                        description='Delay fission sampling on/off',
                        restriction='no == "no"',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='nonu',
                mnemonic='nonu',
                attributes=[
                    AttributeScheme(
                        name='settings',
                        type='tuple[types.Integer]',
                        description='Tuple of fission settings',
                        restriction='filter(lambda entry: not (entry == 0 or entry == 1 or entry == 2), settings)',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='awtab',
                mnemonic='awtab',
                attributes=[
                    AttributeScheme(
                        name='weight_ratios',
                        type='tuple[awtab_.AwtabEntry_Substance]',
                        description='Tuple of atomic weight ratios',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='substance',
                        attributes=[
                            AttributeScheme(
                                name='zaid',
                                type='types.Zaid',
                                description='Zaid alias for nuclide',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='weight_ratio',
                                type='types.Real',
                                description='Atomic weight ratios',
                                restriction='weight_ratio > 0',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='xs',
                mnemonic='xs',
                attributes=[
                    AttributeScheme(
                        name='weight_ratios',
                        type='tuple[xs_.XsEntry_Substance]',
                        description='Tuple of atomic weight ratios',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='substance',
                        attributes=[
                            AttributeScheme(
                                name='zaid',
                                type='types.Zaid',
                                description='Zaid alias for nuclide',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='weight_ratio',
                                type='types.Real',
                                description='Atomic weight ratios',
                                restriction='weight_ratio > 0',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='void',
                mnemonic='void',
                attributes=[
                    AttributeScheme(
                        name='numbers',
                        type='tuple[types.Integer]',
                        description='Tuple of cell numbers',
                        restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='mgopt',
                mnemonic='mgopt',
                attributes=[
                    AttributeScheme(
                        name='mcal',
                        type='types.String',
                        description='Problem type setting',
                        restriction='mcal in {"f", "a"}',
                    ),
                    AttributeScheme(
                        name='igm',
                        type='types.Integer',
                        description='Total number of energy groups for all kinds of particle',
                        restriction='igm >= 0',
                    ),
                    AttributeScheme(
                        name='iplt',
                        type='types.Integer',
                        description='Weight windows usage indicator',
                        restriction='iplt == 0 or iplt == 1 or iplt == 2',
                    ),
                    AttributeScheme(
                        name='iab',
                        type='types.Integer',
                        description='Adjoint biasing for adjoint problems contorls',
                        restriction='iab == 0 or iab == 1 or iab == 2',
                    ),
                    AttributeScheme(
                        name='icw',
                        type='types.Integer',
                        description='Name of the reference cell for generated weight windows',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='fnw',
                        type='types.Real',
                        description='Normalization value for generated weight windows',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='rim',
                        type='types.Real',
                        description='Generated weight windows compression limit',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='drxs',
                mnemonic='drxs',
                attributes=[
                    AttributeScheme(
                        name='zaids',
                        type='tuple[types.Zaid]',
                        description='Tuple of ZAID aliases',
                        restriction='',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='mode',
                mnemonic='mode',
                attributes=[
                    AttributeScheme(
                        name='particles',
                        type='tuple[types.Designator]',
                        description='Tuple of particle designators',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='act',
                mnemonic='act',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[act_.ActOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    )
                ],
                options=[
                    OptionScheme(
                        name='fission',
                        mnemonic='fission',
                        attributes=[
                            AttributeScheme(
                                name='kind',
                                type='types.String',
                                description='Type of delayed particle(s) to be produced from residuals created by fission',
                                restriction='type in {"none", "n,p,e,f,a", "all"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='nonfiss',
                        mnemonic='nonfiss',
                        attributes=[
                            AttributeScheme(
                                name='kind',
                                type='types.String',
                                description='Type of delayed particle(s) to be produced by simple multi-particle reaction',
                                restriction='type in {"none", "n,p,e,f,a", "all"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='dn',
                        mnemonic='dn',
                        attributes=[
                            AttributeScheme(
                                name='source',
                                type='types.String',
                                description='Delayed neutron data source',
                                restriction='source in {"model", "library", "both", "prompt"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='dg',
                        mnemonic='dg',
                        attributes=[
                            AttributeScheme(
                                name='source',
                                type='types.String',
                                description='Delayed gamma data source',
                                restriction='source in {"line", "mg", "none"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='thresh',
                        mnemonic='thresh',
                        attributes=[
                            AttributeScheme(
                                name='fraction',
                                type='types.Real',
                                description='Fraction of highest-amplitude discrete delayed-gamma lines retained',
                                restriction='0 <= fraction <= 1',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='dnbais',
                        mnemonic='dnbais',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='Maximum number of neutrons generated per reaction',
                                restriction='0 <= count <= 10',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='nap',
                        mnemonic='nap',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='Number of activation products',
                                restriction='0 <= count',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='dneb',
                        mnemonic='dneb',
                        attributes=[
                            AttributeScheme(
                                name='biases',
                                type='tuple[dneb_.DnebEntry_Bias]',
                                description='Delayed neutron energy biases',
                                restriction='',
                            ),
                        ],
                        entries=[
                            EntryScheme(
                                name='bias',
                                attributes=[
                                    AttributeScheme(
                                        name='weight',
                                        type='types.Real',
                                        description='Weight for bin',
                                        restriction='',
                                    ),
                                    AttributeScheme(
                                        name='energy',
                                        type='types.Real',
                                        description='Upper energy for bin',
                                        restriction='',
                                    ),
                                ],
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='dgeb',
                        mnemonic='dgeb',
                        attributes=[
                            AttributeScheme(
                                name='biases',
                                type='tuple[dgeb_.DgebEntry_Bias]',
                                description='Delayed neutron energy biases',
                                restriction='',
                            ),
                        ],
                        entries=[
                            EntryScheme(
                                name='bias',
                                attributes=[
                                    AttributeScheme(
                                        name='weight',
                                        type='types.Real',
                                        description='Weight for bin',
                                        restriction='',
                                    ),
                                    AttributeScheme(
                                        name='energy',
                                        type='types.Real',
                                        description='Upper energy for bin',
                                        restriction='',
                                    ),
                                ],
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='pecut',
                        mnemonic='pecut',
                        attributes=[
                            AttributeScheme(
                                name='cutoff',
                                type='types.Real',
                                description='Delayed-gamma energy cutoff',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='hlcut',
                        mnemonic='hlcut',
                        attributes=[
                            AttributeScheme(
                                name='cutoff',
                                type='types.Real',
                                description='Spontaneous-decay half-life threshold',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='sample',
                        mnemonic='sample',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Flag for correlated or uncorrelated',
                                restriction='setting in {"correlate", "nonfiss_cor"}',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='cut',
                mnemonic='cut',
                attributes=[
                    AttributeScheme(
                        name='time_cutoff',
                        type='types.Real',
                        description='Time cutoff in shakes',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_cutoff',
                        type='types.Real',
                        description='Lower energy cutoff',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='weight_cutoff1',
                        type='types.Real',
                        description='Weight cutoff #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='weight_cutoff2',
                        type='types.Real',
                        description='Weight cutoff #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='source_weight',
                        type='types.Real',
                        description='Minimum source weight',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='elpt',
                mnemonic='elpt',
                attributes=[
                    AttributeScheme(
                        name='cutoffs',
                        type='tuple[types.Real]',
                        description='Tuple of cell lower energy cutoffs',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='thtme',
                mnemonic='thtme',
                attributes=[
                    AttributeScheme(
                        name='times',
                        type='tuple[types.Real]',
                        description='Tuple of times when thermal temperatures are specified',
                        restriction='filter(lambda entry: not (entry <= 99), times)',
                    ),
                ],
            ),
            OptionScheme(
                name='mphys',
                mnemonic='mphys',
                attributes=[
                    AttributeScheme(
                        name='setting',
                        type='types.String',
                        description='Physics models on/off',
                        restriction='setting in {"on", "off"}',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='lca',
                mnemonic='lca',
                attributes=[
                    AttributeScheme(
                        name='ielas',
                        type='types.Integer',
                        description='Elastic scattering controls',
                        restriction='ielas == 0 or ielas == 1 or ielas == 2',
                    ),
                    AttributeScheme(
                        name='ipreg',
                        type='types.Integer',
                        description='pre-equilibrium model',
                        restriction='ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3',
                    ),
                    AttributeScheme(
                        name='iexisa',
                        type='types.Integer',
                        description='Model choice controls',
                        restriction='iexisa == 0 or iexisa == 1 or iexisa == 2',
                    ),
                    AttributeScheme(
                        name='ichoic',
                        type='types.Integer',
                        description='ISABEL intranuclear cascade model control',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='jcoul',
                        type='types.Integer',
                        description='Coulomb barrier for incident charged particle controls',
                        restriction='jcoul == 0 or jcoul == 1',
                    ),
                    AttributeScheme(
                        name='nexite',
                        type='types.Integer',
                        description='Subtract nuclear recoil energy to get excitation energy',
                        restriction='nexite == 0 or nexite == 1',
                    ),
                    AttributeScheme(
                        name='npidk',
                        type='types.Integer',
                        description='Cutoff interact/terminate control',
                        restriction='npidk == 0 or npidk == 1',
                    ),
                    AttributeScheme(
                        name='noact',
                        type='types.Integer',
                        description='Particle transport settings',
                        restriction='noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2',
                    ),
                    AttributeScheme(
                        name='icem',
                        type='types.Integer',
                        description='Choose alternative physics model',
                        restriction='icem == 0 or icem == 1 or icem == 2',
                    ),
                    AttributeScheme(
                        name='ilaq',
                        type='types.Integer',
                        description='Choose light ion and nucleon physics modules',
                        restriction='ilaq == 0 or ilaq == 1',
                    ),
                    AttributeScheme(
                        name='nevtype',
                        type='types.Integer',
                        description='Choose number of evaporation particles for GEM2',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='lcb',
                mnemonic='lcb',
                attributes=[
                    AttributeScheme(
                        name='flenb1',
                        type='types.Real',
                        description='Kinetic energy for nucleons CEM/Bertini/INCL',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='flenb2',
                        type='types.Real',
                        description='Kinetic energy for nucleons LAQGSM03.03',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='flenb3',
                        type='types.Real',
                        description='Kinetic energy for pions CEM/Bertini/INCL',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='flenb4',
                        type='types.Real',
                        description='Kinetic energy for pions LAQGSM03.03',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='flenb5',
                        type='types.Real',
                        description='Kinetic energy for nucleons ISABEL',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='flenb6',
                        type='types.Real',
                        description='Kinetic energy for appropriate model',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='cotfe',
                        type='types.Real',
                        description='Cutoff kinetic energy for particle escape',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='film0',
                        type='types.Real',
                        description='Maximum correction allowed for masss-energy balancing',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='lcc',
                mnemonic='lcc',
                attributes=[
                    AttributeScheme(
                        name='stincl',
                        type='types.Real',
                        description='Rescaling factor of the cascade duration',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='v0incl',
                        type='types.Real',
                        description='Potential depth',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='xfoisaincl',
                        type='types.Real',
                        description='Maximum impact parameter for Pauli blocking',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='npaulincl',
                        type='types.Integer',
                        description='Pauli blocking parameter setting',
                        restriction='npaulincl == 0 or npaulincl == -1 or npaulincl == 1',
                    ),
                    AttributeScheme(
                        name='nosurfincl',
                        type='types.Integer',
                        description='Difuse nuclear surface based on Wood-Saxon density setting',
                        restriction='xfoisaincl == -2 or xfoisaincl == -1 or xfoisaincl == 0 or xfoisaincl == 1',
                    ),
                    AttributeScheme(
                        name='ecutincl',
                        type='types.Real',
                        description='Bertini model energy below this energy',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ebankincl',
                        type='types.Real',
                        description='INCL bank particles below this energy',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ebankabia',
                        type='types.Real',
                        description='ABLA bank particles below this energy',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='lea',
                mnemonic='lea',
                attributes=[
                    AttributeScheme(
                        name='ipht',
                        type='types.Integer',
                        description='Generation of de-excitation photons setting',
                        restriction='ipht.value in {0, 1}',
                    ),
                    AttributeScheme(
                        name='icc',
                        type='types.Integer',
                        description='Level of physics for PHT physics setting',
                        restriction='icc.value in {0, 1, 2, 3, 4}',
                    ),
                    AttributeScheme(
                        name='nobalc',
                        type='types.Integer',
                        description='Mass-energy balancing in cascade setting',
                        restriction='nobalc.value in {0, 1}',
                    ),
                    AttributeScheme(
                        name='nobale',
                        type='types.Integer',
                        description='Mass-energy balancing in evaporation setting',
                        restriction='nobale.value in {0, 1}',
                    ),
                    AttributeScheme(
                        name='ifbrk',
                        type='types.Integer',
                        description='Mass-energy balancing in Fermi-breakup setting',
                        restriction='ifbrk.value in {0, 1}',
                    ),
                    AttributeScheme(
                        name='ilvden',
                        type='types.Integer',
                        description='Level-density model setting',
                        restriction='ilvden.value in {0, 1, -1}',
                    ),
                    AttributeScheme(
                        name='ievap',
                        type='types.Integer',
                        description='Evaporation and fission model setting',
                        restriction='ievap.value in {0, 1, -1, 2}',
                    ),
                    AttributeScheme(
                        name='nofis',
                        type='types.Integer',
                        description='Fission setting',
                        restriction='nofis.value in {0, 1}',
                    ),
                ],
            ),
            OptionScheme(
                name='leb',
                mnemonic='leb',
                attributes=[
                    AttributeScheme(
                        name='yzere',
                        type='types.Real',
                        description='Y0 parameter in level-density formula for Z≤70',
                        restriction='yzere > 0',
                    ),
                    AttributeScheme(
                        name='bzere',
                        type='types.Real',
                        description='B0 parameter in level-density formula for Z≤70',
                        restriction='bzere > 0',
                    ),
                    AttributeScheme(
                        name='yzero',
                        type='types.Real',
                        description='Y0 parameter in level-density formula for Z≥71',
                        restriction='yzero > 0',
                    ),
                    AttributeScheme(
                        name='bzero',
                        type='types.Real',
                        description='B0 parameter in level-density formula for Z≥70',
                        restriction='bzero > 0',
                    ),
                ],
            ),
            OptionScheme(
                name='fmult',
                mnemonic='fmult',
                attributes=[
                    AttributeScheme(
                        name='zaid',
                        type='types.Zaid',
                        description='Nuclide for which data are entered',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='options',
                        type='tuple[fmult_.FmultOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                # UNION
                options=[
                    #                OptionScheme(
                    #                    name='sfnu',
                    #                    attributes=[
                    #                        AttributeScheme(
                    #                            name='distribution',
                    #                            type='Union[Real, tuple[types.Real]]',
                    #                            description='V bar for or of cumulative distribution the sampling spontaneous fission',
                    #                        ),
                    #                    ],
                    #                ),
                    OptionScheme(
                        name='width',
                        mnemonic='width',
                        attributes=[
                            AttributeScheme(
                                name='width',
                                type='types.Real',
                                description='Width for sampling spontaneous fission',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='sfyield',
                        mnemonic='sfyield',
                        attributes=[
                            AttributeScheme(
                                name='fission_yield',
                                type='types.Real',
                                description='Spontaneous fission yield',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='watt',
                        mnemonic='watt',
                        attributes=[
                            AttributeScheme(
                                name='a',
                                type='types.Real',
                                description='Watt energy spectrum parameters a',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='b',
                                type='types.Real',
                                description='Watt energy spectrum parameters b',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='method',
                        mnemonic='method',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Integer',
                                description='Gaussian sampling algorithm setting',
                                restriction='setting.value in {0, 1, 3, 5, 6, 7}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='data',
                        mnemonic='data',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Integer',
                                description='Sampling method setting',
                                restriction='setting.value in {0, 1, 2, 3}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='shift',
                        mnemonic='shift',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Integer',
                                description='Shift method setting',
                                restriction='setting.value in {0, 1, 2, 3, 4}',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='tropt',
                mnemonic='tropt',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[tropt_.TroptOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='mcscat',
                        mnemonic='mcscat',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Multiple coulomb scattering setting',
                                restriction='setting in {"off", "fnal1", "gaussian", "fnal2"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='eloss',
                        mnemonic='eloss',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Slowing down energy losses setting',
                                restriction='setting in {"off", "strag1", "csda"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='nreact',
                        mnemonic='nreact',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Nuclear reactions setting',
                                restriction='setting in {"off", "on", "atten", "remove"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='nescat',
                        mnemonic='nescat',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Nuclear elastic scattering setting',
                                restriction='setting in {"off", "on"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='genxs',
                        mnemonic='genxs',
                        attributes=[
                            AttributeScheme(
                                name='filename',
                                type='types.String',
                                description='Cross section generation setting',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='unc',
                mnemonic='unc',
                attributes=[
                    AttributeScheme(
                        name='settings',
                        type='tuple[types.Integer]',
                        description='Tuple of uncollided secondary settings',
                        restriction='filter(lambda entry: not (entry.value in {0, 1}), settings)',
                    ),
                ],
            ),
            OptionScheme(
                name='cosyp',
                mnemonic='cosyp',
                attributes=[
                    AttributeScheme(
                        name='prefix',
                        type='types.Integer',
                        description='Prefix number of the COSY map files',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='axsh',
                        type='types.Integer',
                        description='Horiztonal axis orientation',
                        restriction='axsh.value in {1, 2, 3}',
                    ),
                    AttributeScheme(
                        name='axsv',
                        type='types.Integer',
                        description='Vertical axis orientation',
                        restriction='axsv.value in {1, 2, 3}',
                    ),
                    AttributeScheme(
                        name='emaps',
                        type='tuple[types.Real]',
                        description='Tuple of operating beam energies',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='cosy',
                mnemonic='cosy',
                attributes=[
                    AttributeScheme(
                        name='numbers',
                        type='tuple[types.Integer]',
                        description='Tuple of COSY map numbers',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='bfld',
                mnemonic='bfld',
                attributes=[
                    AttributeScheme(
                        name='kind',
                        type='types.String',
                        description='Magnetic field type',
                        restriction='type in {"const", "quad", "quadff"}',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='options',
                        type='tuple[bfld_.BfldOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='field',
                        mnemonic='field',
                        attributes=[
                            AttributeScheme(
                                name='strength_gradient',
                                type='types.Real',
                                description='Magnetic field strength/gradient',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='vec',
                        mnemonic='vec',
                        attributes=[
                            AttributeScheme(
                                name='vector',
                                type='tuple[types.Real]',
                                description='Direction of mangentic field or plane corresponding to the x-axis of the quadrapole',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='maxdeflc',
                        mnemonic='maxdeflc',
                        attributes=[
                            AttributeScheme(
                                name='angle',
                                type='types.Real',
                                description='Maximum deflection angles',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='maxstep',
                        mnemonic='maxstep',
                        attributes=[
                            AttributeScheme(
                                name='size',
                                type='types.Real',
                                description='Maximum step size',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='axs',
                        mnemonic='axs',
                        attributes=[
                            AttributeScheme(
                                name='vector',
                                type='tuple[types.Real]',
                                description='Direction of the cosines of the quadropole beam axis',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ffedges',
                        mnemonic='ffedges',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Real]',
                                description='Surface numbers to apply field fringe edges',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='refpnt',
                        mnemonic='refpnt',
                        attributes=[
                            AttributeScheme(
                                name='point',
                                type='tuple[types.Real]',
                                description='Point anywhere on the quadrapole beam',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='bflcl',
                mnemonic='bflcl',
                attributes=[
                    AttributeScheme(
                        name='numbers',
                        type='tuple[types.Integer]',
                        description='Tuple of BFLD map numbers',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='sdef',
                mnemonic='sdef',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[sdef_.SdefOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='cel',
                        mnemonic='cel',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Cell number',
                                restriction='0 <= number <= 99_999_999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='sur',
                        mnemonic='sur',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Surface number',
                                restriction='0 <= number <= 99_999_999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='erg',
                        mnemonic='erg',
                        attributes=[
                            AttributeScheme(
                                name='energy',
                                type='types.Real',
                                description='Kinetic energy',
                                restriction='',
                            ),
                        ],
                    ),
                    # UNION
                    #            OptionScheme(
                    #                name='tme',
                    #                attributes=[
                    #                    AttributeScheme(
                    #                        name='time',
                    #                        type='Union[Real, types.EmbeddedDistributionNumber]',
                    #                        description='Time in shakes',
                    #                    ),
                    #                ],
                    #            ),
                    OptionScheme(
                        name='dir',
                        mnemonic='dir',
                        attributes=[
                            AttributeScheme(
                                name='cosine',
                                type='types.Real',
                                description='Cosine of the angle between VEC and particle',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='vec',
                        mnemonic='vec',
                        attributes=[
                            AttributeScheme(
                                name='x',
                                type='types.Real',
                                description='Reference vector for DIR x-component',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='y',
                                type='types.Real',
                                description='Reference vector for DIR y-component',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='z',
                                type='types.Real',
                                description='Reference vector for DIR z-component',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='nrm',
                        mnemonic='nrm',
                        attributes=[
                            AttributeScheme(
                                name='sign',
                                type='types.Integer',
                                description='Sign of the surface normal',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='pos',
                        mnemonic='pos',
                        attributes=[
                            AttributeScheme(
                                name='vector',
                                type='tuple[types.Real]',
                                description='Reference point for position sampling in vector notation',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='rad',
                        mnemonic='rad',
                        attributes=[
                            AttributeScheme(
                                name='radial_distance',
                                type='types.Real',
                                description='Radial distance fo the position from POS or AXS',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ext',
                        mnemonic='ext',
                        attributes=[
                            AttributeScheme(
                                name='distance_cosine',
                                type='types.Real',
                                description='Distance for POS along AXS or Cosine of angle from AXS',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='axs',
                        mnemonic='axs',
                        attributes=[
                            AttributeScheme(
                                name='x',
                                type='types.Real',
                                description='Reference vector for EXT and RAD x-component',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='y',
                                type='types.Real',
                                description='Reference vector for EXT and RAD y-component',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='z',
                                type='types.Real',
                                description='Reference vector for EXT and RAD z-component',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='x',
                        mnemonic='x',
                        attributes=[
                            AttributeScheme(
                                name='x_coordinate',
                                type='types.Real',
                                description='X-cordinate of position',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='y',
                        mnemonic='y',
                        attributes=[
                            AttributeScheme(
                                name='y_coordinate',
                                type='types.Real',
                                description='Y-cordinate of position',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='z',
                        mnemonic='z',
                        attributes=[
                            AttributeScheme(
                                name='z_coordinate',
                                type='types.Real',
                                description='Z-cordinate of position',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ccc',
                        mnemonic='ccc',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Cookie-cutter cell number',
                                restriction='0 <= number <= 99_999_999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ara',
                        mnemonic='ara',
                        attributes=[
                            AttributeScheme(
                                name='area',
                                type='types.Real',
                                description='Area of surface',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='wgt',
                        mnemonic='wgt',
                        attributes=[
                            AttributeScheme(
                                name='weight',
                                type='types.Real',
                                description='Particle weight',
                                restriction='',
                            ),
                        ],
                    ),
                    #            OptionScheme(
                    #                name='tr',
                    #                attributes=[
                    #                    AttributeScheme(
                    #                        name='number',
                    #                        type='Union[types.DistributionNumber, Integer]',
                    #                        description='Particle weight',
                    #                    ),
                    #                ],
                    #            ),
                    OptionScheme(
                        name='eff',
                        mnemonic='eff',
                        attributes=[
                            AttributeScheme(
                                name='criterion',
                                type='types.Real',
                                description='Rejection efficiency criterion for position sampling',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='par',
                        mnemonic='par',
                        attributes=[
                            AttributeScheme(
                                name='kind',
                                type='types.String',
                                description='Source particle type',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='dat',
                        mnemonic='dat',
                        attributes=[
                            AttributeScheme(
                                name='month',
                                type='types.Integer',
                                description='Month for cosmic-ray & background sources',
                                restriction='1 <= month <= 12',
                            ),
                            AttributeScheme(
                                name='day',
                                type='types.Integer',
                                description='Day for cosmic-ray & background sources',
                                restriction='1 <= day <= 31',
                            ),
                            AttributeScheme(
                                name='year',
                                type='types.Integer',
                                description='Year for cosmic-ray & background sources',
                                restriction='1 <= year <= 9999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='loc',
                        mnemonic='loc',
                        attributes=[
                            AttributeScheme(
                                name='latitude',
                                type='types.Real',
                                description='Latitude for cosmic source',
                                restriction='-90 <= latitude <= 90',
                            ),
                            AttributeScheme(
                                name='longitude',
                                type='types.Real',
                                description='Longitude for cosmic source',
                                restriction='-180 <= longitude <= 180',
                            ),
                            AttributeScheme(
                                name='altitude',
                                type='types.Real',
                                description='Altitude for cosmic source',
                                restriction='0 <= altitude',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='bem',
                        mnemonic='bem',
                        attributes=[
                            AttributeScheme(
                                name='exn',
                                type='types.Real',
                                description='Normalized beam emittance parameter for x coordinates',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='eyn',
                                type='types.Real',
                                description='Normalized beam emittance parameter for x coordinates',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='bml',
                                type='types.Real',
                                description='Distance from the aperture to the spot',
                                restriction='bml >= 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='bap',
                        mnemonic='bap',
                        attributes=[
                            AttributeScheme(
                                name='ba1',
                                type='types.Real',
                                description='Beam aperture half-width in the x transverse direction',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='ba2',
                                type='types.Real',
                                description='Beam aperture half-width in the y transverse direction',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='u',
                                type='types.Real',
                                description='Unused, arrbirary value',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            # UNION
            #    OptionScheme(
            #        name='si',
            #        attributes=[
            #            AttributeScheme(
            #                name='option',
            #                type='types.String',
            #                description='Information kind setting',
            #            ),
            #            AttributeScheme(
            #                name='information',
            #                type='tuple[Union[Real, types.DistributionNumber]]',
            #                description='Particle source information',
            #            ),
            #            AttributeScheme(
            #                name='suffix',
            #                type='types.Integer',
            #                description='Data card option suffix',
            #            ),
            #        ],
            #    ),
            OptionScheme(
                name='sp_0',
                mnemonic='sp',
                attributes=[
                    AttributeScheme(
                        name='option',
                        type='types.String',
                        description='Probability kind setting',
                        restriction='option in {"d", "c", "v", "w"}',
                    ),
                    AttributeScheme(
                        name='probabilities',
                        type='tuple[types.Real]',
                        description='Particle source probabilities',
                        restriction='filter(lambda entry: not (0 <= entry <= 1), probabilities)',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='1 <= suffix <= 999',
                    ),
                ],
            ),
            OptionScheme(
                name='sp_1',
                mnemonic='sp',
                attributes=[
                    AttributeScheme(
                        name='function',
                        type='types.Integer',
                        description='Built-in function designator',
                        restriction='function in {-2, -3, -4, -5, -6, -7, -21, -31, -41}',
                    ),
                    AttributeScheme(
                        name='a',
                        type='types.Real',
                        description='Built-in function parameter #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='b',
                        type='types.Real',
                        description='Built-in function parameter #2',
                        restriction='',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='sb_0',
                mnemonic='sb',
                attributes=[
                    AttributeScheme(
                        name='option',
                        type='types.String',
                        description='Bias kind setting',
                        restriction='option in {"d", "c", "v", "w"}',
                    ),
                    AttributeScheme(
                        name='biases',
                        type='tuple[types.Real]',
                        description='Particle source biases',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='1 <= suffix <= 999',
                    ),
                ],
            ),
            OptionScheme(
                name='sb_1',
                mnemonic='sb',
                attributes=[
                    AttributeScheme(
                        name='function',
                        type='types.Integer',
                        description='Built-in function designator',
                        restriction='function in {-2, -3, -4, -5, -6, -7, -21, -31, -41}',
                    ),
                    AttributeScheme(
                        name='a',
                        type='types.Real',
                        description='Built-in function parameter #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='b',
                        type='types.Real',
                        description='Built-in function parameter #2',
                        restriction='',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='ds_0',
                mnemonic='ds',
                attributes=[
                    AttributeScheme(
                        name='option',
                        type='types.String',
                        description='Dependent variable setting',
                        restriction='option in {"h", "l", "s"}',
                    ),
                    AttributeScheme(
                        name='js',
                        type='tuple[types.Real]',
                        description='Depdented source dependent variables',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='1 <= suffix <= 999',
                    ),
                ],
            ),
            OptionScheme(
                name='ds_1',
                mnemonic='ds',
                attributes=[
                    AttributeScheme(
                        name='t',
                        type='types.String',
                        description='Dependent source T option',
                        restriction='t in {"t"}',
                    ),
                    AttributeScheme(
                        name='ijs',
                        type='tuple[ds_1_.Ds1Entry_Tpair]',
                        description='Dependent source independent & dependent variables',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='1 <= suffix <= 999',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='tpair',
                        attributes=[
                            AttributeScheme(
                                name='independent',
                                type='types.Real',
                                description='Independent source dependent variable',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='dependent',
                                type='types.Real',
                                description='Dependent source dependent variable',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='ds_2',
                mnemonic='ds',
                attributes=[
                    AttributeScheme(
                        name='q',
                        type='types.String',
                        description='Dependent source Q option',
                        restriction='q in {"q"}',
                    ),
                    AttributeScheme(
                        name='vss',
                        type='tuple[ds_2_.Ds2Entry_Qpair]',
                        description='Dependent source independent & dependent variables',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='1 <= suffix <= 999',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='tpair',
                        attributes=[
                            AttributeScheme(
                                name='independent',
                                type='types.Real',
                                description='Independent source dependent variable',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='dependent',
                                type='types.Real',
                                description='Dependent source dependent variable',
                                restriction='',
                            ),
                        ],
                    ),
                    EntryScheme(
                        name='qpair',
                        attributes=[
                            AttributeScheme(
                                name='distribution_dependent',
                                type='tuple[types.Real]',
                                description='Distribution number for dependent variable',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='sc',
                mnemonic='sc',
                attributes=[
                    AttributeScheme(
                        name='comment',
                        type='tuple[str]',
                        description='source comment',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='1 <= suffix <= 999',
                    ),
                ],
            ),
            OptionScheme(
                name='ssw',
                mnemonic='ssw',
                attributes=[
                    AttributeScheme(
                        name='surfaces',
                        type='tuple[types.Integer]',
                        description='Problem surfaces',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='cells',
                        type='tuple[types.Integer]',
                        description='Problem cells',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='options',
                        type='tuple[ssw_.SswOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='sym',
                        mnemonic='sym',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Integer',
                                description='Symmetric option flag',
                                restriction='setting in {0, 1, 2}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='pty',
                        mnemonic='pty',
                        attributes=[
                            AttributeScheme(
                                name='tracks',
                                type='tuple[types.Designator]',
                                description='Tracks to record',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='cel',
                        mnemonic='cel',
                        attributes=[
                            AttributeScheme(
                                name='cfs',
                                type='tuple[types.Integer]',
                                description='Cells from which KCODE neutrons are written',
                                restriction='filter(lambda entry: not (1 <= entry <= 99_999_999),         cfs)',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='ssr',
                mnemonic='ssr',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[ssr_.SsrOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    )
                ],
                options=[
                    OptionScheme(
                        name='old',
                        mnemonic='old',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='Tuple of surface numbers from subset of surfaces on SSW card',
                                restriction='filter(lambda entry: not (1 <= entry <= 99_999_999),         numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='cel',
                        mnemonic='cel',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='Tuple of cell from subset of cells on SSW card',
                                restriction='filter(lambda entry: not (1 <= entry <= 99_999_999),         numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='new',
                        mnemonic='new',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='Tuple of surface numbers to start run',
                                restriction='filter(lambda entry: not (1 <= entry <= 99_999_999),         numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='pty',
                        mnemonic='pty',
                        attributes=[
                            AttributeScheme(
                                name='particles',
                                type='tuple[types.Designator]',
                                description='Tuple of designators',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='col',
                        mnemonic='col',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Integer',
                                description='Collision option setting',
                                restriction='setting.value in {-1, 0, 1}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='wgt',
                        mnemonic='wgt',
                        attributes=[
                            AttributeScheme(
                                name='constant',
                                type='types.Real',
                                description='Particle weight multiplier',
                                restriction='',
                            ),
                        ],
                    ),
                    # UNION
                    #                    OptionScheme(
                    #                        name='tr',
                    #                        attributes=[
                    #                            AttributeScheme(
                    #                                name='number',
                    #                                type='Union[types.DistributionNumber, Integer]',
                    #                                description='Particle weight',
                    #                            ),
                    #                        ],
                    #                    ),
                    OptionScheme(
                        name='psc',
                        mnemonic='psc',
                        attributes=[
                            AttributeScheme(
                                name='constant',
                                type='types.Real',
                                description='Constant for approximation in PSC evaluation',
                                restriction='constant >= 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='axs',
                        mnemonic='axs',
                        attributes=[
                            AttributeScheme(
                                name='cosines',
                                type='tuple[types.Real]',
                                description='Direction cosines defining',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ext',
                        mnemonic='ext',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.DistributionNumber',
                                description='Distribution number for baising sampling',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='poa',
                        mnemonic='poa',
                        attributes=[
                            AttributeScheme(
                                name='angle',
                                type='types.Real',
                                description='Angle within which particles accepeted for transport',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='bcw',
                        mnemonic='bcw',
                        attributes=[
                            AttributeScheme(
                                name='radius',
                                type='types.Real',
                                description='Radius of cylindrical window',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='zb',
                                type='types.Real',
                                description='Bottom of cylindrical window',
                                restriction='0 < zb',
                            ),
                            AttributeScheme(
                                name='ze',
                                type='types.Real',
                                description='Top of cylindrical window',
                                restriction='0 < zb < ze',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='kcode',
                mnemonic='kcode',
                attributes=[
                    AttributeScheme(
                        name='nsrck',
                        type='types.Integer',
                        description='Number of source histories per cycle',
                        restriction='nsrck >= 0',
                    ),
                    AttributeScheme(
                        name='rkk',
                        type='types.Real',
                        description='Initial guess of keff',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ikz',
                        type='types.Integer',
                        description='Number of cycles to be skipped before beginning tally accumulation',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='kct',
                        type='types.Integer',
                        description='Total number of cycles to be done',
                        restriction='kct > 0',
                    ),
                    AttributeScheme(
                        name='msrk',
                        type='types.Integer',
                        description='Number of source points to allocate for',
                        restriction='msrk < 40 * nsrck',
                    ),
                    AttributeScheme(
                        name='knrm',
                        type='types.Integer',
                        description='Normalization of tallies setting',
                        restriction='knrm.value in {0, 1}',
                    ),
                    AttributeScheme(
                        name='mrkp',
                        type='types.Integer',
                        description='Maximum number of cycle values on MCTAL or RUNTPE files',
                        restriction='mrkp > 0',
                    ),
                    AttributeScheme(
                        name='kc8',
                        type='types.Integer',
                        description='Number of cylces for average setting',
                        restriction='kc8.value in {0, 1}',
                    ),
                ],
            ),
            OptionScheme(
                name='ksrc',
                mnemonic='ksrc',
                attributes=[
                    AttributeScheme(
                        name='locations',
                        type='tuple[ksrc_.KsrcEntry_Location]',
                        description='Tuple of inital source points',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='location',
                        attributes=[
                            AttributeScheme(
                                name='x',
                                type='types.Real',
                                description='Location x-coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='y',
                                type='types.Real',
                                description='Location y-coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='z',
                                type='types.Real',
                                description='Location z-coordinate',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='kopts',
                mnemonic='kopts',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[kopts_.KoptsOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='blocksize',
                        mnemonic='blocksize',
                        attributes=[
                            AttributeScheme(
                                name='ncy',
                                type='types.Integer',
                                description='Number of cycles in every outer iteration',
                                restriction='ncy >= 2',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='kinetics',
                        mnemonic='kinetics',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Yes/No calculate point-kinetics parameters',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='precursor',
                        mnemonic='precursor',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Yes/No detailed precursor information',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ksental',
                        mnemonic='ksental',
                        attributes=[
                            AttributeScheme(
                                name='fileopt',
                                type='types.String',
                                description='Format of sensity profiles output file',
                                restriction='fileopt in {"mctal",}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmat',
                        mnemonic='fmat',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Yes/No FMAT',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmatskpt',
                        mnemonic='fmatskpt',
                        attributes=[
                            AttributeScheme(
                                name='fmat_skip',
                                type='types.Real',
                                description='fmat_skip',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmatncyc',
                        mnemonic='fmatncyc',
                        attributes=[
                            AttributeScheme(
                                name='fmat_ncyc',
                                type='types.Real',
                                description='fmat_ncyc',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmatspace',
                        mnemonic='fmatspace',
                        attributes=[
                            AttributeScheme(
                                name='fmat_space',
                                type='types.Real',
                                description='fmat_space',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmataccel',
                        mnemonic='fmataccel',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='fmataccel',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmatreduce',
                        mnemonic='fmatreduce',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='fmatreduce',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmatnx',
                        mnemonic='fmatnx',
                        attributes=[
                            AttributeScheme(
                                name='fmat_nx',
                                type='types.Real',
                                description='fmat_nx',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmatny',
                        mnemonic='fmatny',
                        attributes=[
                            AttributeScheme(
                                name='fmat_ny',
                                type='types.Real',
                                description='fmat_ny',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fmatnz',
                        mnemonic='fmatnz',
                        attributes=[
                            AttributeScheme(
                                name='fmat_nz',
                                type='types.Real',
                                description='fmat_nz',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='hsrc',
                mnemonic='hsrc',
                attributes=[
                    AttributeScheme(
                        name='x_number',
                        type='types.Integer',
                        description='Number of mesh intervals in x direction',
                        restriction='x_number > 0',
                    ),
                    AttributeScheme(
                        name='x_minimum',
                        type='types.Real',
                        description='Minimum x-value for mesh',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x_maximum',
                        type='types.Real',
                        description='Maximum x-value for mesh',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y_number',
                        type='types.Integer',
                        description='Number of mesh intervals in y direction',
                        restriction='y_number > 0',
                    ),
                    AttributeScheme(
                        name='y_minimum',
                        type='types.Real',
                        description='Minimum y-value for mesh',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='y_maximum',
                        type='types.Real',
                        description='Maximum y-value for mesh',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z_number',
                        type='types.Integer',
                        description='Number of mesh intervals in z direction',
                        restriction='z_number > 0',
                    ),
                    AttributeScheme(
                        name='z_minimum',
                        type='types.Real',
                        description='Minimum z-value for mesh',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='z_maximum',
                        type='types.Real',
                        description='Maximum z-value for mesh',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='fc',
                mnemonic='fc',
                attributes=[
                    AttributeScheme(
                        name='info',
                        type='types.String',
                        description='Title for tally in output and MCTAL file',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            # FORM
            #    OptionScheme(
            #        name='e',
            #        attributes=[
            #            AttributeScheme(
            #                name='bounds',
            #                type='tuple[types.Real]',
            #                description='Upper energy bounds for bin',
            #            ),
            #            AttributeScheme(
            #                name='nt',
            #                type='types.String',
            #                description='Notation to inhibit automatic totaling',
            #                optional=True,
            #            ),
            #            AttributeScheme(
            #                name='c',
            #                type='types.String',
            #                description='Notation to make bin values cumulative',
            #                optional=True,
            #            ),
            #            AttributeScheme(
            #                name='suffix',
            #                type='types.Integer',
            #                description='Data card option suffix',
            #            ),
            #        ],
            #    ),
            #    OptionScheme(
            #        name='t',
            #        attributes=[
            #            AttributeScheme(
            #                name='bounds',
            #                type='tuple[types.Real]',
            #                description='Upper time bounds for bin',
            #            ),
            #            AttributeScheme(
            #                name='nt',
            #                type='types.String',
            #                description='Notation to inhibit automatic totaling',
            #                optional=True,
            #            ),
            #            AttributeScheme(
            #                name='c',
            #                type='types.String',
            #                description='Notation to make bin values cumulative',
            #                optional=True,
            #            ),
            #            AttributeScheme(
            #                name='suffix',
            #                type='types.Integer',
            #                description='Data card option suffix',
            #            ),
            #        ],
            #    ),
            #    OptionScheme(
            #        name='c',
            #        attributes=[
            #            AttributeScheme(
            #                name='bounds',
            #                type='tuple[types.Real]',
            #                description='Upper cosine bounds for bin',
            #            ),
            #            AttributeScheme(
            #                name='t',
            #                type='types.String',
            #                description='Notation to provide totals',
            #                optional=True,
            #            ),
            #            AttributeScheme(
            #                name='c',
            #                type='types.String',
            #                description='Notation to make bin values cumulative',
            #                optional=True,
            #            ),
            #            AttributeScheme(
            #                name='suffix',
            #                type='types.Integer',
            #                description='Data card option suffix',
            #            ),
            #        ],
            #    ),
            OptionScheme(
                name='fq',
                mnemonic='fq',
                attributes=[
                    AttributeScheme(
                        name='a1',
                        type='types.String',
                        description='Letters representing tally bin types',
                        restriction='a1 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                    ),
                    AttributeScheme(
                        name='a2',
                        type='types.String',
                        description='Letters representing tally bin types',
                        restriction='a2 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                    ),
                    AttributeScheme(
                        name='a3',
                        type='types.String',
                        description='Letters representing tally bin types',
                        restriction='a3 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                    ),
                    AttributeScheme(
                        name='a4',
                        type='types.String',
                        description='Letters representing tally bin types',
                        restriction='a4 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                    ),
                    AttributeScheme(
                        name='a5',
                        type='types.String',
                        description='Letters representing tally bin types',
                        restriction='a5 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                    ),
                    AttributeScheme(
                        name='a6',
                        type='types.String',
                        description='Letters representing tally bin types',
                        restriction='a6 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                    ),
                    AttributeScheme(
                        name='a7',
                        type='types.String',
                        description='Letters representing tally bin types',
                        restriction='a7 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                    ),
                    AttributeScheme(
                        name='a8',
                        type='types.String',
                        description='Letters representing tally bin types',
                        restriction='a8 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='de',
                mnemonic='de',
                attributes=[
                    AttributeScheme(
                        name='method',
                        type='types.String',
                        description='Interpolation method for energy table',
                        restriction='method in {"log", "lin"}',
                    ),
                    AttributeScheme(
                        name='values',
                        type='tuple[types.Real]',
                        description='Energy values',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='df',
                mnemonic='df',
                attributes=[
                    AttributeScheme(
                        name='method',
                        type='types.String',
                        description='Interpolation method for dose function table',
                        restriction='method in {"log", "lin"}',
                    ),
                    AttributeScheme(
                        name='values',
                        type='tuple[types.Real]',
                        description='Dose function values',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='em',
                mnemonic='em',
                attributes=[
                    AttributeScheme(
                        name='multipliers',
                        type='tuple[types.Real]',
                        description='Energy bin multiplier to apply',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='tm',
                mnemonic='tm',
                attributes=[
                    AttributeScheme(
                        name='multipliers',
                        type='tuple[types.Real]',
                        description='Time bin multiplier to apply',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='cm',
                mnemonic='cm',
                attributes=[
                    AttributeScheme(
                        name='multipliers',
                        type='tuple[types.Real]',
                        description='Cosine bin multiplier to apply',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='cf',
                mnemonic='cf',
                attributes=[
                    AttributeScheme(
                        name='numbers',
                        type='tuple[types.Integer]',
                        description='Tallies for problem cell numbers to flag',
                        restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='sf',
                mnemonic='sf',
                attributes=[
                    AttributeScheme(
                        name='numbers',
                        type='tuple[types.Integer]',
                        description='Tallies for problem surface numbers to flag',
                        restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='fs',
                mnemonic='fs',
                attributes=[
                    AttributeScheme(
                        name='numbers',
                        type='tuple[types.Integer]',
                        description='Signed problem number of a segmenting surface.',
                        restriction='filter(lambda entry: not (-99_999_999 <= numbers <= 99_999_999), numbers)',
                    ),
                    AttributeScheme(
                        name='t',
                        type='types.String',
                        description='Notation to provide totals',
                        restriction='t in {"t"}',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='c',
                        type='types.String',
                        description='Notation to make bin values cumulative',
                        restriction='c in {"c"}',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='sd',
                mnemonic='sd',
                attributes=[
                    AttributeScheme(
                        name='information',
                        type='tuple[types.Real]',
                        description='Area, volume, or mass by segmented, surface/cell',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='information',
                        attributes=[
                            AttributeScheme(
                                name='values',
                                type='tuple[types.Real]',
                                description='Area, volume, or mass by surface/cell',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='fu',
                mnemonic='fu',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Input parameters for user bins',
                        restriction='filter(lambda entry: not (entry > -1), bounds)',
                    ),
                    AttributeScheme(
                        name='nt',
                        type='types.String',
                        description='Notation to inhibit automatic totaling',
                        restriction='nt in {"nt"}',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='c',
                        type='types.String',
                        description='Notation to make bin values cumulative',
                        restriction='c in {"c"}',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                ],
            ),
            OptionScheme(
                name='notrn',
                mnemonic='notrn',
                attributes=[],
            ),
            OptionScheme(
                name='pert',
                mnemonic='pert',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[pert_.PertOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
                options=[
                    OptionScheme(
                        name='cell',
                        mnemonic='cell',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of cells',
                                restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='mat',
                        mnemonic='mat',
                        attributes=[
                            AttributeScheme(
                                name='material',
                                type='types.Integer',
                                description='Material number to fill cells',
                                restriction='0 <= material <= 99_999_999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='rho',
                        mnemonic='rho',
                        attributes=[
                            AttributeScheme(
                                name='density',
                                type='types.Real',
                                description='Perturbed density',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='method',
                        mnemonic='method',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Integer',
                                description='Printing and specifies setting',
                                restriction='setting in {+1, -1, +2, -2, +3, -3}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='erg',
                        mnemonic='erg',
                        attributes=[
                            AttributeScheme(
                                name='energy_lower_bound',
                                type='types.Real',
                                description='Lower bound for energy pertubation',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='energy_upper_bound',
                                type='types.Real',
                                description='Upper bound for energy pertubation',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='rxn',
                        mnemonic='rxn',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='ENDF/B reaction number',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='kpert',
                mnemonic='kpert',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[kpert_.KpertOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='0 < suffix <= 10_000',
                    ),
                ],
                options=[
                    OptionScheme(
                        name='cell',
                        mnemonic='cell',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of cells',
                                restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='mat',
                        mnemonic='mat',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of materials',
                                restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='rho',
                        mnemonic='rho',
                        attributes=[
                            AttributeScheme(
                                name='densities',
                                type='tuple[types.Zaid]',
                                description='List of densities',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='iso',
                        mnemonic='iso',
                        attributes=[
                            AttributeScheme(
                                name='zaids',
                                type='tuple[types.Real]',
                                description='List of ZAIDs for pertubation',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='rxn',
                        mnemonic='rxn',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of reaction numbers for pertubation',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='erg',
                        mnemonic='erg',
                        attributes=[
                            AttributeScheme(
                                name='energies',
                                type='tuple[types.Real]',
                                description='List of energies',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='linear',
                        mnemonic='linear',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Pertubated fission source on/off',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='ksen',
                mnemonic='ksen',
                attributes=[
                    AttributeScheme(
                        name='sen',
                        type='types.String',
                        description='Type of sensitivity',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='options',
                        type='tuple[ksen_.KsenOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='0 < suffix <= 999',
                    ),
                ],
                options=[
                    OptionScheme(
                        name='iso',
                        mnemonic='iso',
                        attributes=[
                            AttributeScheme(
                                name='zaids',
                                type='tuple[types.Real]',
                                description='List of ZAIDs for pertubation',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='rxn',
                        mnemonic='rxn',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of reaction numbers for pertubation',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='mt',
                        mnemonic='mt',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of reaction numbers for pertubation',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='erg',
                        mnemonic='erg',
                        attributes=[
                            AttributeScheme(
                                name='energies',
                                type='tuple[types.Real]',
                                description='List of energies',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ein',
                        mnemonic='ein',
                        attributes=[
                            AttributeScheme(
                                name='energies',
                                type='tuple[types.Real]',
                                description='List of ranges for incident energies',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='legendre',
                        mnemonic='legendre',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Order of Legendre moments to calculate sensitivities',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='cos',
                        mnemonic='cos',
                        attributes=[
                            AttributeScheme(
                                name='cosines',
                                type='tuple[types.Real]',
                                description='Range of direction-change cosines',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='constrain',
                        mnemonic='constrain',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Renormalize sensitivity distribution on/off',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='fmesh',
                mnemonic='fmesh',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[fmesh_.FmeshOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='0 < suffix <= 999',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
                options=[
                    OptionScheme(
                        name='geom',
                        mnemonic='geom',
                        attributes=[
                            AttributeScheme(
                                name='geometry',
                                type='types.String',
                                description='Mesh geometry',
                                restriction='geometry in {"xyz", "rec", "rzt", "cyl"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='origin',
                        mnemonic='origin',
                        attributes=[
                            AttributeScheme(
                                name='x',
                                type='types.Real',
                                description='Origin x coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='y',
                                type='types.Real',
                                description='Origin y coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='z',
                                type='types.Real',
                                description='Origin z coordinate',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='axs',
                        mnemonic='axs',
                        attributes=[
                            AttributeScheme(
                                name='x',
                                type='types.Real',
                                description='Cylindrical mesh axis vector x component',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='y',
                                type='types.Real',
                                description='Cylindrical mesh axis vector y component',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='z',
                                type='types.Real',
                                description='Cylindrical mesh axis vector z component',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='vec',
                        mnemonic='vec',
                        attributes=[
                            AttributeScheme(
                                name='x',
                                type='types.Real',
                                description='Plane vector x component',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='y',
                                type='types.Real',
                                description='Plane vector y component',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='z',
                                type='types.Real',
                                description='Plane vector z component',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='imesh',
                        mnemonic='imesh',
                        attributes=[
                            AttributeScheme(
                                name='locations',
                                type='types.Real',
                                description='Locations of mesh points x/r for rectangular/cylindrical geometry',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='iints',
                        mnemonic='iints',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='Number of mesh points x/r for rectangular/cylindrical geometry',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='jmesh',
                        mnemonic='jmesh',
                        attributes=[
                            AttributeScheme(
                                name='locations',
                                type='types.Real',
                                description='Locations of mesh points y/z for rectangular/cylindrical geometry',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='jints',
                        mnemonic='jints',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='Number of mesh points y/z for rectangular/cylindrical geometry',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='kmesh',
                        mnemonic='kmesh',
                        attributes=[
                            AttributeScheme(
                                name='locations',
                                type='types.Real',
                                description='Locations of mesh points z/theta for rectangular/cylindrical geometry',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='kints',
                        mnemonic='kints',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='Number of mesh points z/theta for rectangular/cylindrical geometry',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='emesh',
                        mnemonic='emesh',
                        attributes=[
                            AttributeScheme(
                                name='energy',
                                type='types.Real',
                                description='Values of mesh points in energy',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='eints',
                        mnemonic='eints',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='Number of mesh points for each mesh energy',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='enorm',
                        mnemonic='enorm',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Tally results divided by energy yes/no',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='tmesh',
                        mnemonic='tmesh',
                        attributes=[
                            AttributeScheme(
                                name='time',
                                type='types.Real',
                                description='Values of mesh points in time',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='tints',
                        mnemonic='tints',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='Number of mesh points for each mesh time',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='tnorm',
                        mnemonic='tnorm',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Tally results divided by time yes/no',
                                restriction='setting in {"yes", "no"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='factor',
                        mnemonic='factor',
                        attributes=[
                            AttributeScheme(
                                name='multiple',
                                type='types.Real',
                                description='Multiplicative factor for each mesh',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='out',
                        mnemonic='out',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Output format',
                                restriction='setting in {"col", "cf", "ij", "ik", "jk", "none"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='tr',
                        mnemonic='tr',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Transformation applied to the mesh',
                                restriction='1 <= number <= 999',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='inc',
                        mnemonic='inc',
                        attributes=[
                            AttributeScheme(
                                name='lower',
                                type='types.Real',
                                description='Collision for FMESH tally lower bound',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='upper',
                                type='types.Real',
                                description='Collision for FMESH tally upper bound',
                                restriction='',
                                optional=True,
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='type',
                        mnemonic='type',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Tally quantity',
                                restriction='setting in {"flux", "source"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='kclear',
                        mnemonic='kclear',
                        attributes=[
                            AttributeScheme(
                                name='count',
                                type='types.Integer',
                                description='KCODE cycles between zeros',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            # SUBOPTION
            #    OptionScheme(
            #        name='dose',
            #        attributes=[
            #            AttributeScheme(
            #                name='ic',
            #                type='types.Integer',
            #                description='Conversion coefficent',
            #            ),
            #            AttributeScheme(
            #                name='int',
            #                type='types.Integer',
            #                description='Interpolation method',
            #            ),
            #            AttributeScheme(
            #                name='iu',
            #                type='types.Integer',
            #                description='Units of resuts',
            #            ),
            #            AttributeScheme(
            #                name='fac',
            #                type='types.Real',
            #                description='Normalization of factor for dose',
            #            ),
            #        ],
            #    ),
            OptionScheme(
                name='spdtl',
                mnemonic='spdtl',
                attributes=[
                    AttributeScheme(
                        name='keyword',
                        type='types.String',
                        description='keyword in {"force", "off"}',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='imp',
                mnemonic='imp',
                attributes=[
                    AttributeScheme(
                        name='importances',
                        type='tuple[types.Real]',
                        description='Cell importance',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='var',
                mnemonic='var',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[var_.VarOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='rr',
                        mnemonic='rr',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Roulette game for weight windows and cell/energy/time importance off/no',
                                restriction='setting in {"no", "off"}',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='wwe',
                mnemonic='wwe',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Upper energy/time bound',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='wwt',
                mnemonic='wwt',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Upper time bound',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='wwn',
                mnemonic='wwn',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Lower weight bound',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='wwp',
                mnemonic='wwp',
                attributes=[
                    AttributeScheme(
                        name='wupn',
                        type='types.Real',
                        description='Multiplier to define the weight window upper limit',
                        restriction='wupn >= 2',
                    ),
                    AttributeScheme(
                        name='wsurvn',
                        type='types.Real',
                        description='Multiplier to define the maximum Russian roulette survival weight within the window',
                        restriction='1 < wsurvn',
                    ),
                    AttributeScheme(
                        name='mxspln',
                        type='types.Real',
                        description='Maximum number of integer splits',
                        restriction='1 < mxspln',
                    ),
                    AttributeScheme(
                        name='mwhere',
                        type='types.Integer',
                        description='Controls where to check a particle’s weight',
                        restriction='mwhere.value in {-1, 0, 1}',
                    ),
                    AttributeScheme(
                        name='switchn',
                        type='types.Real',
                        description='Controls where to get the lower weight-window bounds',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='mtime',
                        type='types.Integer',
                        description='Energy/time-dependent window setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='wnrom',
                        type='types.Real',
                        description='Weight-window normalization factor',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='etsplt',
                        type='types.Integer',
                        description='ESLPT & TSPLT split/roulette on/off',
                        restriction='etsplt.value in {0, 1}',
                    ),
                    AttributeScheme(
                        name='wu',
                        type='types.Real',
                        description='Limits the maximum lower weight-window bound for any particle, energy, or time',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='nmfp',
                        type='types.Real',
                        description='Limits the maximum lower weight-window bound for any particle, energy, or time',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='wwg',
                mnemonic='wwg',
                attributes=[
                    AttributeScheme(
                        name='tally',
                        type='types.Integer',
                        description='Problem tally number',
                        restriction='tally <= 99_999_999',
                    ),
                    AttributeScheme(
                        name='cell',
                        type='types.Integer',
                        description='Cell-based or mesh-based weight window generator',
                        restriction='cell <= 99_999_999',
                    ),
                    AttributeScheme(
                        name='lower',
                        type='types.Real',
                        description='Value of the generated lower weight-window bound for cell',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='j1',
                        type='types.Jump',
                        description='Placeholder jump #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='j2',
                        type='types.Jump',
                        description='Placeholder jump #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='j3',
                        type='types.Jump',
                        description='Placeholder jump #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='j4',
                        type='types.Jump',
                        description='Placeholder jump #4',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='setting',
                        type='types.Integer',
                        description='Energy- or time-dependent weight window toggle',
                        restriction='setting.value in {0, 1}',
                    ),
                ],
            ),
            OptionScheme(
                name='wwge',
                mnemonic='wwge',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Upper energy bound for weight-window group to be generated',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='wwgt',
                mnemonic='wwgt',
                attributes=[
                    AttributeScheme(
                        name='bounds',
                        type='tuple[types.Real]',
                        description='Upper time bound for weight-window group to be generated',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='mesh',
                mnemonic='mesh',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[mesh_.MeshOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='geom',
                        mnemonic='geom',
                        attributes=[
                            AttributeScheme(
                                name='geometry',
                                type='types.String',
                                description='Controls mesh geometry type',
                                restriction='geometry in {"xyz", "rzt", "rpt"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ref',
                        mnemonic='ref',
                        attributes=[
                            AttributeScheme(
                                name='point',
                                type='tuple[types.Real]',
                                description='Mesh reference point',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='origin',
                        mnemonic='origin',
                        attributes=[
                            AttributeScheme(
                                name='point',
                                type='tuple[types.Real]',
                                description='Mesh origin point',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='axs',
                        mnemonic='axs',
                        attributes=[
                            AttributeScheme(
                                name='vector',
                                type='tuple[types.Real]',
                                description='Vector giving the direction of the polar axis',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='vec',
                        mnemonic='vec',
                        attributes=[
                            AttributeScheme(
                                name='vector',
                                type='tuple[types.Real]',
                                description='Vector giving the direction of the polar axis',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='imesh',
                        mnemonic='imesh',
                        attributes=[
                            AttributeScheme(
                                name='vector',
                                type='tuple[types.Real]',
                                description='Locations of the coarse meshes in the x/r directions',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='iints',
                        mnemonic='iints',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Number of fine meshes within corresponding coarse meshes in the x/r directions',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='jmesh',
                        mnemonic='jmesh',
                        attributes=[
                            AttributeScheme(
                                name='vector',
                                type='tuple[types.Real]',
                                description='Locations of the coarse meshes in the y/z directions',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='jints',
                        mnemonic='jints',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Number of fine meshes within corresponding coarse meshes in the y/z directions',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='kmesh',
                        mnemonic='kmesh',
                        attributes=[
                            AttributeScheme(
                                name='vector',
                                type='tuple[types.Real]',
                                description='Locations of the coarse meshes in the z/theta directions',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='kints',
                        mnemonic='kints',
                        attributes=[
                            AttributeScheme(
                                name='number',
                                type='types.Integer',
                                description='Number of fine meshes within corresponding coarse meshes in the z/theta directions',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='esplt',
                mnemonic='esplt',
                attributes=[
                    AttributeScheme(
                        name='ratio_1',
                        type='types.Real',
                        description='Splitting/roulette ratio #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_1',
                        type='types.Real',
                        description='Splitting/roulette energy #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_2',
                        type='types.Real',
                        description='Splitting/roulette ratio #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_2',
                        type='types.Real',
                        description='Splitting/roulette energy #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_3',
                        type='types.Real',
                        description='Splitting/roulette ratio #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_3',
                        type='types.Real',
                        description='Splitting/roulette energy #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_4',
                        type='types.Real',
                        description='Splitting/roulette ratio #4',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_4',
                        type='types.Real',
                        description='Splitting/roulette energy #4',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_5',
                        type='types.Real',
                        description='Splitting/roulette ratio #5',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_5',
                        type='types.Real',
                        description='Splitting/roulette energy #5',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_6',
                        type='types.Real',
                        description='Splitting/roulette ratio #6',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_6',
                        type='types.Real',
                        description='Splitting/roulette energy #6',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_7',
                        type='types.Real',
                        description='Splitting/roulette ratio #7',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_7',
                        type='types.Real',
                        description='Splitting/roulette energy #7',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_8',
                        type='types.Real',
                        description='Splitting/roulette ratio #8',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_8',
                        type='types.Real',
                        description='Splitting/roulette energy #8',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_9',
                        type='types.Real',
                        description='Splitting/roulette ratio #9',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_9',
                        type='types.Real',
                        description='Splitting/roulette energy #9',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_10',
                        type='types.Real',
                        description='Splitting/roulette ratio #10',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_10',
                        type='types.Real',
                        description='Splitting/roulette energy #10',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_11',
                        type='types.Real',
                        description='Splitting/roulette ratio #11',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_11',
                        type='types.Real',
                        description='Splitting/roulette energy #11',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_12',
                        type='types.Real',
                        description='Splitting/roulette ratio #12',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_12',
                        type='types.Real',
                        description='Splitting/roulette energy #12',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_13',
                        type='types.Real',
                        description='Splitting/roulette ratio #13',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_13',
                        type='types.Real',
                        description='Splitting/roulette energy #13',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_14',
                        type='types.Real',
                        description='Splitting/roulette ratio #14',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_14',
                        type='types.Real',
                        description='Splitting/roulette energy #14',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_15',
                        type='types.Real',
                        description='Splitting/roulette ratio #15',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_15',
                        type='types.Real',
                        description='Splitting/roulette energy #15',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_16',
                        type='types.Real',
                        description='Splitting/roulette ratio #16',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_16',
                        type='types.Real',
                        description='Splitting/roulette energy #16',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_17',
                        type='types.Real',
                        description='Splitting/roulette ratio #17',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_17',
                        type='types.Real',
                        description='Splitting/roulette energy #17',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_18',
                        type='types.Real',
                        description='Splitting/roulette ratio #18',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_18',
                        type='types.Real',
                        description='Splitting/roulette energy #18',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_19',
                        type='types.Real',
                        description='Splitting/roulette ratio #19',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_19',
                        type='types.Real',
                        description='Splitting/roulette energy #19',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_20',
                        type='types.Real',
                        description='Splitting/roulette ratio #20',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='energy_20',
                        type='types.Real',
                        description='Splitting/roulette energy #20',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='tsplt',
                mnemonic='tsplt',
                attributes=[
                    AttributeScheme(
                        name='ratio_1',
                        type='types.Real',
                        description='Splitting/roulette ratio #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_1',
                        type='types.Real',
                        description='Splitting/roulette time #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_2',
                        type='types.Real',
                        description='Splitting/roulette ratio #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_2',
                        type='types.Real',
                        description='Splitting/roulette time #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_3',
                        type='types.Real',
                        description='Splitting/roulette ratio #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_3',
                        type='types.Real',
                        description='Splitting/roulette time #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_4',
                        type='types.Real',
                        description='Splitting/roulette ratio #4',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_4',
                        type='types.Real',
                        description='Splitting/roulette time #4',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_5',
                        type='types.Real',
                        description='Splitting/roulette ratio #5',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_5',
                        type='types.Real',
                        description='Splitting/roulette time #5',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_6',
                        type='types.Real',
                        description='Splitting/roulette ratio #6',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_6',
                        type='types.Real',
                        description='Splitting/roulette time #6',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_7',
                        type='types.Real',
                        description='Splitting/roulette ratio #7',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_7',
                        type='types.Real',
                        description='Splitting/roulette time #7',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_8',
                        type='types.Real',
                        description='Splitting/roulette ratio #8',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_8',
                        type='types.Real',
                        description='Splitting/roulette time #8',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_9',
                        type='types.Real',
                        description='Splitting/roulette ratio #9',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_9',
                        type='types.Real',
                        description='Splitting/roulette time #9',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_10',
                        type='types.Real',
                        description='Splitting/roulette ratio #10',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_10',
                        type='types.Real',
                        description='Splitting/roulette time #10',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_11',
                        type='types.Real',
                        description='Splitting/roulette ratio #11',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_11',
                        type='types.Real',
                        description='Splitting/roulette time #11',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_12',
                        type='types.Real',
                        description='Splitting/roulette ratio #12',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_12',
                        type='types.Real',
                        description='Splitting/roulette time #12',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_13',
                        type='types.Real',
                        description='Splitting/roulette ratio #13',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_13',
                        type='types.Real',
                        description='Splitting/roulette time #13',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_14',
                        type='types.Real',
                        description='Splitting/roulette ratio #14',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_14',
                        type='types.Real',
                        description='Splitting/roulette time #14',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_15',
                        type='types.Real',
                        description='Splitting/roulette ratio #15',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_15',
                        type='types.Real',
                        description='Splitting/roulette time #15',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_16',
                        type='types.Real',
                        description='Splitting/roulette ratio #16',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_16',
                        type='types.Real',
                        description='Splitting/roulette time #16',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_17',
                        type='types.Real',
                        description='Splitting/roulette ratio #17',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_17',
                        type='types.Real',
                        description='Splitting/roulette time #17',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_18',
                        type='types.Real',
                        description='Splitting/roulette ratio #18',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_18',
                        type='types.Real',
                        description='Splitting/roulette time #18',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_19',
                        type='types.Real',
                        description='Splitting/roulette ratio #19',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_19',
                        type='types.Real',
                        description='Splitting/roulette time #19',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ratio_20',
                        type='types.Real',
                        description='Splitting/roulette ratio #20',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='time_20',
                        type='types.Real',
                        description='Splitting/roulette time #20',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='ext',
                mnemonic='ext',
                attributes=[
                    AttributeScheme(
                        name='stretching',
                        type='tuple[types.Real]',
                        description='Stretching direction for the cell',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            # REGEX
            #    OptionScheme(
            #        name='vect',
            #        attributes=[
            #            AttributeScheme(
            #                name='vectors',
            #                type='tuple[vect_.VectEntry_Vector]',
            #                description='Vectrors for EXT',
            #            ),
            #        ],
            #        entries=[
            #            EntryScheme(
            #                name='vector',
            #                attributes=[
            #                    AttributeScheme(
            #                        name='ident',
            #                        type='types.Integer',
            #                        description='Vector identifier',
            #                    ),
            #                    AttributeScheme(
            #                        name='x',
            #                        type='types.Real',
            #                        description='Vector x coordinate',
            #                    ),
            #                    AttributeScheme(
            #                        name='y',
            #                        type='types.Real',
            #                        description='Vector y coordinate',
            #                    ),
            #                    AttributeScheme(
            #                        name='z',
            #                        type='types.Real',
            #                        description='Vector z coordinate',
            #                    ),
            #                ],
            #            )
            #        ],
            #    ),
            OptionScheme(
                name='fcl',
                mnemonic='fcl',
                attributes=[
                    AttributeScheme(
                        name='control',
                        type='tuple[types.Real]',
                        description='Forced-collision control for cell',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='dxt',
                mnemonic='dxt',
                attributes=[
                    AttributeScheme(
                        name='spheres_1',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #1',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_2',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #2',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_3',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #3',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_4',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #4',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_5',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #5',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_6',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #6',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_7',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #7',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_8',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #8',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_9',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #9',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='spheres_10',
                        type='dxt_.DxtEntry_Sphere',
                        description='DXTRAN spheres #10',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='cutoff_1',
                        type='types.Real',
                        description='Upper weight cutoff in the spheres',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='cutoff_2',
                        type='types.Real',
                        description='Lower weight cutoff in the spheres',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='weight',
                        type='types.Real',
                        description='Minimum photon weight',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='sphere',
                        attributes=[
                            AttributeScheme(
                                name='x',
                                type='types.Real',
                                description='Vector x coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='y',
                                type='types.Real',
                                description='Vector y coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='z',
                                type='types.Real',
                                description='Vector z coordinate',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='inner_radius',
                                type='types.Integer',
                                description='Inner sphere radius',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='outer_radius',
                                type='types.Integer',
                                description='Outer sphere radius',
                                restriction='',
                            ),
                        ],
                    )
                ],
            ),
            OptionScheme(
                name='dd',
                mnemonic='dd',
                attributes=[
                    AttributeScheme(
                        name='diagnostics',
                        type='tuple[dd_.DdEntry_Diagnostic]',
                        description='Detector diagnostic entries',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='diagnostic',
                        attributes=[
                            AttributeScheme(
                                name='playing_setting',
                                type='types.Real',
                                description='Criterion for playing Russian roulette for DXTRAN',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='printing_setting',
                                type='types.Real',
                                description='Criterion for printing diagnostics for large contributions for DXTRAN',
                                restriction='',
                            ),
                        ],
                    )
                ],
            ),
            OptionScheme(
                name='pd',
                mnemonic='pd',
                attributes=[
                    AttributeScheme(
                        name='probabilities',
                        type='tuple[types.Real]',
                        description='Probability of contribution to DXTRAN',
                        restriction='filter(lambda entry: not (0 <= entry <= 1), probabilities)',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='dxc',
                mnemonic='dxc',
                attributes=[
                    AttributeScheme(
                        name='probabilities',
                        type='tuple[types.Real]',
                        description='Probability of contribution to DXTRAN',
                        restriction='filter(lambda entry: not (0 <= entry <= 1), probabilities)',
                    ),
                    AttributeScheme(
                        name='suffix',
                        type='types.Integer',
                        description='Data card option suffix',
                        restriction='suffix <= 99_999_999',
                    ),
                    AttributeScheme(
                        name='designator',
                        type='types.Designator',
                        description='Data card particle designator',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='bbrem',
                mnemonic='bbrem',
                attributes=[
                    AttributeScheme(
                        name='bias_1',
                        type='types.Real',
                        description='Bias factor #1 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_2',
                        type='types.Real',
                        description='Bias factor #2 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_3',
                        type='types.Real',
                        description='Bias factor #3 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_4',
                        type='types.Real',
                        description='Bias factor #4 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_5',
                        type='types.Real',
                        description='Bias factor #5 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_6',
                        type='types.Real',
                        description='Bias factor #6 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_7',
                        type='types.Real',
                        description='Bias factor #7 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_8',
                        type='types.Real',
                        description='Bias factor #8 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_9',
                        type='types.Real',
                        description='Bias factor #9 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_10',
                        type='types.Real',
                        description='Bias factor #10 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_11',
                        type='types.Real',
                        description='Bias factor #11 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_12',
                        type='types.Real',
                        description='Bias factor #12 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_13',
                        type='types.Real',
                        description='Bias factor #13 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_14',
                        type='types.Real',
                        description='Bias factor #14 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_15',
                        type='types.Real',
                        description='Bias factor #15 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_16',
                        type='types.Real',
                        description='Bias factor #16 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_17',
                        type='types.Real',
                        description='Bias factor #17 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_18',
                        type='types.Real',
                        description='Bias factor #18 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_19',
                        type='types.Real',
                        description='Bias factor #19 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_20',
                        type='types.Real',
                        description='Bias factor #20 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_21',
                        type='types.Real',
                        description='Bias factor #21 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_22',
                        type='types.Real',
                        description='Bias factor #22 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_23',
                        type='types.Real',
                        description='Bias factor #23 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_24',
                        type='types.Real',
                        description='Bias factor #24 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_25',
                        type='types.Real',
                        description='Bias factor #25 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_26',
                        type='types.Real',
                        description='Bias factor #26 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_27',
                        type='types.Real',
                        description='Bias factor #27 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_28',
                        type='types.Real',
                        description='Bias factor #28 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_29',
                        type='types.Real',
                        description='Bias factor #29 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_30',
                        type='types.Real',
                        description='Bias factor #30 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_31',
                        type='types.Real',
                        description='Bias factor #31 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_32',
                        type='types.Real',
                        description='Bias factor #32 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_33',
                        type='types.Real',
                        description='Bias factor #33 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_34',
                        type='types.Real',
                        description='Bias factor #34 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_35',
                        type='types.Real',
                        description='Bias factor #35 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_36',
                        type='types.Real',
                        description='Bias factor #36 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_37',
                        type='types.Real',
                        description='Bias factor #37 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_38',
                        type='types.Real',
                        description='Bias factor #38 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_39',
                        type='types.Real',
                        description='Bias factor #39 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_40',
                        type='types.Real',
                        description='Bias factor #40 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_41',
                        type='types.Real',
                        description='Bias factor #41 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_42',
                        type='types.Real',
                        description='Bias factor #42 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_43',
                        type='types.Real',
                        description='Bias factor #43 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_44',
                        type='types.Real',
                        description='Bias factor #44 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_45',
                        type='types.Real',
                        description='Bias factor #45 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_46',
                        type='types.Real',
                        description='Bias factor #46 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_47',
                        type='types.Real',
                        description='Bias factor #47 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_48',
                        type='types.Real',
                        description='Bias factor #48 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='bias_49',
                        type='types.Real',
                        description='Bias factor #49 for bremsstrahlung specturm',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='materials',
                        type='tuple[types.Integer]',
                        description='Material to bias',
                        restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), materials)',
                    ),
                ],
            ),
            OptionScheme(
                name='pikmt',
                mnemonic='pikmt',
                attributes=[
                    AttributeScheme(
                        name='biases',
                        type='tuple[pikmt_.PikmtEntry_Bias]',
                        description='Biases for proton production',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='bias',
                        attributes=[
                            AttributeScheme(
                                name='zaid',
                                type='types.Zaid',
                                description='Bias nuclide identifier',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='ipiki',
                                type='types.Integer',
                                description='Bias controls',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='reactions',
                                type='tuple[bias_.BiasEntry_Reaction]',
                                description='Bias MT reactions',
                                restriction='',
                            ),
                        ],
                        entries=[
                            EntryScheme(
                                name='reaction',
                                attributes=[
                                    AttributeScheme(
                                        name='mt',
                                        type='types.Zaid',
                                        description='MT reaction identifiers',
                                        restriction='',
                                    ),
                                    AttributeScheme(
                                        name='pmt',
                                        type='types.Integer',
                                        description='MT reaction frequency control',
                                        restriction='',
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='pwt',
                mnemonic='pwt',
                attributes=[
                    AttributeScheme(
                        name='weights',
                        type='tuple[types.Real]',
                        description='Relative threshold weight of photons produced at neutron collisions in cell',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='nps',
                mnemonic='nps',
                attributes=[
                    AttributeScheme(
                        name='npp',
                        type='types.Integer',
                        description='Total number of histories to run',
                        restriction='npp > 0',
                    ),
                    AttributeScheme(
                        name='npsmg',
                        type='types.Integer',
                        description='Number of history with direct source contributions',
                        restriction='npsmg > 0',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='ctme',
                mnemonic='ctme',
                attributes=[
                    AttributeScheme(
                        name='tme',
                        type='types.Integer',
                        description='maximum amount of minutes for Monte Carlo calculation',
                        restriction='tme >= 0',
                    ),
                ],
            ),
            OptionScheme(
                name='stop',
                mnemonic='stop',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[stop_.StopOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='nps',
                        mnemonic='nps',
                        attributes=[
                            AttributeScheme(
                                name='npp',
                                type='types.Integer',
                                description='Total number of histories before stop',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='npsmg',
                                type='types.Integer',
                                description='Number of histories before stop',
                                restriction='',
                                optional=True,
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='ctme',
                        mnemonic='ctme',
                        attributes=[
                            AttributeScheme(
                                name='tme',
                                type='types.Real',
                                description='Computer time before stop',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='fk',
                        mnemonic='fk',
                        attributes=[
                            AttributeScheme(
                                name='e',
                                type='types.Integer',
                                description='Tally fluctuation relative error before stop',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='suffix',
                                type='types.Integer',
                                description='Data card option option suffix',
                                restriction='suffix <= 99_999_999',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='print',
                mnemonic='print',
                attributes=[
                    AttributeScheme(
                        name='tables',
                        type='tuple[types.Integer]',
                        description='Tables to print',
                        restriction='filter(lambda entry: not (entry.value in {10, 20, 30, 32, 35, 38, 40, 41, 44, 50, 55, 60, 62, 70, 72, 80, 85, 86, 87, 90, 95, 98, 100, 102, 110, 115, 117, 118, 120, 126, 128, 130, 140, 150, 160, 161, 162, 163, 170, 175, 178, 180, 190, 198, 200, 210, 220, -10, -20, -30, -32, -35, -38, -40, -41, -44, -50, -55, -60, -62, -70, -72, -80, -85, -86, -87, -90, -95, -98, -100, -102, -110, -115, -117, -118, -120, -126, -128, -130, -140, -150, -160, -161, -162, -163, -170, -175, -178, -180, -190, -198, -200, -210, -220}), tables)',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='talnp',
                mnemonic='talnp',
                attributes=[
                    AttributeScheme(
                        name='tallies',
                        type='tuple[types.Integer]',
                        description='Tallies to exclude from output',
                        restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), tallies)',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='prdmp',
                mnemonic='prdmp',
                attributes=[
                    AttributeScheme(
                        name='ndp',
                        type='types.Integer',
                        description='Increment for printing tallies',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ndm',
                        type='types.Integer',
                        description='Increment for dumping to RUNTPE file',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='mct',
                        type='types.Integer',
                        description='Controls printing of MCTAL file',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='ndmp',
                        type='types.Integer',
                        description='Maximum number of dumps on RUNTPE file',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='dmmp',
                        type='types.Integer',
                        description='Controls frequently of tally fluctuation chart',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='ptrac',
                mnemonic='ptrac',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[ptrac_.PtracOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='buffer',
                        mnemonic='buffer',
                        attributes=[
                            AttributeScheme(
                                name='storage',
                                type='types.Integer',
                                description='Amount of storage available for filtered events',
                                restriction='storage > 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='file',
                        mnemonic='file',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='PTRAC file type',
                                restriction='setting in {"asc", "bin", "aov", "bov"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='max',
                        mnemonic='max',
                        attributes=[
                            AttributeScheme(
                                name='events',
                                type='types.Integer',
                                description='Maximum number of events to write',
                                restriction='events != 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='meph',
                        mnemonic='meph',
                        attributes=[
                            AttributeScheme(
                                name='events',
                                type='types.Integer',
                                description='Maximum number of events per history to write',
                                restriction='events > 0',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='write',
                        mnemonic='write',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Controls what particle parameters are written',
                                restriction='setting in {"pos", "all"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='conic',
                        mnemonic='conic',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Activates a PTRAC file format specifically for coincidence tally scoring',
                                restriction='setting in {"col", "lin"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='event',
                        mnemonic='event',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.String',
                                description='Specifies the type of events written to the PTRAC file',
                                restriction='setting in {"src", "bnk", "sur", "col", "ter", "cap"}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='filter',
                        mnemonic='filter',
                        attributes=[
                            AttributeScheme(
                                name='variables',
                                type='tuple[filter_.FilterEntry_Variable]',
                                description='MCNP6 variables for filtering',
                                restriction='',
                            ),
                        ],
                        entries=[
                            EntryScheme(
                                name='variable',
                                attributes=[
                                    AttributeScheme(
                                        name='lower',
                                        type='types.Real',
                                        description='Lower bound for filtering',
                                        restriction='',
                                    ),
                                    AttributeScheme(
                                        name='upper',
                                        type='types.Real',
                                        description='Upper bound for filtering',
                                        restriction='upper >= lower',
                                        optional=True,
                                    ),
                                    AttributeScheme(
                                        name='variable',
                                        type='types.String',
                                        description='Variable name for PBL derived structure',
                                        restriction='variable in {""}',
                                    ),
                                ],
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='type',
                        mnemonic='type',
                        attributes=[
                            AttributeScheme(
                                name='particles',
                                type='tuple[types.Designator]',
                                description='Filters events based on one or more particle types',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='nps',
                        mnemonic='nps',
                        attributes=[
                            AttributeScheme(
                                name='particles',
                                type='tuple[types.Integer]',
                                description='Sets the range of particle histories for which events will be output',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='cell',
                        mnemonic='cell',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of cell numbers for filtering',
                                restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='surface',
                        mnemonic='surface',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of surface numbers for filtering',
                                restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='tally',
                        mnemonic='tally',
                        attributes=[
                            AttributeScheme(
                                name='numbers',
                                type='tuple[types.Integer]',
                                description='List of tally numbers for filtering',
                                restriction='filter(lambda entry: not (entry != 0), numbers)',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='value',
                        mnemonic='value',
                        attributes=[
                            AttributeScheme(
                                name='cutoff',
                                type='types.Real',
                                description='Specifies tally cutoff above which history events will be written.',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='histp',
                mnemonic='histp',
                attributes=[
                    AttributeScheme(
                        name='lhist',
                        type='types.Integer',
                        description='Number of words written to a HISTP file',
                        restriction='',
                        optional=True,
                    ),
                    AttributeScheme(
                        name='cells',
                        type='tuple[types.Integer]',
                        description='Cell numbers',
                        restriction='',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='rand',
                mnemonic='rand',
                attributes=[
                    AttributeScheme(
                        name='options',
                        type='tuple[rand_.RandOption_]',
                        description='Dictionary of options',
                        restriction='',
                        optional=True,
                    ),
                ],
                options=[
                    OptionScheme(
                        name='gen',
                        mnemonic='gen',
                        attributes=[
                            AttributeScheme(
                                name='setting',
                                type='types.Integer',
                                description='Type of pseudorandom number generator',
                                restriction='setting.value in {1, 2, 3, 4}',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='seed',
                        mnemonic='seed',
                        attributes=[
                            AttributeScheme(
                                name='seed',
                                type='types.Integer',
                                description='Random number generator seed',
                                restriction='seed.value % 2 == 1',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='stride',
                        mnemonic='stride',
                        attributes=[
                            AttributeScheme(
                                name='stride',
                                type='types.Integer',
                                description='Number of random numbers between source particle',
                                restriction='',
                            ),
                        ],
                    ),
                    OptionScheme(
                        name='hist',
                        mnemonic='hist',
                        attributes=[
                            AttributeScheme(
                                name='hist',
                                type='types.Integer',
                                description='Starting pseudorandom number',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
            OptionScheme(
                name='dbcn',
                mnemonic='dbcn',
                attributes=[
                    AttributeScheme(
                        name='x1',
                        type='types.Integer',
                        description='Obsolete; pseudorandom number for the first particle history',
                        restriction='x1 >= 0',
                    ),
                    AttributeScheme(
                        name='x2',
                        type='types.Integer',
                        description='Debug print interval',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x3',
                        type='types.Integer',
                        description='Lower history number inclusive limit for logging',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x4',
                        type='types.Integer',
                        description='Upper history number inclusive limit for logging',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x5',
                        type='types.Integer',
                        description='Maximnum number of events per history for logging',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x6',
                        type='types.Integer',
                        description='Detector/DXTRAN underflow limit',
                        restriction='50 <= x6 <= 200',
                    ),
                    AttributeScheme(
                        name='x7',
                        type='types.Integer',
                        description='Volume and sufrace area printing on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x8',
                        type='types.Integer',
                        description='Obsolete; starting history offset',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x9',
                        type='types.Integer',
                        description='Distance allowed between cpincident repeated-structures',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x10',
                        type='types.Integer',
                        description='Half-life threshold for stable nuclides',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x11',
                        type='types.Integer',
                        description='Collision event lost particle logging on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x12',
                        type='types.Integer',
                        description='Expected number of random numbers',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x13',
                        type='types.Integer',
                        description='Obsolete; random number stride',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x14',
                        type='types.Integer',
                        description='Obsolete; random number multiplier',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x15',
                        type='types.Integer',
                        description='Usual selection of statistics quantities printing on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x16',
                        type='types.Integer',
                        description='History score grid accumulation scaling',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x17',
                        type='types.Integer',
                        description='Angular treatment for secondary particles setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x18',
                        type='types.Integer',
                        description='Energy-indexing alogrithm for election transport settings',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x19',
                        type='types.Integer',
                        description='Developer; Quadratic polynomical interpolation parameter',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x20',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x21',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x22',
                        type='types.Integer',
                        description='Unsued',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x23',
                        type='types.Integer',
                        description='Pulse-height tally variance reducation tress setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x24',
                        type='types.Integer',
                        description='Grazing contribution cutoff for surface fluxx tallies settings',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x25',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x26',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x27',
                        type='types.Integer',
                        description='Antiparticle promotion settings',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x28',
                        type='types.Integer',
                        description='Bank size',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x29',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x30',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x31',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x32',
                        type='types.Integer',
                        description='GENXS behavior setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x33',
                        type='types.Integer',
                        description='Additional interpolation/smoothing method for heavy ions on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x34',
                        type='types.Integer',
                        description='Developer; Muon-induced gammas bug parameter',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x35',
                        type='types.Integer',
                        description='Slight spreading of nuclear exitation on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x36',
                        type='types.Integer',
                        description='User-provided data for muon-induced gamma rays on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x37',
                        type='types.Integer',
                        description='Mimumum of internal bremsstrahlung spectrum',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x38',
                        type='types.Integer',
                        description='Barashenkov/Polanski data file on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x39',
                        type='types.Integer',
                        description='Default S(α,β) smoothing behavior on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x40',
                        type='types.Integer',
                        description='Developer; MCPLIB and XSDIR lines writing setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x41',
                        type='types.Integer',
                        description='Developer; Phonton/election data printing setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x42',
                        type='types.Integer',
                        description='Model cross section setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x43',
                        type='types.Integer',
                        description='Developer; Photo form-factor interpolation setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x44',
                        type='types.Integer',
                        description='Developer; Coherent scattering in isolation setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x45',
                        type='types.Integer',
                        description='MCNP6/MCNPX elastic scattering method selector',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x46',
                        type='types.Integer',
                        description='CEM-to_LAQGSM photonuclear energy boundary setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x47',
                        type='types.Integer',
                        description='Cosmic-rasy spectra setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x48',
                        type='types.Integer',
                        description='MCNP6 threading on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x49',
                        type='types.Integer',
                        description='Normal input checking on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x50',
                        type='types.Integer',
                        description='TFC priting setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x51',
                        type='types.Integer',
                        description='Developer; Photon-induced fluoresence on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x52',
                        type='types.Integer',
                        description='Developer; Compton-induced relaxation on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x53',
                        type='types.Integer',
                        description='Photoelectric relazation data setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x54',
                        type='types.Integer',
                        description='Sampling method for ENDF Law 9 setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x55',
                        type='types.Integer',
                        description='Spontaneous decay integration time',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x56',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x57',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x58',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x59',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x60',
                        type='types.Integer',
                        description='Print number of calls to each high-energy model',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x61',
                        type='types.Integer',
                        description='Developer; models of knock-on electron angles',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x62',
                        type='types.Integer',
                        description='Developer; single-event electrons excitation energy loss debugger',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x63',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x64',
                        type='types.Integer',
                        description='Developer; single-event electrons angular deflaction debugger',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x65',
                        type='types.Integer',
                        description='Developer; single-event ionization and treat deflection dubgger',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x66',
                        type='types.Integer',
                        description='Developer; single-event bremsstrahlung photon angles setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x67',
                        type='types.Integer',
                        description='Particle histories setting for detectors and DXTRAN',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x68',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x69',
                        type='types.Integer',
                        description='LJA array size setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x70',
                        type='types.Integer',
                        description='Developer; interaction models setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x71',
                        type='types.Integer',
                        description='Model photonuclear capability on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x72',
                        type='types.Integer',
                        description='Log-log/linear interpolation in ELXS_MOD setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x73',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x74',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x75',
                        type='types.Integer',
                        description='Print extra info for F-matrix calculation on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x76',
                        type='types.Integer',
                        description='Print array storage info after setup on/off',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x77',
                        type='types.Integer',
                        description='Has-based cross-section serach bin number',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x78',
                        type='types.Integer',
                        description='Developer; S(A,B) method old/new setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x79',
                        type='types.Integer',
                        description='MT for absorption and fission setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x80',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x81',
                        type='types.Integer',
                        description='Developer; interpolation for electron elastic scatter setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x82',
                        type='types.Integer',
                        description='Developer; interpolation for electron elastic scatter setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x83',
                        type='types.Integer',
                        description='Developer; interpolation for electron partial x-s setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x84',
                        type='types.Integer',
                        description='Developer; interpolation for electron bremsstrahlung energy setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x85',
                        type='types.Integer',
                        description='Developer; interpolation for electron bremsstrahlung energy setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x86',
                        type='types.Integer',
                        description='Developer; interpolation for electron excitation setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x87',
                        type='types.Integer',
                        description='Developer; interpolation for electron knock-on energy setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x88',
                        type='types.Integer',
                        description='Developer; interpolation for electron knock-on energy setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x89',
                        type='types.Integer',
                        description='Developer; interpolation for electron ionization x-s setting',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x90',
                        type='types.Integer',
                        description='Mximum number of terms for Goudsmit-Saunderson distribution',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x91',
                        type='types.Integer',
                        description='Minimum ROC curve count value',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x92',
                        type='types.Integer',
                        description='Maximum ROC curve count value',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x93',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x94',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x95',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x96',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x97',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x98',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x99',
                        type='types.Integer',
                        description='Unused',
                        restriction='',
                    ),
                    AttributeScheme(
                        name='x100',
                        type='types.Integer',
                        description='Coincident-surface method old/new setting',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='lost',
                mnemonic='lost',
                attributes=[
                    AttributeScheme(
                        name='lost1',
                        type='types.Integer',
                        description='Number of particles which can be lost before job termination',
                        restriction='lost1 >= 0',
                    ),
                    AttributeScheme(
                        name='lost2',
                        type='types.Integer',
                        description='Maximum number of debug prints for lost particles.',
                        restriction='lost2 >= 0',
                    ),
                ],
            ),
            OptionScheme(
                name='idum',
                mnemonic='idum',
                attributes=[
                    AttributeScheme(
                        name='intergers',
                        type='tuple[types.Integer]',
                        description='Integer array',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='rdum',
                mnemonic='rdum',
                attributes=[
                    AttributeScheme(
                        name='floats',
                        type='tuple[types.Real]',
                        description='Floating point array',
                        restriction='',
                    ),
                ],
            ),
            OptionScheme(
                name='za',
                mnemonic='za',
                attributes=[
                    AttributeScheme(
                        name='anything',
                        type='types.String',
                        description='Any parameters',
                        restriction='',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='zb',
                mnemonic='zb',
                attributes=[
                    AttributeScheme(
                        name='anything',
                        type='types.String',
                        description='Any parameters',
                        restriction='',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='zc',
                mnemonic='zc',
                attributes=[
                    AttributeScheme(
                        name='anything',
                        type='types.String',
                        description='Any parameters',
                        restriction='',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='zd',
                mnemonic='zd',
                attributes=[
                    AttributeScheme(
                        name='anything',
                        type='types.String',
                        description='Any parameters',
                        restriction='',
                        optional=True,
                    ),
                ],
            ),
            OptionScheme(
                name='files',
                mnemonic='files',
                attributes=[
                    AttributeScheme(
                        name='creations',
                        type='tuple[files_.FilesEntry_File]',
                        description='Files to create',
                        restriction='',
                    ),
                ],
                entries=[
                    EntryScheme(
                        name='file',
                        attributes=[
                            AttributeScheme(
                                name='unit',
                                type='types.Integer',
                                description='Unit number of file to create',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='filename',
                                type='types.String',
                                description='Name of file to create',
                                restriction='',
                            ),
                            AttributeScheme(
                                name='access',
                                type='types.String',
                                description='access of file to create',
                                restriction='access in {"sequential", "direct"}',
                            ),
                            AttributeScheme(
                                name='form',
                                type='types.String',
                                description='Format of file to create',
                                restriction='format in {"formatted", "unformatted"}',
                            ),
                            AttributeScheme(
                                name='length',
                                type='types.Integer',
                                description='Record length of file to create',
                                restriction='',
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ),
)
