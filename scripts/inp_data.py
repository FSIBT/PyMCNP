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
        restriction: str = '',
        optional: bool = False,
        extra: str = '',
    ):
        """
        Initializes ``AttributeScheme``.

        Parameters:
            name: INP attribute name.
            type: INP attribute type.
            descirption: INP attribute comment description.
            restriction: INP attribute restriction.
            optional: INP attribute optional setting.

        Returns:
            ``AttributeScheme``.
        """

        self.name: typing.Final[str] = name
        self.type: typing.Final[str] = type
        self.description: typing.Final[str] = description
        self.restriction: typing.Final[str] = restriction
        self.optional: typing.Final[bool] = optional
        self.extra: typing.Final[str] = extra

        GET[name] = self


class ElementScheme:
    """
    Stores INP card metadata.

    Attributes:
        name: INP parser class name.
        mnemonic: INP parser class MCNP mnemonic.
        attributes: INP parser class attributes.
        options: INP parser class options.
        error: INP parser class error.
        extra: INP parser class extra methods.
    """

    def __init__(
        self,
        *,
        name: str,
        mnemonic: str,
        attributes: tuple[AttributeScheme],
        options: tuple[any] = None,
        error: str = 'SEMANTICS_OPTION_VALUE',
        extra: str = '',
    ):
        """
        Initializes ``ElementScheme``.

        Parameters:
            name: INP parser class name.
            mnemonic: INP parser class MCNP mnemonic.
            attributes: INP parser class attributes.
            options: INP parser class options.
            error: INP parser class error.
            extra: INP parser class extra methods.

        Returns:
            ``ElementScheme``.
        """

        self.name: typing.Final[str] = name
        self.mnemonic: typing.Final[str] = mnemonic
        self.attributes: typing.Final[tuple[AttributeScheme]] = attributes
        self.options: typing.Final[tuple[ElementScheme]] = options
        self.error: typing.Final[str] = error
        self.extra: typing.Final[str] = extra


