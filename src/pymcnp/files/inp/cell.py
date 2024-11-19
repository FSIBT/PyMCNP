"""
Contains the class representing INP cell cards.

``cell`` packages the ``Cell`` class, providing an object-oriented, importable
interface for INP cell cards.
"""

import re
from typing import Final

from . import _card
from . import _factory
from ..utils import types
from ..utils import errors
from ..utils import _parser


class CellGeometry(_card.CardEntry):
    """
    ``CellGeometry`` represents INP cell card geometry formulas.

    ``CellGeometry`` implements ``_card.CardMnemonic``.

    Attributes:
        string: Geometry formula string representation.
    """

    _OPERATIONS_ORDER = {'#': 0, ' ': 1, ':': 2}

    def __init__(self, formula: str):
        """
        Initializes ``CellGeometry``.

        Parameters:
            formula: INP for cell geometry.

        Raises:
            MCNPSemanticError: INVALID_CELL_GEOMETRY.
            MCNPSyntaxError: TOOFEW_CELL_GEOMETRY, TOOLONG_CELL_GEOMETRY.
        """

        if not formula:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY)

        # Running Shunting-Yard Algorithm
        ops_stack = _parser.Parser(
            [], errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY)
        )
        out_stack = _parser.Parser(
            [], errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY)
        )
        inp_stack = re.findall(r'#|:| : |[()]| [()]|[()] | [()] | |[+-]?\d+', formula)

        if ''.join(inp_stack) != formula:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY)

        for token in inp_stack:
            if re.match(r'[+-]?\d+', token):
                # Processing Surface Number

                entry = int(token)
                if entry is None or not (entry != 0 and -99_999_999 <= entry <= 99_999_999):
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY)

                out_stack.pushr(token)

            elif re.match(r'#', token):
                # Processing Unary Operator
                ops_stack.pushr(token)

            elif re.match(r'([(]| [(]|[(] | [(] )', token):
                # Processing Left Parenthesis
                ops_stack.pushr('(')

            elif re.match(r'([)]| [)]|[)] | [)] )', token):
                # Processing Right Parenthesis
                while ops_stack.peekr() != '(':
                    out_stack.pushr(ops_stack.popr())

                ops_stack.popr()

            elif re.match(r':| : | |: | :', token):
                # Processing Binary Operator
                token = token.strip() if token != ' ' else token

                while (
                    ops_stack
                    and ops_stack.peekr() not in {'(', ')'}
                    and self._OPERATIONS_ORDER[ops_stack.peekr()] >= self._OPERATIONS_ORDER[token]
                ):
                    out_stack.pushr(ops_stack.popr())

                ops_stack.pushr(token)

            else:
                # Unrecognized Character
                assert False

        while ops_stack:
            out_stack.pushr(ops_stack.popr())

        self.formula = formula

    @staticmethod
    def from_mcnp(source: str) -> str:
        """
        Generates ``CellGeometry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for cell card geometry.

        Returns:
            ``CellGeometry`` object.
        """

        return CellGeometry(source)

    def to_mcnp(self) -> str:
        """
        Generates INP from ``CellGeometry``.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``CellGeometry``.
        """

        return self.formula


class CellKeyword(_card.CardKeyword):
    """
    Represents INP cell card option keywords.

    ``CellKeyword`` implements ``_card.CardKeyword``.
    """

    IMP = 'imp'
    VOL = 'vol'
    PWT = 'pwt'
    EXT = 'ext'
    FCL = 'fcl'
    WWN = 'wwn'
    DXC = 'dxc'
    NONU = 'nonu'
    PD = 'pd'
    TMP = 'tmp'
    U = 'u'
    TRCL = 'trcl'
    # COORDINATE_TRANSFORMATION_ANGLE = '*trcl'
    LAT = 'lat'
    FILL = 'fill'
    # FILL_ANGLE = '*fill'
    ELPT = 'elpt'
    COSY = 'cosy'
    BFIELD = 'bflcl'
    UNC = 'unc'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``CellKeyword``

        Returns:
            ``CellKeyword`` object.

        Raises:
            MCNPSemanticError: INVALID_CELL_OPTION_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return CellKeyword(source)
        except ValueError:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD)


