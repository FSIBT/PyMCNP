import typing


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
        can_paren: bool = False,
        can_quote: bool = False,
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
        self.can_paren: typing.Final[bool] = can_paren
        self.can_quote: typing.Final[bool] = can_quote


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
        error: str = 'SEMANTICS_OPTION',
        regex: str = '',
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
        self.regex: typing.Final[str] = regex


cards = ElementScheme(
    name='',
    mnemonic='',
    attributes=[],
    options=[
        ElementScheme(
            name='comment',
            error='SEMANTICS_CARD',
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
            error='SEMANTICS_CARD',
            mnemonic='',
            attributes=[
                AttributeScheme(
                    name='number',
                    type='types.Integer',
                    description='cell number',
                    restriction='number >= 1 and number <= 99_999_999',
                ),
                AttributeScheme(
                    name='material',
                    type='types.Integer',
                    description='cell material',
                    restriction='material >= 0 and material <= 99_999_999',
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
                    type='cell.Geometry',
                    description='cell geometry',
                    restriction='# TODO #',
                ),
                AttributeScheme(
                    name='options',
                    type='types.Tuple[cell.CellOption]',
                    description='Dictionary of options',
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
                            description='Data option particle designator',
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
                            restriction='control >= -1 and control <= 1',
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
                            restriction='probability >= 0 and probability <= 1',
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
                            restriction='setting in {0, 1, 2}',
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
                            restriction='probability >= 0 and probability <= 1',
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
                            restriction='number == 10000000000 or (number >= -9 and number <= 99_999_999)',
                        ),
                    ),
                ),
                ElementScheme(
                    name='trcl_0',
                    mnemonic='trcl',
                    regex='([*])?trcl( {types.Integer._REGEX.pattern[2:-2]})',
                    attributes=(
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            description='Star prefix',
                            restriction='prefix in {"*"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='transformation',
                            type='types.Integer',
                            description='Cell transformation number',
                            restriction='transformation >= 0 and transformation <= 999',
                        ),
                    ),
                ),
                ElementScheme(
                    name='trcl_1',
                    mnemonic='trcl',
                    regex='([*])?trcl( {types.Transformation_0._REGEX.pattern[2:-2]})',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            description='Star prefix',
                            restriction='prefix in {"*"}',
                            optional=True,
                        ),
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
                    regex='([*])?trcl( {types.Transformation_1._REGEX.pattern[2:-2]})',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            description='Star prefix',
                            restriction='prefix in {"*"}',
                            optional=True,
                        ),
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
                    regex='([*])?trcl( {types.Transformation_2._REGEX.pattern[2:-2]})',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            description='Star prefix',
                            restriction='prefix in {"*"}',
                            optional=True,
                        ),
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
                    regex='([*])?trcl( {types.Transformation_3._REGEX.pattern[2:-2]})',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            description='Star prefix',
                            restriction='prefix in {"*"}',
                            optional=True,
                        ),
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
                    regex='([*])?trcl( {types.Transformation_4._REGEX.pattern[2:-2]})',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            description='Star prefix',
                            restriction='prefix in {"*"}',
                            optional=True,
                        ),
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
                            restriction='shape in {1, 2}',
                        ),
                    ),
                ),
                ElementScheme(
                    name='fill_0',
                    mnemonic='fill',
                    regex='([*])?fill (\\S+:\\S+) (\\S+:\\S+) (\\S+:\\S+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)(?: [(]({types.Integer._REGEX.pattern[2:-2]})[)])?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            description='Star prefix',
                            restriction='prefix in {"*"}',
                            optional=True,
                        ),
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
                            # restriction='len(universes) == (i.upper - i.lower) * (j.upper - j.lower) * (k.upper - k.lower)',
                        ),
                        AttributeScheme(
                            name='m',
                            type='types.Integer',
                            description='Displacement vector origin',
                            optional=True,
                            can_paren=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_1',
                    mnemonic='fill',
                    regex='([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_0._REGEX.pattern[2:-2]}| [(]{types.Transformation_0._REGEX.pattern[2:-2]}[)])?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='universe',
                            type='types.Integer',
                            description='Cell fill universe number',
                            restriction='universe == 10000000000 or (universe >= 0 and universe <= 99_999_999)',
                        ),
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_0',
                            description='Cell fill transformation',
                            optional=True,
                            can_paren=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_2',
                    mnemonic='fill',
                    regex='([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_1._REGEX.pattern[2:-2]}| [(]{types.Transformation_1._REGEX.pattern[2:-2]}[)])?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='universe',
                            type='types.Integer',
                            description='Cell fill universe number',
                            restriction='universe == 10000000000 or (universe >= 0 and universe <= 99_999_999)',
                        ),
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_1',
                            description='Cell fill transformation',
                            optional=True,
                            can_paren=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_3',
                    mnemonic='fill',
                    regex='([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_2._REGEX.pattern[2:-2]}| [(]{types.Transformation_2._REGEX.pattern[2:-2]}[)])?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='universe',
                            type='types.Integer',
                            description='Cell fill universe number',
                            restriction='universe == 10000000000 or (universe >= 0 and universe <= 99_999_999)',
                        ),
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_2',
                            description='Cell fill transformation',
                            optional=True,
                            can_paren=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_4',
                    mnemonic='fill',
                    regex='([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_3._REGEX.pattern[2:-2]}| [(]{types.Transformation_3._REGEX.pattern[2:-2]}[)])?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='universe',
                            type='types.Integer',
                            description='Cell fill universe number',
                            restriction='universe == 10000000000 or (universe >= 0 and universe <= 99_999_999)',
                        ),
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_3',
                            description='Cell fill transformation',
                            optional=True,
                            can_paren=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_5',
                    mnemonic='fill',
                    regex='([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_4._REGEX.pattern[2:-2]}| [(]{types.Transformation_4._REGEX.pattern[2:-2]}[)])?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='universe',
                            type='types.Integer',
                            description='Cell fill universe number',
                            restriction='universe == 10000000000 or (universe >= 0 and universe <= 99_999_999)',
                        ),
                        AttributeScheme(
                            name='transformation',
                            type='types.Transformation_4',
                            description='Cell fill transformation',
                            optional=True,
                            can_paren=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill_6',
                    mnemonic='fill',
                    regex='([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]}| [(]{types.Integer._REGEX.pattern[2:-2]}[)])?',
                    attributes=(
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='universe',
                            type='types.Integer',
                            description='Cell fill universe number',
                            restriction='universe == 10000000000 or (universe >= 0 and universe <= 99_999_999)',
                        ),
                        AttributeScheme(
                            name='transformation',
                            type='types.Integer',
                            description='Cell fill transformation number',
                            restriction='transformation >= 0 and transformation <= 999',
                            optional=True,
                            can_paren=True,
                        ),
                    ),
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
                    name='tmp',
                    mnemonic='tmp',
                    attributes=(
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Thermal time index',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='temperature',
                            type='types.Tuple[types.Real]',
                            description='Temperature at time index',
                            restriction='min(map(lambda temp: temp, temperature)) > 0',
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
                            restriction='number in {1, 2, 3, 4, 5, 6}',
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
                            restriction='setting in {0, 1}',
                        ),
                    ),
                ),
            ],
        ),
        ElementScheme(
            name='surface',
            error='SEMANTICS_CARD',
            mnemonic='',
            attributes=[
                AttributeScheme(
                    name='option',
                    type='surface.SurfaceOption',
                    description='Dictionary of options',
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
            float(self.a), float(self.b), float(self.c), float(self.d)
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
        Generates ``Visualization`` from ``P_1``.

        Returns:
            ``pyvista.PolyData`` for ``P_1``
        """

        a = _visualization.Vector(self.x2 - self.x1, self.y2 - self.y1, self.z2 - self.z1)
        b = _visualization.Vector(self.x3 - self.x1, self.y3 - self.y1, self.z3 - self.z1)
        n = a * b

        vis = _visualization.Visualization.get_plane(
            float(n.x), float(n.y), float(n.z), float(n.x * self.x1) + float(n.y * self.y1) + float(n.z * self.z1)
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

        vis = _visualization.Visualization.get_plane(1, 0, 0, float(self.d))
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

        vis = _visualization.Visualization.get_plane(0, 1, 0, float(self.d))
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

        vis = _visualization.Visualization.get_plane(0, 0, 1, float(self.d))

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

        vis = _visualization.Visualization.get_sphere(float(self.r))

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

        vis = _visualization.Visualization.get_sphere(float(self.r))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, self.z))

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

        vis = _visualization.Visualization.get_sphere(float(self.r))
        vis = vis.add_translation(_visualization.Vector(self.x, 0, 0))

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

        vis = _visualization.Visualization.get_sphere(float(self.r))
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y, 0))

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

        vis = _visualization.Visualization.get_sphere(float(self.r))
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z))

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

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y, self.z))

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

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, 0, self.z))

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

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, 0))

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

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))
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

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))
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

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))

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

        vis = _visualization.Visualization.get_cone_unbounded(
            float(self.t_squared) ** (1 / 2), float(self.plusminus_1)
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, self.z))

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

        vis = _visualization.Visualization.get_cone_unbounded(
            float(self.t_squared) ** (1 / 2), float(self.plusminus_1)
        )
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, self.z))

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

        vis = _visualization.Visualization.get_cone_unbounded(
            float(self.t_squared) ** (1 / 2), float(self.plusminus_1)
        )
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, self.z))

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

        vis = _visualization.Visualization.get_cone_unbounded(
            float(self.t_squared) ** (1 / 2), float(self.plusminus_1)
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, 0, 0))

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

        vis = _visualization.Visualization.get_cone_unbounded(
            float(self.t_squared) ** (1 / 2), float(self.plusminus_1)
        )
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y, 0))

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

        vis = _visualization.Visualization.get_cone_unbounded(
            float(self.t_squared) ** (1 / 2), float(self.plusminus_1)
        )
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z))

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

        vis = _visualization.Visualization.get_torus(float(self.b), float(self.c), float(self.a))
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, self.z))

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

        vis = _visualization.Visualization.get_torus(float(self.b), float(self.c), float(self.a))
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, self.z))

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

        vis = _visualization.Visualization.get_torus(float(self.b), float(self.c), float(self.a))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, self.z))

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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='r2',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #2 radius',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x3',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #3 x component',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='r3',
                            type='types.Real',
                            description='X-axisymmetric point-defined surface point #3 radius',
                            optional=True,
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='r2',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #2 radius',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='y3',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #3 y component',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='r3',
                            type='types.Real',
                            description='Y-axisymmetric point-defined surface point #3 radius',
                            optional=True,
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='r2',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #2 radius',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='z3',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #3 z component',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='r3',
                            type='types.Real',
                            description='Z-axisymmetric point-defined surface point #3 radius',
                            optional=True,
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

        v = _visualization.Vector(self.vx, self.vy, self.vz)
        a1 = _visualization.Vector(self.a1x, self.a1y, self.a1z)
        a2 = _visualization.Vector(self.a2x, self.a2y, self.a2z)
        a3 = _visualization.Vector(self.a3x, self.a3y, self.a3z)
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='zmax',
                            type='types.Real',
                            description='Parallelepiped z termini maximum',
                            optional=True,
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
            float(self.xmin),
            float(self.xmax),
            float(self.ymin),
            float(self.ymax),
            float(self.zmin),
            float(self.zmax),
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

        vis = _visualization.Visualization.get_sphere(float(self.r))
        vis = vis.add_translation(
            _visualization.Vector(self.vx, self.vy, self.vz)
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

        v = _visualization.Vector(self.vx, self.vy, self.vz)
        h = _visualization.Vector(self.hx, self.hy, self.hz)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cylinder_circle(h.norm(), self.r)
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='s2',
                            type='types.Real',
                            description='Hexagonal prism facet #2 vector y component',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='s3',
                            type='types.Real',
                            description='Hexagonal prism facet #2 vector z component',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='t1',
                            type='types.Real',
                            description='Hexagonal prism facet #3 vector x component',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='t2',
                            type='types.Real',
                            description='Hexagonal prism facet #3 vector y component',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='t3',
                            type='types.Real',
                            description='Hexagonal prism facet #3 vector z component',
                            optional=True,
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Rhp``.

        Returns:
            ``pyvista.PolyData`` for ``Rhp``
        """

        v = _visualization.Vector(self.vx, self.vy, self.vz)
        h = _visualization.Vector(self.hx, self.hy, self.hz)
        r = _visualization.Vector(self.r1, self.r2, self.r3)
        s = _visualization.Vector(self.s1, self.s2, self.s3)
        t = _visualization.Vector(self.t1, self.t2, self.t3)

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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='v2z',
                            type='types.Real',
                            description='Elliptical cylinder minor axis vector z component',
                            optional=True,
                        ),
                    ],
                    extra='''
    def draw(self):
        """
        Generates ``Visualization`` from ``Rec``.

        Returns:
            ``pyvista.PolyData`` for ``Rec``
        """

        v = _visualization.Vector(self.vx, self.vy, self.vz)
        h = _visualization.Vector(self.hx, self.hy, self.hz)
        v1 = _visualization.Vector(self.v1x, self.v1y, self.v1z)
        v2 = _visualization.Vector(self.v2x, self.v2y, self.v2z)

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

        h = _visualization.Vector(self.hx, self.hy, self.hz)

        cross = h * _visualization.Vector(0, 0, 1)
        angle = h & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cone_truncated(
            h.norm(), float(self.r1), float(self.r2)
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(
            _visualization.Vector(self.vx, self.vy, self.vz)
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

        v1 = _visualization.Vector(self.v1x, self.v1y, self.v1z)
        v2 = _visualization.Vector(self.v2x, self.v2y, self.v2z)

        if self.rm > 0:
            center = _visualization.Vector(
                (v2 - v1).x / 2 + v1.x, (v2 - v1).y / 2 + v1.y, (v2 - v1).z / 2 + v1.z
            )
            major_length = float(self.rm)
            minor_length = 2 * (((major_length / 2) ** 2 - ((v2 - v1).norm() / 2) ** 2) ** 0.5)
            cross = (v2 - v1) * _visualization.Vector(1, 0, 0)
            angle = (v2 - v1) & _visualization.Vector(1, 0, 0)
        elif self.rm < 0:
            center = v1
            major_length = v2.norm()
            minor_length = -float(self.rm)
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

        v = _visualization.Vector(self.vx, self.vy, self.vz)
        v1 = _visualization.Vector(self.v1x, self.v1y, self.v1z)
        v2 = _visualization.Vector(self.v2x, self.v2y, self.v2z)
        v3 = _visualization.Vector(self.v3x, self.v3y, self.v3z)

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
            error='SEMANTICS_CARD',
            mnemonic='',
            attributes=[
                AttributeScheme(
                    name='option',
                    type='data.DataOption',
                    description='Help Me!',
                ),
            ],
            options=[
                ElementScheme(
                    name='vol',
                    mnemonic='vol',
                    regex='vol(?: (no))?((?: {types.Real._REGEX.pattern[2:-2]})+?)',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
                            description='Tuple of surface areas',
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_0',
                    regex='([*])?tr(\\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='xx',
                            type='types.Real',
                            description="Rotation matrix xx' component",
                        ),
                        AttributeScheme(
                            name='xy',
                            type='types.Real',
                            description="Rotation matrix xy' component",
                        ),
                        AttributeScheme(
                            name='xz',
                            type='types.Real',
                            description="Rotation matrix xz' component",
                        ),
                        AttributeScheme(
                            name='yx',
                            type='types.Real',
                            description="Rotation matrix yx' component",
                        ),
                        AttributeScheme(
                            name='yy',
                            type='types.Real',
                            description="Rotation matrix yy' component",
                        ),
                        AttributeScheme(
                            name='yz',
                            type='types.Real',
                            description="Rotation matrix yz' component",
                        ),
                        AttributeScheme(
                            name='zx',
                            type='types.Real',
                            description="Rotation matrix zx' component",
                        ),
                        AttributeScheme(
                            name='zy',
                            type='types.Real',
                            description="Rotation matrix zy' component",
                        ),
                        AttributeScheme(
                            name='zz',
                            type='types.Real',
                            description="Rotation matrix zz' component",
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.Integer',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_1',
                    regex='([*])?tr(\\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='xx',
                            type='types.Real',
                            description="Rotation matrix xx' component",
                        ),
                        AttributeScheme(
                            name='xy',
                            type='types.Real',
                            description="Rotation matrix xy' component",
                        ),
                        AttributeScheme(
                            name='xz',
                            type='types.Real',
                            description="Rotation matrix xz' component",
                        ),
                        AttributeScheme(
                            name='yx',
                            type='types.Real',
                            description="Rotation matrix yx' component",
                        ),
                        AttributeScheme(
                            name='yy',
                            type='types.Real',
                            description="Rotation matrix yy' component",
                        ),
                        AttributeScheme(
                            name='yz',
                            type='types.Real',
                            description="Rotation matrix yz' component",
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.Integer',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_2',
                    regex='([*])?tr(\\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='xx',
                            type='types.Real',
                            description="Rotation matrix xx' component",
                        ),
                        AttributeScheme(
                            name='xy',
                            type='types.Real',
                            description="Rotation matrix xy' component",
                        ),
                        AttributeScheme(
                            name='xz',
                            type='types.Real',
                            description="Rotation matrix xz' component",
                        ),
                        AttributeScheme(
                            name='yx',
                            type='types.Real',
                            description="Rotation matrix yx' component",
                        ),
                        AttributeScheme(
                            name='yy',
                            type='types.Real',
                            description="Rotation matrix yy' component",
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.Integer',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_3',
                    regex='([*])?tr(\\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?',
                    mnemonic='tr',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='xx',
                            type='types.Real',
                            description="Rotation matrix xx' component",
                        ),
                        AttributeScheme(
                            name='xy',
                            type='types.Real',
                            description="Rotation matrix xy' component",
                        ),
                        AttributeScheme(
                            name='xz',
                            type='types.Real',
                            description="Rotation matrix xz' component",
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.Integer',
                            description='Coordinate system setting',
                            restriction='system == -1 or system == 1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tr_4',
                    mnemonic='tr',
                    regex='([*])?tr(\\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
                        ),
                        AttributeScheme(
                            name='x',
                            type='types.Real',
                            description='Displacement vector x component',
                        ),
                        AttributeScheme(
                            name='y',
                            type='types.Real',
                            description='Displacement vector y component',
                        ),
                        AttributeScheme(
                            name='z',
                            type='types.Real',
                            description='Displacement vector z component',
                        ),
                        AttributeScheme(
                            name='system',
                            type='types.Integer',
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
                            type='types.Tuple[types.Integer]',
                            description='Tuple of cell numbers',
                        ),
                    ],
                ),
                ElementScheme(
                    name='lat',
                    mnemonic='lat',
                    attributes=[
                        AttributeScheme(
                            name='type',
                            type='types.Tuple[types.Integer]',
                            description='Tuple of lattice types',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fill',
                    mnemonic='fill',
                    attributes=[
                        AttributeScheme(
                            name='numbers',
                            type='types.Tuple[types.Integer]',
                            description='Tuple of universe numbers',
                        ),
                    ],
                ),
                ElementScheme(
                    name='uran',
                    regex='uran((?: \\S+ \\S+ \\S+ \\S+)+?)',
                    mnemonic='uran',
                    attributes=[
                        AttributeScheme(
                            name='transformations',
                            type='types.Tuple[uran.Stochastic]',
                            description='Tuple of stochastic transformations',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='stochastic',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(name='universe', type='types.Integer', description='Universe number', restriction='0 <= universe.value <= 99_999_999'),
                                AttributeScheme(
                                    name='maximum_x',
                                    type='types.Real',
                                    description='Maximum x displacement',
                                ),
                                AttributeScheme(
                                    name='maximum_y',
                                    type='types.Real',
                                    description='Maximum y displacement',
                                ),
                                AttributeScheme(
                                    name='maximum_z',
                                    type='types.Real',
                                    description='Maximum z displacement',
                                ),
                            ],
                        )
                    ],
                ),
                ElementScheme(
                    name='dm',
                    mnemonic='dm',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
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
                            type='types.Tuple[dawwg.DawwgOption]',
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
                                    name='count',
                                    type='types.Integer',
                                    description='Number of sample points for each direction in each mesh',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='xsec',
                            mnemonic='xsec',
                            attributes=[
                                AttributeScheme(
                                    name='name',
                                    type='types.String',
                                    description='Cross section library',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='block',
                            mnemonic='block',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.Integer',
                                    description='Destination of key-value pairs',
                                    restriction='setting in {1, 3, 5, 6}',
                                ),
                                AttributeScheme(
                                    name='options',
                                    type='types.Tuple[block.BlockOption]',
                                    description='Dictionary of options',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
                                            description='Quadrature',
                                            restriction='setting in {1, 2, 3, 4, 5, 6, 7, 8, 9}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='fmmix',
                                    mnemonic='fmmix',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Read composition from LNK3DNT on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nosolv',
                                    mnemonic='nosolv',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress solver module on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noedit',
                                    mnemonic='noedit',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress edit module on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nogeod',
                                    mnemonic='nogeod',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress writing GEODST on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nomix',
                                    mnemonic='nomix',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress writing mixing on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noasg',
                                    mnemonic='noasg',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress writing ASGMAT on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='nomacr',
                                    mnemonic='nomacr',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress writing MACRXS on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noslnp',
                                    mnemonic='noslnp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress writing SOLINP on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noedtt',
                                    mnemonic='noedtt',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress writing EDITIT on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='noadjm',
                                    mnemonic='noadjm',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Suppress writing ADJMAC on/off',
                                            restriction='setting in {0, 1}',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
                                            description='Cross-section balance control',
                                            restriction='setting in {-1, 0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='ntichi',
                                    mnemonic='ntichi',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Real',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
                                            description='Inhibit fission multiplication on/off',
                                            restriction='setting in {0, 1}',
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
                                            type='types.Integer',
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
                                            type='types.Real',
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
                                            type='types.Integer',
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
                                            type='types.Real',
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
                                            type='types.Integer',
                                            description='Special criticality convergence scheme on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='norm',
                                    mnemonic='norm',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Real',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
                                            description='Print fission source rate on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
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
                                ElementScheme(
                                    name='angp',
                                    mnemonic='angp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Print angular flux on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='balp',
                                    mnemonic='balp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Print coarse-mesh balance tables on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='raflux',
                                    mnemonic='raflux',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Prepare angular flux file on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='rmflux',
                                    mnemonic='rmflux',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Prepare flux moments file on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='avatar',
                                    mnemonic='avatar',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Prepare special XMFLUXA file on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='asleft',
                                    mnemonic='asleft',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
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
                                            type='types.Integer',
                                            description='Mass edits on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='pted',
                                    mnemonic='pted',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Edits by fine mesh on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='zned',
                                    mnemonic='zned',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Edits by zone on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='rzflux',
                                    mnemonic='rzflux',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Write a-flux file on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
                                    name='rzmflux',
                                    mnemonic='rzmflux',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Write b-flux file on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
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
                                ElementScheme(
                                    name='byvolp',
                                    mnemonic='byvolp',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Printed point reactions rates on/off',
                                            restriction='setting in {0, 1}',
                                        ),
                                    ],
                                ),
                                ElementScheme(
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
                                ElementScheme(
                                    name='fluxone',
                                    mnemonic='fluxone',
                                    attributes=[
                                        AttributeScheme(
                                            name='setting',
                                            type='types.Integer',
                                            description='Flux override on/off',
                                            restriction='setting in {0, 1}',
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
                    regex='embed(\\d+)?((?: (?:{embed.EmbedOption._REGEX.pattern[2:-2]}))+?)?',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[embed.EmbedOption]',
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
                                    type='types.Integer',
                                    description='Background pseudo-cell number',
                                    restriction='number >= 1 and number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='matcell',
                            mnemonic='matcell',
                            attributes=[
                                AttributeScheme(
                                    name='pairs',
                                    type='types.Tuple[matcell.Entry]',
                                    description='Tuple of material-cell paris',
                                ),
                            ],
                            options=[
                                ElementScheme(
                                    name='entry',
                                    mnemonic='',
                                    attributes=[
                                        AttributeScheme(name='material', type='types.Integer', description='Material number', restriction='0 <= material.value <= 99_999_999'),
                                        AttributeScheme(name='cell', type='types.Integer', description='Geometry number', restriction='0 <= cell.value <= 99_999_999'),
                                    ],
                                )
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
                                    restriction='form in {"lnk3dnt", "abaqus", "mcnpum"}',
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
                                    restriction='kind in {"ascii", "binary"}',
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
                                    type='types.Real',
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
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[embee.EmbeeOption]',
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
                                    type='types.Integer',
                                    description='Embedded mesh universe number',
                                    restriction='number >= 0 and number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
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
                        ElementScheme(
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Integer',
                                    description='Material number',
                                    restriction='number >= 0 and number <= 99_999_999',
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
                                    restriction='kind in {"flux", "isotropic", "population", "reaction", "source", "track"}',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
                            description='Tuple of dose energy multipliers',
                        ),
                    ],
                ),
                ElementScheme(
                    name='m_0',
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
                            type='types.Tuple[m_0.MOption_0]',
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
                                    type='types.Integer',
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
                                    type='types.Integer',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Real]',
                                    description='Sellmeier coefficents',
                                ),
                            ],
                        ),
                    ],
                    extra='''
    @staticmethod
    def from_formula(number: int, formulas: dict[str, float], is_weight: bool = True):
        """
        Generates ``M_0`` from INP.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            is_weight: Weight (atomic) fraction true (false) flag.

        Returns:
            ``M_0`` object.
        """

        substances = []
        comments = []
        for formula, mixture_fraction in formulas.items():
            formula = molmass.Formula(formula)

            composition = formula.composition()
            for element in composition:
                compound_fraction = (
                    composition[element].fraction
                    if is_weight
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
                        types.Real(
                            (-1 if is_weight else 1)
                            * mixture_fraction
                            * compound_fraction
                            * isotropic_fraction
                        ),
                    )
                    for zaid, isotropic_fraction in zaids
                ]

                comments += subcomments
                substances += entries

        material = M_0(types.Integer(number), types.Tuple(substances))
        material.comment = tuple(comments)

        return material
    ''',
                ),
                ElementScheme(
                    name='m_1',
                    mnemonic='m',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='abx',
                            type='types.String',
                            description='Material library',
                        ),
                    ],
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
                            name='identifiers',
                            type='types.Tuple[types.String]',
                            description='Corresponding S(α,β) identifier',
                        ),
                    ],
                ),
                ElementScheme(
                    name='mx',
                    regex='mx(\\d+):(\\S+)((?: (?:{types.Zaid._REGEX.pattern[2:-2]}|j|model|0))+?)',
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
                            type='types.Tuple[types.String]',
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
                            type='types.Tuple[types.Integer]',
                            description='Tuple of fission settings',
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
                            type='types.Tuple[types.Integer]',
                            description='Tuple of cell numbers',
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
                            type='types.Integer',
                            description='Total number of energy groups for all kinds of particle',
                            restriction='igm >= 0',
                        ),
                        AttributeScheme(
                            name='iplt',
                            type='types.Integer',
                            description='Weight windows usage indicator',
                            restriction='iplt in {0, 1, 2}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='iab',
                            type='types.Integer',
                            description='Adjoint biasing for adjoint problems contorls',
                            restriction='iab in {0, 1, 2}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='icw',
                            type='types.Integer',
                            description='Name of the reference cell for generated weight windows',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='fnw',
                            type='types.Real',
                            description='Normalization value for generated weight windows',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='rim',
                            type='types.Real',
                            description='Generated weight windows compression limit',
                            optional=True,
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
                            type='types.Real',
                            description='Upper limit for neutron energy',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='emcnf',
                            type='types.Real',
                            description='Analog energy limit',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='iunr',
                            type='types.Integer',
                            description='Unresolved resonanace controls',
                            restriction='isinstance(iunr.value, types.Jump) or iunr in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='coilf',
                            type='types.Real',
                            description='Light-ion and heavy-ion recoil and NCIA control',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='cutn',
                            type='types.Integer',
                            description='Table-based physics cutoff controls',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ngam',
                            type='types.Integer',
                            description='Secondary photon production controls',
                            restriction='isinstance(ngam.value, types.Jump) or ngam in {0, 1, 2}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_int_model',
                            type='types.Integer',
                            description='Treataement of nuclear interactions controls',
                            restriction='isinstance(i_int_model.value, types.Jump) or i_int_model in {-1, 0, 1, 2, 3}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_els_model',
                            type='types.Integer',
                            description='Treatment of nuclear elastic scattering controls',
                            restriction='isinstance(i_els_model.value, types.Jump) or i_els_model in {-1, 0, 1}',
                            optional=True,
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
                            type='types.Real',
                            description='Upper energy limit for photon treatment',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ides',
                            type='types.Integer',
                            description='Generation of elections by photon controls',
                            restriction='isinstance(ides.value, types.Jump) or ides in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='nocoh',
                            type='types.Integer',
                            description='Coherent Thomson scattering controls',
                            restriction='isinstance(nocoh.value, types.Jump) or nocoh in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ispn',
                            type='types.Integer',
                            description='Photonuclear particle production controls',
                            restriction='isinstance(ispn.value, types.Jump) or ispn in {-1, 0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='nodop',
                            type='types.Integer',
                            description='Photon Doppler energy broadening controls',
                            restriction='isinstance(nodop.value, types.Jump) or nodop in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='fism',
                            type='types.Integer',
                            description='Selection of photofission method controls',
                            # restriction='isinstance(fism.value, types.Jump) or fism in {0, 1}',
                            optional=True,
                        ),
                    ],
                ),
                # REGEX
                ElementScheme(
                    name='phys_2',
                    regex='phys:e(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?(?: (\\S+))?',
                    mnemonic='phys:e',
                    attributes=[
                        AttributeScheme(
                            name='emax',
                            type='types.Real',
                            description='Upper limit for electron energy',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ides',
                            type='types.Integer',
                            description='Photon electron production controls',
                            restriction='isinstance(ides.value, types.Jump) or ides in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='iphot',
                            type='types.Integer',
                            description='Electron photon production controls',
                            restriction='isinstance(iphot.value, types.Jump) or iphot in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ibad',
                            type='types.Integer',
                            description='Bremsstrahlung angular distribution method controls',
                            restriction='isinstance(ibad.value, types.Jump) or ibad in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='istrg',
                            type='types.Integer',
                            description='Electron continuous-energy straggling controls',
                            restriction='isinstance(istrg.value, types.Jump) or istrg in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='bnum',
                            type='types.Real',
                            description='Bremsstrahlung photon production controls',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='xnum',
                            type='types.Real',
                            description='Sampling of electron-induced x-rays controls',
                            restriction='isinstance(xnum.value, types.Jump) or xnum >= 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='rnok',
                            type='types.Integer',
                            description='Knock-on electron creation controls',
                            restriction='isinstance(rnok.value, types.Jump) or rnok >= 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='enum',
                            type='types.Integer',
                            description='Photon-induced secondary electron creation controls',
                            restriction='isinstance(enum.value, types.Jump) or enum >= 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='numb',
                            type='types.Integer',
                            description='Bremsstrahlung electron creation controls',
                            restriction='isinstance(numb.value, types.Jump) or numb >= 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_mcs_model',
                            type='types.Integer',
                            description='Choice of Coulomb scattering model controls',
                            restriction='isinstance(i_mcs_model.value, types.Jump) or i_mcs_model in {-1, 0}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='efac',
                            type='types.Real',
                            description='Stopping power energy spacing controls',
                            restriction='isinstance(efac.value, types.Jump) or (efac >= 0.8 and efac <= 0.99)',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='electron_method_boundary',
                            type='types.Real',
                            description='Single-event transport start sontrols',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ckvnum',
                            type='types.Real',
                            description='Crenkov photon emission scalar',
                            restriction='isinstance(ckvnum.value, types.Jump) or ckvnum >= 0 and ckvnum < 1',
                            optional=True,
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
                            type='types.Real',
                            description='Upper proton energy limit',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ean',
                            type='types.Real',
                            description='Analog energy limit',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='tabl',
                            type='types.Real',
                            description='Table-based physics cutoff',
                            restriction='isinstance(tabl.value, types.Jump) or tabl == -1 or tabl >= 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='istrg',
                            type='types.Integer',
                            description='Charged-particle straggling controls',
                            restriction='isinstance(istrg.value, types.Jump) or istrg in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='recl',
                            type='types.Real',
                            description='Light ion recoil control',
                            restriction='isinstance(recl.value, types.Jump) or (recl >= 0 and recl <= 1)',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_mcs_model',
                            type='types.Integer',
                            description='Choice of Coulomb scattering model controls',
                            restriction='isinstance(i_mcs_model.value, types.Jump) or i_mcs_model in {-1, 0, 1, 2}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_int_model',
                            type='types.Integer',
                            description='Treatment of nuclear interactions controls',
                            restriction='isinstance(i_int_model.value, types.Jump) or i_int_model in {-1, 0, 1, 2}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_els_model',
                            type='types.Integer',
                            description='Treatment of nuclear elastic scattering controls',
                            restriction='isinstance(i_els_model.value, types.Jump) or i_els_model in {-1, 0}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='efac',
                            type='types.Real',
                            description='Stopping power energy spacing',
                            restriction='isinstance(efac.value, types.Jump) or (efac >= 0.8 and efac <= 0.99)',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ckvnum',
                            type='types.Real',
                            description='Crenkov photon emission scalar',
                            restriction='isinstance(ckvnum.value, types.Jump) or ckvnum >= 0 and ckvnum < 1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='drp',
                            type='types.Real',
                            description='Lower energy delta-ray cutoff',
                            restriction='isinstance(drp.value, types.Jump) or drp >= 0 or drp == -1',
                            optional=True,
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
                            type='types.Real',
                            description='Upper energy limit',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='istrg',
                            type='types.Integer',
                            description='Charged-particle straggling controls',
                            restriction='isinstance(istrg.value, types.Jump) or istrg in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='xmunum',
                            type='types.Integer',
                            description='Selection of muonic x-ray controls',
                            restriction='isinstance(xmunum.value, types.Jump) or xmunum in {-1, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='xmugam',
                            type='types.Real',
                            description='Probability for emitting k-shell photon',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_mcs_model',
                            type='types.Integer',
                            description='Choice of Coulomb scattering model controls',
                            restriction='isinstance(i_mcs_model.value, types.Jump) or i_mcs_model in {-1, 0, 1, 2}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_int_model',
                            type='types.Integer',
                            description='Treatment of nuclear interactions controls',
                            restriction='isinstance(i_int_model.value, types.Jump) or i_int_model in {-1, 0, 1, 2}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='i_els_model',
                            type='types.Integer',
                            description='Treatment of nuclear elastic scattering controls',
                            restriction='isinstance(i_els_model.value, types.Jump) or i_els_model in {-1, 0}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='efac',
                            type='types.Real',
                            description='Stopping power energy spacing',
                            restriction='isinstance(efac.value, types.Jump) or (efac >= 0.8 and efac <= 0.99)',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ckvnum',
                            type='types.Real',
                            description='Crenkov photon emission scalar',
                            restriction='isinstance(ckvnum.value, types.Jump) or ckvnum >= 0 and ckvnum < 1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='drp',
                            type='types.Real',
                            description='Lower energy delta-ray cutoff',
                            restriction='isinstance(drp.value, types.Jump) or drp >= 0 or drp == -1',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='act',
                    mnemonic='act',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[act.ActOption]',
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
                                    restriction='kind in {"none", "n,p,e,f,a", "all"}',
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
                                    restriction='kind in {"none", "n,p,e,f,a", "all"}',
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
                                    type='types.Real',
                                    description='Fraction of highest-amplitude discrete delayed-gamma lines retained',
                                    restriction='fraction >= 0 and fraction <= 1',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dnbais',
                            mnemonic='dnbais',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.Integer',
                                    description='Maximum number of neutrons generated per reaction',
                                    restriction='count >= 0 and count <= 10',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='nap',
                            mnemonic='nap',
                            attributes=[
                                AttributeScheme(
                                    name='count',
                                    type='types.Integer',
                                    description='Number of activation products',
                                    restriction='count >= 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dneb',
                            mnemonic='dneb',
                            attributes=[
                                AttributeScheme(
                                    name='biases',
                                    type='types.Tuple[dneb.Bias]',
                                    description='Delayed neutron energy biases',
                                ),
                            ],
                            options=[
                                ElementScheme(
                                    name='bias',
                                    mnemonic='',
                                    attributes=[
                                        AttributeScheme(
                                            name='weight',
                                            type='types.Real',
                                            description='Weight for bias',
                                        ),
                                        AttributeScheme(
                                            name='energy',
                                            type='types.Real',
                                            description='Energy boundary for bias',
                                        ),
                                    ],
                                )
                            ],
                        ),
                        ElementScheme(
                            name='dgeb',
                            mnemonic='dgeb',
                            attributes=[
                                AttributeScheme(
                                    name='biases',
                                    type='types.Tuple[dgeb.Bias]',
                                    description='Delayed neutron energy biases',
                                ),
                            ],
                            options=[
                                ElementScheme(
                                    name='bias',
                                    mnemonic='',
                                    attributes=[
                                        AttributeScheme(
                                            name='weight',
                                            type='types.Real',
                                            description='Weight for bias',
                                        ),
                                        AttributeScheme(
                                            name='energy',
                                            type='types.Real',
                                            description='Energy boundary for bias',
                                        ),
                                    ],
                                )
                            ],
                        ),
                        ElementScheme(
                            name='pecut',
                            mnemonic='pecut',
                            attributes=[
                                AttributeScheme(
                                    name='cutoff',
                                    type='types.Real',
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
                                    type='types.Real',
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
                            name='designator',
                            type='types.Designator',
                            description='Data option particle designator',
                        ),
                        AttributeScheme(
                            name='time_cutoff',
                            type='types.Real',
                            description='Time cutoff in shakes',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_cutoff',
                            type='types.Real',
                            description='Lower energy cutoff',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='weight_cutoff1',
                            type='types.Real',
                            description='Weight cutoff #1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='weight_cutoff2',
                            type='types.Real',
                            description='Weight cutoff #2',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='source_weight',
                            type='types.Real',
                            description='Minimum source weight',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='elpt',
                    mnemonic='elpt',
                    attributes=[
                        AttributeScheme(
                            name='cutoffs',
                            type='types.Tuple[types.Real]',
                            description='Tuple of cell lower energy cutoffs',
                        ),
                    ],
                ),
                ElementScheme(
                    name='tmp',
                    regex='tmp(\\d+)?((?: {types.Real._REGEX.pattern[2:-2]})+?)',
                    mnemonic='tmp',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='temperatures',
                            type='types.Tuple[types.Real]',
                            description='Cell temperatrues',
                        ),
                    ],
                ),
                ElementScheme(
                    name='thtme',
                    mnemonic='thtme',
                    attributes=[
                        AttributeScheme(
                            name='times',
                            type='types.Tuple[types.Real]',
                            description='Tuple of times when thermal temperatures are specified',
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
                            type='types.Integer',
                            description='Elastic scattering controls',
                            optional=True,
                            restriction='isinstance(ielas.value, types.Jump) or ielas == 0 or ielas == 1 or ielas == 2',
                        ),
                        AttributeScheme(
                            name='ipreg',
                            type='types.Integer',
                            description='pre-equilibrium model',
                            optional=True,
                            restriction='isinstance(ipreg.value, types.Jump) or ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3',
                        ),
                        AttributeScheme(
                            name='iexisa',
                            type='types.Integer',
                            description='Model choice controls',
                            restriction='isinstance(iexisa.value, types.Jump) or iexisa == 0 or iexisa == 1 or iexisa == 2',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ichoic',
                            type='types.Integer',
                            description='ISABEL intranuclear cascade model control',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='jcoul',
                            type='types.Integer',
                            description='Coulomb barrier for incident charged particle controls',
                            restriction='isinstance(jcoul.value, types.Jump) or jcoul == 0 or jcoul == 1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='nexite',
                            type='types.Integer',
                            description='Subtract nuclear recoil energy to get excitation energy',
                            restriction='isinstance(nexite.value, types.Jump) or nexite == 0 or nexite == 1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='npidk',
                            type='types.Integer',
                            description='Cutoff interact/terminate control',
                            restriction='isinstance(npidk.value, types.Jump) or npidk == 0 or npidk == 1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='noact',
                            type='types.Integer',
                            description='Particle transport settings',
                            restriction='isinstance(noact.value, types.Jump) or noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='icem',
                            type='types.Integer',
                            description='Choose alternative physics model',
                            optional=True,
                            restriction='isinstance(icem.value, types.Jump) or icem == 0 or icem == 1 or icem == 2',
                        ),
                        AttributeScheme(
                            name='ilaq',
                            type='types.Integer',
                            description='Choose light ion and nucleon physics modules',
                            restriction='isinstance(ilaq.value, types.Jump) or ilaq == 0 or ilaq == 1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='nevtype',
                            type='types.Integer',
                            description='Choose number of evaporation particles for GEM2',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='lcb',
                    mnemonic='lcb',
                    attributes=[
                        AttributeScheme(
                            name='flenb1',
                            type='types.Real',
                            description='Kinetic energy for nucleons CEM/Bertini/INCL',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='flenb2',
                            type='types.Real',
                            description='Kinetic energy for nucleons LAQGSM03.03',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='flenb3',
                            type='types.Real',
                            description='Kinetic energy for pions CEM/Bertini/INCL',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='flenb4',
                            type='types.Real',
                            description='Kinetic energy for pions LAQGSM03.03',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='flenb5',
                            type='types.Real',
                            description='Kinetic energy for nucleons ISABEL',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='flenb6',
                            type='types.Real',
                            description='Kinetic energy for appropriate model',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='cotfe',
                            type='types.Real',
                            description='Cutoff kinetic energy for particle escape',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='film0',
                            type='types.Real',
                            description='Maximum correction allowed for masss-energy balancing',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='lcc',
                    mnemonic='lcc',
                    attributes=[
                        AttributeScheme(
                            name='stincl',
                            type='types.Real',
                            description='Rescaling factor of the cascade duration',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='v0incl',
                            type='types.Real',
                            description='Potential depth',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='xfoisaincl',
                            type='types.Real',
                            description='Maximum impact parameter for Pauli blocking',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='npaulincl',
                            type='types.Integer',
                            description='Pauli blocking parameter setting',
                            optional=True,
                            restriction='npaulincl == 0 or npaulincl == -1 or npaulincl == 1',
                        ),
                        AttributeScheme(
                            name='nosurfincl',
                            type='types.Integer',
                            description='Difuse nuclear surface based on Wood-Saxon density setting',
                            optional=True,
                            restriction='nosurfincl in {-2, -1, 0, 1}',
                        ),
                        AttributeScheme(
                            name='ecutincl',
                            type='types.Real',
                            description='Bertini model energy below this energy',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ebankincl',
                            type='types.Real',
                            description='INCL bank particles below this energy',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ebankabia',
                            type='types.Real',
                            description='ABLA bank particles below this energy',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='lea',
                    mnemonic='lea',
                    attributes=[
                        AttributeScheme(
                            name='ipht',
                            type='types.Integer',
                            description='Generation of de-excitation photons setting',
                            restriction='isinstance(ipht.value, types.Jump) or ipht in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='icc',
                            type='types.Integer',
                            description='Level of physics for PHT physics setting',
                            restriction='isinstance(icc.value, types.Jump) or icc in {0, 1, 2, 3, 4}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='nobalc',
                            type='types.Integer',
                            description='Mass-energy balancing in cascade setting',
                            restriction='isinstance(nobalc.value, types.Jump) or nobalc in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='nobale',
                            type='types.Integer',
                            description='Mass-energy balancing in evaporation setting',
                            restriction='isinstance(nobale.value, types.Jump) or nobale in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ifbrk',
                            type='types.Integer',
                            description='Mass-energy balancing in Fermi-breakup setting',
                            restriction='isinstance(ifbrk.value, types.Jump) or ifbrk in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ilvden',
                            type='types.Integer',
                            description='Level-density model setting',
                            restriction='isinstance(ilvden.value, types.Jump) or ilvden in {0, 1, -1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ievap',
                            type='types.Integer',
                            description='Evaporation and fission model setting',
                            restriction='isinstance(ievap.value, types.Jump) or ievap in {0, 1, -1, 2}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='nofis',
                            type='types.Integer',
                            description='Fission setting',
                            restriction='isinstance(nofis.value, types.Jump) or nofis in {0, 1}',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='leb',
                    mnemonic='leb',
                    attributes=[
                        AttributeScheme(
                            name='yzere',
                            type='types.Real',
                            description='Y0 parameter in level-density formula for Z≤70',
                            restriction='isinstance(yzere.value, types.Jump) or yzere > 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='bzere',
                            type='types.Real',
                            description='B0 parameter in level-density formula for Z≤70',
                            restriction='isinstance(bzere.value, types.Jump) or bzere > 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='yzero',
                            type='types.Real',
                            description='Y0 parameter in level-density formula for Z≥71',
                            restriction='isinstance(yzero.value, types.Jump) or yzero > 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='bzero',
                            type='types.Real',
                            description='B0 parameter in level-density formula for Z≥70',
                            restriction='isinstance(bzero.value, types.Jump) or bzero > 0',
                            optional=True,
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
                            type='types.Tuple[fmult.FmultOption]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
                                    description='Watt energy spectrum parameters a',
                                ),
                                AttributeScheme(
                                    name='b',
                                    type='types.Real',
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
                                    type='types.Integer',
                                    description='Gaussian sampling algorithm setting',
                                    restriction='setting in {0, 1, 3, 5, 6, 7}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='data',
                            mnemonic='data',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.Integer',
                                    description='Sampling method setting',
                                    restriction='setting in {0, 1, 2, 3}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='shift',
                            mnemonic='shift',
                            attributes=[
                                AttributeScheme(
                                    name='setting',
                                    type='types.Integer',
                                    description='Shift method setting',
                                    restriction='setting in {0, 1, 2, 3, 4}',
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
                            type='types.Tuple[tropt.TroptOption]',
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
                                    optional=True,
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
                            name='designator',
                            type='types.Designator',
                            description='Data option particle designator',
                        ),
                        AttributeScheme(
                            name='settings',
                            type='types.Tuple[types.Integer]',
                            description='Tuple of uncollided secondary settings',
                        ),
                    ],
                ),
                ElementScheme(
                    name='cosyp',
                    regex='cosyp( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})((?: {types.Real._REGEX.pattern[2:-2]})+?)',
                    mnemonic='cosyp',
                    attributes=[
                        AttributeScheme(
                            name='pre',
                            type='types.Integer',
                            description='Prefix number of the COSY map files',
                        ),
                        AttributeScheme(
                            name='axsh',
                            type='types.Integer',
                            description='Horiztonal axis orientation',
                            restriction='axsh in {1, 2, 3}',
                        ),
                        AttributeScheme(
                            name='axsv',
                            type='types.Integer',
                            description='Vertical axis orientation',
                            restriction='axsv in {1, 2, 3}',
                        ),
                        AttributeScheme(
                            name='emaps',
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Integer]',
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
                            restriction='kind in {"const", "quad", "quadff"}',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[bfld.BfldOption]',
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
                                    type='types.Real',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Integer]',
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
                            type='types.Tuple[sdef.SdefOption]',
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
                                    type='types.Integer',
                                    description='Cell number',
                                    restriction='isinstance(number.value, types.Jump) or (number >= 0 and number <= 99_999_999)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='sur',
                            mnemonic='sur',
                            attributes=[
                                AttributeScheme(
                                    name='number',
                                    type='types.Integer',
                                    description='Surface number',
                                    restriction='isinstance(number.value, types.Jump) or (number >= 0 and number <= 99_999_999)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='erg_0',
                            mnemonic='erg',
                            attributes=[
                                AttributeScheme(
                                    name='energy',
                                    type='types.Real',
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
                                    type='types.Distribution',
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
                                    type='types.Real',
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
                                    type='types.EmbeddedDistribution',
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
                                    type='types.Real',
                                    description='Cosine of the angle between VEC and particle',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dir_1',
                            mnemonic='dir',
                            attributes=[
                                AttributeScheme(
                                    name='cosine',
                                    type='types.Distribution',
                                    description='Cosine of the angle between VEC and particle',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='vec',
                            mnemonic='vec',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.Real',
                                    description='Reference vector for DIR x-component',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Reference vector for DIR y-component',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.Real',
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
                                    type='types.Integer',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Real',
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
                                    type='types.Distribution',
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
                                    type='types.Real',
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
                                    type='types.Real',
                                    description='Reference vector for EXT and RAD x-component',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Reference vector for EXT and RAD y-component',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Integer',
                                    description='Cookie-cutter cell number',
                                    restriction='number >= 0 and number <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ara',
                            mnemonic='ara',
                            attributes=[
                                AttributeScheme(
                                    name='area',
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Integer',
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
                                    type='types.Integer',
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
                                    type='types.Real',
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
                                    type='types.Integer',
                                    description='Month for cosmic-ray & background sources',
                                    restriction='month >= 1 and month <= 12',
                                ),
                                AttributeScheme(
                                    name='day',
                                    type='types.Integer',
                                    description='Day for cosmic-ray & background sources',
                                    restriction='day >= 1 and day <= 31',
                                ),
                                AttributeScheme(
                                    name='year',
                                    type='types.Integer',
                                    description='Year for cosmic-ray & background sources',
                                    restriction='year >= 1 and year <= 9999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='loc',
                            mnemonic='loc',
                            attributes=[
                                AttributeScheme(
                                    name='latitude',
                                    type='types.Real',
                                    description='Latitude for cosmic source',
                                    restriction='latitude >= -0 and latitude <= 90',
                                ),
                                AttributeScheme(
                                    name='longitude',
                                    type='types.Real',
                                    description='Longitude for cosmic source',
                                    restriction='longitude >= -0 and longitude <= 180',
                                ),
                                AttributeScheme(
                                    name='altitude',
                                    type='types.Real',
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
                                    type='types.Real',
                                    description='Normalized beam emittance parameter for x coordinates',
                                ),
                                AttributeScheme(
                                    name='eyn',
                                    type='types.Real',
                                    description='Normalized beam emittance parameter for x coordinates',
                                ),
                                AttributeScheme(
                                    name='bml',
                                    type='types.Real',
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
                                    type='types.Real',
                                    description='Beam aperture half-width in the x transverse direction',
                                ),
                                AttributeScheme(
                                    name='ba2',
                                    type='types.Real',
                                    description='Beam aperture half-width in the y transverse direction',
                                ),
                                AttributeScheme(
                                    name='u',
                                    type='types.Real',
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='information',
                            type='types.Tuple[types.Distribution]',
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='information',
                            type='types.Tuple[types.Real]',
                            description='Particle source information',
                        ),
                    ],
                ),
                ElementScheme(
                    name='si_2',
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='information',
                            type='types.Tuple[types.Designator]',
                            description='Particle source information',
                        ),
                    ],
                ),
                ElementScheme(
                    name='sp_0',
                    mnemonic='sp',
                    regex='sp(\\d+)( [dcvw])?((?: {types.Real._REGEX.pattern[2:-2]})+?)',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
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
                            type='types.Tuple[types.Real]',
                            description='Particle source probabilities',
                        ),
                    ],
                ),
                ElementScheme(
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
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.Real',
                            description='Built-in function parameter #2',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='sb_0',
                    mnemonic='sb',
                    regex='sb(\\d+)( [dcvw])?((?: {types.Real._REGEX.pattern[2:-2]})+?)',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Integer',
                            description='Built-in function designator',
                            restriction='function in {-2, -3, -4, -5, -6, -7, -21, -31, -41}',
                        ),
                        AttributeScheme(
                            name='a',
                            type='types.Real',
                            description='Built-in function parameter #1',
                        ),
                        AttributeScheme(
                            name='b',
                            type='types.Real',
                            description='Built-in function parameter #2',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='ds_0',
                    mnemonic='ds',
                    regex='ds(\\d+)( [hls])?((?: {types.Real._REGEX.pattern[2:-2]})+?)',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
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
                            type='types.Tuple[types.Real]',
                            description='Depdented source dependent variables',
                        ),
                    ],
                ),
                ElementScheme(
                    name='ds_1',
                    mnemonic='ds',
                    regex='ds(\\d+) t((?: {ds_1.Variables._REGEX.pattern[2:-2]})+?)',
                    extra='''
    def to_mcnp(self):
        """
        Generates INP from ``Ds_1``.

        Returns:
            INP for ``Ds_1``.
        """
        return f'ds{self.suffix} t {self.ijs}'
    ''',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
                        ),
                        # t
                        AttributeScheme(
                            name='ijs',
                            type='types.Tuple[ds_1.Variables]',
                            description='Dependent source independent & dependent variables',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='variables',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='independent',
                                    type='types.Real',
                                    description='Independent source dependent variable',
                                ),
                                AttributeScheme(
                                    name='dependent',
                                    type='types.Real',
                                    description='Dependent source dependent variable',
                                ),
                            ],
                        )
                    ],
                ),
                ElementScheme(
                    name='ds_2',
                    mnemonic='ds',
                    regex='ds(\\d+) q((?: {ds_2.Variables._REGEX.pattern[2:-2]})+?)',
                    extra='''
    def to_mcnp(self):
        """
        Generates INP from ``Ds_2``.

        Returns:
            INP for ``Ds_2``.
        """
        return f'ds{self.suffix} q {self.vss}'
    ''',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix >= 1 and suffix <= 999',
                        ),
                        # q
                        AttributeScheme(
                            name='vss',
                            type='types.Tuple[ds_2.Variables]',
                            description='Dependent source independent & dependent variables',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='variables',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='independent',
                                    type='types.Real',
                                    description='Independent source dependent variable',
                                ),
                                AttributeScheme(
                                    name='dependent',
                                    type='types.Real',
                                    description='Dependent source dependent variable',
                                ),
                            ],
                        )
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
                            restriction='suffix >= 1 and suffix <= 999',
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
                            type='types.Tuple[types.Integer]',
                            description='Problem surfaces',
                        ),
                        AttributeScheme(
                            name='cells',
                            type='types.Tuple[types.Integer]',
                            description='Problem cells',
                            optional=True,
                            can_paren=True,
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[ssw.SswOption]',
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
                                    type='types.Integer',
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
                                    type='types.Tuple[types.Integer]',
                                    description='Cells from which KCODE neutrons are written',
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
                            type='types.Tuple[ssr.SsrOption]',
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
                                    type='types.Tuple[types.Integer]',
                                    description='Tuple of surface numbers from subset of surfaces on SSW card',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='cel',
                            mnemonic='cel',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.Integer]',
                                    description='Tuple of cell from subset of cells on SSW card',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='new',
                            mnemonic='new',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.Integer]',
                                    description='Tuple of surface numbers to start run',
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
                                    type='types.Integer',
                                    description='Collision option setting',
                                    restriction='setting in {-1, 0, 1}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='wgt',
                            mnemonic='wgt',
                            attributes=[
                                AttributeScheme(
                                    name='constant',
                                    type='types.Real',
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
                                    type='types.Distribution',
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
                                    type='types.Integer',
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
                                    type='types.Real',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Distribution',
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
                                    type='types.Real',
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
                                    type='types.Real',
                                    description='Radius of cylindrical window',
                                ),
                                AttributeScheme(
                                    name='zb',
                                    type='types.Real',
                                    description='Bottom of cylindrical window',
                                    restriction='zb > 0',
                                ),
                                AttributeScheme(
                                    name='ze',
                                    type='types.Real',
                                    description='Top of cylindrical window',
                                    restriction='self.zb > 0 and self.zb < ze',
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
                            type='types.Integer',
                            description='Number of source histories per cycle',
                            restriction='isinstance(nsrck.value, types.Jump) or nsrck >= 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='rkk',
                            type='types.Real',
                            description='Initial guess of keff',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ikz',
                            type='types.Integer',
                            description='Number of cycles to be skipped before beginning tally accumulation',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='kct',
                            type='types.Integer',
                            description='Total number of cycles to be done',
                            restriction='isinstance(kct.value, types.Jump) or kct > 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='msrk',
                            type='types.Integer',
                            description='Number of source points to allocate for',
                            restriction='isinstance(msrk.value, types.Jump) or msrk < 40 * (1000 if not self.nsrck or isinstance(self.nsrck.value, types.Jump) else self.nsrck)',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='knrm',
                            type='types.Integer',
                            description='Normalization of tallies setting',
                            restriction='isinstance(knrm.value, types.Jump) or knrm in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='mrkp',
                            type='types.Integer',
                            description='Maximum number of cycle values on MCTAL or RUNTPE files',
                            restriction='isinstance(mrkp.value, types.Jump) or mrkp > 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='kc8',
                            type='types.Integer',
                            description='Number of cylces for average setting',
                            restriction='isinstance(kc8.value, types.Jump) or kc8 in {0, 1}',
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
                            type='types.Tuple[ksrc.Location]',
                            description='Tuple of inital source points',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='location',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.Real',
                                    description='Location x-coordinate',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Location y-coordinate',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.Real',
                                    description='Location z-coordinate',
                                ),
                            ],
                        )
                    ],
                ),
                ElementScheme(
                    name='kopts',
                    mnemonic='kopts',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[kopts.KoptsOption]',
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
                                    type='types.Integer',
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
                                    restriction='fileopt in {"mctal", "tsunami-b"}',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                            type='types.Integer',
                            description='Number of mesh intervals in x direction',
                            restriction='x_number > 0',
                        ),
                        AttributeScheme(
                            name='x_minimum',
                            type='types.Real',
                            description='Minimum x-value for mesh',
                        ),
                        AttributeScheme(
                            name='x_maximum',
                            type='types.Real',
                            description='Maximum x-value for mesh',
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
                        ),
                        AttributeScheme(
                            name='y_maximum',
                            type='types.Real',
                            description='Maximum y-value for mesh',
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
                        ),
                        AttributeScheme(
                            name='z_maximum',
                            type='types.Real',
                            description='Maximum z-value for mesh',
                        ),
                    ],
                ),
                ElementScheme(
                    name='f_0',
                    mnemonic='f',
                    regex='([*+])?f(\\d*[123467])(?::(\\S+))?((?: {types.Integer._REGEX.pattern[2:-2]})+?)( t)?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*", "+"}',
                            description='Star prefix',
                            optional=True,
                        ),
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='problems',
                            type='types.Tuple[types.Integer]',
                            description='Problem numbers of surface or cell',
                        ),
                        AttributeScheme(
                            name='t',
                            type='types.String',
                            description='Notation to make bin values cumulative',
                            restriction='t == "t"',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='f_1',
                    mnemonic='f',
                    regex='([*+])?f(\\d*[5])(?::(\\S+))?((?: \\S+ \\S+ \\S+ \\S+)+?)( nd)?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*", "+"}',
                            description='Star prefix',
                            optional=True,
                        ),
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='spheres',
                            type='types.Tuple[f_1.Sphere]',
                            description='Detector points',
                        ),
                        AttributeScheme(
                            name='nd',
                            type='types.String',
                            description='Total/average specified surfaces/cells option',
                            restriction='nd == "nd"',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='sphere',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.Real',
                                    description='Vector x coordinate',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Vector y coordinate',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.Integer',
                                    description='Vector z coordinate',
                                ),
                                AttributeScheme(
                                    name='ro',
                                    type='types.Integer',
                                    description='Sphere exclusion radius',
                                ),
                            ],
                        )
                    ],
                ),
                ElementScheme(
                    name='f_2',
                    mnemonic='f',
                    regex='([*+])?f(\\d*[5])([xyz])(?::(\\S+))?((?: \\S+ \\S+ \\S+)+?)( nd)?',
                    extra='''
    def to_mcnp(self):
        """
        Generates INP from ``F_2``.

        Returns:
            INP for ``F_2``.
        """

        return f'{self.prefix or ""}f{self.suffix}{self.a}{f":{self.designator}" if self.designator else ""} {self.rings} {self.nd or ""}'
    ''',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*", "+"}',
                            description='Star prefix',
                            optional=True,
                        ),
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='rings',
                            type='types.Tuple[f_2.Ring]',
                            description='Detector points',
                        ),
                        AttributeScheme(
                            name='nd',
                            type='types.String',
                            description='Total/average specified surfaces/cells option',
                            restriction='nd == "nd"',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='ring',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='distance',
                                    type='types.Real',
                                    description='Ring position',
                                ),
                                AttributeScheme(
                                    name='radius',
                                    type='types.Real',
                                    description='Ring radius',
                                ),
                                AttributeScheme(
                                    name='ro',
                                    type='types.Integer',
                                    description='Ring radius',
                                ),
                            ],
                        )
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
                            type='types.Real',
                            description='Pinhole center x-coordinate',
                        ),
                        AttributeScheme(
                            name='y1',
                            type='types.Real',
                            description='Pinhole center y-coordinate',
                        ),
                        AttributeScheme(
                            name='z1',
                            type='types.Real',
                            description='Pinhole center z-coordinate',
                        ),
                        AttributeScheme(
                            name='ro',
                            type='types.Real',
                            description='Pinhole exclusion radius',
                            restriction='ro == 0',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.Real',
                            description='Reference direction x-coordinate',
                        ),
                        AttributeScheme(
                            name='y2',
                            type='types.Real',
                            description='Reference direction y-coordinate',
                        ),
                        AttributeScheme(
                            name='z2',
                            type='types.Real',
                            description='Reference direction z-coordinate',
                        ),
                        AttributeScheme(
                            name='f1',
                            type='types.Real',
                            description='Cylindrical collimator radius',
                            restriction='f1 >= 0',
                        ),
                        AttributeScheme(
                            name='f2',
                            type='types.Real',
                            description='Pinhole radius in the direction perpendiuclar to the reference direction',
                            restriction='f2 >= 0',
                        ),
                        AttributeScheme(
                            name='f3',
                            type='types.Real',
                            description='Distance between pinhole and and detector grid',
                            restriction='f3 >= 0',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fir',
                    regex='fir(\\d+)(?::(\\S+))?( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})',
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x1',
                            type='types.Real',
                            description='Rectangular grid center x-coordinate',
                        ),
                        AttributeScheme(
                            name='y1',
                            type='types.Real',
                            description='Rectangular grid center y-coordinate',
                        ),
                        AttributeScheme(
                            name='z1',
                            type='types.Real',
                            description='Rectangular grid center z-coordinate',
                        ),
                        AttributeScheme(
                            name='ro',
                            type='types.Real',
                            description='Rectangular grid exclusion radius',
                            restriction='ro == 0',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.Real',
                            description='Reference direction x-coordinate',
                        ),
                        AttributeScheme(
                            name='y2',
                            type='types.Real',
                            description='Reference direction y-coordinate',
                        ),
                        AttributeScheme(
                            name='z2',
                            type='types.Real',
                            description='Reference direction z-coordinate',
                        ),
                        AttributeScheme(
                            name='f1',
                            type='types.Real',
                            description='Source contributions on/off',
                            restriction='f1 in {0, -1, 1}',
                        ),
                        AttributeScheme(
                            name='f2',
                            type='types.Real',
                            description='Radial view of field',
                        ),
                        AttributeScheme(
                            name='f3',
                            type='types.Real',
                            description='Contribution offset setting',
                            restriction='f3 in {0, -1, 1}',
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
                            type='types.Real',
                            description='Cylindrical grid center x-coordinate',
                        ),
                        AttributeScheme(
                            name='y1',
                            type='types.Real',
                            description='Cylindrical grid center y-coordinate',
                        ),
                        AttributeScheme(
                            name='z1',
                            type='types.Real',
                            description='Cylindrical grid center z-coordinate',
                        ),
                        AttributeScheme(
                            name='ro',
                            type='types.Real',
                            description='Cylindrical grid exclusion radius',
                            restriction='ro == 0',
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.Real',
                            description='Reference direction x-coordinate',
                        ),
                        AttributeScheme(
                            name='y2',
                            type='types.Real',
                            description='Reference direction y-coordinate',
                        ),
                        AttributeScheme(
                            name='z2',
                            type='types.Real',
                            description='Reference direction z-coordinate',
                        ),
                        AttributeScheme(
                            name='f1',
                            type='types.Real',
                            description='Source contributions on/off',
                            restriction='f1 in {0, -1}',
                        ),
                        AttributeScheme(
                            name='f2',
                            type='types.Real',
                            description='Radial view of field',
                            restriction='f2 != 0',
                        ),
                        AttributeScheme(
                            name='f3',
                            type='types.Real',
                            description='Contribution offset setting',
                            restriction='f3 in {0, -1}',
                        ),
                    ],
                ),
                ElementScheme(
                    name='f_3',
                    mnemonic='f',
                    regex='([*+])?f(\\d*[8])(?::(\\S+))?((?: {types.Integer._REGEX.pattern[2:-2]})+?)( t)?',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*", "+"}',
                            description='Star prefix',
                            optional=True,
                        ),
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
                            optional=True,
                        ),
                        AttributeScheme(
                            name='problems',
                            type='types.Tuple[types.Integer]',
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
                    regex='fc(\\d+)( [\\S\\s]+)',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[t_1.TOption_1]',
                            description='Dictionary of options',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='cbeg',
                            mnemonic='cbeg',
                            attributes=[
                                AttributeScheme(
                                    name='time',
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Real',
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
                                    type='types.Integer',
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
                                    type='types.Real',
                                    description='Reference ending time',
                                )
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='c',
                    regex='([*]?)c(\\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?',
                    mnemonic='c',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*", "+"}',
                            description='Star prefix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.Real]',
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
                    name='fq',
                    regex='fq(\\d+)?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?',
                    mnemonic='fq',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='a1',
                            type='types.String',
                            description='Letters representing tally bin types',
                            restriction='a1 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='a2',
                            type='types.String',
                            description='Letters representing tally bin types',
                            restriction='a2 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='a3',
                            type='types.String',
                            description='Letters representing tally bin types',
                            restriction='a3 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='a4',
                            type='types.String',
                            description='Letters representing tally bin types',
                            restriction='a4 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='a5',
                            type='types.String',
                            description='Letters representing tally bin types',
                            restriction='a5 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='a6',
                            type='types.String',
                            description='Letters representing tally bin types',
                            restriction='a6 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='a7',
                            type='types.String',
                            description='Letters representing tally bin types',
                            restriction='a7 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='a8',
                            type='types.String',
                            description='Letters representing tally bin types',
                            restriction='a8 in {"f", "d", "u", "s", "m", "c", "e", "t"}',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='fm',
                    mnemonic='fm',
                    regex='([+*])?fm(\\d+)( [\\S\\s]+)',
                    attributes=[
                        AttributeScheme(
                            name='prefix',
                            type='types.String',
                            restriction='prefix in {"*", "+"}',
                            description='Star prefix',
                            optional=True,
                        ),
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
                        ),
                    ],
                ),
                ElementScheme(
                    name='de',
                    mnemonic='de',
                    regex='de(\\d+)( (?:log|lin))?((?: {types.Real._REGEX.pattern[2:-2]})+?)',
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
                            type='types.Tuple[types.Real]',
                            description='Energy values',
                        ),
                    ],
                ),
                ElementScheme(
                    name='df_0',
                    mnemonic='df',
                    regex='df(\\d+)( (?:log|lin))?((?: {types.Real._REGEX.pattern[2:-2]})+?)',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[df_1.DfOption_1]',
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
                                    type='types.Integer',
                                    description='Control units',
                                    restriction='isinstance(units.value, types.Jump) or units in {1, 2}',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='fac',
                            mnemonic='fac',
                            attributes=[
                                AttributeScheme(
                                    name='normalization',
                                    type='types.Integer',
                                    description='Normalization factor for dose',
                                    restriction='isinstance(normalization.value, types.Jump) or normalization >= -3',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='ic',
                            mnemonic='ic',
                            attributes=[
                                AttributeScheme(
                                    name='function',
                                    type='types.Integer',
                                    description='Standard dose function',
                                    restriction='isinstance(function.value, types.Jump) or function in {10, 20, 31, 32, 33, 34, 35, 40, 99}',
                                )
                            ],
                        ),
                        ElementScheme(
                            name='log',
                            mnemonic='log',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='lin',
                            mnemonic='lin',
                            attributes=[],
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Integer]',
                            description='Tallies for problem cell numbers to flag',
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
                            type='types.Tuple[types.Integer]',
                            description='Tallies for problem surface numbers to flag',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fs',
                    regex='fs(\\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)( t)?( c)?',
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
                            type='types.Tuple[types.Integer]',
                            description='Signed problem number of a segmenting surface.',
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
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='information',
                            type='types.Tuple[types.Real]',
                            description='Area, volume, or mass by segmented, surface/cell',
                        ),
                    ],
                ),
                ElementScheme(
                    name='fu',
                    mnemonic='fu',
                    regex='fu(\\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)(?: (nt))?(?: (c))?',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.Real]',
                            description='Input parameters for user bins',
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
                    regex='ft(\\d+)( [\\S\\s]+)',
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
                        ),
                    ],
                ),
                ElementScheme(
                    name='tf_0',
                    mnemonic='tf',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='if1',
                            type='types.Integer',
                            description='Cell, surface, or detector bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='id1',
                            type='types.Integer',
                            description='Total, flagged, or un-collided bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='iu1',
                            type='types.Integer',
                            description='User bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='is1',
                            type='types.Integer',
                            description='Segment bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='im1',
                            type='types.Integer',
                            description='Multiplier bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ic1',
                            type='types.Integer',
                            description='Cosine bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ie1',
                            type='types.Integer',
                            description='Energy bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='it1',
                            type='types.Integer',
                            description='Time bin number',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='tf_1',
                    mnemonic='tf',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            restriction='suffix <= 99_999_999',
                        ),
                        AttributeScheme(
                            name='if1',
                            type='types.Integer',
                            description='Cell, surface, or detector bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='id1',
                            type='types.Integer',
                            description='Total, flagged, or un-collided bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='iu1',
                            type='types.Integer',
                            description='User bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='is1',
                            type='types.Integer',
                            description='Segment bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='im1',
                            type='types.Integer',
                            description='Multiplier bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ic1',
                            type='types.Integer',
                            description='Cosine bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ie1',
                            type='types.Integer',
                            description='Energy bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='it1',
                            type='types.Integer',
                            description='Time bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='if2',
                            type='types.Integer',
                            description='Cell, surface, or detector bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='id2',
                            type='types.Integer',
                            description='Total, flagged, or un-collided bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='iu2',
                            type='types.Integer',
                            description='User bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='is2',
                            type='types.Integer',
                            description='Segment bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='im2',
                            type='types.Integer',
                            description='Multiplier bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ic2',
                            type='types.Integer',
                            description='Cosine bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ie2',
                            type='types.Integer',
                            description='Energy bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='it2',
                            type='types.Integer',
                            description='Time bin number',
                            optional=True,
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
                            type='types.Tuple[pert.PertOption]',
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
                                    type='types.Tuple[types.Integer]',
                                    description='List of cells',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='mat',
                            mnemonic='mat',
                            attributes=[
                                AttributeScheme(
                                    name='material',
                                    type='types.Integer',
                                    description='Material number to fill cells',
                                    restriction='material >= 0 and material <= 99_999_999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rho',
                            mnemonic='rho',
                            attributes=[
                                AttributeScheme(
                                    name='density',
                                    type='types.Real',
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
                                    type='types.Integer',
                                    description='Printing and specifies setting',
                                    restriction='setting in {1, -1, 2, -2, 3, -3}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='erg',
                            mnemonic='erg',
                            attributes=[
                                AttributeScheme(
                                    name='energy_lower_bound',
                                    type='types.Real',
                                    description='Lower bound for energy pertubation',
                                ),
                                AttributeScheme(
                                    name='energy_upper_bound',
                                    type='types.Real',
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
                                    type='types.Tuple[types.Integer]',
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
                            restriction='suffix > 0 and suffix <= 10_000',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[kpert.KpertOption]',
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
                                    type='types.Tuple[types.Integer]',
                                    description='List of cells',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='mat',
                            mnemonic='mat',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.Integer]',
                                    description='List of materials',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rho',
                            mnemonic='rho',
                            attributes=[
                                AttributeScheme(
                                    name='densities',
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Zaid]',
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Tuple[types.Real]',
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
                            restriction='suffix > 0 and suffix <= 999',
                        ),
                        AttributeScheme(
                            name='sen',
                            type='types.String',
                            description='Type of sensitivity',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[ksen.KsenOption]',
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
                                    type='types.Tuple[types.Zaid]',
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Integer',
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
                                    type='types.Tuple[types.Real]',
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
                            restriction='suffix > 0 and suffix <= 999',
                        ),
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[fmesh.FmeshOption]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='geom',
                            mnemonic='geom',
                            regex='geom(?: (xyz|rec|rzt|cyl))',
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
                                    type='types.Real',
                                    description='Origin x coordinate',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Origin y coordinate',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.Real',
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
                                    type='types.Real',
                                    description='Cylindrical mesh axis vector x component',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Cylindrical mesh axis vector y component',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.Real',
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
                                    type='types.Real',
                                    description='Plane vector x component',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Plane vector y component',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.Real',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Real',
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
                                    type='types.Integer',
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
                                    type='types.Real',
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
                                    type='types.Integer',
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
                                    type='types.Real',
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
                                    type='types.Integer',
                                    description='Transformation applied to the mesh',
                                    restriction='number >= 1 and number <= 999',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='inc',
                            mnemonic='inc',
                            attributes=[
                                AttributeScheme(
                                    name='lower',
                                    type='types.Real',
                                    description='Collision for FMESH tally lower bound',
                                ),
                                AttributeScheme(
                                    name='upper',
                                    type='types.Real',
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
                                    type='types.Integer',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[var.VarOption]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Real',
                            description='Multiplier to define the weight window upper limit',
                            restriction='isinstance(wupn.value, types.Jump) or wupn >= 2',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='wsurvn',
                            type='types.Real',
                            description='Multiplier to define the maximum Russian roulette survival weight within the window',
                            restriction='isinstance(wsurvn.value, types.Jump) or 1 < wsurvn',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='mxspln',
                            type='types.Real',
                            description='Maximum number of integer splits',
                            restriction='isinstance(mxspln.value, types.Jump) or 1 < mxspln',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='mwhere',
                            type='types.Integer',
                            description='Controls where to check a particle’s weight',
                            restriction='isinstance(mwhere.value, types.Jump) or mwhere in {-1, 0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='switchn',
                            type='types.Real',
                            description='Controls where to get the lower weight-window bounds',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='mtime',
                            type='types.Integer',
                            description='Energy/time-dependent window setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='wnrom',
                            type='types.Real',
                            description='Weight-window normalization factor',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='etsplt',
                            type='types.Integer',
                            description='ESLPT & TSPLT split/roulette on/off',
                            restriction='isinstance(etsplt.value, types.Jump) or etsplt in {0, 1}',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='wu',
                            type='types.Real',
                            description='Limits the maximum lower weight-window bound for any particle, energy, or time',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='nmfp',
                            type='types.Real',
                            description='Limits the maximum lower weight-window bound for any particle, energy, or time',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
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
                        ),
                        AttributeScheme(
                            name='setting',
                            type='types.Integer',
                            description='Energy- or time-dependent weight window toggle',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='wwge',
                    mnemonic='wwge',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.Real]',
                            description='Upper energy bound for weight-window group to be generated',
                        ),
                    ],
                ),
                ElementScheme(
                    name='wwgt',
                    mnemonic='wwgt',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='bounds',
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[mesh.MeshOption]',
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
                                    restriction='geometry in {"xyz", "rzt", "rpt", "cyl", "rec", "sph"}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ref',
                            mnemonic='ref',
                            attributes=[
                                AttributeScheme(
                                    name='point',
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Tuple[types.Real]',
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
                                    type='types.Tuple[types.Integer]',
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
                            type='types.Real',
                            description='Splitting/roulette ratio #1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_1',
                            type='types.Real',
                            description='Splitting/roulette energy #1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_2',
                            type='types.Real',
                            description='Splitting/roulette ratio #2',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_2',
                            type='types.Real',
                            description='Splitting/roulette energy #2',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_3',
                            type='types.Real',
                            description='Splitting/roulette ratio #3',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_3',
                            type='types.Real',
                            description='Splitting/roulette energy #3',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_4',
                            type='types.Real',
                            description='Splitting/roulette ratio #4',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_4',
                            type='types.Real',
                            description='Splitting/roulette energy #4',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_5',
                            type='types.Real',
                            description='Splitting/roulette ratio #5',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_5',
                            type='types.Real',
                            description='Splitting/roulette energy #5',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_6',
                            type='types.Real',
                            description='Splitting/roulette ratio #6',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_6',
                            type='types.Real',
                            description='Splitting/roulette energy #6',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_7',
                            type='types.Real',
                            description='Splitting/roulette ratio #7',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_7',
                            type='types.Real',
                            description='Splitting/roulette energy #7',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_8',
                            type='types.Real',
                            description='Splitting/roulette ratio #8',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_8',
                            type='types.Real',
                            description='Splitting/roulette energy #8',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_9',
                            type='types.Real',
                            description='Splitting/roulette ratio #9',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_9',
                            type='types.Real',
                            description='Splitting/roulette energy #9',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_10',
                            type='types.Real',
                            description='Splitting/roulette ratio #10',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_10',
                            type='types.Real',
                            description='Splitting/roulette energy #10',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_11',
                            type='types.Real',
                            description='Splitting/roulette ratio #11',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_11',
                            type='types.Real',
                            description='Splitting/roulette energy #11',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_12',
                            type='types.Real',
                            description='Splitting/roulette ratio #12',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_12',
                            type='types.Real',
                            description='Splitting/roulette energy #12',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_13',
                            type='types.Real',
                            description='Splitting/roulette ratio #13',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_13',
                            type='types.Real',
                            description='Splitting/roulette energy #13',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_14',
                            type='types.Real',
                            description='Splitting/roulette ratio #14',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_14',
                            type='types.Real',
                            description='Splitting/roulette energy #14',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_15',
                            type='types.Real',
                            description='Splitting/roulette ratio #15',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_15',
                            type='types.Real',
                            description='Splitting/roulette energy #15',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_16',
                            type='types.Real',
                            description='Splitting/roulette ratio #16',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_16',
                            type='types.Real',
                            description='Splitting/roulette energy #16',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_17',
                            type='types.Real',
                            description='Splitting/roulette ratio #17',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_17',
                            type='types.Real',
                            description='Splitting/roulette energy #17',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_18',
                            type='types.Real',
                            description='Splitting/roulette ratio #18',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_18',
                            type='types.Real',
                            description='Splitting/roulette energy #18',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_19',
                            type='types.Real',
                            description='Splitting/roulette ratio #19',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_19',
                            type='types.Real',
                            description='Splitting/roulette energy #19',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_20',
                            type='types.Real',
                            description='Splitting/roulette ratio #20',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='energy_20',
                            type='types.Real',
                            description='Splitting/roulette energy #20',
                            optional=True,
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
                            type='types.Real',
                            description='Splitting/roulette ratio #1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_1',
                            type='types.Real',
                            description='Splitting/roulette time #1',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_2',
                            type='types.Real',
                            description='Splitting/roulette ratio #2',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_2',
                            type='types.Real',
                            description='Splitting/roulette time #2',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_3',
                            type='types.Real',
                            description='Splitting/roulette ratio #3',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_3',
                            type='types.Real',
                            description='Splitting/roulette time #3',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_4',
                            type='types.Real',
                            description='Splitting/roulette ratio #4',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_4',
                            type='types.Real',
                            description='Splitting/roulette time #4',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_5',
                            type='types.Real',
                            description='Splitting/roulette ratio #5',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_5',
                            type='types.Real',
                            description='Splitting/roulette time #5',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_6',
                            type='types.Real',
                            description='Splitting/roulette ratio #6',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_6',
                            type='types.Real',
                            description='Splitting/roulette time #6',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_7',
                            type='types.Real',
                            description='Splitting/roulette ratio #7',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_7',
                            type='types.Real',
                            description='Splitting/roulette time #7',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_8',
                            type='types.Real',
                            description='Splitting/roulette ratio #8',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_8',
                            type='types.Real',
                            description='Splitting/roulette time #8',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_9',
                            type='types.Real',
                            description='Splitting/roulette ratio #9',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_9',
                            type='types.Real',
                            description='Splitting/roulette time #9',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_10',
                            type='types.Real',
                            description='Splitting/roulette ratio #10',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_10',
                            type='types.Real',
                            description='Splitting/roulette time #10',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_11',
                            type='types.Real',
                            description='Splitting/roulette ratio #11',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_11',
                            type='types.Real',
                            description='Splitting/roulette time #11',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_12',
                            type='types.Real',
                            description='Splitting/roulette ratio #12',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_12',
                            type='types.Real',
                            description='Splitting/roulette time #12',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_13',
                            type='types.Real',
                            description='Splitting/roulette ratio #13',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_13',
                            type='types.Real',
                            description='Splitting/roulette time #13',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_14',
                            type='types.Real',
                            description='Splitting/roulette ratio #14',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_14',
                            type='types.Real',
                            description='Splitting/roulette time #14',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_15',
                            type='types.Real',
                            description='Splitting/roulette ratio #15',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_15',
                            type='types.Real',
                            description='Splitting/roulette time #15',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_16',
                            type='types.Real',
                            description='Splitting/roulette ratio #16',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_16',
                            type='types.Real',
                            description='Splitting/roulette time #16',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_17',
                            type='types.Real',
                            description='Splitting/roulette ratio #17',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_17',
                            type='types.Real',
                            description='Splitting/roulette time #17',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_18',
                            type='types.Real',
                            description='Splitting/roulette ratio #18',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_18',
                            type='types.Real',
                            description='Splitting/roulette time #18',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_19',
                            type='types.Real',
                            description='Splitting/roulette ratio #19',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_19',
                            type='types.Real',
                            description='Splitting/roulette time #19',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ratio_20',
                            type='types.Real',
                            description='Splitting/roulette ratio #20',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='time_20',
                            type='types.Real',
                            description='Splitting/roulette time #20',
                            optional=True,
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
                            type='types.Tuple[types.String]',
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
                            type='types.Tuple[types.Real]',
                            description='Forced-collision control for cell',
                        ),
                    ],
                ),
                ElementScheme(
                    name='dxt',
                    regex='dxt:(\\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( \\S+ \\S+ \\S+ \\S+ \\S+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})',
                    mnemonic='dxt',
                    attributes=[
                        AttributeScheme(
                            name='designator',
                            type='types.Designator',
                            description='Data card particle designator',
                        ),
                        AttributeScheme(
                            name='spheres_1',
                            type='dxt.Shell',
                            description='DXTRAN spheres #1',
                        ),
                        AttributeScheme(
                            name='spheres_2',
                            type='dxt.Shell',
                            description='DXTRAN spheres #2',
                        ),
                        AttributeScheme(
                            name='spheres_3',
                            type='dxt.Shell',
                            description='DXTRAN spheres #3',
                        ),
                        AttributeScheme(
                            name='spheres_4',
                            type='dxt.Shell',
                            description='DXTRAN spheres #4',
                        ),
                        AttributeScheme(
                            name='spheres_5',
                            type='dxt.Shell',
                            description='DXTRAN spheres #5',
                        ),
                        AttributeScheme(
                            name='spheres_6',
                            type='dxt.Shell',
                            description='DXTRAN spheres #6',
                        ),
                        AttributeScheme(
                            name='spheres_7',
                            type='dxt.Shell',
                            description='DXTRAN spheres #7',
                        ),
                        AttributeScheme(
                            name='spheres_8',
                            type='dxt.Shell',
                            description='DXTRAN spheres #8',
                        ),
                        AttributeScheme(
                            name='spheres_9',
                            type='dxt.Shell',
                            description='DXTRAN spheres #9',
                        ),
                        AttributeScheme(
                            name='spheres_10',
                            type='dxt.Shell',
                            description='DXTRAN spheres #10',
                        ),
                        AttributeScheme(
                            name='cutoff_1',
                            type='types.Real',
                            description='Upper weight cutoff in the spheres',
                        ),
                        AttributeScheme(
                            name='cutoff_2',
                            type='types.Real',
                            description='Lower weight cutoff in the spheres',
                        ),
                        AttributeScheme(
                            name='weight',
                            type='types.Real',
                            description='Minimum photon weight',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='shell',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.Real',
                                    description='Vector x coordinate',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Vector y coordinate',
                                ),
                                AttributeScheme(
                                    name='z',
                                    type='types.Real',
                                    description='Vector z coordinate',
                                ),
                                AttributeScheme(
                                    name='inner_radius',
                                    type='types.Integer',
                                    description='Inner sphere radius',
                                ),
                                AttributeScheme(
                                    name='outer_radius',
                                    type='types.Integer',
                                    description='Outer sphere radius',
                                ),
                            ],
                        )
                    ],
                ),
                ElementScheme(
                    name='dd',
                    regex='dd(\\d+)?((?: {dd.Diagnostic._REGEX.pattern[2:-2]})+?)',
                    mnemonic='dd',
                    attributes=[
                        AttributeScheme(
                            name='suffix',
                            type='types.Integer',
                            description='Data card option suffix',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='diagnostics',
                            type='types.Tuple[dd.Diagnostic]',
                            description='Detector diagnostic entries',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='diagnostic',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='playing_setting',
                                    type='types.Real',
                                    description='Criterion for playing Russian roulette for DXTRAN',
                                ),
                                AttributeScheme(
                                    name='printing_setting',
                                    type='types.Real',
                                    description='Criterion for printing diagnostics for large contributions for DXTRAN',
                                ),
                            ],
                        )
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
                            type='types.Tuple[types.Real]',
                            description='Probability of contribution to DXTRAN',
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
                            type='types.Tuple[types.Real]',
                            description='Probability of contribution to DXTRAN',
                        ),
                    ],
                ),
                ElementScheme(
                    name='bbrem',
                    mnemonic='bbrem',
                    attributes=[
                        AttributeScheme(
                            name='bias_1',
                            type='types.Real',
                            description='Bias factor #1 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_2',
                            type='types.Real',
                            description='Bias factor #2 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_3',
                            type='types.Real',
                            description='Bias factor #3 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_4',
                            type='types.Real',
                            description='Bias factor #4 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_5',
                            type='types.Real',
                            description='Bias factor #5 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_6',
                            type='types.Real',
                            description='Bias factor #6 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_7',
                            type='types.Real',
                            description='Bias factor #7 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_8',
                            type='types.Real',
                            description='Bias factor #8 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_9',
                            type='types.Real',
                            description='Bias factor #9 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_10',
                            type='types.Real',
                            description='Bias factor #10 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_11',
                            type='types.Real',
                            description='Bias factor #11 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_12',
                            type='types.Real',
                            description='Bias factor #12 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_13',
                            type='types.Real',
                            description='Bias factor #13 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_14',
                            type='types.Real',
                            description='Bias factor #14 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_15',
                            type='types.Real',
                            description='Bias factor #15 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_16',
                            type='types.Real',
                            description='Bias factor #16 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_17',
                            type='types.Real',
                            description='Bias factor #17 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_18',
                            type='types.Real',
                            description='Bias factor #18 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_19',
                            type='types.Real',
                            description='Bias factor #19 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_20',
                            type='types.Real',
                            description='Bias factor #20 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_21',
                            type='types.Real',
                            description='Bias factor #21 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_22',
                            type='types.Real',
                            description='Bias factor #22 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_23',
                            type='types.Real',
                            description='Bias factor #23 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_24',
                            type='types.Real',
                            description='Bias factor #24 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_25',
                            type='types.Real',
                            description='Bias factor #25 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_26',
                            type='types.Real',
                            description='Bias factor #26 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_27',
                            type='types.Real',
                            description='Bias factor #27 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_28',
                            type='types.Real',
                            description='Bias factor #28 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_29',
                            type='types.Real',
                            description='Bias factor #29 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_30',
                            type='types.Real',
                            description='Bias factor #30 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_31',
                            type='types.Real',
                            description='Bias factor #31 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_32',
                            type='types.Real',
                            description='Bias factor #32 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_33',
                            type='types.Real',
                            description='Bias factor #33 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_34',
                            type='types.Real',
                            description='Bias factor #34 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_35',
                            type='types.Real',
                            description='Bias factor #35 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_36',
                            type='types.Real',
                            description='Bias factor #36 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_37',
                            type='types.Real',
                            description='Bias factor #37 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_38',
                            type='types.Real',
                            description='Bias factor #38 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_39',
                            type='types.Real',
                            description='Bias factor #39 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_40',
                            type='types.Real',
                            description='Bias factor #40 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_41',
                            type='types.Real',
                            description='Bias factor #41 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_42',
                            type='types.Real',
                            description='Bias factor #42 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_43',
                            type='types.Real',
                            description='Bias factor #43 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_44',
                            type='types.Real',
                            description='Bias factor #44 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_45',
                            type='types.Real',
                            description='Bias factor #45 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_46',
                            type='types.Real',
                            description='Bias factor #46 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_47',
                            type='types.Real',
                            description='Bias factor #47 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_48',
                            type='types.Real',
                            description='Bias factor #48 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='bias_49',
                            type='types.Real',
                            description='Bias factor #49 for bremsstrahlung specturm',
                        ),
                        AttributeScheme(
                            name='materials',
                            type='types.Tuple[types.Integer]',
                            description='Material to bias',
                        ),
                    ],
                ),
                ElementScheme(
                    name='pikmt',
                    mnemonic='pikmt',
                    attributes=[
                        AttributeScheme(
                            name='biases',
                            type='types.Tuple[pikmt.Photonbias]',
                            description='Biases for proton production',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='photonbias',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='zaid',
                                    type='types.Zaid',
                                    description='Bias nuclide identifier',
                                ),
                                AttributeScheme(
                                    name='ipiki',
                                    type='types.Integer',
                                    description='Bias controls',
                                ),
                            ],
                        )
                    ],
                ),
                ElementScheme(
                    name='pwt',
                    mnemonic='pwt',
                    attributes=[
                        AttributeScheme(
                            name='weights',
                            type='types.Tuple[types.Real]',
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
                            type='types.Integer',
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
                            type='types.Tuple[stop.StopOption]',
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
                                    type='types.Integer',
                                    description='Total number of histories before stop',
                                ),
                                AttributeScheme(
                                    name='npsmg',
                                    type='types.Integer',
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
                                    type='types.Real',
                                    description='Computer time before stop',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='f',
                            mnemonic='f',
                            attributes=[
                                AttributeScheme(
                                    name='suffix',
                                    type='types.Integer',
                                    description='Data card option option suffix',
                                    restriction='suffix <= 99_999_999',
                                ),
                                AttributeScheme(
                                    name='e',
                                    type='types.Integer',
                                    description='Tally fluctuation relative error before stop',
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
                            type='types.Tuple[types.Integer]',
                            description='Tables to print',
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
                            type='types.Tuple[types.Integer]',
                            description='Tallies to exclude from output',
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
                            type='types.Integer',
                            description='Increment for printing tallies',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ndm',
                            type='types.Integer',
                            description='Increment for dumping to RUNTPE file',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='mct',
                            type='types.Integer',
                            description='Controls printing of MCTAL file',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='ndmp',
                            type='types.Integer',
                            description='Maximum number of dumps on RUNTPE file',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='dmmp',
                            type='types.Integer',
                            description='Controls frequently of tally fluctuation chart',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
                    name='ptrac',
                    mnemonic='ptrac',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[ptrac.PtracOption]',
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
                                    type='types.Integer',
                                    description='Amount of storage available for filtered events',
                                    restriction='storage > 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='file',
                            mnemonic='file',
                            regex='file(?: (asc|bin|aov|bov))',
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
                                    type='types.Integer',
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
                                    type='types.Integer',
                                    description='Maximum number of events per history to write',
                                    restriction='events > 0',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='write',
                            mnemonic='write',
                            regex='write(?: (pos|all))',
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
                            regex='conic(?: (col|lin))',
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
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='filter',
                            mnemonic='filter',
                            attributes=[
                                AttributeScheme(
                                    name='variables',
                                    type='types.Tuple[filter.Entry]',
                                    description='MCNP6 variables for filtering',
                                ),
                            ],
                            options=[
                                ElementScheme(
                                    name='entry',
                                    mnemonic='',
                                    attributes=[
                                        AttributeScheme(
                                            name='lower',
                                            type='types.Real',
                                            description='Lower bound for filtering',
                                        ),
                                        AttributeScheme(
                                            name='variable',
                                            type='types.String',
                                            description='Variable name for PBL derived structure',
                                            optional=True,
                                        ),
                                        AttributeScheme(
                                            name='upper',
                                            type='types.Real',
                                            description='Upper bound for filtering',
                                        ),
                                    ],
                                )
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
                                    type='types.Tuple[types.Integer]',
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
                                    type='types.Tuple[types.Integer]',
                                    description='List of cell numbers for filtering',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='surface',
                            mnemonic='surface',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.Integer]',
                                    description='List of surface numbers for filtering',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tally',
                            mnemonic='tally',
                            attributes=[
                                AttributeScheme(
                                    name='numbers',
                                    type='types.Tuple[types.Integer]',
                                    description='List of tally numbers for filtering',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='value',
                            mnemonic='value',
                            attributes=[
                                AttributeScheme(
                                    name='cutoff',
                                    type='types.Real',
                                    description='Specifies tally cutoff above which history events will be written.',
                                ),
                            ],
                        ),
                    ],
                ),
                ElementScheme(
                    name='mplot',
                    mnemonic='mplot',
                    attributes=[
                        AttributeScheme(
                            name='options',
                            type='types.Tuple[mplot.MplotOption]',
                            description='Dictionary of options',
                            optional=True,
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='term',
                            mnemonic='term',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Output decive specifier',
                                    restriction='n in {0, 1}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='file',
                            mnemonic='file',
                            regex='file(?: (all|none))?',
                            attributes=[
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Graphics metafile on/off',
                                    restriction='aa in {"all", "none"}',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='coplot',
                            mnemonic='coplot',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='freq',
                            mnemonic='freq',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Number of histories between plotting calls',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='return',
                            mnemonic='return',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='plot',
                            mnemonic='plot',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='pause',
                            mnemonic='pause',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Pause duration',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='end',
                            mnemonic='end',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='options',
                            mnemonic='options',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='help',
                            mnemonic='help',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='status',
                            mnemonic='status',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='printal',
                            mnemonic='printal',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='iptal',
                            mnemonic='iptal',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='printpts',
                            mnemonic='printpts',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='runtpe',
                            mnemonic='runtpe',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='RUNTPE file to read dump',
                                ),
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='RUNTPE read dump number',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='dump',
                            mnemonic='dump',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='RUNTPE read dump number',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='wmctal',
                            mnemonic='wmctal',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='MCTAL file to write',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='rmctal',
                            mnemonic='rmctal',
                            attributes=[
                                AttributeScheme(
                                    name='filename',
                                    type='types.String',
                                    description='MCTAL file to read',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tally',
                            mnemonic='tally',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Number of current tally',
                                    optional=True,
                                )
                            ],
                        ),
                        ElementScheme(
                            name='pert',
                            mnemonic='pert',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Number on a PERT card',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='lethargy',
                            mnemonic='lethargy',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='nonorm',
                            mnemonic='nonorm',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='factor',
                            mnemonic='factor',
                            attributes=[
                                AttributeScheme(
                                    name='a',
                                    type='types.String',
                                    description='Multiplication axis',
                                    restriction='a in {"x", "y", "z"}',
                                ),
                                AttributeScheme(
                                    name='f',
                                    type='types.Real',
                                    description='Multiplication factor',
                                ),
                                AttributeScheme(
                                    name='s',
                                    type='types.Real',
                                    description='Addative term',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='reset',
                            mnemonic='reset',
                            regex='reset(?: (all|coplot))?',
                            attributes=[
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Command parameter reset',
                                    restriction='aa in {"all", "coplot"}',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='title',
                            mnemonic='title',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Line number',
                                    restriction='n > 0',
                                ),
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Line to substitute',
                                    restriction='len(aa) <= 40',
                                    can_quote=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='below',
                            mnemonic='below',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='subtitle',
                            mnemonic='subtitle',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.Integer',
                                    description='x-coordinate of location',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Integer',
                                    description='y-coordinate of location',
                                ),
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Line to substitute',
                                    restriction='len(aa) <= 40',
                                    can_quote=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='xtitle',
                            mnemonic='xtitle',
                            attributes=[
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Line to substitute',
                                    restriction='len(aa) <= 40',
                                    can_quote=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ytitle',
                            mnemonic='ytitle',
                            attributes=[
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Line to substitute',
                                    restriction='len(aa) <= 40',
                                    can_quote=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ztitle',
                            mnemonic='ztitle',
                            attributes=[
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Line to substitute',
                                    restriction='len(aa) <= 40',
                                    can_quote=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='label',
                            mnemonic='label',
                            attributes=[
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Line to substitute',
                                    restriction='len(aa) <= 10',
                                    can_quote=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='free',
                            mnemonic='free',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.String',
                                    description='Independent variable',
                                    restriction='x in {"f", "d", "u", "s", "m", "c", "e", "t", "i", "j", "k"}',
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.String',
                                    description='Dependent variable',
                                    restriction='y in {"f", "d", "u", "s", "m", "c", "e", "t", "i", "j", "k"}',
                                ),
                                AttributeScheme(
                                    name='option',
                                    type='free.FreeOption',
                                    description='free option',
                                    optional=True,
                                ),
                            ],
                            options=[
                                ElementScheme(
                                    name='all',
                                    mnemonic='all',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='noall',
                                    mnemonic='noall',
                                    attributes=[],
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='fixed',
                            mnemonic='fixed',
                            attributes=[
                                AttributeScheme(
                                    name='q',
                                    type='types.String',
                                    description='Fixed variable',
                                    restriction='q in {"f", "d", "u", "s", "m", "c", "e", "t", "i", "j", "k"}',
                                ),
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Bin number',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='set',
                            mnemonic='set',
                            attributes=[
                                AttributeScheme(
                                    name='f',
                                    type='types.Integer',
                                    description='F bin number',
                                ),
                                AttributeScheme(
                                    name='d',
                                    type='types.Integer',
                                    description='D bin number',
                                ),
                                AttributeScheme(
                                    name='u',
                                    type='types.Integer',
                                    description='U bin number',
                                ),
                                AttributeScheme(
                                    name='s',
                                    type='types.Integer',
                                    description='S bin number',
                                ),
                                AttributeScheme(
                                    name='m',
                                    type='types.Integer',
                                    description='M bin number',
                                ),
                                AttributeScheme(
                                    name='c',
                                    type='types.Integer',
                                    description='C bin number',
                                ),
                                AttributeScheme(
                                    name='e',
                                    type='types.Integer',
                                    description='E bin number',
                                ),
                                AttributeScheme(
                                    name='t',
                                    type='types.Integer',
                                    description='T bin number',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tfc',
                            mnemonic='tfc',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.String',
                                    description='Independent variable selector',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='kcode',
                            mnemonic='kcode',
                            attributes=[
                                AttributeScheme(
                                    name='i',
                                    type='types.Integer',
                                    description='Lifetime to remove',
                                    restriction='(i >= 1 and i <= 6) or (i >= 1 and i <= 19)',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='xs_0',
                            mnemonic='xs',
                            attributes=[
                                AttributeScheme(
                                    name='m',
                                    type='types.Integer',
                                    description='Material number',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='xs_1',
                            mnemonic='xs',
                            attributes=[
                                AttributeScheme(
                                    name='m',
                                    type='types.Zaid',
                                    description='Material ZAID',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='xs_2',
                            mnemonic='xs',
                            attributes=[
                                AttributeScheme(
                                    name='m',
                                    type='types.String',
                                    description='Material question mark',
                                    restriction='m == "?"',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='mt',
                            mnemonic='mt',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Reaction number to print',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='par',
                            mnemonic='par',
                            attributes=[
                                AttributeScheme(
                                    name='particle',
                                    type='types.Designator',
                                    description='Particle type to plot',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='linlin',
                            mnemonic='linlin',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='linlog',
                            mnemonic='linlog',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='loglin',
                            mnemonic='loglin',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='loglog',
                            mnemonic='loglog',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='xlims',
                            mnemonic='xlims',
                            attributes=[
                                AttributeScheme(
                                    name='lower',
                                    type='types.Real',
                                    description='x-axis lower limit',
                                ),
                                AttributeScheme(
                                    name='upper',
                                    type='types.Real',
                                    description='x-axis upper limit',
                                    restriction='self.lower < upper',
                                ),
                                AttributeScheme(
                                    name='nsteps',
                                    type='types.Real',
                                    description='x-axis interval',
                                    restriction='nsteps >= 0',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ylims',
                            mnemonic='ylims',
                            attributes=[
                                AttributeScheme(
                                    name='lower',
                                    type='types.Real',
                                    description='y-axis lower limit',
                                ),
                                AttributeScheme(
                                    name='upper',
                                    type='types.Real',
                                    description='y-axis upper limit',
                                    restriction='self.lower < upper',
                                ),
                                AttributeScheme(
                                    name='nsteps',
                                    type='types.Real',
                                    description='y-axis interval',
                                    restriction='nsteps >= 0',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='scales',
                            mnemonic='scales',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Plot scale setting',
                                    restriction='n in {1, 2, 3}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='hist',
                            mnemonic='hist',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='plinear',
                            mnemonic='plinear',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='spline',
                            mnemonic='spline',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.Real',
                                    description='Tension of rational splines',
                                    optional=True,
                                )
                            ],
                        ),
                        ElementScheme(
                            name='bar',
                            mnemonic='bar',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='noerrbar',
                            mnemonic='noerrbar',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='thick',
                            mnemonic='thick',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.Real',
                                    description='Thickness of plot curves',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='thin',
                            mnemonic='thin',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='legend',
                            mnemonic='legend',
                            attributes=[
                                AttributeScheme(
                                    name='x',
                                    type='types.Real',
                                    description='Label x-location',
                                    optional=True,
                                ),
                                AttributeScheme(
                                    name='y',
                                    type='types.Real',
                                    description='Label x-location',
                                    optional=True,
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='contour',
                            mnemonic='contour',
                            attributes=[
                                AttributeScheme(
                                    name='cmin',
                                    type='types.Real',
                                    description='Contour lower limit',
                                ),
                                AttributeScheme(
                                    name='cmax',
                                    type='types.Real',
                                    description='Contour upper limit',
                                ),
                                AttributeScheme(
                                    name='cstep',
                                    type='types.Real',
                                    description='Contour interval',
                                ),
                                AttributeScheme(
                                    name='options',
                                    type='types.Tuple[contour.ContourOption]',
                                    description='Dictionary of options',
                                    optional=True,
                                ),
                            ],
                            options=[
                                ElementScheme(
                                    name='pct',
                                    mnemonic='pct',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='lin',
                                    mnemonic='lin',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='log',
                                    mnemonic='log',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='all',
                                    mnemonic='all',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='noall',
                                    mnemonic='noall',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='line',
                                    mnemonic='line',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='noline',
                                    mnemonic='noline',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='color',
                                    mnemonic='color',
                                    attributes=[],
                                ),
                                ElementScheme(
                                    name='nocolor',
                                    mnemonic='nocolor',
                                    attributes=[],
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='wash',
                            mnemonic='wash',
                            attributes=[
                                AttributeScheme(
                                    name='aa',
                                    type='types.String',
                                    description='Color-wash on/offs',
                                    restriction='aa in {"on", "off"}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='fmesh',
                            mnemonic='fmesh',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Tally to plot',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='fmrelerr',
                            mnemonic='fmrelerr',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Tally error to plot',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='zlev',
                            mnemonic='zlev',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Tuple[types.String]',
                                    description='Scales of tally plots',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='ebin',
                            mnemonic='ebin',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Energy bin to plot',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='tbin',
                            mnemonic='tbin',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Time bin to plot',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='cop',
                            mnemonic='cop',
                            attributes=[],
                        ),
                        ElementScheme(
                            name='tal',
                            mnemonic='tal',
                            attributes=[
                                AttributeScheme(
                                    name='n',
                                    type='types.Integer',
                                    description='Tally number',
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
                            type='types.Integer',
                            description='Number of words written to a HISTP file',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='cells',
                            type='types.Tuple[types.Integer]',
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
                            type='types.Tuple[rand.RandOption]',
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
                                    type='types.Integer',
                                    description='Type of pseudorandom number generator',
                                    restriction='setting in {1, 2, 3, 4}',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='seed',
                            mnemonic='seed',
                            attributes=[
                                AttributeScheme(
                                    name='seed',
                                    type='types.Integer',
                                    description='Random number generator seed',
                                    restriction='seed % 2 == 1',
                                ),
                            ],
                        ),
                        ElementScheme(
                            name='stride',
                            mnemonic='stride',
                            attributes=[
                                AttributeScheme(
                                    name='stride',
                                    type='types.Integer',
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
                                    type='types.Integer',
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
                            type='types.Integer',
                            description='Obsolete; pseudorandom number for the first particle history',
                            restriction='x1 >= 0',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x2',
                            type='types.Integer',
                            description='Debug print interval',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x3',
                            type='types.Integer',
                            description='Lower history number inclusive limit for logging',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x4',
                            type='types.Integer',
                            description='Upper history number inclusive limit for logging',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x5',
                            type='types.Integer',
                            description='Maximnum number of events per history for logging',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x6',
                            type='types.Integer',
                            description='Detector/DXTRAN underflow limit',
                            restriction='x6 >= 50 and x6 <= 200',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x7',
                            type='types.Integer',
                            description='Volume and sufrace area printing on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x8',
                            type='types.Integer',
                            description='Obsolete; starting history offset',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x9',
                            type='types.Integer',
                            description='Distance allowed between cpincident repeated-structures',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x10',
                            type='types.Integer',
                            description='Half-life threshold for stable nuclides',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x11',
                            type='types.Integer',
                            description='Collision event lost particle logging on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x12',
                            type='types.Integer',
                            description='Expected number of random numbers',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x13',
                            type='types.Integer',
                            description='Obsolete; random number stride',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x14',
                            type='types.Integer',
                            description='Obsolete; random number multiplier',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x15',
                            type='types.Integer',
                            description='Usual selection of statistics quantities printing on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x16',
                            type='types.Integer',
                            description='History score grid accumulation scaling',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x17',
                            type='types.Integer',
                            description='Angular treatment for secondary particles setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x18',
                            type='types.Integer',
                            description='Energy-indexing alogrithm for election transport settings',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x19',
                            type='types.Integer',
                            description='Developer; Quadratic polynomical interpolation parameter',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x20',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x21',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x22',
                            type='types.Integer',
                            description='Unsued',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x23',
                            type='types.Integer',
                            description='Pulse-height tally variance reducation tress setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x24',
                            type='types.Integer',
                            description='Grazing contribution cutoff for surface fluxx tallies settings',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x25',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x26',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x27',
                            type='types.Integer',
                            description='Antiparticle promotion settings',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x28',
                            type='types.Integer',
                            description='Bank size',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x29',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x30',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x31',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x32',
                            type='types.Integer',
                            description='GENXS behavior setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x33',
                            type='types.Integer',
                            description='Additional interpolation/smoothing method for heavy ions on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x34',
                            type='types.Integer',
                            description='Developer; Muon-induced gammas bug parameter',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x35',
                            type='types.Integer',
                            description='Slight spreading of nuclear exitation on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x36',
                            type='types.Integer',
                            description='User-provided data for muon-induced gamma rays on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x37',
                            type='types.Integer',
                            description='Mimumum of internal bremsstrahlung spectrum',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x38',
                            type='types.Integer',
                            description='Barashenkov/Polanski data file on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x39',
                            type='types.Integer',
                            description='Default S(α,β) smoothing behavior on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x40',
                            type='types.Integer',
                            description='Developer; MCPLIB and XSDIR lines writing setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x41',
                            type='types.Integer',
                            description='Developer; Phonton/election data printing setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x42',
                            type='types.Integer',
                            description='Model cross section setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x43',
                            type='types.Integer',
                            description='Developer; Photo form-factor interpolation setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x44',
                            type='types.Integer',
                            description='Developer; Coherent scattering in isolation setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x45',
                            type='types.Integer',
                            description='MCNP6/MCNPX elastic scattering method selector',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x46',
                            type='types.Integer',
                            description='CEM-to_LAQGSM photonuclear energy boundary setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x47',
                            type='types.Integer',
                            description='Cosmic-rasy spectra setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x48',
                            type='types.Integer',
                            description='MCNP6 threading on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x49',
                            type='types.Integer',
                            description='Normal input checking on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x50',
                            type='types.Integer',
                            description='TFC priting setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x51',
                            type='types.Integer',
                            description='Developer; Photon-induced fluoresence on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x52',
                            type='types.Integer',
                            description='Developer; Compton-induced relaxation on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x53',
                            type='types.Integer',
                            description='Photoelectric relazation data setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x54',
                            type='types.Integer',
                            description='Sampling method for ENDF Law 9 setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x55',
                            type='types.Integer',
                            description='Spontaneous decay integration time',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x56',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x57',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x58',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x59',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x60',
                            type='types.Integer',
                            description='Print number of calls to each high-energy model',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x61',
                            type='types.Integer',
                            description='Developer; models of knock-on electron angles',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x62',
                            type='types.Integer',
                            description='Developer; single-event electrons excitation energy loss debugger',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x63',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x64',
                            type='types.Integer',
                            description='Developer; single-event electrons angular deflaction debugger',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x65',
                            type='types.Integer',
                            description='Developer; single-event ionization and treat deflection dubgger',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x66',
                            type='types.Integer',
                            description='Developer; single-event bremsstrahlung photon angles setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x67',
                            type='types.Integer',
                            description='Particle histories setting for detectors and DXTRAN',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x68',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x69',
                            type='types.Integer',
                            description='LJA array size setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x70',
                            type='types.Integer',
                            description='Developer; interaction models setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x71',
                            type='types.Integer',
                            description='Model photonuclear capability on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x72',
                            type='types.Integer',
                            description='Log-log/linear interpolation in ELXS_MOD setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x73',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x74',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x75',
                            type='types.Integer',
                            description='Print extra info for F-matrix calculation on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x76',
                            type='types.Integer',
                            description='Print array storage info after setup on/off',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x77',
                            type='types.Integer',
                            description='Has-based cross-section serach bin number',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x78',
                            type='types.Integer',
                            description='Developer; S(A,B) method old/new setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x79',
                            type='types.Integer',
                            description='MT for absorption and fission setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x80',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x81',
                            type='types.Integer',
                            description='Developer; interpolation for electron elastic scatter setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x82',
                            type='types.Integer',
                            description='Developer; interpolation for electron elastic scatter setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x83',
                            type='types.Integer',
                            description='Developer; interpolation for electron partial x-s setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x84',
                            type='types.Integer',
                            description='Developer; interpolation for electron bremsstrahlung energy setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x85',
                            type='types.Integer',
                            description='Developer; interpolation for electron bremsstrahlung energy setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x86',
                            type='types.Integer',
                            description='Developer; interpolation for electron excitation setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x87',
                            type='types.Integer',
                            description='Developer; interpolation for electron knock-on energy setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x88',
                            type='types.Integer',
                            description='Developer; interpolation for electron knock-on energy setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x89',
                            type='types.Integer',
                            description='Developer; interpolation for electron ionization x-s setting',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x90',
                            type='types.Integer',
                            description='Mximum number of terms for Goudsmit-Saunderson distribution',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x91',
                            type='types.Integer',
                            description='Minimum ROC curve count value',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x92',
                            type='types.Integer',
                            description='Maximum ROC curve count value',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x93',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x94',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x95',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x96',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x97',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x98',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x99',
                            type='types.Integer',
                            description='Unused',
                            optional=True,
                        ),
                        AttributeScheme(
                            name='x100',
                            type='types.Integer',
                            description='Coincident-surface method old/new setting',
                            optional=True,
                        ),
                    ],
                ),
                ElementScheme(
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
                ElementScheme(
                    name='idum',
                    mnemonic='idum',
                    attributes=[
                        AttributeScheme(
                            name='intergers',
                            type='types.Tuple[types.Integer]',
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
                            type='types.Tuple[types.Real]',
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
                            type='types.Tuple[files.File]',
                            description='Files to create',
                        ),
                    ],
                    options=[
                        ElementScheme(
                            name='file',
                            mnemonic='',
                            attributes=[
                                AttributeScheme(
                                    name='unit',
                                    type='types.Integer',
                                    description='Unit number of file to create',
                                ),
                                AttributeScheme(
                                    name='filename',
                                    type='types.Integer',
                                    description='Name of file to create',
                                ),
                                AttributeScheme(
                                    name='access',
                                    type='types.String',
                                    description='access of file to create',
                                    restriction="access.value not in {'sequential', 'direct', 's', 'd'}",
                                    optional=True,
                                ),
                                AttributeScheme(
                                    name='form',
                                    type='types.String',
                                    description='Format of file to create',
                                    restriction="form.value not in {'formatted', 'unformatted', 'f', 'u'}",
                                    optional=True,
                                ),
                                AttributeScheme(
                                    name='length',
                                    type='types.Integer',
                                    description='Record length of file to create',
                                    optional=True,
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
    ],
)
