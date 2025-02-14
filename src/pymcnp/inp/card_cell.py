import re
import typing

from . import cell
from . import _card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Cell(_card.InpCard_):
    """
    Represents INP cell cards.

    Attributes:
        number:   INP cell number.
        material: INP cell material.
        density:  INP cell density.
        geometry: INP cell geometry.
        options:  INP cell options.
    """

    _REGEX = re.compile(
        r'\A(\S+)( \S+)((?<! 0) \S+|(?<= 0))( [^a-z]+)(( (((imp):(\S+?)( \S+))|((vol)( \S+))|((pwt)( \S+))|((ext):(\S+?)( \S+))|((fcl):(\S+?)( \S+))|((wwn)(\d+?):(\S+?)( \S+))|((dxc)(\d+?):(\S+?)( \S+))|((nonu)( \S+))|((pd)(\d+?)( \S+))|((tmp)(\d+?)( \S+))|((u)( \S+))|((trcl)( \S+))|((trcl)( ( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)))|((lat)( \S+))|((fill)( \S+)( \S+)?)|((fill)( \S+)( ( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))?)|((elpt):(\S+?)( \S+))|((cosy)( \S+))|((bflcl)( \S+))|((unc):(\S+?)( \S+))))+)?\Z'
    )

    def __init__(
        self,
        number: types.Integer,
        material: types.Integer,
        density: types.Real,
        geometry: cell.CellEntry_Geometry,
        options: tuple[cell.CellOption_] = None,
    ):
        """
        Initializes ``Cell``.

        Parameters:
            number:   INP cell number.
            material: INP cell material.
            density:  INP cell density.
            geometry: INP cell geometry.
            options:  INP cell options.

        Returns:
            ``Cell``.

        Raises:
            McnpError: SEMANTICS_CELL_NUMBER.
            McnpError: SEMANTICS_CELL_MATERIAL.
            McnpError: SEMANTICS_CELL_DENSITY.
            McnpError: SEMANTICS_CELL_GEOMETRY.
            McnpError: SEMANTICS_CELL_OPTIONS.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_NUMBER, number)

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_MATERIAL, material)

        if (density is not None and material == 0) or (density is None and material != 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_DENSITY, density)

        if geometry is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_GEOMETRY, geometry)

        if options is not None and None in options:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTIONS, options)

        self.number: typing.Final[types.Integer] = number
        self.material: typing.Final[types.Integer] = material
        self.density: typing.Final[types.Real] = density
        self.geometry: typing.Final[cell.CellEntry_Geometry] = geometry
        self.options: typing.Final[tuple[cell.CellOption_]] = options

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cell`` from INP.

        Parameters:
            source: INP cell card.

        Returns:
            ``Cell``.

        Raises:
            McnpError: SYNTAX_CELL.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Cell._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL, source)

        number = types.Integer.from_mcnp(tokens[1])
        material = types.Integer.from_mcnp(tokens[2])
        density = types.Real.from_mcnp(tokens[3]) if tokens[3] else None
        geometry = cell.CellEntry_Geometry.from_mcnp(tokens[4])
        options = (
            {val._KEYWORD: val for val in _parser.process_inp_option(cell.CellOption_, tokens[5])}
            if tokens[5]
            else None
        )

        c = Cell(number, material, density, geometry, options)
        c.comments = comments

        return c

    def to_mcnp(self):
        """
        Generates INP from ``Cell``.

        Returns:
            INP cell card.
        """

        return _parser.postprocess_continuation_line(
            f'{self.number} {self.material} {self.density or ""} {self.geometry} {types._Tuple((self.options or {}).values())}'
        )