class CellOption(_card.CardOption):
    """
    Represents INP cell card option keywords.

    ``CellOption`` implements ``_card.CardOption``.

    Attributes:
        keyword: Cell card option keyword.
        value: Cell card option value.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``CellOption`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``CellOption``.
        """

        # Processing Suffix
        suffix_str = str(self.suffix.to_mcnp()) if hasattr(self, 'suffix') else ''

        # Processing Designator
        designator_str = (
            f":{','.join(self.designator.particles)}"
            if hasattr(self, 'designator') and self.designator is not None
            else ''
        )

        value_str = ''
        if isinstance(self.value, tuple):
            value_str = ' '.join(
                [
                    str(param.value) if hasattr(param, 'value') else str(param)
                    for param in self.value
                ]
            )
        else:
            value_str = self.value.value if hasattr(self.value, 'value') else str(self.value)

        return f'{self.keyword.to_mcnp()}{suffix_str}{designator_str}={value_str}'

    def __repr__(self):
        return f'<CellOption: {self.__class__.__name__} ({self.to_mcnp()})>'


_CellImpFactory = _factory.CellOptionFactory(
    'imp',
    False,
    True,
    _factory.AttributeFactory('importance', 'types.McnpReal', 'Particle(s) importance in cell', ''),
)

_CellVolFactory = _factory.CellOptionFactory(
    'vol',
    False,
    False,
    _factory.AttributeFactory(
        'volume',
        'types.McnpReal',
        'Cell volume',
        'volume >= 0',
    ),
)

_CellPwtFactory = _factory.CellOptionFactory(
    'pwt',
    False,
    False,
    _factory.AttributeFactory(
        'weight',
        'types.McnpReal',
        'Cell weight of photons produced at neutron collisions',
        '',
    ),
)

_CellExtFactory = _factory.CellOptionFactory(
    'ext',
    False,
    True,
    _factory.AttributeFactory(
        'stretch',
        'str',
        'Cell exponential transform stretching specifier',
        '',
    ),
)

_CellFclFactory = _factory.CellOptionFactory(
    'fcl',
    False,
    True,
    _factory.AttributeFactory(
        'control', 'types.McnpReal', 'Cell forced-collision control.', '-1 <= control <= 1'
    ),
)

_CellWwnFactory = _factory.CellOptionFactory(
    'wwn',
    True,
    True,
    _factory.AttributeFactory(
        'bound',
        'types.McnpReal',
        'Cell weight-window space, time, or energy lower bound.',
        'bound == -1 or bound >= 0',
    ),
)

_CellDxcFactory = _factory.CellOptionFactory(
    'dxc',
    True,
    True,
    _factory.AttributeFactory(
        'probability',
        'types.McnpReal',
        'Cell probability of DXTRAN contribution.',
        '0 <= probability <= 1',
    ),
)

_CellNonuFactory = _factory.CellOptionFactory(
    'nonu',
    False,
    False,
    _factory.AttributeFactory(
        'setting', 'types.McnpInteger', 'Cell fission setting.', 'setting in {0, 1, 2}'
    ),
)

_CellPdFactory = _factory.CellOptionFactory(
    'pd',
    True,
    False,
    _factory.AttributeFactory(
        'probability',
        'types.McnpReal',
        'Cell probability of DXTRAN contribution.',
        '0 <= probability <= 1',
    ),
)

_CellTmpFactory = _factory.CellOptionFactory(
    'tmp',
    True,
    False,
    _factory.AttributeFactory(
        'temperature',
        'types.McnpReal',
        'Cell temperature at suffix time index.',
        'temperature > 0',
    ),
)

_CellUFactory = _factory.CellOptionFactory(
    'u',
    False,
    False,
    _factory.AttributeFactory(
        'number',
        'types.McnpInteger',
        'Cell universe number.',
        '-99_999_999 <= number <= 99_999_999',
    ),
)

_CellTrclFactory = _factory.CellOptionFactory(
    'trcl',
    False,
    False,
    _factory.AttributeFactory(
        'value', 'int', 'Cell coordinate transformation option value(s).', '1 <= value <= 999'
    ),
)

