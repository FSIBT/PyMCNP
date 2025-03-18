import re

import pyvista

from . import cell
from .card_ import Card_
from ..utils import types
from ..utils import errors
from ..utils import _parser
from ..utils import _visualization


class Cell(Card_):
    """
    Represents INP cell cards.

    Attributes:
        InpError: SEMANTICS_CARD_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
        'material': types.Integer,
        'density': types.Real,
        'geometry': types.Geometry,
        'options': types.Tuple[cell.CellOption_],
    }

    _REGEX = re.compile(
        rf'\A(\S+)( \S+)((?<! 0) \S+|(?<= 0))( [^a-z]+)( ({cell.CellOption_._REGEX.pattern}))*\Z'
    )

    def __init__(
        self,
        number: types.Integer,
        material: types.Integer,
        density: types.Integer,
        geometry: types.Geometry,
        options: types.Tuple[cell.CellOption_] = None,
    ):
        """
        Initializes ``Cell``.

        Parameters:
            number: cell number.
            material: cell material.
            density: cell density.
            geometry: cell geometry.
            options: cell options.

        Raises:
            InpError: SEMANTICS_CARD_VALUE.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, number)
        if material is None or not (0 <= material <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, material)
        if (density is not None and material == 0) or (density is None and material != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, density)
        if geometry is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, geometry)

        self.number: types.Integer = number
        self.material: types.Integer = material
        self.density: types.Integer = density
        self.geometry: types.Geometry = geometry
        self.options: types.Tuple[cell.CellOption_] = options

    def to_mcnp(self):
        """
        Generates INP from ``Cell``.

        Returns:
            INP cell card.
        """

        return _parser.postprocess_continuation_line(
            f'{self.number} {self.material} {self.density or ""} {self.geometry} {self.options or ""}'
        )

    def draw(self, surfaces: dict[int, _visualization.Visualization]):
        """
        Generates ``Visualization`` from ``Cell``.

        Returns:
            ``pyvista.PolyData`` for ``Cell``
        """

        temp = re.sub(r' 0+', '', self.geometry.infix)
        temp = re.sub(r' +', ' ', temp)
        temp = re.sub(r'\+', '', temp)
        temp = re.sub(r' ?: ?', '|', temp)
        temp = re.sub(r' ', '&', temp)
        temp = re.sub(r'(\d+)', r'surfaces[\1]', temp)

        if '-' in temp or '#' in temp:
            assert False, "I'm working on it!"

        return eval(temp)
