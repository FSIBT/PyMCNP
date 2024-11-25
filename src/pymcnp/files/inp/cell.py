"""
Contains classes representing INP cell cards.
"""

import re
from typing import Final

from . import _card
from .subclasses_cell_options import Imp
from .subclasses_cell_options import Vol
from .subclasses_cell_options import Pwt
from .subclasses_cell_options import Ext
from .subclasses_cell_options import Fcl
from .subclasses_cell_options import Wwn
from .subclasses_cell_options import Dxc
from .subclasses_cell_options import Nonu
from .subclasses_cell_options import Pd
from .subclasses_cell_options import Tmp
from .subclasses_cell_options import U
from .subclasses_cell_options import Trcl
from .subclasses_cell_options import Lat
from .subclasses_cell_options import Fill
from .subclasses_cell_options import Elpt
from .subclasses_cell_options import Cosy
from .subclasses_cell_options import Bflcl
from .subclasses_cell_options import Unc
from .cell_option import CellOption
from .cell_option import CellKeyword
from ..utils import types
from ..utils import errors
from ..utils import _parser


class CellGeometry(_card.CardEntry):
    """
    Represents INP cell card geometry formulas.

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
            McnpError: EXPECTED_TOKEN.
            McnpError: INVALID_CELL_GEOMETRY.
        """

        if not formula:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_GEOMETRY, formula)

        # Running Shunting-Yard Algorithm
        ops_stack = _parser.Parser(
            [],
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, formula),
        )
        out_stack = _parser.Parser(
            [],
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, formula),
        )
        inp_stack = re.findall(
            r'#|:| : |[()]| [()]|[()] | [()] | |[+-]?\d+',
            formula,
        )

        if ''.join(inp_stack) != formula:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_GEOMETRY, formula)

        for token in inp_stack:
            if re.match(r'[+-]?\d+', token):
                # Processing Surface Number

                entry = int(token)
                if entry is None or not (entry != 0 and -99_999_999 <= entry <= 99_999_999):
                    raise errors.McnpError(errors.McnpCode.INVALID_CELL_GEOMETRY, formula)

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


class Cell(_card.Card):
    """
    Represents INP cell cards.

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
            McnpError: INVALID_CELL_NUMBER.
            McnpError: INVALID_CELL_MATERIAL.
            McnpError: INVALID_CELL_DENSITY.
            McnpError: INVALID_CELL_GEOMETRY.
            McnpError: INVALID_CELL_OPTION.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_NUMBER, str(number))

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_MATERIAL, str(material))

        if material != 0:
            if density is None or (density == 0):
                raise errors.McnpError(errors.McnpCode.INVALID_CELL_DENSITY, str(density))

        if geometry is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_GEOMETRY, str(geometry))

        if options is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION, str(options))

        for option in options.items():
            if option is None:
                raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION, str(options))

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
            McnpError: EXPECTED_TOKEN.
        """

        # Processing Inline Comment
        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
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
                    options['imp'] = Imp.from_mcnp(f'{keyword}{value}')
                case 'vol':
                    options['vol'] = Vol.from_mcnp(f'{keyword}{value}')
                case 'pwt':
                    options['pwt'] = Pwt.from_mcnp(f'{keyword}{value}')
                case 'ext':
                    options['ext'] = Ext.from_mcnp(f'{keyword}{value}')
                case 'fcl':
                    options['fcl'] = Fcl.from_mcnp(f'{keyword}{value}')
                case 'wwn':
                    options['wwn'] = Wwn.from_mcnp(f'{keyword}{value}')
                case 'dxc':
                    options['dxc'] = Dxc.from_mcnp(f'{keyword}{value}')
                case 'nonu':
                    options['nonu'] = Nonu.from_mcnp(f'{keyword}{value}')
                case 'pd':
                    options['pd'] = Pd.from_mcnp(f'{keyword}{value}')
                case 'tmp':
                    options['tmp'] = Tmp.from_mcnp(f'{keyword}{value}')
                case 'u':
                    options['u'] = U.from_mcnp(f'{keyword}{value}')
                case 'trcl':
                    options['trcl'] = Trcl.from_mcnp(f'{keyword}{value}')
                case 'lat':
                    options['lat'] = Lat.from_mcnp(f'{keyword}{value}')
                case 'fill':
                    options['fill'] = Fill.from_mcnp(f'{keyword}{value}')
                case 'elpt':
                    options['elpt'] = Elpt.from_mcnp(f'{keyword}{value}')
                case 'cosy':
                    options['cosy'] = Cosy.from_mcnp(f'{keyword}{value}')
                case 'bflcl':
                    options['bflcl'] = Bflcl.from_mcnp(f'{keyword}{value}')
                case 'unc':
                    options['unc'] = Unc.from_mcnp(f'{keyword}{value}')

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