_CellLatFactory = _factory.CellOptionFactory(
    'lat',
    False,
    False,
    _factory.AttributeFactory(
        'shape', 'types.McnpInteger', 'Cell lattice shape.', 'shape in {1, 2}'
    ),
)

_CellFillFactory = _factory.CellOptionFactory(
    'fill',
    False,
    False,
    _factory.AttributeFactory(
        'value',
        'tuple[types.McnpInteger]',
        'Fill cell option value or value(s) tuple.',
        '0 <= entry <= 99_999_999',
    ),
)

_CellElptFactory = _factory.CellOptionFactory(
    'elpt',
    False,
    True,
    _factory.AttributeFactory('cutoff', 'types.McnpReal', 'Cell energy cutoff.', ''),
)

_CellCosyFactory = _factory.CellOptionFactory(
    'cosy',
    False,
    False,
    _factory.AttributeFactory(
        'number', 'types.McnpInteger', 'Cell cosy map number.', 'number in {1, 2, 3, 4, 5, 6}'
    ),
)

_CellBflclFactory = _factory.CellOptionFactory(
    'bflcl',
    False,
    False,
    _factory.AttributeFactory(
        'number', 'types.McnpInteger', 'Cell magnetic field number.', 'number >= 0'
    ),
)

_CellUncFactory = _factory.CellOptionFactory(
    'unc',
    False,
    True,
    _factory.AttributeFactory(
        'setting',
        'types.McnpInteger',
        'Cell uncollided secondaries setting.',
        'setting in {0, 1}',
    ),
)

CellImp = None
CellVol = None
CellPwt = None
CellExt = None
CellFcl = None
CellWwn = None
CellDxc = None
CellNonu = None
CellPd = None
CellTmp = None
CellU = None
CellTrcl = None
CellLat = None
CellFill = None
CellElpt = None
CellCosy = None
CellBflcl = None
CellUnc = None

exec(_CellImpFactory.build())
exec(_CellVolFactory.build())
exec(_CellPwtFactory.build())
exec(_CellExtFactory.build())
exec(_CellFclFactory.build())
exec(_CellWwnFactory.build())
exec(_CellDxcFactory.build())
exec(_CellNonuFactory.build())
exec(_CellPdFactory.build())
exec(_CellTmpFactory.build())
exec(_CellUFactory.build())
exec(_CellTrclFactory.build())
exec(_CellLatFactory.build())
exec(_CellFillFactory.build())
exec(_CellElptFactory.build())
exec(_CellCosyFactory.build())
exec(_CellBflclFactory.build())
exec(_CellUncFactory.build())