cards = ElementScheme(
    name='',
    mnemonic='',
    attributes=[],
    options=[
        ElementScheme(
            name='comment',
            error='SEMANTICS_CARD_VALUE',
            mnemonic='c',
            attributes=[
                AttributeScheme(
                    name='text',
                    type='types.String',
                    description='comment text',
                )
            ],
        ),
        ElementScheme(
            name='cell',
            error='SEMANTICS_CARD_VALUE',
            mnemonic='',
            attributes=[
                AttributeScheme(
                    name='number',
                    type='types.Integer',
                    description='cell number',
                    restriction='1 <= number <= 99_999_999',
                ),
                AttributeScheme(
                    name='material',
                    type='types.Integer',
                    description='cell material',
                    restriction='0 <= material <= 99_999_999',
                ),
                AttributeScheme(
                    name='density',
                    type='types.Integer',
                    description='cell density',
                    restriction='# TODO #',
                    optional=True,
                ),
                AttributeScheme(
                    name='geometry',
                    type='types.Geometry',
                    description='cell geometry',
                    restriction='# TODO #',
                ),
                AttributeScheme(
                    name='options',
                    type='types.Tuple[cell.CellOption_]',
                    description='cell options',
                    optional=True,
                ),
            ],
            options=[
                ElementScheme(
                    name='imp',
                    mnemonic='imp',
                    attributes=(
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Particle designator',
                        ),
                        AttributeScheme(
                            name='importance',
                            type='types.Real',
                            description='Cell particle importance',
                        ),
                    ),
                ),
                ElementScheme(
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
                ElementScheme(
                    name='pwt',
                    mnemonic='pwt',
                    attributes=(
                        AttributeScheme(
                            name='weight',
                            type='types.Real',
                            description='Cell weight of photons produced at neutron collisions',
                        ),
                    ),
                ),
                ElementScheme(
                    name='ext',
                    mnemonic='ext',
                    attributes=(
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Cell particle designator',
                        ),
                        AttributeScheme(
                            name='stretch',
                            type='types.String',
                            description='Cell exponential transform stretching specifier',
                        ),
                    ),
                ),
                ElementScheme(
                    name='fcl',
                    mnemonic='fcl',
                    attributes=(
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Cell particle designator',
                        ),
                        AttributeScheme(
                            name='control',
                            type='types.Real',
                            description='Cell forced-collision control',
                            restriction='-1 <= control <= 1',
                        ),
                    ),
                ),
                ElementScheme(
                    name='wwn',
                    mnemonic='wwn',
                    attributes=(
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Cell option suffix',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Cell particle designator',
                        ),
                        AttributeScheme(
                            name='bound',
                            type='types.Real',
                            description='Cell weight-window space, time, or energy lower bound',
                            restriction='bound == -1 or bound >= 0',
                        ),
                    ),
                ),
                ElementScheme(
                    name='dxc',
                    mnemonic='dxc',
                    attributes=(
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Cell option suffix',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Cell particle designator',
                        ),
                        AttributeScheme(
                            name='probability',
                            type='types.Real',
                            description='Cell probability of DXTRAN contribution',
                            restriction='0 <= probability <= 1',
                        ),
                    ),
                ),
                ElementScheme(
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
                ElementScheme(
                    name='pd',
                    mnemonic='pd',
                    attributes=(
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Cell option suffix',
                        ),
                        AttributeScheme(
                            name='probability',
                            type='types.Real',
                            description='Cell probability of DXTRAN contribution',
                            restriction='0 <= probability <= 1',
                        ),
                    ),
                ),
                ElementScheme(
                    name='tmp',
                    mnemonic='tmp',
                    attributes=(
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Cell option suffix',
                        ),
                        AttributeScheme(
                            name='temperature',
                            type='types.Real',
                            description='Cell temperature at suffix time index',
                            restriction='temperature > 0',
                        ),
                    ),
                ),
                ElementScheme(
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
                ElementScheme(
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
                ElementScheme(
                    name='trcl_1',
                    mnemonic='trcl',
                    attributes=[
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_0',
                            description='Cell transformation.',
                        ),
                    ],
                ),
                ElementScheme(
                    name='trcl_2',
                    mnemonic='trcl',
                    attributes=[
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_1',
                            description='Cell transformation.',
                        ),
                    ],
                ),
                ElementScheme(
                    name='trcl_3',
                    mnemonic='trcl',
                    attributes=[
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_2',
                            description='Cell transformation.',
                        ),
                    ],
                ),
                ElementScheme(
                    name='trcl_4',
                    mnemonic='trcl',
                    attributes=[
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_3',
                            description='Cell transformation.',
                        ),
                    ],
                ),
                ElementScheme(
                    name='trcl_5',
                    mnemonic='trcl',
                    attributes=[
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_4',
                            description='Cell transformation.',
                        ),
                    ],
                ),
                ElementScheme(
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
                ElementScheme(
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
                ElementScheme(
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
                            type='types.Transformation_0',
                            description='Cell fill transformation',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_2',
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
                            type='types.Transformation_1',
                            description='Cell fill transformation',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_3',
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
                            type='types.Transformation_2',
                            description='Cell fill transformation',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_4',
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
                            type='types.Transformation_3',
                            description='Cell fill transformation',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_5',
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
                            type='types.Transformation_4',
                            description='Cell fill transformation',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_6',
                    mnemonic='fill',
                    attributes=[
                        AttributeScheme(
                            name='i',
                            type='types.Index',
                            description='Lattice parameter #1',
                        ),
                        AttributeScheme(
                            name='j',
                            type='types.Index',
                            description='Lattice parameter #2',
                        ),
                        AttributeScheme(
                            name='k',
                            type='types.Index',
                            description='Lattice parameter #3',
                        ),
                        AttributeScheme(
                            name='universes',
                            type='types.Tuple[types.Integer]',
                            description='Fill universe numbers',
                            restriction='len(universes) == (i.upper - i.lower) * (j.upper - j.lower) * (k.upper - k.lower)',
                        ),
                        AttributeScheme(
                            name='m',
                            type='types.Integer',
                            description='Displacement vector origin',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='elpt',
                    mnemonic='elpt',
                    attributes=(
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Cell particle designator',
                        ),
                        AttributeScheme(
                            name='cutoff',
                            type='types.Real',
                            description='Cell energy cutoff',
                        ),
                    ),
                ),
                ElementScheme(
                    name='tmp_0',
                    mnemonic='tmp',
                    attributes=(
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Thermal time index',
                        ),
                        AttributeScheme(
                            name='temperature',
                            type='types.Tuple[types.Real]',
                            description='Temperature at time index',
                            restriction='min(temperature) > 0',
                        ),
                    ),
                ),
                ElementScheme(
                    name='tmp_1',
                    mnemonic='tmp',
                    attributes=(
                        AttributeScheme(
                            name='temperature',
                            type='types.Tuple[types.Real]',
                            description='Temperature at time index',
                            restriction='min(temperature) > 0',
                        ),
                    ),
                ),
                ElementScheme(
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
                ElementScheme(
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
                ElementScheme(
                    name='unc',
                    mnemonic='unc',
                    attributes=(
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Cell particle designator',
                        ),
                        AttributeScheme(
                            name='setting',
                            type='types.Integer',
                            description='Cell uncollided secondaries setting',
                            restriction='setting.value in {0, 1}',
                        ),
                    ),
                ),
            ],
        ),
        ElementScheme(
            name='surface',
            error='SEMANTICS_CARD_VALUE',
            mnemonic='',
            attributes=[
                AttributeScheme(
                    name='options',
                    type='surface.SurfaceOption_',
                    description='Help Me!',
                ),
            ],
            options=[
                ElementScheme(
                    name='p_0',
                    mnemonic='p',
                    attributes=[
                        AttributeScheme(
                            name='a',
                            type='types.Real',
                            description='Equation-defined general plane A coefficent',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.Real',
                            description='Equation-defined general plane B coefficent',
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.Real',
                            description='Equation-defined general plane C coefficent',
                        ),
                        AttributeScheme(
                            name='d',
                            type='types.Real',
                            description='Equation-defined general plane D coefficent',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Px``.

        Returns:
            ``pyvista.PolyData`` for ``Px``
        """

        vis = _visualization.Visualization.get_plane(
            self.a.value, self.b.value, self.c.value, self.d.value
        )

        return vis
    ''',
                ),
                ElementScheme(
                    name='p_1',
                    mnemonic='p',
                    attributes=[
                        AttributeScheme(
                            name='x1',
                            type='types.Real',
                            description='point-defined general plane x-coordinate #1',
                        ),
                        AttributeScheme(
                            name='y1',
                            type='types.Real',
                            description='point-defined general plane y-coordinate #1',
                        ),
                        AttributeScheme(
                            name='z1',
                            type='types.Real',
                            description='point-defined general plane z-coordinate #1',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.Real',
                            description='point-defined general plane x-coordinate #2',
                        ),
                        AttributeScheme(
                            name='y2',
                            type='types.Real',
                            description='point-defined general plane y-coordinate #2',
                        ),
                        AttributeScheme(
                            name='z2',
                            type='types.Real',
                            description='point-defined general plane z-coordinate #2',
                        ),
                        AttributeScheme(
                            name='x3',
                            type='types.Real',
                            description='point-defined general plane x-coordinate #3',
                        ),
                        AttributeScheme(
                            name='y3',
                            type='types.Real',
                            description='point-defined general plane y-coordinate #3',
                        ),
                        AttributeScheme(
                            name='z3',
                            type='types.Real',
                            description='point-defined general plane z-coordinate #3',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``P0``.

        Returns:
            ``pyvista.PolyData`` for ``P1``
        """

        a = _visualization.Vector(self.x2 - self.x1, self.y2 - self.y1, self.z2 - self.z1)
        b = _visualization.Vector(self.x3 - self.x1, self.y3 - self.y1, self.z3 - self.z1)
        n = a * b

        vis = _visualization.Visualization.get_plane(
            n.x, n.y, n.z, n.x * self.x1 + n.y * self.y1 + n.z * self.z1
        )

        return vis
    ''',
                ),
                ElementScheme(
                    name='px',
                    mnemonic='px',
                    attributes=[
                        AttributeScheme(
                            name='d',
                            type='types.Real',
                            description='Normal-to-the-x-axis plane D coefficent',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Px``.

        Returns:
            ``pyvista.PolyData`` for ``Px``
        """

        vis = _visualization.Visualization.get_plane(1, 0, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='py',
                    mnemonic='py',
                    attributes=[
                        AttributeScheme(
                            name='d',
                            type='types.Real',
                            description='Normal-to-the-y-axis plane D coefficent',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Py``.

        Returns:
            ``pyvista.PolyData`` for ``Py``
        """

        vis = _visualization.Visualization.get_plane(0, 1, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='pz',
                    mnemonic='pz',
                    attributes=[
                        AttributeScheme(
                            name='d',
                            type='types.Real',
                            description='Normal-to-the-z-axis plane D coefficent',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Pz``.

        Returns:
            ``pyvista.PolyData`` for ``Pz``
        """

        vis = _visualization.Visualization.get_plane(0, 0, 1, self.d.value)

        return vis
    ''',
                ),
                ElementScheme(
                    name='so',
                    mnemonic='so',
                    attributes=[
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='Origin-centered sphere radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``So``.

        Returns:
            ``pyvista.PolyData`` for ``So``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)

        return vis
    ''',
                ),
                ElementScheme(
                    name='s',
                    mnemonic='s',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='General sphere center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='General sphere center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='General sphere center z component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='General sphere radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``S``.

        Returns:
            ``pyvista.PolyData`` for ``S``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='sx',
                    mnemonic='sx',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='On-x-axis sphere center x component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='On-x-axis sphere radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Sx``.

        Returns:
            ``pyvista.PolyData`` for ``Sx``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='sy',
                    mnemonic='sy',
                    attributes=[
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='On-y-axis sphere center y component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='On-y-axis sphere radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Sy``.

        Returns:
            ``pyvista.PolyData`` for ``Sy``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='sz',
                    mnemonic='sz',
                    attributes=[
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='On-z-axis sphere center z component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='On-z-axis sphere radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Sz``.

        Returns:
            ``pyvista.PolyData`` for ``Sz``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='c/x',
                    mnemonic='c/x',
                    attributes=[
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Parallel-to-x-axis cylinder center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Parallel-to-x-axis cylinder center z component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='Parallel-to-x-axis cylinder radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``C_x``.

        Returns:
            ``pyvista.PolyData`` for ``C_x``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='c/y',
                    mnemonic='c/y',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Parallel-to-y-axis cylinder center x component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Parallel-to-y-axis cylinder center z component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='Parallel-to-y-axis cylinder radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``C_y``.

        Returns:
            ``pyvista.PolyData`` for ``C_y``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='c/z',
                    mnemonic='c/z',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Parallel-to-z-axis cylinder center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Parallel-to-z-axis cylinder center y component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='Parallel-to-z-axis cylinder radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``C_z``.
        Returns:
            ``pyvista.PolyData`` for ``C_z``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='cx',
                    mnemonic='cx',
                    attributes=[
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='On-x-axis cylinder radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Cx``.

        Returns:
            ``pyvista.PolyData`` for ``Cx``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='cy',
                    mnemonic='cy',
                    attributes=[
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='On-y-axis cylinder radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Cy``.

        Returns:
            ``pyvista.PolyData`` for ``Cy``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='cz',
                    mnemonic='cz',
                    attributes=[
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='On-z-axis cylinder radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Cz``.

        Returns:
            ``pyvista.PolyData`` for ``Cz``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)

        return vis
    ''',
                ),
                ElementScheme(
                    name='k/x',
                    mnemonic='k/x',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Parallel-to-x-axis cone center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Parallel-to-x-axis cone center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Parallel-to-x-axis cone center z component',
                        ),
                        AttributeScheme(
                            name='t_squared',
                            type='types.Real',
                            description='Parallel-to-x-axis cone t^2 coefficent',
                        ),
                        AttributeScheme(
                            name='plusminus_1',
                            type='types.Real',
                            description='Parallel-to-x-axis cone sheet selector',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``K_x``.

        Returns:
            ``pyvista.PolyData`` for ``K_x``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='k/y',
                    mnemonic='k/y',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Parallel-to-y-axis cone center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Parallel-to-y-axis cone center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Parallel-to-y-axis cone center z component',
                        ),
                        AttributeScheme(
                            name='t_squared',
                            type='types.Real',
                            description='Parallel-to-y-axis cone t^2 coefficent',
                        ),
                        AttributeScheme(
                            name='plusminus_1',
                            type='types.Real',
                            description='Parallel-to-y-axis cone sheet selector',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``K_y``.

        Returns:
            ``pyvista.PolyData`` for ``K_y``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='k/z',
                    mnemonic='k/z',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Parallel-to-z-axis cone center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Parallel-to-z-axis cone center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Parallel-to-z-axis cone center z component',
                        ),
                        AttributeScheme(
                            name='t_squared',
                            type='types.Real',
                            description='Parallel-to-z-axis cone t^2 coefficent',
                        ),
                        AttributeScheme(
                            name='plusminus_1',
                            type='types.Real',
                            description='Parallel-to-z-axis cone sheet selector',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``K_z``.

        Returns:
            ``pyvista.PolyData`` for ``K_z``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='kx',
                    mnemonic='kx',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='On-x-axis cone center x component',
                        ),
                        AttributeScheme(
                            name='t_squared',
                            type='types.Real',
                            description='On-x-axis cone t^2 coefficent',
                        ),
                        AttributeScheme(
                            name='plusminus_1',
                            type='types.Real',
                            description='On-x-axis cone sheet selector',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Kx``.

        Returns:
            ``pyvista.PolyData`` for ``Kx``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='ky',
                    mnemonic='ky',
                    attributes=[
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='On-y-axis cone center y component',
                        ),
                        AttributeScheme(
                            name='t_squared',
                            type='types.Real',
                            description='On-y-axis cone t^2 coefficent',
                        ),
                        AttributeScheme(
                            name='plusminus_1',
                            type='types.Real',
                            description='On-y-axis cone sheet selector',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Ky``.

        Returns:
            ``pyvista.PolyData`` for ``Ky``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis
    ''',
                ),
                ElementScheme(
                    name='kz',
                    mnemonic='kz',
                    attributes=[
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='On-z-axis cone center z component',
                        ),
                        AttributeScheme(
                            name='t_squared',
                            type='types.Real',
                            description='On-z-axis cone t^2 coefficent',
                        ),
                        AttributeScheme(
                            name='plusminus_1',
                            type='types.Real',
                            description='On-z-axis cone sheet selector',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Kz``.

        Returns:
            ``pyvista.PolyData`` for ``Kz``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='sq',
                    mnemonic='sq',
                    attributes=[
                        AttributeScheme(
                            name='a',
                            type='types.Real',
                            description='Oblique special quadratic A coefficent',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.Real',
                            description='Oblique special quadratic B coefficent',
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.Real',
                            description='Oblique special quadratic C coefficent',
                        ),
                        AttributeScheme(
                            name='d',
                            type='types.Real',
                            description='Oblique special quadratic D coefficent',
                        ),
                        AttributeScheme(
                            name='e',
                            type='types.Real',
                            description='Oblique special quadratic E coefficent',
                        ),
                        AttributeScheme(
                            name='f',
                            type='types.Real',
                            description='Oblique special quadratic F coefficent',
                        ),
                        AttributeScheme(
                            name='g',
                            type='types.Real',
                            description='Oblique special quadratic G coefficent',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Oblique special quadratic center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Oblique special quadratic center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Oblique special quadratic center z component',
                        ),
                    ],
                ),
                ElementScheme(
                    name='gq',
                    mnemonic='gq',
                    attributes=[
                        AttributeScheme(
                            name='a',
                            type='types.Real',
                            description='Oblique special quadratic A coefficent',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.Real',
                            description='Oblique special quadratic B coefficent',
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.Real',
                            description='Oblique special quadratic C coefficent',
                        ),
                        AttributeScheme(
                            name='d',
                            type='types.Real',
                            description='Oblique special quadratic D coefficent',
                        ),
                        AttributeScheme(
                            name='e',
                            type='types.Real',
                            description='Oblique special quadratic E coefficent',
                        ),
                        AttributeScheme(
                            name='f',
                            type='types.Real',
                            description='Oblique special quadratic F coefficent',
                        ),
                        AttributeScheme(
                            name='g',
                            type='types.Real',
                            description='Oblique special quadratic G coefficent',
                        ),
                        AttributeScheme(
                            name='h',
                            type='types.Real',
                            description='Oblique special quadratic H coefficent',
                        ),
                        AttributeScheme(
                            name='j',
                            type='types.Real',
                            description='Oblique special quadratic J coefficent',
                        ),
                        AttributeScheme(
                            name='k',
                            type='types.Real',
                            description='Oblique special quadratic K coefficent',
                        ),
                    ],
                ),
                ElementScheme(
                    name='tx',
                    mnemonic='tx',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Parallel-to-x-axis tori center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Parallel-to-x-axis tori center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Parallel-to-x-axis tori center z component',
                        ),
                        AttributeScheme(
                            name='a',
                            type='types.Real',
                            description='Parallel-to-x-axis tori A coefficent',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.Real',
                            description='Parallel-to-x-axis tori B coefficent',
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.Real',
                            description='Parallel-to-x-axis tori C coefficent',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Tx``.

        Returns:
            ``pyvista.PolyData`` for ``Tx``
        """

        vis = _visualization.Visualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='ty',
                    mnemonic='ty',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Parallel-to-y-axis tori center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Parallel-to-y-axis tori center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Parallel-to-y-axis tori center z component',
                        ),
                        AttributeScheme(
                            name='a',
                            type='types.Real',
                            description='Parallel-to-y-axis tori A coefficent',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.Real',
                            description='Parallel-to-y-axis tori B coefficent',
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.Real',
                            description='Parallel-to-y-axis tori C coefficent',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Ty``.

        Returns:
            ``pyvista.PolyData`` for ``Ty``
        """

        vis = _visualization.Visualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='tz',
                    mnemonic='tz',
                    attributes=[
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Parallel-to-z-axis tori center x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Parallel-to-z-axis tori center y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Parallel-to-z-axis tori center z component',
                        ),
                        AttributeScheme(
                            name='a',
                            type='types.Real',
                            description='Parallel-to-z-axis tori A coefficent',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.Real',
                            description='Parallel-to-z-axis tori B coefficent',
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.Real',
                            description='Parallel-to-z-axis tori C coefficent',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Tz``.

        Returns:
            ``pyvista.PolyData`` for ``Tz``
        """

        vis = _visualization.Visualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
    ''',
                ),
                ElementScheme(
                    name='x',
                    mnemonic='x',
                    attributes=[
                        AttributeScheme(
                            name='x1',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #1 x component',
                        ),
                        AttributeScheme(
                            name='r1',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #1 radius',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #2 x component',
                        ),
                        AttributeScheme(
                            name='r2',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #2 radius',
                        ),
                        AttributeScheme(
                            name='x3',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #3 x component',
                        ),
                        AttributeScheme(
                            name='r3',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #3 radius',
                        ),
                    ],
                ),
                ElementScheme(
                    name='y',
                    mnemonic='y',
                    attributes=[
                        AttributeScheme(
                            name='y1',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #1 y component',
                        ),
                        AttributeScheme(
                            name='r1',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #1 radius',
                        ),
                        AttributeScheme(
                            name='y2',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #2 y component',
                        ),
                        AttributeScheme(
                            name='r2',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #2 radius',
                        ),
                        AttributeScheme(
                            name='y3',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #3 y component',
                        ),
                        AttributeScheme(
                            name='r3',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #3 radius',
                        ),
                    ],
                ),
                ElementScheme(
                    name='z',
                    mnemonic='z',
                    attributes=[
                        AttributeScheme(
                            name='z1',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #1 z component',
                        ),
                        AttributeScheme(
                            name='r1',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #1 radius',
                        ),
                        AttributeScheme(
                            name='z2',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #2 z component',
                        ),
                        AttributeScheme(
                            name='r2',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #2 radius',
                        ),
                        AttributeScheme(
                            name='z3',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #3 z component',
                        ),
                        AttributeScheme(
                            name='r3',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #3 radius',
                        ),
                    ],
                ),
                ElementScheme(
                    name='box',
                    mnemonic='box',
                    attributes=[
                        AttributeScheme(
                            name='vx',
                            type='types.Real',
                            description='Box macrobody position vector x component',
                        ),
                        AttributeScheme(
                            name='vy',
                            type='types.Real',
                            description='Box macrobody position vector y component',
                        ),
                        AttributeScheme(
                            name='vz',
                            type='types.Real',
                            description='Box macrobody position vector z component',
                        ),
                        AttributeScheme(
                            name='a1x',
                            type='types.Real',
                            description='Box macrobody vector #1 x component',
                        ),
                        AttributeScheme(
                            name='a1y',
                            type='types.Real',
                            description='Box macrobody vector #1 y component',
                        ),
                        AttributeScheme(
                            name='a1z',
                            type='types.Real',
                            description='Box macrobody vector #1 z component',
                        ),
                        AttributeScheme(
                            name='a2x',
                            type='types.Real',
                            description='Box macrobody vector #2 x component',
                        ),
                        AttributeScheme(
                            name='a2y',
                            type='types.Real',
                            description='Box macrobody vector #2 y component',
                        ),
                        AttributeScheme(
                            name='a2z',
                            type='types.Real',
                            description='Box macrobody vector #2 z component',
                        ),
                        AttributeScheme(
                            name='a3x',
                            type='types.Real',
                            description='Box macrobody vector #3 x component',
                        ),
                        AttributeScheme(
                            name='a3y',
                            type='types.Real',
                            description='Box macrobody vector #3 y component',
                        ),
                        AttributeScheme(
                            name='a3z',
                            type='types.Real',
                            description='Box macrobody vector #3 z component',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Box``.

        Returns:
            ``pyvista.PolyData`` for ``Box``.
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        a1 = _visualization.Vector(self.a1x.value, self.a1y.value, self.a1z.value)
        a2 = _visualization.Vector(self.a2x.value, self.a2y.value, self.a2z.value)
        a3 = _visualization.Vector(self.a3x.value, self.a3y.value, self.a3z.value)
        cross = _visualization.Vector(1, 0, 0) * a1
        angle = _visualization.Vector(1, 0, 0) & a1

        vis = _visualization.Visualization.get_box(a1.norm(), a2.norm(), a3.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis
    ''',
                ),
                ElementScheme(
                    name='rpp',
                    mnemonic='rpp',
                    attributes=[
                        AttributeScheme(
                            name='xmin',
                            type='types.Real',
                            description='Parallelepiped x termini minimum',
                        ),
                        AttributeScheme(
                            name='xmax',
                            type='types.Real',
                            description='Parallelepiped x termini maximum',
                        ),
                        AttributeScheme(
                            name='ymin',
                            type='types.Real',
                            description='Parallelepiped y termini minimum',
                        ),
                        AttributeScheme(
                            name='ymax',
                            type='types.Real',
                            description='Parallelepiped y termini maximum',
                        ),
                        AttributeScheme(
                            name='zmin',
                            type='types.Real',
                            description='Parallelepiped z termini minimum',
                        ),
                        AttributeScheme(
                            name='zmax',
                            type='types.Real',
                            description='Parallelepiped z termini maximum',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Rpp``.

        Returns:
            ``pyvista.PolyData`` for ``Rpp``
        """

        vis = _visualization.Visualization.get_parallelipiped(
            self.xmin.value,
            self.xmax.value,
            self.ymin.value,
            self.ymax.value,
            self.zmin.value,
            self.zmax.value,
        )

        return vis
    ''',
                ),
                ElementScheme(
                    name='sph',
                    mnemonic='sph',
                    attributes=[
                        AttributeScheme(
                            name='vx',
                            type='types.Real',
                            description='Sphere macrobody position vector x component',
                        ),
                        AttributeScheme(
                            name='vy',
                            type='types.Real',
                            description='Sphere macrobody position vector y component',
                        ),
                        AttributeScheme(
                            name='vz',
                            type='types.Real',
                            description='Sphere macrobody position vector z component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='Sphere macrobody radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Sph``.

        Returns:
            ``pyvista.PolyData`` for ``Sph``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(
            _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        )

        return vis
    ''',
                ),
                ElementScheme(
                    name='rcc',
                    mnemonic='rcc',
                    attributes=[
                        AttributeScheme(
                            name='vx',
                            type='types.Real',
                            description='Circular cylinder macrobody position vector x component',
                        ),
                        AttributeScheme(
                            name='vy',
                            type='types.Real',
                            description='Circular cylinder macrobody position vector y component',
                        ),
                        AttributeScheme(
                            name='vz',
                            type='types.Real',
                            description='Circular cylinder macrobody position vector z component',
                        ),
                        AttributeScheme(
                            name='hx',
                            type='types.Real',
                            description='Circular cylinder macrobody height vector x component',
                        ),
                        AttributeScheme(
                            name='hy',
                            type='types.Real',
                            description='Circular cylinder macrobody height vector y component',
                        ),
                        AttributeScheme(
                            name='hz',
                            type='types.Real',
                            description='Circular cylinder macrobody height vector z component',
                        ),
                        AttributeScheme(
                            name='r',
                            type='types.Real',
                            description='Circular cylinder macrobody radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Rcc``.

        Returns:
            ``pyvista.PolyData`` for ``Rcc``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cylinder_circle(h.norm(), self.r.value)
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis
    ''',
                ),
                ElementScheme(
                    name='rhp',
                    mnemonic='rhp',
                    attributes=[
                        AttributeScheme(
                            name='vx',
                            type='types.Real',
                            description='Hexagonal prism position vector x component',
                        ),
                        AttributeScheme(
                            name='vy',
                            type='types.Real',
                            description='Hexagonal prism position vector y component',
                        ),
                        AttributeScheme(
                            name='vz',
                            type='types.Real',
                            description='Hexagonal prism position vector z component',
                        ),
                        AttributeScheme(
                            name='hx',
                            type='types.Real',
                            description='Hexagonal prism height vector x component',
                        ),
                        AttributeScheme(
                            name='hy',
                            type='types.Real',
                            description='Hexagonal prism height vector y component',
                        ),
                        AttributeScheme(
                            name='hz',
                            type='types.Real',
                            description='Hexagonal prism height vector z component',
                        ),
                        AttributeScheme(
                            name='r1',
                            type='types.Real',
                            description='Hexagonal prism facet #1 vector x component',
                        ),
                        AttributeScheme(
                            name='r2',
                            type='types.Real',
                            description='Hexagonal prism facet #1 vector y component',
                        ),
                        AttributeScheme(
                            name='r3',
                            type='types.Real',
                            description='Hexagonal prism facet #1 vector z component',
                        ),
                        AttributeScheme(
                            name='s1',
                            type='types.Real',
                            description='Hexagonal prism facet #2 vector x component',
                        ),
                        AttributeScheme(
                            name='s2',
                            type='types.Real',
                            description='Hexagonal prism facet #2 vector y component',
                        ),
                        AttributeScheme(
                            name='s3',
                            type='types.Real',
                            description='Hexagonal prism facet #2 vector z component',
                        ),
                        AttributeScheme(
                            name='t1',
                            type='types.Real',
                            description='Hexagonal prism facet #3 vector x component',
                        ),
                        AttributeScheme(
                            name='t2',
                            type='types.Real',
                            description='Hexagonal prism facet #3 vector y component',
                        ),
                        AttributeScheme(
                            name='t3',
                            type='types.Real',
                            description='Hexagonal prism facet #3 vector z component',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Rhp``.

        Returns:
            ``pyvista.PolyData`` for ``Rhp``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)
        r = _visualization.Vector(self.r1.value, self.r2.value, self.r3.value)
        s = _visualization.Vector(self.s1.value, self.s2.value, self.s3.value)
        t = _visualization.Vector(self.t1.value, self.t2.value, self.t3.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cylinder_hexagon(
            h.norm(), r.apothem(), s.apothem(), t.apothem()
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis
    ''',
                ),
                ElementScheme(
                    name='rec',
                    mnemonic='rec',
                    attributes=[
                        AttributeScheme(
                            name='vx',
                            type='types.Real',
                            description='Elliptical cylinder position vector x component',
                        ),
                        AttributeScheme(
                            name='vy',
                            type='types.Real',
                            description='Elliptical cylinder position vector y component',
                        ),
                        AttributeScheme(
                            name='vz',
                            type='types.Real',
                            description='Elliptical cylinder position vector z component',
                        ),
                        AttributeScheme(
                            name='hx',
                            type='types.Real',
                            description='Elliptical cylinder height vector x component',
                        ),
                        AttributeScheme(
                            name='hy',
                            type='types.Real',
                            description='Elliptical cylinder height vector y component',
                        ),
                        AttributeScheme(
                            name='hz',
                            type='types.Real',
                            description='Elliptical cylinder height vector z component',
                        ),
                        AttributeScheme(
                            name='v1x',
                            type='types.Real',
                            description='Elliptical cylinder major axis vector x component',
                        ),
                        AttributeScheme(
                            name='v1y',
                            type='types.Real',
                            description='Elliptical cylinder major axis vector y component',
                        ),
                        AttributeScheme(
                            name='v1z',
                            type='types.Real',
                            description='Elliptical cylinder major axis vector z component',
                        ),
                        AttributeScheme(
                            name='v2x',
                            type='types.Real',
                            description='Elliptical cylinder minor axis vector x component',
                        ),
                        AttributeScheme(
                            name='v2y',
                            type='types.Real',
                            description='Elliptical cylinder minor axis vector y component',
                        ),
                        AttributeScheme(
                            name='v2z',
                            type='types.Real',
                            description='Elliptical cylinder minor axis vector z component',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Rec``.

        Returns:
            ``pyvista.PolyData`` for ``Rec``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)
        v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cylinder_ellipse(h.norm(), v1.norm(), v2.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis
    ''',
                ),
                ElementScheme(
                    name='trc',
                    mnemonic='trc',
                    attributes=[
                        AttributeScheme(
                            name='vx',
                            type='types.Real',
                            description='Truncated cone position vector x component',
                        ),
                        AttributeScheme(
                            name='vy',
                            type='types.Real',
                            description='Truncated cone position vector y component',
                        ),
                        AttributeScheme(
                            name='vz',
                            type='types.Real',
                            description='Truncated cone position vector z component',
                        ),
                        AttributeScheme(
                            name='hx',
                            type='types.Real',
                            description='Truncated cone height vector x component',
                        ),
                        AttributeScheme(
                            name='hy',
                            type='types.Real',
                            description='Truncated cone height vector y component',
                        ),
                        AttributeScheme(
                            name='hz',
                            type='types.Real',
                            description='Truncated cone height vector z component',
                        ),
                        AttributeScheme(
                            name='r1',
                            type='types.Real',
                            description='Truncated cone lower cone radius',
                        ),
                        AttributeScheme(
                            name='r2',
                            type='types.Real',
                            description='Truncated cone upper cone radius',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Trc``.

        Returns:
            ``pyvista.PolyData`` for ``Trc``
        """

        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)

        cross = h * _visualization.Vector(0, 0, 1)
        angle = h & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cone_truncated(
            h.norm(), self.r1.value, self.r2.value
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(
            _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        )

        return vis
    ''',
                ),
                ElementScheme(
                    name='ell',
                    mnemonic='ell',
                    attributes=[
                        AttributeScheme(
                            name='v1x',
                            type='types.Real',
                            description='Ellipsoid focus #1 or center x component',
                        ),
                        AttributeScheme(
                            name='v1y',
                            type='types.Real',
                            description='Ellipsoid focus #1 or center y component',
                        ),
                        AttributeScheme(
                            name='v1z',
                            type='types.Real',
                            description='Ellipsoid focus #1 or center z component',
                        ),
                        AttributeScheme(
                            name='v2x',
                            type='types.Real',
                            description='Ellipsoid focus #2 or major axis x component',
                        ),
                        AttributeScheme(
                            name='v2y',
                            type='types.Real',
                            description='Ellipsoid focus #2 or major axis y component',
                        ),
                        AttributeScheme(
                            name='v2z',
                            type='types.Real',
                            description='Ellipsoid focus #2 or major axis z component',
                        ),
                        AttributeScheme(
                            name='rm',
                            type='types.Real',
                            description='Ellipsoid major/minor axis radius length',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Ell``.

        Returns:
            ``pyvista.PolyData`` for ``Ell``.
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

        vis = _visualization.Visualization.get_ellipsoid(major_length, minor_length)
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(center)

        return vis
    ''',
                ),
                ElementScheme(
                    name='wed',
                    mnemonic='wed',
                    attributes=[
                        AttributeScheme(
                            name='vx',
                            type='types.Real',
                            description='Wedge position vector x component',
                        ),
                        AttributeScheme(
                            name='vy',
                            type='types.Real',
                            description='Wedge position vector y component',
                        ),
                        AttributeScheme(
                            name='vz',
                            type='types.Real',
                            description='Wedge position vector z component',
                        ),
                        AttributeScheme(
                            name='v1x',
                            type='types.Real',
                            description='Wedge side vector #1 x component',
                        ),
                        AttributeScheme(
                            name='v1y',
                            type='types.Real',
                            description='Wedge side vector #1 y component',
                        ),
                        AttributeScheme(
                            name='v1z',
                            type='types.Real',
                            description='Wedge side vector #1 z component',
                        ),
                        AttributeScheme(
                            name='v2x',
                            type='types.Real',
                            description='Wedge side vector #2 x component',
                        ),
                        AttributeScheme(
                            name='v2y',
                            type='types.Real',
                            description='Wedge side vector #2 y component',
                        ),
                        AttributeScheme(
                            name='v2z',
                            type='types.Real',
                            description='Wedge side vector #2 z component',
                        ),
                        AttributeScheme(
                            name='v3x',
                            type='types.Real',
                            description='Wedge height vector x component',
                        ),
                        AttributeScheme(
                            name='v3y',
                            type='types.Real',
                            description='Wedge height vector y component',
                        ),
                        AttributeScheme(
                            name='v3z',
                            type='types.Real',
                            description='Wedge height vector z component',
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Wed``.

        Returns:
            ``pyvista.PolyData`` for ``Wed``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)
        v3 = _visualization.Vector(self.v3x.value, self.v3y.value, self.v3z.value)

        cross = _visualization.Vector(1, 0, 0) * v1
        angle = _visualization.Vector(1, 0, 0) & v1

        vis = _visualization.Visualization.get_wedge(v1.norm(), v2.norm(), v3.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis
    ''',
                ),
                ElementScheme(
                    name='arb',
                    mnemonic='arb',
                    attributes=[
                        AttributeScheme(
                            name='ax',
                            type='types.Real',
                            description='Polyhedron corner #1 x component',
                        ),
                        AttributeScheme(
                            name='ay',
                            type='types.Real',
                            description='Polyhedron corner #1 y component',
                        ),
                        AttributeScheme(
                            name='az',
                            type='types.Real',
                            description='Polyhedron corner #1 z component',
                        ),
                        AttributeScheme(
                            name='bx',
                            type='types.Real',
                            description='Polyhedron corner #2 x component',
                        ),
                        AttributeScheme(
                            name='by',
                            type='types.Real',
                            description='Polyhedron corner #2 y component',
                        ),
                        AttributeScheme(
                            name='bz',
                            type='types.Real',
                            description='Polyhedron corner #2 z component',
                        ),
                        AttributeScheme(
                            name='cx',
                            type='types.Real',
                            description='Polyhedron corner #3 x component',
                        ),
                        AttributeScheme(
                            name='cy',
                            type='types.Real',
                            description='Polyhedron corner #3 y component',
                        ),
                        AttributeScheme(
                            name='cz',
                            type='types.Real',
                            description='Polyhedron corner #3 z component',
                        ),
                        AttributeScheme(
                            name='dx',
                            type='types.Real',
                            description='Polyhedron corner #4 x component',
                        ),
                        AttributeScheme(
                            name='dy',
                            type='types.Real',
                            description='Polyhedron corner #4 y component',
                        ),
                        AttributeScheme(
                            name='dz',
                            type='types.Real',
                            description='Polyhedron corner #4 z component',
                        ),
                        AttributeScheme(
                            name='ex',
                            type='types.Real',
                            description='Polyhedron corner #5 x component',
                        ),
                        AttributeScheme(
                            name='ey',
                            type='types.Real',
                            description='Polyhedron corner #5 y component',
                        ),
                        AttributeScheme(
                            name='ez',
                            type='types.Real',
                            description='Polyhedron corner #5 z component',
                        ),
                        AttributeScheme(
                            name='fx',
                            type='types.Real',
                            description='Polyhedron corner #6 x component',
                        ),
                        AttributeScheme(
                            name='fy',
                            type='types.Real',
                            description='Polyhedron corner #6 y component',
                        ),
                        AttributeScheme(
                            name='fz',
                            type='types.Real',
                            description='Polyhedron corner #6 z component',
                        ),
                        AttributeScheme(
                            name='gx',
                            type='types.Real',
                            description='Polyhedron corner #7 x component',
                        ),
                        AttributeScheme(
                            name='gy',
                            type='types.Real',
                            description='Polyhedron corner #7 y component',
                        ),
                        AttributeScheme(
                            name='gz',
                            type='types.Real',
                            description='Polyhedron corner #7 z component',
                        ),
                        AttributeScheme(
                            name='hx',
                            type='types.Real',
                            description='Polyhedron corner #8 x component',
                        ),
                        AttributeScheme(
                            name='hy',
                            type='types.Real',
                            description='Polyhedron corner #8 y component',
                        ),
                        AttributeScheme(
                            name='hz',
                            type='types.Real',
                            description='Polyhedron corner #8 z component',
                        ),
                        AttributeScheme(
                            name='n1',
                            type='types.Real',
                            description='Polyhedron four-digit side specificer #1',
                        ),
                        AttributeScheme(
                            name='n2',
                            type='types.Real',
                            description='Polyhedron four-digit side specificer #2',
                        ),
                        AttributeScheme(
                            name='n3',
                            type='types.Real',
                            description='Polyhedron four-digit side specificer #3',
                        ),
                        AttributeScheme(
                            name='n4',
                            type='types.Real',
                            description='Polyhedron four-digit side specificer #4',
                        ),
                        AttributeScheme(
                            name='n5',
                            type='types.Real',
                            description='Polyhedron four-digit side specificer #5',
                        ),
                        AttributeScheme(
                            name='n6',
                            type='types.Real',
                            description='Polyhedron four-digit side specificer #6',
                        ),
                    ],
                ),
            ],
        ),
        ElementScheme(
            name='data',
            error='SEMANTICS_CARD_VALUE',
            mnemonic='',
            attributes=[
                AttributeScheme(
                    name='option',
                    type='data.DataOption_',
                    description='Help Me!',
                ),
            ],
            options=[
                ElementScheme(
                    name='vol',
                    mnemonic='vol',
                    attributes=[
                        AttributeScheme(
                            name='no',
                            type='types.String',
                            description='Volume calculation on/off',
                            restriction='no in {"no"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='volumes',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of cell volumes',
                        ),
                    ],
                ),
                ElementScheme(
                    name='area',
                    mnemonic='area',
                    attributes=[
                        AttributeScheme(
                            name='areas',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of surface areas',
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_0',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.RealOrJump',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.RealOrJump',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.RealOrJump',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='xx',
                            type='types.RealOrJump',
                            description="Rotation matrix xx' component",
                        ),
                        AttributeScheme(
                            name='xy',
                            type='types.RealOrJump',
                            description="Rotation matrix xy' component",
                        ),
                        AttributeScheme(
                            name='xz',
                            type='types.RealOrJump',
                            description="Rotation matrix xz' component",
                        ),
                        AttributeScheme(
                            name='yx',
                            type='types.RealOrJump',
                            description="Rotation matrix yx' component",
                        ),
                        AttributeScheme(
                            name='yy',
                            type='types.RealOrJump',
                            description="Rotation matrix yy' component",
                        ),
                        AttributeScheme(
                            name='yz',
                            type='types.RealOrJump',
                            description="Rotation matrix yz' component",
                        ),
                        AttributeScheme(
                            name='zx',
                            type='types.RealOrJump',
                            description="Rotation matrix zx' component",
                        ),
                        AttributeScheme(
                            name='zy',
                            type='types.RealOrJump',
                            description="Rotation matrix zy' component",
                        ),
                        AttributeScheme(
                            name='zz',
                            type='types.RealOrJump',
                            description="Rotation matrix zz' component",
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.IntegerOrJump',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_1',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.RealOrJump',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.RealOrJump',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.RealOrJump',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='xx',
                            type='types.RealOrJump',
                            description="Rotation matrix xx' component",
                        ),
                        AttributeScheme(
                            name='xy',
                            type='types.RealOrJump',
                            description="Rotation matrix xy' component",
                        ),
                        AttributeScheme(
                            name='xz',
                            type='types.RealOrJump',
                            description="Rotation matrix xz' component",
                        ),
                        AttributeScheme(
                            name='yx',
                            type='types.RealOrJump',
                            description="Rotation matrix yx' component",
                        ),
                        AttributeScheme(
                            name='yy',
                            type='types.RealOrJump',
                            description="Rotation matrix yy' component",
                        ),
                        AttributeScheme(
                            name='yz',
                            type='types.RealOrJump',
                            description="Rotation matrix yz' component",
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.IntegerOrJump',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_2',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.RealOrJump',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.RealOrJump',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.RealOrJump',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='xx',
                            type='types.RealOrJump',
                            description="Rotation matrix xx' component",
                        ),
                        AttributeScheme(
                            name='xy',
                            type='types.RealOrJump',
                            description="Rotation matrix xy' component",
                        ),
                        AttributeScheme(
                            name='xz',
                            type='types.RealOrJump',
                            description="Rotation matrix xz' component",
                        ),
                        AttributeScheme(
                            name='yx',
                            type='types.RealOrJump',
                            description="Rotation matrix yx' component",
                        ),
                        AttributeScheme(
                            name='yy',
                            type='types.RealOrJump',
                            description="Rotation matrix yy' component",
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.IntegerOrJump',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_3',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.RealOrJump',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.RealOrJump',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.RealOrJump',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='xx',
                            type='types.RealOrJump',
                            description="Rotation matrix xx' component",
                        ),
                        AttributeScheme(
                            name='xy',
                            type='types.RealOrJump',
                            description="Rotation matrix xy' component",
                        ),
                        AttributeScheme(
                            name='xz',
                            type='types.RealOrJump',
                            description="Rotation matrix xz' component",
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.IntegerOrJump',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_4',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.RealOrJump',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.RealOrJump',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.RealOrJump',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.IntegerOrJump',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='u',
                    mnemonic='u',
                    attributes=[
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tuple of cell numbers',
                            restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='lat',
                    mnemonic='lat',
                    attributes=[
                        AttributeScheme(
                            name='type',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tuple of lattice types',
                            restriction='filter(lambda entry: not (entry == 1 or entry == 2), type)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill',
                    mnemonic='fill',
                    attributes=[
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tuple of universe numbers',
                            restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='uran',
                    mnemonic='uran',
                    attributes=[
                        AttributeScheme(
                            name='transformations',
                            type='types.Tuple[types.Stochastic]',
                            description='Tuple of stochastic transformations',
                        ),
                    ],
                ),
                ElementScheme(
                    name='dm',
                    mnemonic='dm',
                    attributes=[
                        AttributeScheme(
                            name='zaids',
                            type='types.Tuple[types.Zaid]',
                            description='Tuple of ZAID aliases',
                        ),
                    ],
                ),
                ElementScheme(
                    name='dawwg',
                    mnemonic='dawwg',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[dawwg.DawwgOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='points',
                            mnemonic='points',
                            attributes=[
                                AttributeScheme(
                                    name='name',
                                    type='types.String',
                                    description='Cross section library',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='xsec',
                            mnemonic='xsec',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Number of sample points for each direction in each mesh',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='block',
                            mnemonic='block',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.IntegerOrJump',
                                    description='Destination of key-value pairs',
                                    restriction='setting.value in {1, 3, 5, 6}',
                                ),
                                AttributeScheme(
                                    name='options',
                                    type='types.Tuple[block.BlockOption_]',
                                    description='Dictionary of dawwg block options',
                                    optional=True,
                                ),
                            ],
                            options=[
                                ElementScheme(
                                    name='ngroup',
                                    mnemonic='ngroup',
                                    attributes=[
                                        AttributeScheme(
                                            name='value',
                                            type='types.IntegerOrJump',
                                            description='Number of energy groups',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='isn',
                                    mnemonic='isn',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Sn order',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='niso',
                                    mnemonic='niso',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Number of isotopes',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='mt',
                                    mnemonic='mt',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Number of materials',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='iquad',
                                    mnemonic='iquad',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Quadrature',
                                            restriction='setting.value in {1, 2, 3, 4, 5, 6, 7, 8, 9}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='fmmix',
                                    mnemonic='fmmix',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Read composition from LNK3DNT on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nosolv',
                                    mnemonic='nosolv',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress solver module on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noedit',
                                    mnemonic='noedit',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress edit module on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nogeod',
                                    mnemonic='nogeod',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress writing GEODST on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nomix',
                                    mnemonic='nomix',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress writing mixing on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noasg',
                                    mnemonic='noasg',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress writing ASGMAT on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nomacr',
                                    mnemonic='nomacr',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress writing MACRXS on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noslnp',
                                    mnemonic='noslnp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress writing SOLINP on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noedtt',
                                    mnemonic='noedtt',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress writing EDITIT on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noadjm',
                                    mnemonic='noadjm',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Suppress writing ADJMAC on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='lib',
                                    mnemonic='lib',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.String',
                                            description='Name of cross-section file',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='libname',
                                    mnemonic='libname',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.String',
                                            description='Cross-section file name',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='fissneut',
                                    mnemonic='fissneut',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Fission neutron flag',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='lng',
                                    mnemonic='lng',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Number of the last neutron group',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='balxs',
                                    mnemonic='balxs',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Cross-section balance control',
                                            restriction='setting.value in {-1, 0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ntichi',
                                    mnemonic='ntichi',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='MENDF fission fraction',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ievt',
                                    mnemonic='ievt',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Calculation type',
                                            restriction='setting in {0, 1, 2, 3, 4}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='isct',
                                    mnemonic='isct',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Legendre order',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ith',
                                    mnemonic='ith',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Direction/adjoint calculation control',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
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
                                ElementScheme(
                                    name='ibl',
                                    mnemonic='ibl',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Left boundary condition',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ibr',
                                    mnemonic='ibr',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Right boudary condition',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ibt',
                                    mnemonic='ibt',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Top boudary condition',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ibb',
                                    mnemonic='ibb',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Bottom  boudary condition',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ibfrnt',
                                    mnemonic='ibfrnt',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Front boudary condition',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ibback',
                                    mnemonic='ibback',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Back boudary condition',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='epsi',
                                    mnemonic='epsi',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.RealOrJump',
                                            description='Convergence precision',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='oitm',
                                    mnemonic='oitm',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Maximum outer iteration count',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nosigf',
                                    mnemonic='nosigf',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Inhibit fission multiplication on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
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
                                ElementScheme(
                                    name='diffsol',
                                    mnemonic='diffsol',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.String',
                                            description='Diffusion operator solver',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='tsasn',
                                    mnemonic='tsasn',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Sn order for lower order TSA sweeps',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='tsaepsi',
                                    mnemonic='tsaepsi',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.RealOrJump',
                                            description='Convergence criteria for TSA sweeps',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='tsaits',
                                    mnemonic='tsaits',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Maximum TSA iteration count',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='tsabeta',
                                    mnemonic='tsabeta',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.RealOrJump',
                                            description='Scattering cross-section reduction for TSA',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ptconv',
                                    mnemonic='ptconv',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Special criticality convergence scheme on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='norm',
                                    mnemonic='norm',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.RealOrJump',
                                            description='Norm',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='xsectp',
                                    mnemonic='xsectp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Cross-section print flag',
                                            restriction='setting in {0, 1, 2}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='fissrp',
                                    mnemonic='fissrp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Print fission source rate on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='sourcp',
                                    mnemonic='sourcp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Source print flag',
                                            restriction='setting in {0, 1, 2, 3}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='angp',
                                    mnemonic='angp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Print angular flux on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='balp',
                                    mnemonic='balp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Print coarse-mesh balance tables on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='raflux',
                                    mnemonic='raflux',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Prepare angular flux file on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='rmflux',
                                    mnemonic='rmflux',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Prepare flux moments file on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='avatar',
                                    mnemonic='avatar',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Prepare special XMFLUXA file on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='asleft',
                                    mnemonic='asleft',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Right-going flux at plane i',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='asrite',
                                    mnemonic='asrite',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Left-going flux at plane i',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='asbott',
                                    mnemonic='asbott',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Top-going flux at plane j',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='astop',
                                    mnemonic='astop',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Bottom-going flux at plane j',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='asfrnt',
                                    mnemonic='asfrnt',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Back-going flux at plane k',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='asback',
                                    mnemonic='asback',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Front-going flux at plane k',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='massed',
                                    mnemonic='massed',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Mass edits on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='pted',
                                    mnemonic='pted',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Edits by fine mesh on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='zned',
                                    mnemonic='zned',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Edits by zone on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='rzflux',
                                    mnemonic='rzflux',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Write a-flux file on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='rzmflux',
                                    mnemonic='rzmflux',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Write b-flux file on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='edoutf',
                                    mnemonic='edoutf',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='ASCII output files control',
                                            restriction='setting in {-3, -2, -1, 0, 1, 2, 3}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='byvolp',
                                    mnemonic='byvolp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Printed point reactions rates on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ajed',
                                    mnemonic='ajed',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Regular/adjoint edits control',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='fluxone',
                                    mnemonic='fluxone',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.IntegerOrJump',
                                            description='Flux override on/off',
                                            restriction='setting.value in {0, 1}',
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='embed',
                    mnemonic='embed',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[embed.EmbedOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='background',
                            mnemonic='background',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Background pseudo-cell number',
                                    restriction='1 <= number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
                            name='mgeoin',
                            mnemonic='mgeoin',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='Name of the input file containing the mesh description',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='meeout',
                            mnemonic='meeout',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='Name assigned to EEOUT, the elemental edit output file',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='meein',
                            mnemonic='meein',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='Name of the EEOUT results file to read',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
                            name='gmvfile',
                            mnemonic='gmvfile',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='Name of the GMV output file',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='length',
                            mnemonic='length',
                            attributes=[
                                AttributeScheme(
                                    name='factor',
                                    type='types.RealOrJump',
                                    description='Conversion factor to centimeters for all mesh dimentions',
                                    restriction='factor > 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='mcnpumfile',
                            mnemonic='mcnpumfile',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='Name of the MCNPUM output file',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='embee',
                    mnemonic='embee',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[embee.EmbeeOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='embed',
                            mnemonic='embed',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Embedded mesh universe number',
                                    restriction='0 <= number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='energy',
                            mnemonic='energy',
                            attributes=[
                                AttributeScheme(
                                    name='factor',
                                    type='types.RealOrJump',
                                    description='Multiplicative conversion factor for energy-related output',
                                    restriction='factor > 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='time',
                            mnemonic='time',
                            attributes=[
                                AttributeScheme(
                                    name='factor',
                                    type='types.RealOrJump',
                                    description='Multiplicative conversion factor for time-related output',
                                    restriction='factor > 0',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
                            name='factor',
                            mnemonic='factor',
                            attributes=[
                                AttributeScheme(
                                    name='constant',
                                    type='types.RealOrJump',
                                    description='Multiplicative constant',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='list',
                            mnemonic='list',
                            attributes=[
                                AttributeScheme(
                                    name='reactions',
                                    type='types.RealOrJump',
                                    description='List of reactions',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='mat',
                            mnemonic='mat',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Material number',
                                    restriction='0 <= number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                ElementScheme(
                    name='embeb',
                    mnemonic='embeb',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of upper energy bounds',
                        ),
                    ],
                ),
                ElementScheme(
                    name='embem',
                    mnemonic='embem',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='multipliers',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of energy multipliers',
                        ),
                    ],
                ),
                ElementScheme(
                    name='embtb',
                    mnemonic='embtb',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of upper time bounds',
                        ),
                    ],
                ),
                ElementScheme(
                    name='embtm',
                    mnemonic='embtm',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='multipliers',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of time multipliers',
                        ),
                    ],
                ),
                ElementScheme(
                    name='embdb',
                    mnemonic='embdb',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of upper dose energy bounds',
                        ),
                    ],
                ),
                ElementScheme(
                    name='embdf',
                    mnemonic='embdf',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='multipliers',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of dose energy multipliers',
                        ),
                    ],
                ),
                ElementScheme(
                    name='m',
                    mnemonic='m',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='substances',
                            type='types.Tuple[types.Substance]',
                            description='Tuple of material constituents',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[m.MOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
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
                        ElementScheme(
                            name='estep',
                            mnemonic='estep',
                            attributes=[
                                AttributeScheme(
                                    name='step',
                                    type='types.IntegerOrJump',
                                    description='Number of electron sub-step per energy step',
                                    restriction='step >= 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='hstep',
                            mnemonic='hstep',
                            attributes=[
                                AttributeScheme(
                                    name='step',
                                    type='types.IntegerOrJump',
                                    description='Number of proton sub-step per energy step',
                                    restriction='step >= 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='nlib',
                            mnemonic='nlib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default neutron table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='plib',
                            mnemonic='plib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default photoatomic table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='pnlib',
                            mnemonic='pnlib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default photonuclear table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='elib',
                            mnemonic='elib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default electron table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='hlib',
                            mnemonic='hlib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default proton table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='alib',
                            mnemonic='alib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default alpha table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='slib',
                            mnemonic='slib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default helion table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tlib',
                            mnemonic='tlib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default triton table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dlib',
                            mnemonic='dlib',
                            attributes=[
                                AttributeScheme(
                                    name='abx',
                                    type='types.String',
                                    description='Default deuteron table identifier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='cond',
                            mnemonic='cond',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.RealOrJump',
                                    description='Conduction state for EL03 electron-transport evaluation',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='refi',
                            mnemonic='refi',
                            attributes=[
                                AttributeScheme(
                                    name='refractive_index',
                                    type='types.RealOrJump',
                                    description='Refractive index constant',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='refc',
                            mnemonic='refc',
                            attributes=[
                                AttributeScheme(
                                    name='coefficents',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Cauchy coefficents',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='refs',
                            mnemonic='refs',
                            attributes=[
                                AttributeScheme(
                                    name='coefficents',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Sellmeier coefficents',
                                ),
                            ],
                        ),
                    ],
                    extra='''
    @staticmethod
    def from_formula(number: int, formulas: dict[str, float], atomic_or_weight: bool = True):
        """
        Generates ``M`` from INP.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            atomic_or_weight: Atomtic/Weight fraction true/false flag.

        Returns:
            ``M`` object.
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
                    types.Substance(
                        zaid,
                        types.RealOrJump(
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

        material = M(types.IntegerOrJump(number), types.Tuple(substances))
        material.comment = tuple(comments)

        return material
    ''',
                ),
                ElementScheme(
                    name='mt',
                    mnemonic='mt',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='identifier',
                            type='types.String',
                            description='Corresponding S(α,β) identifier',
                        ),
                    ],
                ),
                ElementScheme(
                    name='mx',
                    mnemonic='mx',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='zaids',
                            type='types.Tuple[types.Zaid]',
                            description='Zaid substitutions for particles',
                        ),
                    ],
                ),
                ElementScheme(
                    name='otfdb',
                    mnemonic='otfdb',
                    attributes=[
                        AttributeScheme(
                            name='zaids',
                            type='types.Tuple[types.Zaid]',
                            description='Identifiers for the broadening tables',
                        ),
                    ],
                ),
                ElementScheme(
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
                ElementScheme(
                    name='nonu',
                    mnemonic='nonu',
                    attributes=[
                        AttributeScheme(
                            name='settings',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tuple of fission settings',
                            restriction='filter(lambda entry: not (entry == 0 or entry == 1 or entry == 2), settings)',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='awtab',
                    mnemonic='awtab',
                    attributes=[
                        AttributeScheme(
                            name='weight_ratios',
                            type='types.Tuple[types.Substance]',
                            description='Tuple of atomic weight ratios',
                        ),
                    ],
                ),
                ElementScheme(
                    name='xs',
                    mnemonic='xs',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='weight_ratios',
                            type='types.Tuple[types.Substance]',
                            description='Tuple of atomic weight ratios',
                        ),
                    ],
                ),
                ElementScheme(
                    name='void',
                    mnemonic='void',
                    attributes=[
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tuple of cell numbers',
                            restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
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
                            type='types.IntegerOrJump',
                            description='Total number of energy groups for all kinds of particle',
                            restriction='igm >= 0',
                        ),
                        AttributeScheme(
                            name='iplt',
                            type='types.IntegerOrJump',
                            description='Weight windows usage indicator',
                            restriction='iplt == 0 or iplt == 1 or iplt == 2',
                        ),
                        AttributeScheme(
                            name='iab',
                            type='types.IntegerOrJump',
                            description='Adjoint biasing for adjoint problems contorls',
                            restriction='iab == 0 or iab == 1 or iab == 2',
                        ),
                        AttributeScheme(
                            name='icw',
                            type='types.IntegerOrJump',
                            description='Name of the reference cell for generated weight windows',
                        ),
                        AttributeScheme(
                            name='fnw',
                            type='types.RealOrJump',
                            description='Normalization value for generated weight windows',
                        ),
                        AttributeScheme(
                            name='rim',
                            type='types.RealOrJump',
                            description='Generated weight windows compression limit',
                        ),
                    ],
                ),
                ElementScheme(
                    name='drxs',
                    mnemonic='drxs',
                    attributes=[
                        AttributeScheme(
                            name='zaids',
                            type='types.Tuple[types.Zaid]',
                            description='Tuple of ZAID aliases',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='mode',
                    mnemonic='mode',
                    attributes=[
                        AttributeScheme(
                            name='particles',
                            type='types.Tuple[types.Designator]',
                            description='Tuple of particle designators',
                        ),
                    ],
                ),
                # REGEX
                ElementScheme(
                    name='phys_0',
                    mnemonic='phys:n',
                    attributes=[
                        AttributeScheme(
                            name='emax',
                            type='types.RealOrJump',
                            description='Upper limit for neutron energy',
                        ),
                        AttributeScheme(
                            name='emcnf',
                            type='types.RealOrJump',
                            description='Analog energy limit',
                        ),
                        AttributeScheme(
                            name='iunr',
                            type='types.RealOrJump',
                            description='Unresolved resonanace controls',
                            restriction='iunr in {0, 1}',
                        ),
                        AttributeScheme(
                            name='coilf',
                            type='types.RealOrJump',
                            description='Light-ion and heavy-ion recoil and NCIA control',
                        ),
                        AttributeScheme(
                            name='cutn',
                            type='types.IntegerOrJump',
                            description='Table-based physics cutoff controls',
                        ),
                        AttributeScheme(
                            name='ngam',
                            type='types.IntegerOrJump',
                            description='Secondary photon production controls',
                            restriction='ngam in {0, 1, 2}',
                        ),
                        AttributeScheme(
                            name='i_int_model',
                            type='types.IntegerOrJump',
                            description='Treataement of nuclear interactions controls',
                            restriction='i_int_model in {-1, 0, 1, 2}',
                        ),
                        AttributeScheme(
                            name='i_els_model',
                            type='types.IntegerOrJump',
                            description='Treatment of nuclear elastic scattering controls',
                            restriction='i_els_model in {-1, 0}',
                        ),
                    ],
                ),
                # REGEX
                ElementScheme(
                    name='phys_1',
                    mnemonic='phys:p',
                    attributes=[
                        AttributeScheme(
                            name='emcpf',
                            type='types.RealOrJump',
                            description='Upper energy limit for photon treatment',
                        ),
                        AttributeScheme(
                            name='ides',
                            type='types.IntegerOrJump',
                            description='Generation of elections by photon controls',
                            restriction='isinstance(types.Jump, ides) and ides in {0, 1}',
                        ),
                        AttributeScheme(
                            name='nocoh',
                            type='types.IntegerOrJump',
                            description='Coherent Thomson scattering controls',
                            restriction='isinstance(types.Jump, nocoh) and nocoh in {0, 1}',
                        ),
                        AttributeScheme(
                            name='ispn',
                            type='types.IntegerOrJump',
                            description='Photonuclear particle production controls',
                            restriction='isinstance(types.Jump, ispn) and ispn in {-1, 0, 1}',
                        ),
                        AttributeScheme(
                            name='nodop',
                            type='types.IntegerOrJump',
                            description='Photon Doppler energy broadening controls',
                            restriction='isinstance(types.Jump, nodop) and nodop in {0, 1}',
                        ),
                        AttributeScheme(
                            name='fism',
                            type='types.IntegerOrJump',
                            description='Selection of photofission method controls',
                            restriction='isinstance(types.Jump, fism) and fism in {0, 1}',
                        ),
                    ],
                ),
                # REGEX
                ElementScheme(
                    name='phys_2',
                    mnemonic='phys:e',
                    attributes=[
                        AttributeScheme(
                            name='emax',
                            type='types.RealOrJump',
                            description='Upper limit for electron energy',
                        ),
                        AttributeScheme(
                            name='ides',
                            type='types.IntegerOrJump',
                            description='Photon electron production controls',
                            restriction='ides in {0, 1}',
                        ),
                        AttributeScheme(
                            name='iphot',
                            type='types.IntegerOrJump',
                            description='Electron photon production controls',
                            restriction='iphot in {0, 1}',
                        ),
                        AttributeScheme(
                            name='ibad',
                            type='types.IntegerOrJump',
                            description='Bremsstrahlung angular distribution method controls',
                            restriction='ibad in {0, 1}',
                        ),
                        AttributeScheme(
                            name='istrg',
                            type='types.IntegerOrJump',
                            description='Electron continuous-energy straggling controls',
                            restriction='istrg in {0, 1}',
                        ),
                        AttributeScheme(
                            name='bnum',
                            type='types.RealOrJump',
                            description='Bremsstrahlung photon production controls',
                        ),
                        AttributeScheme(
                            name='xnum',
                            type='types.RealOrJump',
                            description='Sampling of electron-induced x-rays controls',
                            restriction='xnum >= 0',
                        ),
                        AttributeScheme(
                            name='rnok',
                            type='types.IntegerOrJump',
                            description='Knock-on electron creation controls',
                            restriction='rnok >= 0',
                        ),
                        AttributeScheme(
                            name='enum',
                            type='types.IntegerOrJump',
                            description='Photon-induced secondary electron creation controls',
                            restriction='enum >= 0',
                        ),
                        AttributeScheme(
                            name='numb',
                            type='types.IntegerOrJump',
                            description='Bremsstrahlung electron creation controls',
                            restriction='i_mcs_model >= 0',
                        ),
                        AttributeScheme(
                            name='i_mcs_model',
                            type='types.IntegerOrJump',
                            description='Choice of Coulomb scattering model controls',
                            restriction='i_mcs_model in {-1, 0}',
                        ),
                        AttributeScheme(
                            name='efac',
                            type='types.RealOrJump',
                            description='Stopping power energy spacing controls',
                            restriction='0.8 <= efac <= 0.99',
                        ),
                        AttributeScheme(
                            name='electron_method_boundary',
                            type='types.RealOrJump',
                            description='Single-event transport start sontrols',
                        ),
                        AttributeScheme(
                            name='ckvnum',
                            type='types.RealOrJump',
                            description='Crenkov photon emission scalar',
                            restriction='0 <= ckvnum < 1',
                        ),
                    ],
                ),
                # REGEX
                ElementScheme(
                    name='phys_3',
                    mnemonic='phys:h',
                    attributes=[
                        AttributeScheme(
                            name='emax',
                            type='types.RealOrJump',
                            description='Upper proton energy limit',
                        ),
                        AttributeScheme(
                            name='ean', type='types.RealOrJump', description='Analog energy limit'
                        ),
                        AttributeScheme(
                            name='tabl',
                            type='types.RealOrJump',
                            description='Table-based physics cutoff',
                            restriction='tabl == -1 or tabl >= 0',
                        ),
                        AttributeScheme(
                            name='istrg',
                            type='types.IntegerOrJump',
                            description='Charged-particle straggling controls',
                            restriction='istrg in {0, 1}',
                        ),
                        AttributeScheme(
                            name='recl',
                            type='types.RealOrJump',
                            description='Light ion recoil control',
                            restriction='0 <= recl <= 1',
                        ),
                        AttributeScheme(
                            name='i_mcs_model',
                            type='types.IntegerOrJump',
                            description='Choice of Coulomb scattering model controls',
                            restriction='i_mcs_model in {-1, 0, 1, 2}',
                        ),
                        AttributeScheme(
                            name='i_int_model',
                            type='types.IntegerOrJump',
                            description='Treatment of nuclear interactions controls',
                            restriction='i_int_model in {-1, 0, 1, 2}',
                        ),
                        AttributeScheme(
                            name='i_els_model',
                            type='types.IntegerOrJump',
                            description='Treatment of nuclear elastic scattering controls',
                            restriction='i_els_model in {-1, 0}',
                        ),
                        AttributeScheme(
                            name='efac',
                            type='types.RealOrJump',
                            description='Stopping power energy spacing',
                            restriction='0.8 <= efac <= 0.99',
                        ),
                        AttributeScheme(
                            name='ckvnum',
                            type='types.RealOrJump',
                            description='Crenkov photon emission scalar',
                            restriction='0 <= ckvnum < 1',
                        ),
                        AttributeScheme(
                            name='drp',
                            type='types.RealOrJump',
                            description='Lower energy delta-ray cutoff',
                            restriction='drp >= 0 or drp == -1',
                        ),
                    ],
                ),
                # REGEX
                ElementScheme(
                    name='phys_4',
                    mnemonic='phys',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='emax',
                            type='types.RealOrJump',
                            description='Upper energy limit',
                        ),
                        AttributeScheme(
                            name='istrg',
                            type='types.IntegerOrJump',
                            description='Charged-particle straggling controls',
                            restriction='istrg in {0, 1}',
                        ),
                        AttributeScheme(
                            name='xmunum',
                            type='types.IntegerOrJump',
                            description='Selection of muonic x-ray controls',
                            restriction='xmunum in {-1, 1}',
                        ),
                        AttributeScheme(
                            name='xmugam',
                            type='types.RealOrJump',
                            description='Probability for emitting k-shell photon',
                        ),
                        AttributeScheme(
                            name='i_mcs_model',
                            type='types.IntegerOrJump',
                            description='Choice of Coulomb scattering model controls',
                            restriction='i_mcs_model in {-1, 0, 1, 2}',
                        ),
                        AttributeScheme(
                            name='i_int_model',
                            type='types.IntegerOrJump',
                            description='Treatment of nuclear interactions controls',
                            restriction='i_int_model in {-1, 0, 1, 2}',
                        ),
                        AttributeScheme(
                            name='i_els_model',
                            type='types.IntegerOrJump',
                            description='Treatment of nuclear elastic scattering controls',
                            restriction='i_els_model in {-1, 0}',
                        ),
                        AttributeScheme(
                            name='efac',
                            type='types.RealOrJump',
                            description='Stopping power energy spacing',
                            restriction='0.8 <= efac <= 0.99',
                        ),
                        AttributeScheme(
                            name='ckvnum',
                            type='types.RealOrJump',
                            description='Crenkov photon emission scalar',
                            restriction='0 <= ckvnum < 1',
                        ),
                        AttributeScheme(
                            name='drp',
                            type='types.RealOrJump',
                            description='Lower energy delta-ray cutoff',
                            restriction='drp >= 0 or drp == -1',
                        ),
                    ],
                ),
                ElementScheme(
                    name='act',
                    mnemonic='act',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[act.ActOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
                            name='thresh',
                            mnemonic='thresh',
                            attributes=[
                                AttributeScheme(
                                    name='fraction',
                                    type='types.RealOrJump',
                                    description='Fraction of highest-amplitude discrete delayed-gamma lines retained',
                                    restriction='0 <= fraction <= 1',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dnbais',
                            mnemonic='dnbais',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Maximum number of neutrons generated per reaction',
                                    restriction='0 <= count <= 10',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='nap',
                            mnemonic='nap',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Number of activation products',
                                    restriction='0 <= count',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dneb',
                            mnemonic='dneb',
                            attributes=[
                                AttributeScheme(
                                    name='biases',
                                    type='types.Tuple[types.Bias]',
                                    description='Delayed neutron energy biases',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dgeb',
                            mnemonic='dgeb',
                            attributes=[
                                AttributeScheme(
                                    name='biases',
                                    type='types.Tuple[types.Bias]',
                                    description='Delayed neutron energy biases',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='pecut',
                            mnemonic='pecut',
                            attributes=[
                                AttributeScheme(
                                    name='cutoff',
                                    type='types.RealOrJump',
                                    description='Delayed-gamma energy cutoff',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='hlcut',
                            mnemonic='hlcut',
                            attributes=[
                                AttributeScheme(
                                    name='cutoff',
                                    type='types.RealOrJump',
                                    description='Spontaneous-decay half-life threshold',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                ElementScheme(
                    name='cut',
                    mnemonic='cut',
                    attributes=[
                        AttributeScheme(
                            name='time_cutoff',
                            type='types.RealOrJump',
                            description='Time cutoff in shakes',
                        ),
                        AttributeScheme(
                            name='energy_cutoff',
                            type='types.RealOrJump',
                            description='Lower energy cutoff',
                        ),
                        AttributeScheme(
                            name='weight_cutoff1',
                            type='types.RealOrJump',
                            description='Weight cutoff #1',
                        ),
                        AttributeScheme(
                            name='weight_cutoff2',
                            type='types.RealOrJump',
                            description='Weight cutoff #2',
                        ),
                        AttributeScheme(
                            name='source_weight',
                            type='types.RealOrJump',
                            description='Minimum source weight',
                        ),
                    ],
                ),
                ElementScheme(
                    name='elpt',
                    mnemonic='elpt',
                    attributes=[
                        AttributeScheme(
                            name='cutoffs',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of cell lower energy cutoffs',
                        ),
                    ],
                ),
                ElementScheme(
                    name='thtme',
                    mnemonic='thtme',
                    attributes=[
                        AttributeScheme(
                            name='times',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of times when thermal temperatures are specified',
                            restriction='filter(lambda entry: not (entry <= 99), times)',
                        ),
                    ],
                ),
                ElementScheme(
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
                ElementScheme(
                    name='lca',
                    mnemonic='lca',
                    attributes=[
                        AttributeScheme(
                            name='ielas',
                            type='types.IntegerOrJump',
                            description='Elastic scattering controls',
                            restriction='ielas == 0 or ielas == 1 or ielas == 2',
                        ),
                        AttributeScheme(
                            name='ipreg',
                            type='types.IntegerOrJump',
                            description='pre-equilibrium model',
                            restriction='ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3',
                        ),
                        AttributeScheme(
                            name='iexisa',
                            type='types.IntegerOrJump',
                            description='Model choice controls',
                            restriction='iexisa == 0 or iexisa == 1 or iexisa == 2',
                        ),
                        AttributeScheme(
                            name='ichoic',
                            type='types.IntegerOrJump',
                            description='ISABEL intranuclear cascade model control',
                        ),
                        AttributeScheme(
                            name='jcoul',
                            type='types.IntegerOrJump',
                            description='Coulomb barrier for incident charged particle controls',
                            restriction='jcoul == 0 or jcoul == 1',
                        ),
                        AttributeScheme(
                            name='nexite',
                            type='types.IntegerOrJump',
                            description='Subtract nuclear recoil energy to get excitation energy',
                            restriction='nexite == 0 or nexite == 1',
                        ),
                        AttributeScheme(
                            name='npidk',
                            type='types.IntegerOrJump',
                            description='Cutoff interact/terminate control',
                            restriction='npidk == 0 or npidk == 1',
                        ),
                        AttributeScheme(
                            name='noact',
                            type='types.IntegerOrJump',
                            description='Particle transport settings',
                            restriction='noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2',
                        ),
                        AttributeScheme(
                            name='icem',
                            type='types.IntegerOrJump',
                            description='Choose alternative physics model',
                            restriction='icem == 0 or icem == 1 or icem == 2',
                        ),
                        AttributeScheme(
                            name='ilaq',
                            type='types.IntegerOrJump',
                            description='Choose light ion and nucleon physics modules',
                            restriction='ilaq == 0 or ilaq == 1',
                        ),
                        AttributeScheme(
                            name='nevtype',
                            type='types.IntegerOrJump',
                            description='Choose number of evaporation particles for GEM2',
                        ),
                    ],
                ),
                ElementScheme(
                    name='lcb',
                    mnemonic='lcb',
                    attributes=[
                        AttributeScheme(
                            name='flenb1',
                            type='types.RealOrJump',
                            description='Kinetic energy for nucleons CEM/Bertini/INCL',
                        ),
                        AttributeScheme(
                            name='flenb2',
                            type='types.RealOrJump',
                            description='Kinetic energy for nucleons LAQGSM03.03',
                        ),
                        AttributeScheme(
                            name='flenb3',
                            type='types.RealOrJump',
                            description='Kinetic energy for pions CEM/Bertini/INCL',
                        ),
                        AttributeScheme(
                            name='flenb4',
                            type='types.RealOrJump',
                            description='Kinetic energy for pions LAQGSM03.03',
                        ),
                        AttributeScheme(
                            name='flenb5',
                            type='types.RealOrJump',
                            description='Kinetic energy for nucleons ISABEL',
                        ),
                        AttributeScheme(
                            name='flenb6',
                            type='types.RealOrJump',
                            description='Kinetic energy for appropriate model',
                        ),
                        AttributeScheme(
                            name='cotfe',
                            type='types.RealOrJump',
                            description='Cutoff kinetic energy for particle escape',
                        ),
                        AttributeScheme(
                            name='film0',
                            type='types.RealOrJump',
                            description='Maximum correction allowed for masss-energy balancing',
                        ),
                    ],
                ),
                ElementScheme(
                    name='lcc',
                    mnemonic='lcc',
                    attributes=[
                        AttributeScheme(
                            name='stincl',
                            type='types.RealOrJump',
                            description='Rescaling factor of the cascade duration',
                        ),
                        AttributeScheme(
                            name='v0incl',
                            type='types.RealOrJump',
                            description='Potential depth',
                        ),
                        AttributeScheme(
                            name='xfoisaincl',
                            type='types.RealOrJump',
                            description='Maximum impact parameter for Pauli blocking',
                        ),
                        AttributeScheme(
                            name='npaulincl',
                            type='types.IntegerOrJump',
                            description='Pauli blocking parameter setting',
                            restriction='npaulincl == 0 or npaulincl == -1 or npaulincl == 1',
                        ),
                        AttributeScheme(
                            name='nosurfincl',
                            type='types.IntegerOrJump',
                            description='Difuse nuclear surface based on Wood-Saxon density setting',
                            restriction='xfoisaincl == -2 or xfoisaincl == -1 or xfoisaincl == 0 or xfoisaincl == 1',
                        ),
                        AttributeScheme(
                            name='ecutincl',
                            type='types.RealOrJump',
                            description='Bertini model energy below this energy',
                        ),
                        AttributeScheme(
                            name='ebankincl',
                            type='types.RealOrJump',
                            description='INCL bank particles below this energy',
                        ),
                        AttributeScheme(
                            name='ebankabia',
                            type='types.RealOrJump',
                            description='ABLA bank particles below this energy',
                        ),
                    ],
                ),
                ElementScheme(
                    name='lea',
                    mnemonic='lea',
                    attributes=[
                        AttributeScheme(
                            name='ipht',
                            type='types.IntegerOrJump',
                            description='Generation of de-excitation photons setting',
                            restriction='ipht.value in {0, 1}',
                        ),
                        AttributeScheme(
                            name='icc',
                            type='types.IntegerOrJump',
                            description='Level of physics for PHT physics setting',
                            restriction='icc.value in {0, 1, 2, 3, 4}',
                        ),
                        AttributeScheme(
                            name='nobalc',
                            type='types.IntegerOrJump',
                            description='Mass-energy balancing in cascade setting',
                            restriction='nobalc.value in {0, 1}',
                        ),
                        AttributeScheme(
                            name='nobale',
                            type='types.IntegerOrJump',
                            description='Mass-energy balancing in evaporation setting',
                            restriction='nobale.value in {0, 1}',
                        ),
                        AttributeScheme(
                            name='ifbrk',
                            type='types.IntegerOrJump',
                            description='Mass-energy balancing in Fermi-breakup setting',
                            restriction='ifbrk.value in {0, 1}',
                        ),
                        AttributeScheme(
                            name='ilvden',
                            type='types.IntegerOrJump',
                            description='Level-density model setting',
                            restriction='ilvden.value in {0, 1, -1}',
                        ),
                        AttributeScheme(
                            name='ievap',
                            type='types.IntegerOrJump',
                            description='Evaporation and fission model setting',
                            restriction='ievap.value in {0, 1, -1, 2}',
                        ),
                        AttributeScheme(
                            name='nofis',
                            type='types.IntegerOrJump',
                            description='Fission setting',
                            restriction='nofis.value in {0, 1}',
                        ),
                    ],
                ),
                ElementScheme(
                    name='leb',
                    mnemonic='leb',
                    attributes=[
                        AttributeScheme(
                            name='yzere',
                            type='types.RealOrJump',
                            description='Y0 parameter in level-density formula for Z≤70',
                            restriction='yzere > 0',
                        ),
                        AttributeScheme(
                            name='bzere',
                            type='types.RealOrJump',
                            description='B0 parameter in level-density formula for Z≤70',
                            restriction='bzere > 0',
                        ),
                        AttributeScheme(
                            name='yzero',
                            type='types.RealOrJump',
                            description='Y0 parameter in level-density formula for Z≥71',
                            restriction='yzero > 0',
                        ),
                        AttributeScheme(
                            name='bzero',
                            type='types.RealOrJump',
                            description='B0 parameter in level-density formula for Z≥70',
                            restriction='bzero > 0',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fmult',
                    mnemonic='fmult',
                    attributes=[
                        AttributeScheme(
                            name='zaid',
                            type='types.Zaid',
                            description='Nuclide for which data are entered',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[fmult.FmultOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='sfnu',
                            mnemonic='sfnu',
                            attributes=[
                                AttributeScheme(
                                    name='distribution',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='V bar for or of cumulative distribution the sampling spontaneous fission',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='width',
                            mnemonic='width',
                            attributes=[
                                AttributeScheme(
                                    name='width',
                                    type='types.RealOrJump',
                                    description='Width for sampling spontaneous fission',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='sfyield',
                            mnemonic='sfyield',
                            attributes=[
                                AttributeScheme(
                                    name='fission_yield',
                                    type='types.RealOrJump',
                                    description='Spontaneous fission yield',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='watt',
                            mnemonic='watt',
                            attributes=[
                                AttributeScheme(
                                    name='a',
                                    type='types.RealOrJump',
                                    description='Watt energy spectrum parameters a',
                                ),
                                AttributeScheme(
                                    name='b',
                                    type='types.RealOrJump',
                                    description='Watt energy spectrum parameters b',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='method',
                            mnemonic='method',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.IntegerOrJump',
                                    description='Gaussian sampling algorithm setting',
                                    restriction='setting.value in {0, 1, 3, 5, 6, 7}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='data',
                            mnemonic='data',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.IntegerOrJump',
                                    description='Sampling method setting',
                                    restriction='setting.value in {0, 1, 2, 3}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='shift',
                            mnemonic='shift',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.IntegerOrJump',
                                    description='Shift method setting',
                                    restriction='setting.value in {0, 1, 2, 3, 4}',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='tropt',
                    mnemonic='tropt',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[tropt.TroptOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
                            name='genxs',
                            mnemonic='genxs',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='Cross section generation setting',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='unc',
                    mnemonic='unc',
                    attributes=[
                        AttributeScheme(
                            name='settings',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tuple of uncollided secondary settings',
                            restriction='filter(lambda entry: not (entry.value in {0, 1}), settings)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='cosyp',
                    mnemonic='cosyp',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.IntegerOrJump',
                            description='Prefix number of the COSY map files',
                        ),
                        AttributeScheme(
                            name='axsh',
                            type='types.IntegerOrJump',
                            description='Horiztonal axis orientation',
                            restriction='axsh.value in {1, 2, 3}',
                        ),
                        AttributeScheme(
                            name='axsv',
                            type='types.IntegerOrJump',
                            description='Vertical axis orientation',
                            restriction='axsv.value in {1, 2, 3}',
                        ),
                        AttributeScheme(
                            name='emaps',
                            type='types.Tuple[types.RealOrJump]',
                            description='Tuple of operating beam energies',
                        ),
                    ],
                ),
                ElementScheme(
                    name='cosy',
                    mnemonic='cosy',
                    attributes=[
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tuple of COSY map numbers',
                        ),
                    ],
                ),
                ElementScheme(
                    name='bfld',
                    mnemonic='bfld',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='kind',
                            type='types.String',
                            description='Magnetic field type',
                            restriction='type in {"const", "quad", "quadff"}',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[bfld.BfldOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='field',
                            mnemonic='field',
                            attributes=[
                                AttributeScheme(
                                    name='strength_gradient',
                                    type='types.RealOrJump',
                                    description='Magnetic field strength/gradient',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='vec',
                            mnemonic='vec',
                            attributes=[
                                AttributeScheme(
                                    name='vector',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Direction of mangentic field or plane corresponding to the x-axis of the quadrapole',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='maxdeflc',
                            mnemonic='maxdeflc',
                            attributes=[
                                AttributeScheme(
                                    name='angle',
                                    type='types.RealOrJump',
                                    description='Maximum deflection angles',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='maxstep',
                            mnemonic='maxstep',
                            attributes=[
                                AttributeScheme(
                                    name='size',
                                    type='types.RealOrJump',
                                    description='Maximum step size',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='axs',
                            mnemonic='axs',
                            attributes=[
                                AttributeScheme(
                                    name='vector',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Direction of the cosines of the quadropole beam axis',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ffedges',
                            mnemonic='ffedges',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Surface numbers to apply field fringe edges',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='refpnt',
                            mnemonic='refpnt',
                            attributes=[
                                AttributeScheme(
                                    name='point',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Point anywhere on the quadrapole beam',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='bflcl',
                    mnemonic='bflcl',
                    attributes=[
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tuple of BFLD map numbers',
                        ),
                    ],
                ),
                ElementScheme(
                    name='sdef',
                    mnemonic='sdef',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[sdef.SdefOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='cel',
                            mnemonic='cel',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Cell number',
                                    restriction='0 <= number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='sur',
                            mnemonic='sur',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Surface number',
                                    restriction='0 <= number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='erg_0',
                            mnemonic='erg',
                            attributes=[
                                AttributeScheme(
                                    name='energy',
                                    type='types.RealOrJump',
                                    description='Kinetic energy',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='erg_1',
                            mnemonic='erg',
                            attributes=[
                                AttributeScheme(
                                    name='energy',
                                    type='types.DistributionNumber',
                                    description='Kinetic energy',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tme_0',
                            mnemonic='tme',
                            attributes=[
                                AttributeScheme(
                                    name='time',
                                    type='types.RealOrJump',
                                    description='Time in shakes',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tme_1',
                            mnemonic='tme',
                            attributes=[
                                AttributeScheme(
                                    name='time',
                                    type='types.EmbeddedDistributionNumber',
                                    description='Time in shakes',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dir_0',
                            mnemonic='dir',
                            attributes=[
                                AttributeScheme(
                                    name='cosine',
                                    type='types.RealOrJump',
                                    description='Cosine of the angle between VEC and particle',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dir_1',
                            mnemonic='dir',
                            attributes=[
                                AttributeScheme(
                                    name='cosine',
                                    type='types.DistributionNumber',
                                    description='Cosine of the angle between VEC and particle',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='vec',
                            mnemonic='vec',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.RealOrJump',
                                    description='Reference vector for DIR x-component',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.RealOrJump',
                                    description='Reference vector for DIR y-component',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.RealOrJump',
                                    description='Reference vector for DIR z-component',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='nrm',
                            mnemonic='nrm',
                            attributes=[
                                AttributeScheme(
                                    name='sign',
                                    type='types.IntegerOrJump',
                                    description='Sign of the surface normal',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='pos',
                            mnemonic='pos',
                            attributes=[
                                AttributeScheme(
                                    name='vector',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Reference point for position sampling in vector notation',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rad_0',
                            mnemonic='rad',
                            attributes=[
                                AttributeScheme(
                                    name='radial_distance',
                                    type='types.RealOrJump',
                                    description='Radial distance fo the position from POS or AXS',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rad_1',
                            mnemonic='rad',
                            attributes=[
                                AttributeScheme(
                                    name='radial_distance',
                                    type='types.DistributionNumber',
                                    description='Radial distance fo the position from POS or AXS',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ext',
                            mnemonic='ext',
                            attributes=[
                                AttributeScheme(
                                    name='distance_cosine',
                                    type='types.RealOrJump',
                                    description='Distance for POS along AXS or Cosine of angle from AXS',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='axs',
                            mnemonic='axs',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.RealOrJump',
                                    description='Reference vector for EXT and RAD x-component',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.RealOrJump',
                                    description='Reference vector for EXT and RAD y-component',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.RealOrJump',
                                    description='Reference vector for EXT and RAD z-component',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='x',
                            mnemonic='x',
                            attributes=[
                                AttributeScheme(
                                    name='x_coordinate',
                                    type='types.RealOrJump',
                                    description='X-cordinate of position',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='y',
                            mnemonic='y',
                            attributes=[
                                AttributeScheme(
                                    name='y_coordinate',
                                    type='types.RealOrJump',
                                    description='Y-cordinate of position',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='z',
                            mnemonic='z',
                            attributes=[
                                AttributeScheme(
                                    name='z_coordinate',
                                    type='types.RealOrJump',
                                    description='Z-cordinate of position',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ccc',
                            mnemonic='ccc',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Cookie-cutter cell number',
                                    restriction='0 <= number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ara',
                            mnemonic='ara',
                            attributes=[
                                AttributeScheme(
                                    name='area',
                                    type='types.RealOrJump',
                                    description='Area of surface',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='wgt',
                            mnemonic='wgt',
                            attributes=[
                                AttributeScheme(
                                    name='weight',
                                    type='types.RealOrJump',
                                    description='Particle weight',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tr_0',
                            mnemonic='tr',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Particle weight',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tr_1',
                            mnemonic='tr',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Particle weight',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='eff',
                            mnemonic='eff',
                            attributes=[
                                AttributeScheme(
                                    name='criterion',
                                    type='types.RealOrJump',
                                    description='Rejection efficiency criterion for position sampling',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='par',
                            mnemonic='par',
                            attributes=[
                                AttributeScheme(
                                    name='kind',
                                    type='types.String',
                                    description='Source particle type',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dat',
                            mnemonic='dat',
                            attributes=[
                                AttributeScheme(
                                    name='month',
                                    type='types.IntegerOrJump',
                                    description='Month for cosmic-ray & background sources',
                                    restriction='1 <= month <= 12',
                                ),
                                AttributeScheme(
                                    name='day',
                                    type='types.IntegerOrJump',
                                    description='Day for cosmic-ray & background sources',
                                    restriction='1 <= day <= 31',
                                ),
                                AttributeScheme(
                                    name='year',
                                    type='types.IntegerOrJump',
                                    description='Year for cosmic-ray & background sources',
                                    restriction='1 <= year <= 9999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='loc',
                            mnemonic='loc',
                            attributes=[
                                AttributeScheme(
                                    name='latitude',
                                    type='types.RealOrJump',
                                    description='Latitude for cosmic source',
                                    restriction='-90 <= latitude <= 90',
                                ),
                                AttributeScheme(
                                    name='longitude',
                                    type='types.RealOrJump',
                                    description='Longitude for cosmic source',
                                    restriction='-180 <= longitude <= 180',
                                ),
                                AttributeScheme(
                                    name='altitude',
                                    type='types.RealOrJump',
                                    description='Altitude for cosmic source',
                                    restriction='0 <= altitude',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='bem',
                            mnemonic='bem',
                            attributes=[
                                AttributeScheme(
                                    name='exn',
                                    type='types.RealOrJump',
                                    description='Normalized beam emittance parameter for x coordinates',
                                ),
                                AttributeScheme(
                                    name='eyn',
                                    type='types.RealOrJump',
                                    description='Normalized beam emittance parameter for x coordinates',
                                ),
                                AttributeScheme(
                                    name='bml',
                                    type='types.RealOrJump',
                                    description='Distance from the aperture to the spot',
                                    restriction='bml >= 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='bap',
                            mnemonic='bap',
                            attributes=[
                                AttributeScheme(
                                    name='ba1',
                                    type='types.RealOrJump',
                                    description='Beam aperture half-width in the x transverse direction',
                                ),
                                AttributeScheme(
                                    name='ba2',
                                    type='types.RealOrJump',
                                    description='Beam aperture half-width in the y transverse direction',
                                ),
                                AttributeScheme(
                                    name='u',
                                    type='types.RealOrJump',
                                    description='Unused, arrbirary value',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='si_0',
                    mnemonic='si',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='option',
                            type='types.String',
                            description='Information kind setting',
                        ),
                        AttributeScheme(
                            name='information',
                            type='types.Tuple[types.DistributionNumber]',
                            description='Particle source information',
                        ),
                    ],
                ),
                ElementScheme(
                    name='si_1',
                    mnemonic='si',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='option',
                            type='types.String',
                            description='Information kind setting',
                        ),
                        AttributeScheme(
                            name='information',
                            type='types.Tuple[types.RealOrJump]',
                            description='Particle source information',
                        ),
                    ],
                ),
                ElementScheme(
                    name='sp_0',
                    mnemonic='sp',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='option',
                            type='types.String',
                            description='Probability kind setting',
                            restriction='option in {"d", "c", "v", "w"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='probabilities',
                            type='types.Tuple[types.RealOrJump]',
                            description='Particle source probabilities',
                            restriction='filter(lambda entry: not (0 <= entry <= 1), probabilities)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='sp_1',
                    mnemonic='sp',
                    attributes=[
                        AttributeScheme(
                            name='function',
                            type='types.IntegerOrJump',
                            description='Built-in function designator',
                            restriction='function in {-2, -3, -4, -5, -6, -7, -21, -31, -41}',
                        ),
                        AttributeScheme(
                            name='a',
                            type='types.RealOrJump',
                            description='Built-in function parameter #1',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.RealOrJump',
                            description='Built-in function parameter #2',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='sb_0',
                    mnemonic='sb',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='option',
                            type='types.String',
                            description='Bias kind setting',
                            restriction='option in {"d", "c", "v", "w"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='biases',
                            type='types.Tuple[types.RealOrJump]',
                            description='Particle source biases',
                        ),
                    ],
                ),
                ElementScheme(
                    name='sb_1',
                    mnemonic='sb',
                    attributes=[
                        AttributeScheme(
                            name='function',
                            type='types.IntegerOrJump',
                            description='Built-in function designator',
                            restriction='function in {-2, -3, -4, -5, -6, -7, -21, -31, -41}',
                        ),
                        AttributeScheme(
                            name='a',
                            type='types.RealOrJump',
                            description='Built-in function parameter #1',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.RealOrJump',
                            description='Built-in function parameter #2',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='ds_0',
                    mnemonic='ds',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='option',
                            type='types.String',
                            description='Dependent variable setting',
                            restriction='option in {"h", "l", "s"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='js',
                            type='types.Tuple[types.RealOrJump]',
                            description='Depdented source dependent variables',
                        ),
                    ],
                ),
                ElementScheme(
                    name='ds_1',
                    mnemonic='ds',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        # t
                        AttributeScheme(
                            name='ijs',
                            type='types.Tuple[types.IndependentDependent]',
                            description='Dependent source independent & dependent variables',
                        ),
                    ],
                ),
                ElementScheme(
                    name='ds_2',
                    mnemonic='ds',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        # q
                        AttributeScheme(
                            name='vss',
                            type='types.Tuple[types.IndependentDependent]',
                            description='Dependent source independent & dependent variables',
                        ),
                    ],
                ),
                ElementScheme(
                    name='sc',
                    mnemonic='sc',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='1 <= suffix <= 999',
                        ),
                        AttributeScheme(
                            name='comment',
                            type='types.Tuple[types.String]',
                            description='source comment',
                        ),
                    ],
                ),
                ElementScheme(
                    name='ssw',
                    mnemonic='ssw',
                    attributes=[
                        AttributeScheme(
                            name='surfaces',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Problem surfaces',
                        ),
                        AttributeScheme(
                            name='cells',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Problem cells',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[ssw.SswOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='sym',
                            mnemonic='sym',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.IntegerOrJump',
                                    description='Symmetric option flag',
                                    restriction='setting in {0, 1, 2}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='pty',
                            mnemonic='pty',
                            attributes=[
                                AttributeScheme(
                                    name='tracks',
                                    type='types.Tuple[types.Designator]',
                                    description='Tracks to record',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='cel',
                            mnemonic='cel',
                            attributes=[
                                AttributeScheme(
                                    name='cfs',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='Cells from which KCODE neutrons are written',
                                    restriction='filter(lambda entry: not (1 <= entry <= 99_999_999),         cfs)',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='ssr',
                    mnemonic='ssr',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[ssr.SsrOption_]',
                            description='Dictionary of options',
                            optional=True,
                        )
                    ],
                    options=[
                        ElementScheme(
                            name='old',
                            mnemonic='old',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='Tuple of surface numbers from subset of surfaces on SSW card',
                                    restriction='filter(lambda entry: not (1 <= entry <= 99_999_999),         numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='cel',
                            mnemonic='cel',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='Tuple of cell from subset of cells on SSW card',
                                    restriction='filter(lambda entry: not (1 <= entry <= 99_999_999),         numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='new',
                            mnemonic='new',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='Tuple of surface numbers to start run',
                                    restriction='filter(lambda entry: not (1 <= entry <= 99_999_999),         numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='pty',
                            mnemonic='pty',
                            attributes=[
                                AttributeScheme(
                                    name='particles',
                                    type='types.Tuple[types.Designator]',
                                    description='Tuple of designators',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='col',
                            mnemonic='col',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.IntegerOrJump',
                                    description='Collision option setting',
                                    restriction='setting.value in {-1, 0, 1}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='wgt',
                            mnemonic='wgt',
                            attributes=[
                                AttributeScheme(
                                    name='constant',
                                    type='types.RealOrJump',
                                    description='Particle weight multiplier',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tr_0',
                            mnemonic='tr',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.DistributionNumber',
                                    description='Particle weight',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tr_1',
                            mnemonic='tr',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Particle weight',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='psc',
                            mnemonic='psc',
                            attributes=[
                                AttributeScheme(
                                    name='constant',
                                    type='types.RealOrJump',
                                    description='Constant for approximation in PSC evaluation',
                                    restriction='constant >= 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='axs',
                            mnemonic='axs',
                            attributes=[
                                AttributeScheme(
                                    name='cosines',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Direction cosines defining',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ext',
                            mnemonic='ext',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.DistributionNumber',
                                    description='Distribution number for baising sampling',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='poa',
                            mnemonic='poa',
                            attributes=[
                                AttributeScheme(
                                    name='angle',
                                    type='types.RealOrJump',
                                    description='Angle within which particles accepeted for transport',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='bcw',
                            mnemonic='bcw',
                            attributes=[
                                AttributeScheme(
                                    name='radius',
                                    type='types.RealOrJump',
                                    description='Radius of cylindrical window',
                                ),
                                AttributeScheme(
                                    name='zb',
                                    type='types.RealOrJump',
                                    description='Bottom of cylindrical window',
                                    restriction='0 < zb',
                                ),
                                AttributeScheme(
                                    name='ze',
                                    type='types.RealOrJump',
                                    description='Top of cylindrical window',
                                    restriction='0 < zb < ze',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='kcode',
                    mnemonic='kcode',
                    attributes=[
                        AttributeScheme(
                            name='nsrck',
                            type='types.IntegerOrJump',
                            description='Number of source histories per cycle',
                            restriction='nsrck >= 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='rkk',
                            type='types.RealOrJump',
                            description='Initial guess of keff',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ikz',
                            type='types.IntegerOrJump',
                            description='Number of cycles to be skipped before beginning tally accumulation',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='kct',
                            type='types.IntegerOrJump',
                            description='Total number of cycles to be done',
                            restriction='kct > 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='msrk',
                            type='types.Integer',
                            description='Number of source points to allocate for',
                            restriction='msrk < 40 * nsrck',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='knrm',
                            type='types.IntegerOrJump',
                            description='Normalization of tallies setting',
                            restriction='knrm in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='mrkp',
                            type='types.IntegerOrJump',
                            description='Maximum number of cycle values on MCTAL or RUNTPE files',
                            restriction='mrkp > 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='kc8',
                            type='types.IntegerOrJump',
                            description='Number of cylces for average setting',
                            restriction='kc8 in {0, 1}',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='ksrc',
                    mnemonic='ksrc',
                    attributes=[
                        AttributeScheme(
                            name='locations',
                            type='types.Tuple[types.Location]',
                            description='Tuple of inital source points',
                        ),
                    ],
                ),
                ElementScheme(
                    name='kopts',
                    mnemonic='kopts',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[kopts.KoptsOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='blocksize',
                            mnemonic='blocksize',
                            attributes=[
                                AttributeScheme(
                                    name='ncy',
                                    type='types.IntegerOrJump',
                                    description='Number of cycles in every outer iteration',
                                    restriction='ncy >= 2',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
                            name='fmatskpt',
                            mnemonic='fmatskpt',
                            attributes=[
                                AttributeScheme(
                                    name='fmat_skip',
                                    type='types.RealOrJump',
                                    description='fmat_skip',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='fmatncyc',
                            mnemonic='fmatncyc',
                            attributes=[
                                AttributeScheme(
                                    name='fmat_ncyc',
                                    type='types.RealOrJump',
                                    description='fmat_ncyc',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='fmatspace',
                            mnemonic='fmatspace',
                            attributes=[
                                AttributeScheme(
                                    name='fmat_space',
                                    type='types.RealOrJump',
                                    description='fmat_space',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
                            name='fmatnx',
                            mnemonic='fmatnx',
                            attributes=[
                                AttributeScheme(
                                    name='fmat_nx',
                                    type='types.RealOrJump',
                                    description='fmat_nx',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='fmatny',
                            mnemonic='fmatny',
                            attributes=[
                                AttributeScheme(
                                    name='fmat_ny',
                                    type='types.RealOrJump',
                                    description='fmat_ny',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='fmatnz',
                            mnemonic='fmatnz',
                            attributes=[
                                AttributeScheme(
                                    name='fmat_nz',
                                    type='types.RealOrJump',
                                    description='fmat_nz',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='hsrc',
                    mnemonic='hsrc',
                    attributes=[
                        AttributeScheme(
                            name='x_number',
                            type='types.IntegerOrJump',
                            description='Number of mesh intervals in x direction',
                            restriction='x_number > 0',
                        ),
                        AttributeScheme(
                            name='x_minimum',
                            type='types.RealOrJump',
                            description='Minimum x-value for mesh',
                        ),
                        AttributeScheme(
                            name='x_maximum',
                            type='types.RealOrJump',
                            description='Maximum x-value for mesh',
                        ),
                        AttributeScheme(
                            name='y_number',
                            type='types.IntegerOrJump',
                            description='Number of mesh intervals in y direction',
                            restriction='y_number > 0',
                        ),
                        AttributeScheme(
                            name='y_minimum',
                            type='types.RealOrJump',
                            description='Minimum y-value for mesh',
                        ),
                        AttributeScheme(
                            name='y_maximum',
                            type='types.RealOrJump',
                            description='Maximum y-value for mesh',
                        ),
                        AttributeScheme(
                            name='z_number',
                            type='types.IntegerOrJump',
                            description='Number of mesh intervals in z direction',
                            restriction='z_number > 0',
                        ),
                        AttributeScheme(
                            name='z_minimum',
                            type='types.RealOrJump',
                            description='Minimum z-value for mesh',
                        ),
                        AttributeScheme(
                            name='z_maximum',
                            type='types.RealOrJump',
                            description='Maximum z-value for mesh',
                        ),
                    ],
                ),
                ElementScheme(
                    name='f_0',
                    mnemonic='f',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999 and suffix % 10 in {1, 2, 4, 6, 7}',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='problems',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Problem numbers of surface or cell',
                        ),
                        AttributeScheme(
                            name='t',
                            type='types.String',
                            description='Notation to make bin values cumulative',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='f_1',
                    mnemonic='f',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999 and suffix % 10 == 5',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='spheres',
                            type='types.Tuple[types.Sphere]',
                            description='Detector points',
                        ),
                        AttributeScheme(
                            name='nd',
                            type='types.String',
                            description='Total/average specified surfaces/cells option',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='f_2',
                    mnemonic='f',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999 and suffix % 10 == 5',
                        ),
                        AttributeScheme(
                            name='a',
                            type='types.String',
                            description='Letter',
                            restriction='a in {"x", "y", "z"}',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='rings',
                            type='types.Tuple[types.Ring]',
                            description='Detector points',
                        ),
                        AttributeScheme(
                            name='nd',
                            type='types.String',
                            description='Total/average specified surfaces/cells option',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fip',
                    mnemonic='fip',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999 and suffix % 10 == 5',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='x1',
                            type='types.RealOrJump',
                            description='Pinhole center x-coordinate',
                        ),
                        AttributeScheme(
                            name='y1',
                            type='types.RealOrJump',
                            description='Pinhole center y-coordinate',
                        ),
                        AttributeScheme(
                            name='z1',
                            type='types.RealOrJump',
                            description='Pinhole center z-coordinate',
                        ),
                        AttributeScheme(
                            name='ro',
                            type='types.RealOrJump',
                            description='Pinhole exclusion radius',
                            restriction='ro == 0',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.RealOrJump',
                            description='Reference direction x-coordinate',
                        ),
                        AttributeScheme(
                            name='y2',
                            type='types.RealOrJump',
                            description='Reference direction y-coordinate',
                        ),
                        AttributeScheme(
                            name='z2',
                            type='types.RealOrJump',
                            description='Reference direction z-coordinate',
                        ),
                        AttributeScheme(
                            name='f1',
                            type='types.RealOrJump',
                            description='Cylindrical collimator radius',
                            restriction='f1 >= 0',
                        ),
                        AttributeScheme(
                            name='f2',
                            type='types.RealOrJump',
                            description='Pinhole radius in the direction perpendiuclar to the reference direction',
                            restriction='f2 >= 0',
                        ),
                        AttributeScheme(
                            name='f3',
                            type='types.RealOrJump',
                            description='Distance between pinhole and and detector grid',
                            restriction='f3 >= 0',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fir',
                    mnemonic='fir',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999 and suffix % 10 == 5',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='x1',
                            type='types.RealOrJump',
                            description='Rectangular grid center x-coordinate',
                        ),
                        AttributeScheme(
                            name='y1',
                            type='types.RealOrJump',
                            description='Rectangular grid center y-coordinate',
                        ),
                        AttributeScheme(
                            name='z1',
                            type='types.RealOrJump',
                            description='Rectangular grid center z-coordinate',
                        ),
                        AttributeScheme(
                            name='ro',
                            type='types.RealOrJump',
                            description='Rectangular grid exclusion radius',
                            restriction='ro == 0',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.RealOrJump',
                            description='Reference direction x-coordinate',
                        ),
                        AttributeScheme(
                            name='y2',
                            type='types.RealOrJump',
                            description='Reference direction y-coordinate',
                        ),
                        AttributeScheme(
                            name='z2',
                            type='types.RealOrJump',
                            description='Reference direction z-coordinate',
                        ),
                        AttributeScheme(
                            name='f1',
                            type='types.RealOrJump',
                            description='Source contributions on/off',
                            restriction='f1 in {0, -1}',
                        ),
                        AttributeScheme(
                            name='f2',
                            type='types.RealOrJump',
                            description='Radial view of field',
                        ),
                        AttributeScheme(
                            name='f3',
                            type='types.RealOrJump',
                            description='Contribution offset setting',
                            restriction='f2 in {0, -1}',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fic',
                    mnemonic='fic',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999 and suffix % 10 == 5',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='x1',
                            type='types.RealOrJump',
                            description='Cylindrical grid center x-coordinate',
                        ),
                        AttributeScheme(
                            name='y1',
                            type='types.RealOrJump',
                            description='Cylindrical grid center y-coordinate',
                        ),
                        AttributeScheme(
                            name='z1',
                            type='types.RealOrJump',
                            description='Cylindrical grid center z-coordinate',
                        ),
                        AttributeScheme(
                            name='ro',
                            type='types.RealOrJump',
                            description='Cylindrical grid exclusion radius',
                            restriction='ro == 0',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.RealOrJump',
                            description='Reference direction x-coordinate',
                        ),
                        AttributeScheme(
                            name='y2',
                            type='types.RealOrJump',
                            description='Reference direction y-coordinate',
                        ),
                        AttributeScheme(
                            name='z2',
                            type='types.RealOrJump',
                            description='Reference direction z-coordinate',
                        ),
                        AttributeScheme(
                            name='f1',
                            type='types.RealOrJump',
                            description='Source contributions on/off',
                            restriction='f1 in {0, -1}',
                        ),
                        AttributeScheme(
                            name='f2',
                            type='types.RealOrJump',
                            description='Radial view of field',
                            restriction='f2 != 0',
                        ),
                        AttributeScheme(
                            name='f3',
                            type='types.RealOrJump',
                            description='Contribution offset setting',
                            restriction='f2 in {0, -1}',
                        ),
                    ],
                ),
                ElementScheme(
                    name='f_3',
                    mnemonic='f',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999 and suffix % 10 == 8',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='problems',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Problem numbers of cell',
                        ),
                        AttributeScheme(
                            name='t',
                            type='types.String',
                            description='Average tallies option',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fc',
                    mnemonic='fc',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='info',
                            type='types.String',
                            description='Title for tally in output and MCTAL file',
                        ),
                    ],
                ),
                ElementScheme(
                    name='e',
                    mnemonic='e',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Upper energy bounds for bin',
                        ),
                        AttributeScheme(
                            name='nt',
                            type='types.String',
                            description='Notation to inhibit automatic totaling',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.String',
                            description='Notation to make bin values cumulative',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='t_0',
                    mnemonic='t',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Upper time bounds for bin',
                        ),
                        AttributeScheme(
                            name='nt',
                            type='types.String',
                            description='Notation to inhibit automatic totaling',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.String',
                            description='Notation to make bin values cumulative',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='t_1',
                    mnemonic='t',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[t_1.T_1Option_]',
                            description='Data card options',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='cbeg',
                            mnemonic='cbeg',
                            attributes=[
                                AttributeScheme(
                                    name='time',
                                    type='types.RealOrJump',
                                    description='Reference starting time',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='cfrq',
                            mnemonic='cfrq',
                            attributes=[
                                AttributeScheme(
                                    name='frequency',
                                    type='types.RealOrJump',
                                    description='Frequency of cycling',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='cofi',
                            mnemonic='cofi',
                            attributes=[
                                AttributeScheme(
                                    name='time',
                                    type='types.RealOrJump',
                                    description='Dead time interval',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='coni',
                            mnemonic='coni',
                            attributes=[
                                AttributeScheme(
                                    name='time',
                                    type='types.RealOrJump',
                                    description='Alive time interval',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='csub',
                            mnemonic='csub',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Number of subdivisions to use',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='cend',
                            mnemonic='cend',
                            attributes=[
                                AttributeScheme(
                                    name='time',
                                    type='types.RealOrJump',
                                    description='Reference ending time',
                                )
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='c_0',
                    mnemonic='c',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Upper cosine bounds for bin',
                        ),
                        AttributeScheme(
                            name='t',
                            type='types.String',
                            description='Notation to provide totals',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.String',
                            description='Notation to make bin values cumulative',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='c_1',
                    mnemonic=r'[*]c',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Upper angle limit for bin',
                            restriction='bounds[-1] == 0 and max(bounds) <= 180',
                        ),
                        AttributeScheme(
                            name='t',
                            type='types.String',
                            description='Notation to provide totals',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='c',
                            type='types.String',
                            description='Notation to make bin values cumulative',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fq',
                    mnemonic='fq',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
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
                    ],
                ),
                ElementScheme(
                    name='fm',
                    mnemonic='fm',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='bins',
                            type='types.String',
                            description='Tally multiplier bins',
                            restriction='',
                        ),
                    ],
                ),
                ElementScheme(
                    name='de',
                    mnemonic='de',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='method',
                            type='types.String',
                            description='Interpolation method for energy table',
                            restriction='method in {"log", "lin"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='values',
                            type='types.Tuple[types.RealOrJump]',
                            description='Energy values',
                        ),
                    ],
                ),
                ElementScheme(
                    name='df_0',
                    mnemonic='df',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='method',
                            type='types.String',
                            description='Interpolation method for dose function table',
                            restriction='method in {"log", "lin"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='values',
                            type='types.Tuple[types.RealOrJump]',
                            description='Dose function values',
                        ),
                    ],
                ),
                ElementScheme(
                    name='df_1',
                    mnemonic='df',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[df_1.Df_1Option_]',
                            description='Dictionary of options',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='iu',
                            mnemonic='iu',
                            attributes=[
                                AttributeScheme(
                                    name='units',
                                    type='types.IntegerOrJump',
                                    description='Control units',
                                    restriction='units in {1, 2}',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='fac',
                            mnemonic='fac',
                            attributes=[
                                AttributeScheme(
                                    name='normalization',
                                    type='types.IntegerOrJump',
                                    description='Normalization factor for dose',
                                    restriction='normalization >= -3',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='ic',
                            mnemonic='ic',
                            attributes=[
                                AttributeScheme(
                                    name='function',
                                    type='types.IntegerOrJump',
                                    description='Standard dose function',
                                    restriction='function in {10, 20, 31, 32, 33, 34, 35, 40, 99}',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='int',
                            mnemonic='int',
                            attributes=[
                                AttributeScheme(
                                    name='interpolation',
                                    type='types.String',
                                    description='Energy interpolation',
                                    restriction='interpolation in {"log", "lin"}',
                                )
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='em',
                    mnemonic='em',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='multipliers',
                            type='types.Tuple[types.RealOrJump]',
                            description='Energy bin multiplier to apply',
                        ),
                    ],
                ),
                ElementScheme(
                    name='tm',
                    mnemonic='tm',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='multipliers',
                            type='types.Tuple[types.RealOrJump]',
                            description='Time bin multiplier to apply',
                        ),
                    ],
                ),
                ElementScheme(
                    name='cm',
                    mnemonic='cm',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='multipliers',
                            type='types.Tuple[types.RealOrJump]',
                            description='Cosine bin multiplier to apply',
                        ),
                    ],
                ),
                ElementScheme(
                    name='cf',
                    mnemonic='cf',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tallies for problem cell numbers to flag',
                            restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='sf',
                    mnemonic='sf',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tallies for problem surface numbers to flag',
                            restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fs',
                    mnemonic='fs',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.IntegerOrJump]',
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
                    ],
                ),
                ElementScheme(
                    name='sd',
                    mnemonic='sd',
                    attributes=[
                        AttributeScheme(
                            name='information',
                            type='types.Tuple[types.RealOrJump]',
                            description='Area, volume, or mass by segmented, surface/cell',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fu',
                    mnemonic='fu',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
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
                    ],
                ),
                ElementScheme(
                    name='ft',
                    mnemonic='ft',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='treatments',
                            type='types.String',
                            description='Tally special treatments',
                            restriction='',
                        ),
                    ],
                ),
                ElementScheme(
                    name='notrn',
                    mnemonic='notrn',
                    attributes=[],
                ),
                ElementScheme(
                    name='pert',
                    mnemonic='pert',
                    attributes=[
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
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[pert.PertOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='cell',
                            mnemonic='cell',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of cells',
                                    restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='mat',
                            mnemonic='mat',
                            attributes=[
                                AttributeScheme(
                                    name='material',
                                    type='types.IntegerOrJump',
                                    description='Material number to fill cells',
                                    restriction='0 <= material <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rho',
                            mnemonic='rho',
                            attributes=[
                                AttributeScheme(
                                    name='density',
                                    type='types.RealOrJump',
                                    description='Perturbed density',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='method',
                            mnemonic='method',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.IntegerOrJump',
                                    description='Printing and specifies setting',
                                    restriction='setting in {+1, -1, +2, -2, +3, -3}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='erg',
                            mnemonic='erg',
                            attributes=[
                                AttributeScheme(
                                    name='energy_lower_bound',
                                    type='types.RealOrJump',
                                    description='Lower bound for energy pertubation',
                                ),
                                AttributeScheme(
                                    name='energy_upper_bound',
                                    type='types.RealOrJump',
                                    description='Upper bound for energy pertubation',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rxn',
                            mnemonic='rxn',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='ENDF/B reaction number',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='kpert',
                    mnemonic='kpert',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='0 < suffix <= 10_000',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[kpert.KpertOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='cell',
                            mnemonic='cell',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of cells',
                                    restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='mat',
                            mnemonic='mat',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of materials',
                                    restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rho',
                            mnemonic='rho',
                            attributes=[
                                AttributeScheme(
                                    name='densities',
                                    type='types.Tuple[types.Zaid]',
                                    description='List of densities',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='iso',
                            mnemonic='iso',
                            attributes=[
                                AttributeScheme(
                                    name='zaids',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='List of ZAIDs for pertubation',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rxn',
                            mnemonic='rxn',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of reaction numbers for pertubation',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='erg',
                            mnemonic='erg',
                            attributes=[
                                AttributeScheme(
                                    name='energies',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='List of energies',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                ElementScheme(
                    name='ksen',
                    mnemonic='ksen',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='0 < suffix <= 999',
                        ),
                        AttributeScheme(
                            name='sen',
                            type='types.String',
                            description='Type of sensitivity',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[ksen.KsenOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='iso',
                            mnemonic='iso',
                            attributes=[
                                AttributeScheme(
                                    name='zaids',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='List of ZAIDs for pertubation',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rxn',
                            mnemonic='rxn',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of reaction numbers for pertubation',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='mt',
                            mnemonic='mt',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of reaction numbers for pertubation',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='erg',
                            mnemonic='erg',
                            attributes=[
                                AttributeScheme(
                                    name='energies',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='List of energies',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ein',
                            mnemonic='ein',
                            attributes=[
                                AttributeScheme(
                                    name='energies',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='List of ranges for incident energies',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='legendre',
                            mnemonic='legendre',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Order of Legendre moments to calculate sensitivities',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='cos',
                            mnemonic='cos',
                            attributes=[
                                AttributeScheme(
                                    name='cosines',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Range of direction-change cosines',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                ElementScheme(
                    name='fmesh',
                    mnemonic='fmesh',
                    attributes=[
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
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[fmesh.FmeshOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
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
                        ElementScheme(
                            name='origin',
                            mnemonic='origin',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.RealOrJump',
                                    description='Origin x coordinate',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.RealOrJump',
                                    description='Origin y coordinate',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.RealOrJump',
                                    description='Origin z coordinate',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='axs',
                            mnemonic='axs',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.RealOrJump',
                                    description='Cylindrical mesh axis vector x component',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.RealOrJump',
                                    description='Cylindrical mesh axis vector y component',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.RealOrJump',
                                    description='Cylindrical mesh axis vector z component',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='vec',
                            mnemonic='vec',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.RealOrJump',
                                    description='Plane vector x component',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.RealOrJump',
                                    description='Plane vector y component',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.RealOrJump',
                                    description='Plane vector z component',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='imesh',
                            mnemonic='imesh',
                            attributes=[
                                AttributeScheme(
                                    name='locations',
                                    type='types.RealOrJump',
                                    description='Locations of mesh points x/r for rectangular/cylindrical geometry',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='iints',
                            mnemonic='iints',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Number of mesh points x/r for rectangular/cylindrical geometry',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='jmesh',
                            mnemonic='jmesh',
                            attributes=[
                                AttributeScheme(
                                    name='locations',
                                    type='types.RealOrJump',
                                    description='Locations of mesh points y/z for rectangular/cylindrical geometry',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='jints',
                            mnemonic='jints',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Number of mesh points y/z for rectangular/cylindrical geometry',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='kmesh',
                            mnemonic='kmesh',
                            attributes=[
                                AttributeScheme(
                                    name='locations',
                                    type='types.RealOrJump',
                                    description='Locations of mesh points z/theta for rectangular/cylindrical geometry',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='kints',
                            mnemonic='kints',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Number of mesh points z/theta for rectangular/cylindrical geometry',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='emesh',
                            mnemonic='emesh',
                            attributes=[
                                AttributeScheme(
                                    name='energy',
                                    type='types.RealOrJump',
                                    description='Values of mesh points in energy',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='eints',
                            mnemonic='eints',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Number of mesh points for each mesh energy',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
                            name='tmesh',
                            mnemonic='tmesh',
                            attributes=[
                                AttributeScheme(
                                    name='time',
                                    type='types.RealOrJump',
                                    description='Values of mesh points in time',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tints',
                            mnemonic='tints',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='Number of mesh points for each mesh time',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
                            name='factor',
                            mnemonic='factor',
                            attributes=[
                                AttributeScheme(
                                    name='multiple',
                                    type='types.RealOrJump',
                                    description='Multiplicative factor for each mesh',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
                            name='tr',
                            mnemonic='tr',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Transformation applied to the mesh',
                                    restriction='1 <= number <= 999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='inc',
                            mnemonic='inc',
                            attributes=[
                                AttributeScheme(
                                    name='lower',
                                    type='types.RealOrJump',
                                    description='Collision for FMESH tally lower bound',
                                ),
                                AttributeScheme(
                                    name='upper',
                                    type='types.RealOrJump',
                                    description='Collision for FMESH tally upper bound',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
                            name='kclear',
                            mnemonic='kclear',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.IntegerOrJump',
                                    description='KCODE cycles between zeros',
                                ),
                            ],
                        ),
                    ],
                ),
                # SUBOPTION
                #    ElementScheme(
                #        name='dose',
                #        attributes=[
                #            AttributeScheme(
                #                name='ic',
                #                type='types.IntegerOrJump',
                #                description='Conversion coefficent',
                #            ),
                #            AttributeScheme(
                #                name='int',
                #                type='types.IntegerOrJump',
                #                description='Interpolation method',
                #            ),
                #            AttributeScheme(
                #                name='iu',
                #                type='types.IntegerOrJump',
                #                description='Units of resuts',
                #            ),
                #            AttributeScheme(
                #                name='fac',
                #                type='types.RealOrJump',
                #                description='Normalization of factor for dose',
                #            ),
                #        ],
                #    ),
                ElementScheme(
                    name='spdtl',
                    mnemonic='spdtl',
                    attributes=[
                        AttributeScheme(
                            name='keyword',
                            type='types.String',
                            description='keyword in {"force", "off"}',
                        ),
                    ],
                ),
                ElementScheme(
                    name='imp',
                    mnemonic='imp',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='importances',
                            type='types.Tuple[types.RealOrJump]',
                            description='Cell importance',
                        ),
                    ],
                ),
                ElementScheme(
                    name='var',
                    mnemonic='var',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[var.VarOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
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
                ElementScheme(
                    name='wwe',
                    mnemonic='wwe',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Upper energy/time bound',
                        ),
                    ],
                ),
                ElementScheme(
                    name='wwt',
                    mnemonic='wwt',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Upper time bound',
                        ),
                    ],
                ),
                ElementScheme(
                    name='wwn',
                    mnemonic='wwn',
                    attributes=[
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
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Lower weight bound',
                        ),
                    ],
                ),
                ElementScheme(
                    name='wwp',
                    mnemonic='wwp',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='wupn',
                            type='types.RealOrJump',
                            description='Multiplier to define the weight window upper limit',
                            restriction='wupn >= 2',
                        ),
                        AttributeScheme(
                            name='wsurvn',
                            type='types.RealOrJump',
                            description='Multiplier to define the maximum Russian roulette survival weight within the window',
                            restriction='1 < wsurvn',
                        ),
                        AttributeScheme(
                            name='mxspln',
                            type='types.RealOrJump',
                            description='Maximum number of integer splits',
                            restriction='1 < mxspln',
                        ),
                        AttributeScheme(
                            name='mwhere',
                            type='types.IntegerOrJump',
                            description='Controls where to check a particle’s weight',
                            restriction='mwhere.value in {-1, 0, 1}',
                        ),
                        AttributeScheme(
                            name='switchn',
                            type='types.RealOrJump',
                            description='Controls where to get the lower weight-window bounds',
                        ),
                        AttributeScheme(
                            name='mtime',
                            type='types.IntegerOrJump',
                            description='Energy/time-dependent window setting',
                        ),
                        AttributeScheme(
                            name='wnrom',
                            type='types.RealOrJump',
                            description='Weight-window normalization factor',
                        ),
                        AttributeScheme(
                            name='etsplt',
                            type='types.IntegerOrJump',
                            description='ESLPT & TSPLT split/roulette on/off',
                            restriction='etsplt.value in {0, 1}',
                        ),
                        AttributeScheme(
                            name='wu',
                            type='types.RealOrJump',
                            description='Limits the maximum lower weight-window bound for any particle, energy, or time',
                        ),
                        AttributeScheme(
                            name='nmfp',
                            type='types.RealOrJump',
                            description='Limits the maximum lower weight-window bound for any particle, energy, or time',
                        ),
                    ],
                ),
                ElementScheme(
                    name='wwg',
                    mnemonic='wwg',
                    attributes=[
                        AttributeScheme(
                            name='tally',
                            type='types.IntegerOrJump',
                            description='Problem tally number',
                            restriction='tally <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='cell',
                            type='types.IntegerOrJump',
                            description='Cell-based or mesh-based weight window generator',
                            restriction='cell <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='lower',
                            type='types.RealOrJump',
                            description='Value of the generated lower weight-window bound for cell',
                        ),
                        AttributeScheme(
                            name='j1',
                            type='types.Jump',
                            description='Placeholder jump #1',
                        ),
                        AttributeScheme(
                            name='j2',
                            type='types.Jump',
                            description='Placeholder jump #2',
                        ),
                        AttributeScheme(
                            name='j3',
                            type='types.Jump',
                            description='Placeholder jump #3',
                        ),
                        AttributeScheme(
                            name='j4',
                            type='types.Jump',
                            description='Placeholder jump #4',
                        ),
                        AttributeScheme(
                            name='setting',
                            type='types.IntegerOrJump',
                            description='Energy- or time-dependent weight window toggle',
                            restriction='setting.value in {0, 1}',
                        ),
                    ],
                ),
                ElementScheme(
                    name='wwge',
                    mnemonic='wwge',
                    attributes=[
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Upper energy bound for weight-window group to be generated',
                        ),
                    ],
                ),
                ElementScheme(
                    name='wwgt',
                    mnemonic='wwgt',
                    attributes=[
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.RealOrJump]',
                            description='Upper time bound for weight-window group to be generated',
                        ),
                    ],
                ),
                ElementScheme(
                    name='mesh',
                    mnemonic='mesh',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[mesh.MeshOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
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
                        ElementScheme(
                            name='ref',
                            mnemonic='ref',
                            attributes=[
                                AttributeScheme(
                                    name='point',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Mesh reference point',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='origin',
                            mnemonic='origin',
                            attributes=[
                                AttributeScheme(
                                    name='point',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Mesh origin point',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='axs',
                            mnemonic='axs',
                            attributes=[
                                AttributeScheme(
                                    name='vector',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Vector giving the direction of the polar axis',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='vec',
                            mnemonic='vec',
                            attributes=[
                                AttributeScheme(
                                    name='vector',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Vector giving the direction of the polar axis',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='imesh',
                            mnemonic='imesh',
                            attributes=[
                                AttributeScheme(
                                    name='vector',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Locations of the coarse meshes in the x/r directions',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='iints',
                            mnemonic='iints',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Number of fine meshes within corresponding coarse meshes in the x/r directions',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='jmesh',
                            mnemonic='jmesh',
                            attributes=[
                                AttributeScheme(
                                    name='vector',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Locations of the coarse meshes in the y/z directions',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='jints',
                            mnemonic='jints',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Number of fine meshes within corresponding coarse meshes in the y/z directions',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='kmesh',
                            mnemonic='kmesh',
                            attributes=[
                                AttributeScheme(
                                    name='vector',
                                    type='types.Tuple[types.RealOrJump]',
                                    description='Locations of the coarse meshes in the z/theta directions',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='kints',
                            mnemonic='kints',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.IntegerOrJump',
                                    description='Number of fine meshes within corresponding coarse meshes in the z/theta directions',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='esplt',
                    mnemonic='esplt',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='ratio_1',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #1',
                        ),
                        AttributeScheme(
                            name='energy_1',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #1',
                        ),
                        AttributeScheme(
                            name='ratio_2',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #2',
                        ),
                        AttributeScheme(
                            name='energy_2',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #2',
                        ),
                        AttributeScheme(
                            name='ratio_3',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #3',
                        ),
                        AttributeScheme(
                            name='energy_3',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #3',
                        ),
                        AttributeScheme(
                            name='ratio_4',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #4',
                        ),
                        AttributeScheme(
                            name='energy_4',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #4',
                        ),
                        AttributeScheme(
                            name='ratio_5',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #5',
                        ),
                        AttributeScheme(
                            name='energy_5',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #5',
                        ),
                        AttributeScheme(
                            name='ratio_6',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #6',
                        ),
                        AttributeScheme(
                            name='energy_6',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #6',
                        ),
                        AttributeScheme(
                            name='ratio_7',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #7',
                        ),
                        AttributeScheme(
                            name='energy_7',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #7',
                        ),
                        AttributeScheme(
                            name='ratio_8',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #8',
                        ),
                        AttributeScheme(
                            name='energy_8',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #8',
                        ),
                        AttributeScheme(
                            name='ratio_9',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #9',
                        ),
                        AttributeScheme(
                            name='energy_9',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #9',
                        ),
                        AttributeScheme(
                            name='ratio_10',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #10',
                        ),
                        AttributeScheme(
                            name='energy_10',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #10',
                        ),
                        AttributeScheme(
                            name='ratio_11',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #11',
                        ),
                        AttributeScheme(
                            name='energy_11',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #11',
                        ),
                        AttributeScheme(
                            name='ratio_12',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #12',
                        ),
                        AttributeScheme(
                            name='energy_12',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #12',
                        ),
                        AttributeScheme(
                            name='ratio_13',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #13',
                        ),
                        AttributeScheme(
                            name='energy_13',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #13',
                        ),
                        AttributeScheme(
                            name='ratio_14',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #14',
                        ),
                        AttributeScheme(
                            name='energy_14',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #14',
                        ),
                        AttributeScheme(
                            name='ratio_15',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #15',
                        ),
                        AttributeScheme(
                            name='energy_15',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #15',
                        ),
                        AttributeScheme(
                            name='ratio_16',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #16',
                        ),
                        AttributeScheme(
                            name='energy_16',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #16',
                        ),
                        AttributeScheme(
                            name='ratio_17',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #17',
                        ),
                        AttributeScheme(
                            name='energy_17',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #17',
                        ),
                        AttributeScheme(
                            name='ratio_18',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #18',
                        ),
                        AttributeScheme(
                            name='energy_18',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #18',
                        ),
                        AttributeScheme(
                            name='ratio_19',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #19',
                        ),
                        AttributeScheme(
                            name='energy_19',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #19',
                        ),
                        AttributeScheme(
                            name='ratio_20',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #20',
                        ),
                        AttributeScheme(
                            name='energy_20',
                            type='types.RealOrJump',
                            description='Splitting/roulette energy #20',
                        ),
                    ],
                ),
                ElementScheme(
                    name='tsplt',
                    mnemonic='tsplt',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='ratio_1',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #1',
                        ),
                        AttributeScheme(
                            name='time_1',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #1',
                        ),
                        AttributeScheme(
                            name='ratio_2',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #2',
                        ),
                        AttributeScheme(
                            name='time_2',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #2',
                        ),
                        AttributeScheme(
                            name='ratio_3',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #3',
                        ),
                        AttributeScheme(
                            name='time_3',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #3',
                        ),
                        AttributeScheme(
                            name='ratio_4',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #4',
                        ),
                        AttributeScheme(
                            name='time_4',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #4',
                        ),
                        AttributeScheme(
                            name='ratio_5',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #5',
                        ),
                        AttributeScheme(
                            name='time_5',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #5',
                        ),
                        AttributeScheme(
                            name='ratio_6',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #6',
                        ),
                        AttributeScheme(
                            name='time_6',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #6',
                        ),
                        AttributeScheme(
                            name='ratio_7',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #7',
                        ),
                        AttributeScheme(
                            name='time_7',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #7',
                        ),
                        AttributeScheme(
                            name='ratio_8',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #8',
                        ),
                        AttributeScheme(
                            name='time_8',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #8',
                        ),
                        AttributeScheme(
                            name='ratio_9',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #9',
                        ),
                        AttributeScheme(
                            name='time_9',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #9',
                        ),
                        AttributeScheme(
                            name='ratio_10',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #10',
                        ),
                        AttributeScheme(
                            name='time_10',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #10',
                        ),
                        AttributeScheme(
                            name='ratio_11',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #11',
                        ),
                        AttributeScheme(
                            name='time_11',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #11',
                        ),
                        AttributeScheme(
                            name='ratio_12',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #12',
                        ),
                        AttributeScheme(
                            name='time_12',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #12',
                        ),
                        AttributeScheme(
                            name='ratio_13',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #13',
                        ),
                        AttributeScheme(
                            name='time_13',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #13',
                        ),
                        AttributeScheme(
                            name='ratio_14',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #14',
                        ),
                        AttributeScheme(
                            name='time_14',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #14',
                        ),
                        AttributeScheme(
                            name='ratio_15',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #15',
                        ),
                        AttributeScheme(
                            name='time_15',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #15',
                        ),
                        AttributeScheme(
                            name='ratio_16',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #16',
                        ),
                        AttributeScheme(
                            name='time_16',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #16',
                        ),
                        AttributeScheme(
                            name='ratio_17',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #17',
                        ),
                        AttributeScheme(
                            name='time_17',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #17',
                        ),
                        AttributeScheme(
                            name='ratio_18',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #18',
                        ),
                        AttributeScheme(
                            name='time_18',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #18',
                        ),
                        AttributeScheme(
                            name='ratio_19',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #19',
                        ),
                        AttributeScheme(
                            name='time_19',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #19',
                        ),
                        AttributeScheme(
                            name='ratio_20',
                            type='types.RealOrJump',
                            description='Splitting/roulette ratio #20',
                        ),
                        AttributeScheme(
                            name='time_20',
                            type='types.RealOrJump',
                            description='Splitting/roulette time #20',
                        ),
                    ],
                ),
                ElementScheme(
                    name='ext',
                    mnemonic='ext',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='stretching',
                            type='types.Tuple[types.RealOrJump]',
                            description='Stretching direction for the cell',
                        ),
                    ],
                ),
                # REGEX
                #    ElementScheme(
                #        name='vect',
                #        attributes=[
                #            AttributeScheme(
                #                name='vectors',
                #                type='types.Tuple[vect.Vect_Vector]',
                #                description='Vectrors for EXT',
                #            ),
                #        ],
                #    ),
                ElementScheme(
                    name='fcl',
                    mnemonic='fcl',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='control',
                            type='types.Tuple[types.RealOrJump]',
                            description='Forced-collision control for cell',
                        ),
                    ],
                ),
                ElementScheme(
                    name='dxt',
                    mnemonic='dxt',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='spheres_1',
                            type='types.Shell',
                            description='DXTRAN spheres #1',
                        ),
                        AttributeScheme(
                            name='spheres_2',
                            type='types.Shell',
                            description='DXTRAN spheres #2',
                        ),
                        AttributeScheme(
                            name='spheres_3',
                            type='types.Shell',
                            description='DXTRAN spheres #3',
                        ),
                        AttributeScheme(
                            name='spheres_4',
                            type='types.Shell',
                            description='DXTRAN spheres #4',
                        ),
                        AttributeScheme(
                            name='spheres_5',
                            type='types.Shell',
                            description='DXTRAN spheres #5',
                        ),
                        AttributeScheme(
                            name='spheres_6',
                            type='types.Shell',
                            description='DXTRAN spheres #6',
                        ),
                        AttributeScheme(
                            name='spheres_7',
                            type='types.Shell',
                            description='DXTRAN spheres #7',
                        ),
                        AttributeScheme(
                            name='spheres_8',
                            type='types.Shell',
                            description='DXTRAN spheres #8',
                        ),
                        AttributeScheme(
                            name='spheres_9',
                            type='types.Shell',
                            description='DXTRAN spheres #9',
                        ),
                        AttributeScheme(
                            name='spheres_10',
                            type='types.Shell',
                            description='DXTRAN spheres #10',
                        ),
                        AttributeScheme(
                            name='cutoff_1',
                            type='types.RealOrJump',
                            description='Upper weight cutoff in the spheres',
                        ),
                        AttributeScheme(
                            name='cutoff_2',
                            type='types.RealOrJump',
                            description='Lower weight cutoff in the spheres',
                        ),
                        AttributeScheme(
                            name='weight',
                            type='types.RealOrJump',
                            description='Minimum photon weight',
                        ),
                    ],
                ),
                ElementScheme(
                    name='dd',
                    mnemonic='dd',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='diagnostics',
                            type='types.Tuple[types.Diagnostic]',
                            description='Detector diagnostic entries',
                        ),
                    ],
                ),
                ElementScheme(
                    name='pd',
                    mnemonic='pd',
                    attributes=[
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
                        ),
                        AttributeScheme(
                            name='probabilities',
                            type='types.Tuple[types.RealOrJump]',
                            description='Probability of contribution to DXTRAN',
                            restriction='filter(lambda entry: not (0 <= entry <= 1), probabilities)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='dxc',
                    mnemonic='dxc',
                    attributes=[
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
                        ),
                        AttributeScheme(
                            name='probabilities',
                            type='types.Tuple[types.RealOrJump]',
                            description='Probability of contribution to DXTRAN',
                            restriction='filter(lambda entry: not (0 <= entry <= 1), probabilities)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='bbrem',
                    mnemonic='bbrem',
                    attributes=[
                        AttributeScheme(
                            name='bias_1',
                            type='types.RealOrJump',
                            description='Bias factor #1 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_2',
                            type='types.RealOrJump',
                            description='Bias factor #2 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_3',
                            type='types.RealOrJump',
                            description='Bias factor #3 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_4',
                            type='types.RealOrJump',
                            description='Bias factor #4 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_5',
                            type='types.RealOrJump',
                            description='Bias factor #5 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_6',
                            type='types.RealOrJump',
                            description='Bias factor #6 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_7',
                            type='types.RealOrJump',
                            description='Bias factor #7 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_8',
                            type='types.RealOrJump',
                            description='Bias factor #8 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_9',
                            type='types.RealOrJump',
                            description='Bias factor #9 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_10',
                            type='types.RealOrJump',
                            description='Bias factor #10 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_11',
                            type='types.RealOrJump',
                            description='Bias factor #11 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_12',
                            type='types.RealOrJump',
                            description='Bias factor #12 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_13',
                            type='types.RealOrJump',
                            description='Bias factor #13 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_14',
                            type='types.RealOrJump',
                            description='Bias factor #14 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_15',
                            type='types.RealOrJump',
                            description='Bias factor #15 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_16',
                            type='types.RealOrJump',
                            description='Bias factor #16 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_17',
                            type='types.RealOrJump',
                            description='Bias factor #17 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_18',
                            type='types.RealOrJump',
                            description='Bias factor #18 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_19',
                            type='types.RealOrJump',
                            description='Bias factor #19 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_20',
                            type='types.RealOrJump',
                            description='Bias factor #20 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_21',
                            type='types.RealOrJump',
                            description='Bias factor #21 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_22',
                            type='types.RealOrJump',
                            description='Bias factor #22 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_23',
                            type='types.RealOrJump',
                            description='Bias factor #23 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_24',
                            type='types.RealOrJump',
                            description='Bias factor #24 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_25',
                            type='types.RealOrJump',
                            description='Bias factor #25 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_26',
                            type='types.RealOrJump',
                            description='Bias factor #26 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_27',
                            type='types.RealOrJump',
                            description='Bias factor #27 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_28',
                            type='types.RealOrJump',
                            description='Bias factor #28 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_29',
                            type='types.RealOrJump',
                            description='Bias factor #29 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_30',
                            type='types.RealOrJump',
                            description='Bias factor #30 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_31',
                            type='types.RealOrJump',
                            description='Bias factor #31 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_32',
                            type='types.RealOrJump',
                            description='Bias factor #32 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_33',
                            type='types.RealOrJump',
                            description='Bias factor #33 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_34',
                            type='types.RealOrJump',
                            description='Bias factor #34 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_35',
                            type='types.RealOrJump',
                            description='Bias factor #35 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_36',
                            type='types.RealOrJump',
                            description='Bias factor #36 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_37',
                            type='types.RealOrJump',
                            description='Bias factor #37 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_38',
                            type='types.RealOrJump',
                            description='Bias factor #38 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_39',
                            type='types.RealOrJump',
                            description='Bias factor #39 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_40',
                            type='types.RealOrJump',
                            description='Bias factor #40 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_41',
                            type='types.RealOrJump',
                            description='Bias factor #41 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_42',
                            type='types.RealOrJump',
                            description='Bias factor #42 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_43',
                            type='types.RealOrJump',
                            description='Bias factor #43 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_44',
                            type='types.RealOrJump',
                            description='Bias factor #44 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_45',
                            type='types.RealOrJump',
                            description='Bias factor #45 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_46',
                            type='types.RealOrJump',
                            description='Bias factor #46 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_47',
                            type='types.RealOrJump',
                            description='Bias factor #47 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_48',
                            type='types.RealOrJump',
                            description='Bias factor #48 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_49',
                            type='types.RealOrJump',
                            description='Bias factor #49 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='materials',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Material to bias',
                            restriction='filter(lambda entry: not (0 <= entry <= 99_999_999), materials)',
                        ),
                    ],
                ),
                ElementScheme(
                    name='pikmt',
                    mnemonic='pikmt',
                    attributes=[
                        AttributeScheme(
                            name='biases',
                            type='types.Tuple[types.PhotonBias]',
                            description='Biases for proton production',
                        ),
                    ],
                ),
                ElementScheme(
                    name='pwt',
                    mnemonic='pwt',
                    attributes=[
                        AttributeScheme(
                            name='weights',
                            type='types.Tuple[types.RealOrJump]',
                            description='Relative threshold weight of photons produced at neutron collisions in cell',
                        ),
                    ],
                ),
                ElementScheme(
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
                ElementScheme(
                    name='ctme',
                    mnemonic='ctme',
                    attributes=[
                        AttributeScheme(
                            name='tme',
                            type='types.IntegerOrJump',
                            description='maximum amount of minutes for Monte Carlo calculation',
                            restriction='tme >= 0',
                        ),
                    ],
                ),
                ElementScheme(
                    name='stop',
                    mnemonic='stop',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[stop.StopOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='nps',
                            mnemonic='nps',
                            attributes=[
                                AttributeScheme(
                                    name='npp',
                                    type='types.IntegerOrJump',
                                    description='Total number of histories before stop',
                                ),
                                AttributeScheme(
                                    name='npsmg',
                                    type='types.IntegerOrJump',
                                    description='Number of histories before stop',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ctme',
                            mnemonic='ctme',
                            attributes=[
                                AttributeScheme(
                                    name='tme',
                                    type='types.RealOrJump',
                                    description='Computer time before stop',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='fk',
                            mnemonic='fk',
                            attributes=[
                                AttributeScheme(
                                    name='e',
                                    type='types.IntegerOrJump',
                                    description='Tally fluctuation relative error before stop',
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
                ElementScheme(
                    name='print',
                    mnemonic='print',
                    attributes=[
                        AttributeScheme(
                            name='tables',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tables to print',
                            restriction='filter(lambda entry: not (entry.value in {10, 20, 30, 32, 35, 38, 40, 41, 44, 50, 55, 60, 62, 70, 72, 80, 85, 86, 87, 90, 95, 98, 100, 102, 110, 115, 117, 118, 120, 126, 128, 130, 140, 150, 160, 161, 162, 163, 170, 175, 178, 180, 190, 198, 200, 210, 220, -10, -20, -30, -32, -35, -38, -40, -41, -44, -50, -55, -60, -62, -70, -72, -80, -85, -86, -87, -90, -95, -98, -100, -102, -110, -115, -117, -118, -120, -126, -128, -130, -140, -150, -160, -161, -162, -163, -170, -175, -178, -180, -190, -198, -200, -210, -220}), tables)',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='talnp',
                    mnemonic='talnp',
                    attributes=[
                        AttributeScheme(
                            name='tallies',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Tallies to exclude from output',
                            restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), tallies)',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='prdmp',
                    mnemonic='prdmp',
                    attributes=[
                        AttributeScheme(
                            name='ndp',
                            type='types.IntegerOrJump',
                            description='Increment for printing tallies',
                        ),
                        AttributeScheme(
                            name='ndm',
                            type='types.IntegerOrJump',
                            description='Increment for dumping to RUNTPE file',
                        ),
                        AttributeScheme(
                            name='mct',
                            type='types.IntegerOrJump',
                            description='Controls printing of MCTAL file',
                        ),
                        AttributeScheme(
                            name='ndmp',
                            type='types.IntegerOrJump',
                            description='Maximum number of dumps on RUNTPE file',
                        ),
                        AttributeScheme(
                            name='dmmp',
                            type='types.IntegerOrJump',
                            description='Controls frequently of tally fluctuation chart',
                        ),
                    ],
                ),
                ElementScheme(
                    name='ptrac',
                    mnemonic='ptrac',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[ptrac.PtracOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='buffer',
                            mnemonic='buffer',
                            attributes=[
                                AttributeScheme(
                                    name='storage',
                                    type='types.IntegerOrJump',
                                    description='Amount of storage available for filtered events',
                                    restriction='storage > 0',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
                            name='max',
                            mnemonic='max',
                            attributes=[
                                AttributeScheme(
                                    name='events',
                                    type='types.IntegerOrJump',
                                    description='Maximum number of events to write',
                                    restriction='events != 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='meph',
                            mnemonic='meph',
                            attributes=[
                                AttributeScheme(
                                    name='events',
                                    type='types.IntegerOrJump',
                                    description='Maximum number of events per history to write',
                                    restriction='events > 0',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
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
                        ElementScheme(
                            name='event',
                            mnemonic='event',
                            attributes=[
                                AttributeScheme(
                                    name='settings',
                                    type='types.Tuple[types.String]',
                                    description='Specifies the type of events written to the PTRAC file',
                                    restriction='all(map(lambda setting: setting in {"src", "bnk", "sur", "col", "ter", "cap"}, settings))',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='filter',
                            mnemonic='filter',
                            attributes=[
                                AttributeScheme(
                                    name='variables',
                                    type='types.Tuple[types.PtracFilter]',
                                    description='MCNP6 variables for filtering',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='type',
                            mnemonic='type',
                            attributes=[
                                AttributeScheme(
                                    name='particles',
                                    type='types.Tuple[types.Designator]',
                                    description='Filters events based on one or more particle types',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='nps',
                            mnemonic='nps',
                            attributes=[
                                AttributeScheme(
                                    name='particles',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='Sets the range of particle histories for which events will be output',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='cell',
                            mnemonic='cell',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of cell numbers for filtering',
                                    restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='surface',
                            mnemonic='surface',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of surface numbers for filtering',
                                    restriction='filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tally',
                            mnemonic='tally',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.IntegerOrJump]',
                                    description='List of tally numbers for filtering',
                                    restriction='filter(lambda entry: not (entry != 0), numbers)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='value',
                            mnemonic='value',
                            attributes=[
                                AttributeScheme(
                                    name='cutoff',
                                    type='types.RealOrJump',
                                    description='Specifies tally cutoff above which history events will be written.',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='histp',
                    mnemonic='histp',
                    attributes=[
                        AttributeScheme(
                            name='lhist',
                            type='types.IntegerOrJump',
                            description='Number of words written to a HISTP file',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='cells',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Cell numbers',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='rand',
                    mnemonic='rand',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[rand.RandOption_]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='gen',
                            mnemonic='gen',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.IntegerOrJump',
                                    description='Type of pseudorandom number generator',
                                    restriction='setting.value in {1, 2, 3, 4}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='seed',
                            mnemonic='seed',
                            attributes=[
                                AttributeScheme(
                                    name='seed',
                                    type='types.IntegerOrJump',
                                    description='Random number generator seed',
                                    restriction='seed.value % 2 == 1',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='stride',
                            mnemonic='stride',
                            attributes=[
                                AttributeScheme(
                                    name='stride',
                                    type='types.IntegerOrJump',
                                    description='Number of random numbers between source particle',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='hist',
                            mnemonic='hist',
                            attributes=[
                                AttributeScheme(
                                    name='hist',
                                    type='types.IntegerOrJump',
                                    description='Starting pseudorandom number',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='dbcn',
                    mnemonic='dbcn',
                    attributes=[
                        AttributeScheme(
                            name='x1',
                            type='types.IntegerOrJump',
                            description='Obsolete; pseudorandom number for the first particle history',
                            restriction='x1 >= 0',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.IntegerOrJump',
                            description='Debug print interval',
                        ),
                        AttributeScheme(
                            name='x3',
                            type='types.IntegerOrJump',
                            description='Lower history number inclusive limit for logging',
                        ),
                        AttributeScheme(
                            name='x4',
                            type='types.IntegerOrJump',
                            description='Upper history number inclusive limit for logging',
                        ),
                        AttributeScheme(
                            name='x5',
                            type='types.IntegerOrJump',
                            description='Maximnum number of events per history for logging',
                        ),
                        AttributeScheme(
                            name='x6',
                            type='types.IntegerOrJump',
                            description='Detector/DXTRAN underflow limit',
                            restriction='50 <= x6 <= 200',
                        ),
                        AttributeScheme(
                            name='x7',
                            type='types.IntegerOrJump',
                            description='Volume and sufrace area printing on/off',
                        ),
                        AttributeScheme(
                            name='x8',
                            type='types.IntegerOrJump',
                            description='Obsolete; starting history offset',
                        ),
                        AttributeScheme(
                            name='x9',
                            type='types.IntegerOrJump',
                            description='Distance allowed between cpincident repeated-structures',
                        ),
                        AttributeScheme(
                            name='x10',
                            type='types.IntegerOrJump',
                            description='Half-life threshold for stable nuclides',
                        ),
                        AttributeScheme(
                            name='x11',
                            type='types.IntegerOrJump',
                            description='Collision event lost particle logging on/off',
                        ),
                        AttributeScheme(
                            name='x12',
                            type='types.IntegerOrJump',
                            description='Expected number of random numbers',
                        ),
                        AttributeScheme(
                            name='x13',
                            type='types.IntegerOrJump',
                            description='Obsolete; random number stride',
                        ),
                        AttributeScheme(
                            name='x14',
                            type='types.IntegerOrJump',
                            description='Obsolete; random number multiplier',
                        ),
                        AttributeScheme(
                            name='x15',
                            type='types.IntegerOrJump',
                            description='Usual selection of statistics quantities printing on/off',
                        ),
                        AttributeScheme(
                            name='x16',
                            type='types.IntegerOrJump',
                            description='History score grid accumulation scaling',
                        ),
                        AttributeScheme(
                            name='x17',
                            type='types.IntegerOrJump',
                            description='Angular treatment for secondary particles setting',
                        ),
                        AttributeScheme(
                            name='x18',
                            type='types.IntegerOrJump',
                            description='Energy-indexing alogrithm for election transport settings',
                        ),
                        AttributeScheme(
                            name='x19',
                            type='types.IntegerOrJump',
                            description='Developer; Quadratic polynomical interpolation parameter',
                        ),
                        AttributeScheme(
                            name='x20',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x21',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x22',
                            type='types.IntegerOrJump',
                            description='Unsued',
                        ),
                        AttributeScheme(
                            name='x23',
                            type='types.IntegerOrJump',
                            description='Pulse-height tally variance reducation tress setting',
                        ),
                        AttributeScheme(
                            name='x24',
                            type='types.IntegerOrJump',
                            description='Grazing contribution cutoff for surface fluxx tallies settings',
                        ),
                        AttributeScheme(
                            name='x25',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x26',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x27',
                            type='types.IntegerOrJump',
                            description='Antiparticle promotion settings',
                        ),
                        AttributeScheme(
                            name='x28',
                            type='types.IntegerOrJump',
                            description='Bank size',
                        ),
                        AttributeScheme(
                            name='x29',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x30',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x31',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x32',
                            type='types.IntegerOrJump',
                            description='GENXS behavior setting',
                        ),
                        AttributeScheme(
                            name='x33',
                            type='types.IntegerOrJump',
                            description='Additional interpolation/smoothing method for heavy ions on/off',
                        ),
                        AttributeScheme(
                            name='x34',
                            type='types.IntegerOrJump',
                            description='Developer; Muon-induced gammas bug parameter',
                        ),
                        AttributeScheme(
                            name='x35',
                            type='types.IntegerOrJump',
                            description='Slight spreading of nuclear exitation on/off',
                        ),
                        AttributeScheme(
                            name='x36',
                            type='types.IntegerOrJump',
                            description='User-provided data for muon-induced gamma rays on/off',
                        ),
                        AttributeScheme(
                            name='x37',
                            type='types.IntegerOrJump',
                            description='Mimumum of internal bremsstrahlung spectrum',
                        ),
                        AttributeScheme(
                            name='x38',
                            type='types.IntegerOrJump',
                            description='Barashenkov/Polanski data file on/off',
                        ),
                        AttributeScheme(
                            name='x39',
                            type='types.IntegerOrJump',
                            description='Default S(α,β) smoothing behavior on/off',
                        ),
                        AttributeScheme(
                            name='x40',
                            type='types.IntegerOrJump',
                            description='Developer; MCPLIB and XSDIR lines writing setting',
                        ),
                        AttributeScheme(
                            name='x41',
                            type='types.IntegerOrJump',
                            description='Developer; Phonton/election data printing setting',
                        ),
                        AttributeScheme(
                            name='x42',
                            type='types.IntegerOrJump',
                            description='Model cross section setting',
                        ),
                        AttributeScheme(
                            name='x43',
                            type='types.IntegerOrJump',
                            description='Developer; Photo form-factor interpolation setting',
                        ),
                        AttributeScheme(
                            name='x44',
                            type='types.IntegerOrJump',
                            description='Developer; Coherent scattering in isolation setting',
                        ),
                        AttributeScheme(
                            name='x45',
                            type='types.IntegerOrJump',
                            description='MCNP6/MCNPX elastic scattering method selector',
                        ),
                        AttributeScheme(
                            name='x46',
                            type='types.IntegerOrJump',
                            description='CEM-to_LAQGSM photonuclear energy boundary setting',
                        ),
                        AttributeScheme(
                            name='x47',
                            type='types.IntegerOrJump',
                            description='Cosmic-rasy spectra setting',
                        ),
                        AttributeScheme(
                            name='x48',
                            type='types.IntegerOrJump',
                            description='MCNP6 threading on/off',
                        ),
                        AttributeScheme(
                            name='x49',
                            type='types.IntegerOrJump',
                            description='Normal input checking on/off',
                        ),
                        AttributeScheme(
                            name='x50',
                            type='types.IntegerOrJump',
                            description='TFC priting setting',
                        ),
                        AttributeScheme(
                            name='x51',
                            type='types.IntegerOrJump',
                            description='Developer; Photon-induced fluoresence on/off',
                        ),
                        AttributeScheme(
                            name='x52',
                            type='types.IntegerOrJump',
                            description='Developer; Compton-induced relaxation on/off',
                        ),
                        AttributeScheme(
                            name='x53',
                            type='types.IntegerOrJump',
                            description='Photoelectric relazation data setting',
                        ),
                        AttributeScheme(
                            name='x54',
                            type='types.IntegerOrJump',
                            description='Sampling method for ENDF Law 9 setting',
                        ),
                        AttributeScheme(
                            name='x55',
                            type='types.IntegerOrJump',
                            description='Spontaneous decay integration time',
                        ),
                        AttributeScheme(
                            name='x56',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x57',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x58',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x59',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x60',
                            type='types.IntegerOrJump',
                            description='Print number of calls to each high-energy model',
                        ),
                        AttributeScheme(
                            name='x61',
                            type='types.IntegerOrJump',
                            description='Developer; models of knock-on electron angles',
                        ),
                        AttributeScheme(
                            name='x62',
                            type='types.IntegerOrJump',
                            description='Developer; single-event electrons excitation energy loss debugger',
                        ),
                        AttributeScheme(
                            name='x63',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x64',
                            type='types.IntegerOrJump',
                            description='Developer; single-event electrons angular deflaction debugger',
                        ),
                        AttributeScheme(
                            name='x65',
                            type='types.IntegerOrJump',
                            description='Developer; single-event ionization and treat deflection dubgger',
                        ),
                        AttributeScheme(
                            name='x66',
                            type='types.IntegerOrJump',
                            description='Developer; single-event bremsstrahlung photon angles setting',
                        ),
                        AttributeScheme(
                            name='x67',
                            type='types.IntegerOrJump',
                            description='Particle histories setting for detectors and DXTRAN',
                        ),
                        AttributeScheme(
                            name='x68',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x69',
                            type='types.IntegerOrJump',
                            description='LJA array size setting',
                        ),
                        AttributeScheme(
                            name='x70',
                            type='types.IntegerOrJump',
                            description='Developer; interaction models setting',
                        ),
                        AttributeScheme(
                            name='x71',
                            type='types.IntegerOrJump',
                            description='Model photonuclear capability on/off',
                        ),
                        AttributeScheme(
                            name='x72',
                            type='types.IntegerOrJump',
                            description='Log-log/linear interpolation in ELXS_MOD setting',
                        ),
                        AttributeScheme(
                            name='x73',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x74',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x75',
                            type='types.IntegerOrJump',
                            description='Print extra info for F-matrix calculation on/off',
                        ),
                        AttributeScheme(
                            name='x76',
                            type='types.IntegerOrJump',
                            description='Print array storage info after setup on/off',
                        ),
                        AttributeScheme(
                            name='x77',
                            type='types.IntegerOrJump',
                            description='Has-based cross-section serach bin number',
                        ),
                        AttributeScheme(
                            name='x78',
                            type='types.IntegerOrJump',
                            description='Developer; S(A,B) method old/new setting',
                        ),
                        AttributeScheme(
                            name='x79',
                            type='types.IntegerOrJump',
                            description='MT for absorption and fission setting',
                        ),
                        AttributeScheme(
                            name='x80',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x81',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron elastic scatter setting',
                        ),
                        AttributeScheme(
                            name='x82',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron elastic scatter setting',
                        ),
                        AttributeScheme(
                            name='x83',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron partial x-s setting',
                        ),
                        AttributeScheme(
                            name='x84',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron bremsstrahlung energy setting',
                        ),
                        AttributeScheme(
                            name='x85',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron bremsstrahlung energy setting',
                        ),
                        AttributeScheme(
                            name='x86',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron excitation setting',
                        ),
                        AttributeScheme(
                            name='x87',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron knock-on energy setting',
                        ),
                        AttributeScheme(
                            name='x88',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron knock-on energy setting',
                        ),
                        AttributeScheme(
                            name='x89',
                            type='types.IntegerOrJump',
                            description='Developer; interpolation for electron ionization x-s setting',
                        ),
                        AttributeScheme(
                            name='x90',
                            type='types.IntegerOrJump',
                            description='Mximum number of terms for Goudsmit-Saunderson distribution',
                        ),
                        AttributeScheme(
                            name='x91',
                            type='types.IntegerOrJump',
                            description='Minimum ROC curve count value',
                        ),
                        AttributeScheme(
                            name='x92',
                            type='types.IntegerOrJump',
                            description='Maximum ROC curve count value',
                        ),
                        AttributeScheme(
                            name='x93',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x94',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x95',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x96',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x97',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x98',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x99',
                            type='types.IntegerOrJump',
                            description='Unused',
                        ),
                        AttributeScheme(
                            name='x100',
                            type='types.IntegerOrJump',
                            description='Coincident-surface method old/new setting',
                        ),
                    ],
                ),
                ElementScheme(
                    name='lost',
                    mnemonic='lost',
                    attributes=[
                        AttributeScheme(
                            name='lost1',
                            type='types.IntegerOrJump',
                            description='Number of particles which can be lost before job termination',
                            restriction='lost1 >= 0',
                        ),
                        AttributeScheme(
                            name='lost2',
                            type='types.IntegerOrJump',
                            description='Maximum number of debug prints for lost particles.',
                            restriction='lost2 >= 0',
                        ),
                    ],
                ),
                ElementScheme(
                    name='idum',
                    mnemonic='idum',
                    attributes=[
                        AttributeScheme(
                            name='intergers',
                            type='types.Tuple[types.IntegerOrJump]',
                            description='Integer array',
                        ),
                    ],
                ),
                ElementScheme(
                    name='rdum',
                    mnemonic='rdum',
                    attributes=[
                        AttributeScheme(
                            name='floats',
                            type='types.Tuple[types.RealOrJump]',
                            description='Floating point array',
                        ),
                    ],
                ),
                ElementScheme(
                    name='za',
                    mnemonic='za',
                    attributes=[
                        AttributeScheme(
                            name='anything',
                            type='types.String',
                            description='Any parameters',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='zb',
                    mnemonic='zb',
                    attributes=[
                        AttributeScheme(
                            name='anything',
                            type='types.String',
                            description='Any parameters',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='zc',
                    mnemonic='zc',
                    attributes=[
                        AttributeScheme(
                            name='anything',
                            type='types.String',
                            description='Any parameters',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='zd',
                    mnemonic='zd',
                    attributes=[
                        AttributeScheme(
                            name='anything',
                            type='types.String',
                            description='Any parameters',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='files',
                    mnemonic='files',
                    attributes=[
                        AttributeScheme(
                            name='creations',
                            type='types.Tuple[types.File]',
                            description='Files to create',
                        ),
                    ],
                ),
            ],
        ),
    ],
)
