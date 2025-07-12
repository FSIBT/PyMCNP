import re

from . import cell
from ._card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Cell(Card):
    """
    Represents INP cell cards.
    """

    _ATTRS = {
        'number': types.Integer,
        'material': types.Integer,
        'density': types.Real,
        'geometry': types.Geometry,
        'options': types.Tuple[cell.CellOption],
    }

    _REGEX = re.compile(rf'\A(\S+)( \S+)((?<! 0) \S+|(?<= 0))( [^a-z]+)((?: (?:{cell.CellOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(
        self,
        number: types.Integer,
        material: types.Integer,
        density: types.Integer,
        geometry: types.Geometry,
        options: types.Tuple[cell.CellOption] = None,
    ):
        """
        Initializes ``Cell``.

        Parameters:
            number: Cell number.
            material: Cell material.
            density: Cell density.
            geometry: Cell geometry.
            options: Cell options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.number: types.Integer = number
        self.material: types.Integer = material
        self.density: types.Integer = density
        self.geometry: types.Geometry = geometry
        self.options: types.Tuple[cell.CellOption] = options

    def to_mcnp(self):
        """
        Generates INP from ``Cell``.

        Returns:
            INP cell card.
        """

        source = f'{self.number} {self.material} {self.density or ""} {self.geometry} {self.options or ""}'
        source, comments = _parser.preprocess_inp(source)
        source = _parser.postprocess_inp(source)

        return source

    @property
    def number(self) -> types.Integer:
        """
        Cell number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets ``number``.

        Parameters:
            number: Cell number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Integer):
                number = number
            elif isinstance(number, int):
                number = types.Integer(number)
            elif isinstance(number, str):
                number = types.Integer.from_mcnp(number)

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)

        self._number: types.Integer = number

    @property
    def material(self) -> types.Integer:
        """
        Cell material.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._material

    @material.setter
    def material(self, material: str | int | types.Integer) -> None:
        """
        Sets ``material``.

        Parameters:
            material: Cell material.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if material is not None:
            if isinstance(material, types.Integer):
                material = material
            elif isinstance(material, int):
                material = types.Integer(material)
            elif isinstance(material, str):
                material = types.Integer.from_mcnp(material)

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, material)

        self._material: types.Integer = material

    @property
    def density(self) -> types.Real:
        """
        Cell density.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._density

    @density.setter
    def density(self, density: str | int | float | types.Real) -> None:
        """
        Sets ``density``.

        Parameters:
            density: Cell density.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if density is not None:
            if isinstance(density, types.Real):
                density = density
            elif isinstance(density, float) or isinstance(density, int):
                density = types.Real(density)
            elif isinstance(density, str):
                density = types.Real.from_mcnp(density)

        if (density is not None and self.material == 0) or (density is None and self.material != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, density)

        self._density: types.Real = density

    @property
    def geometry(self) -> types.Geometry:
        """
        Cell geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._geometry

    @geometry.setter
    def geometry(self, geometry: str | types.Geometry) -> None:
        """
        Sets ``geometry``.

        Parameters:
            geometry: Cell geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if geometry is not None:
            if isinstance(geometry, types.Geometry):
                geometry = geometry
            elif isinstance(geometry, str):
                geometry = types.Geometry.from_mcnp(geometry)

        if geometry is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, geometry)

        self._geometry: types.Geometry = geometry

    @property
    def options(self) -> types.Tuple[cell.CellOption]:
        """
        Cell options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[cell.CellOption] = None) -> None:
        """
        Sets ``options``.

        Parameters:
            options: Cell options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, cell.CellOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(cell.CellOption.from_mcnp(item))

            options = types.Tuple(array)

        self._options: types.Tuple[cell.CellOption] = options


#    def draw(self, surfaces: dict[int, _visualization.Visualization]):
#        """
#        Generates ``Visualization`` from ``Cell``.
#
#        Returns:
#            ``Visualization`` for ``Cell``
#        """
#
#        temp = re.sub(r' 0+', '', self.geometry.infix)
#        temp = re.sub(r' +', ' ', temp)
#        temp = re.sub(r'\+', '', temp)
#        temp = re.sub(r' ?: ?', '|', temp)
#        temp = re.sub(r' ', '&', temp)
#        temp = re.sub(r'(\d+)', r'surfaces[\1]', temp)
#
#        if '-' in temp or '#' in temp:
#            assert False, "I'm working on it!"
#
#        return eval(temp)