class Cell(_card.Card):
    """
    ``Cell`` represents INP cell cards.

    ``Cell`` implements ``_card.Card``.

    Attributes:
        number: Cell card number.
        material: Cell card material number.
        density: Cell card density value.
        geometry: Cell card geometry specification.
        options: Cell card parameter table.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        material: types.McnpInteger,
        density: types.McnpReal,
        geometry: CellGeometry,
        options: dict[str, CellOption],
    ):
        """
        Initializes ``Cell``.

        Parameters:
            number: Cell card number.
            material: Cell card material number.
            density: Cell card density value.
            geometry: Cell card geometry specification.
            parameters: Cell card parameter table.

        Raises:
            MCNPSemanticError: INVALID_CELL_NUMBER.
            MCNPSemanticError: INVALID_CELL_MATERIAL.
            MCNPSemanticError: INVALID_CELL_DENSITY.
            MCNPSemanticError: INVALID_CELL_MATERIAL.
            MCNPSemanticError: INVALID_CELL_GEOMETRY.
            MCNPSemanticError: INVALID_CELL_OPTION.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_NUMBER)

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_MATERIAL)

        if material != 0:
            if density is None or (density == 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_DENSITY)

        if geometry is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY)

        if options is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION)

        for option in options.items():
            if option is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION)

        self.number: Final[types.McnpInteger] = number
        self.material: Final[types.McnpInteger] = material
        self.density: Final[types.McnpInteger] = density if material != 0 else None
        self.geometry: Final[CellGeometry] = geometry
        self.options: Final[dict[str, CellOption]] = options
        self.ident: Final[int] = number.value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cell`` objects from INP.

        ``from_mcnp`` translate from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Cell``.

        Returns:
            ``Cell`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_CELL, TOOLONG_CELL.
        """

        # Processing Inline Comment
        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' |=', source),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL),
        )

        # Processing Number, Material, & Density
        number = types.McnpInteger.from_mcnp(tokens.popl())
        material = types.McnpInteger.from_mcnp(tokens.popl())
        density = types.McnpReal.from_mcnp(tokens.popl()) if material.value != 0 else None

        # Processing Geometry
        geometry = []
        while tokens:
            try:
                try_keyword = re.search(r'[*]?[A-Za-z]+', tokens.peekl()).group()
                CellKeyword.from_mcnp(try_keyword)
                break
            except Exception:
                geometry.append(tokens.popl())
                pass
        geometry = CellGeometry(' '.join(geometry))

        # Processing Options
        options = {}
        keywords = re.findall(
            r'imp|vol|pwt|ext|fcl|wwn|dxc|nonu|pd|tmp|u|trcl|lat|fill|elpt|cosy|bflcl|unc',
            ' '.join(tokens.deque),
        )
        values = re.split(
            r'imp|vol|pwt|ext|fcl|wwn|dxc|nonu|pd|tmp|u|trcl|lat|fill|elpt|cosy|bflcl|unc',
            ' '.join(tokens.deque),
        )[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'imp':
                    options['imp'] = CellImp.from_mcnp(f'{keyword}{value}')
                case 'vol':
                    options['vol'] = CellVol.from_mcnp(f'{keyword}{value}')
                case 'pwt':
                    options['pwt'] = CellPwt.from_mcnp(f'{keyword}{value}')
                case 'ext':
                    options['ext'] = CellExt.from_mcnp(f'{keyword}{value}')
                case 'fcl':
                    options['fcl'] = CellFcl.from_mcnp(f'{keyword}{value}')
                case 'wwn':
                    options['wwn'] = CellWwn.from_mcnp(f'{keyword}{value}')
                case 'dxc':
                    options['dxc'] = CellDxc.from_mcnp(f'{keyword}{value}')
                case 'nonu':
                    options['nonu'] = CellNonu.from_mcnp(f'{keyword}{value}')
                case 'pd':
                    options['pd'] = CellPd.from_mcnp(f'{keyword}{value}')
                case 'tmp':
                    options['tmp'] = CellTmp.from_mcnp(f'{keyword}{value}')
                case 'u':
                    options['u'] = CellU.from_mcnp(f'{keyword}{value}')
                case 'trcl':
                    options['trcl'] = CellTrcl.from_mcnp(f'{keyword}{value}')
                case 'lat':
                    options['lat'] = CellLat.from_mcnp(f'{keyword}{value}')
                case 'fill':
                    options['fill'] = CellFill.from_mcnp(f'{keyword}{value}')
                case 'elpt':
                    options['elpt'] = CellElpt.from_mcnp(f'{keyword}{value}')
                case 'cosy':
                    options['cosy'] = CellCosy.from_mcnp(f'{keyword}{value}')
                case 'bflcl':
                    options['bflcl'] = CellBflcl.from_mcnp(f'{keyword}{value}')
                case 'unc':
                    options['unc'] = CellUnc.from_mcnp(f'{keyword}{value}')

        cell = Cell(number, material, density, geometry, options)
        cell.comment = comments

        return cell

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Cell`` objects.

        ``to_mcnp`` translates from INP to PyMCNP.

        Returns:
            INP for ``Cell`` object.
        """

        number_str = self.number.to_mcnp()
        material_str = self.material.to_mcnp()
        density_str = self.density.to_mcnp() if self.density is not None else ' '
        geometry_str = self.geometry.to_mcnp()
        options_str = ' '.join([option.to_mcnp() for option in self.options.values()])

        return _parser.Postprocessor.add_continuation_lines(
            f'{number_str} {material_str} {density_str} {geometry_str} {options_str}'
        )
