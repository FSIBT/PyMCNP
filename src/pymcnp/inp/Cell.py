import re

from . import cell
from . import _card
from .M_0 import M_0
from .Surface import Surface
from .. import _show
from .. import types
from .. import errors


NUMBER = iter(range(1, 100000000))


class Cell(_card.Card):
    """
    Represents INP cell cards.
    """

    _ATTRS = {
        'number': types.Integer,
        'material': types.Integer,
        'density': types.Real,
        'geometry': types.Geometry,
        'options': types.Tuple(cell.CellOption),
    }

    _REGEX = re.compile(rf'\A(\S+)( \S+)((?<! 0) \S+|(?<= 0))( [^a-z]+)((?: (?:{cell.CellOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(
        self,
        material: types.Integer,
        geometry: types.Geometry,
        density: types.Real = None,
        number: types.Integer = next(NUMBER),
        options: types.Tuple(cell.CellOption) = None,
    ):
        """
        Initializes `Cell`.

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
        self.density: types.Real = density
        self.geometry: types.Geometry = geometry
        self.options: types.Tuple(cell.CellOption) = options

    def to_mcnp(self):
        """
        Generates INP from `Cell`.

        Returns:
            INP cell card.
        """

        source = f'{self.number} {self.material} {self.density if self.density is not None else ""} {self.geometry} {self.options if self.options is not None else ""}'
        source = _card.Card._postprocess(source)

        return source

    def to_show(self, surfaces: dict[str, _show.Shape], cells: dict[str, _show.Shape], shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Cell`.

        Paramaters:
            surfaces: Dictionary of surfaces and visualizations.
            shapes: Collection of shapes.

        Returns:
            `Visualization` for `Cell`
        """

        return self.geometry.ast.to_show(surfaces, cells)

    @property
    def number(self) -> types.Integer:
        """
        Cell number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets `number`.

        Parameters:
            number: Cell number.

        Raises:
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._material

    @material.setter
    def material(self, material: str | int | types.Integer | M_0) -> None:
        """
        Sets `material`.

        Parameters:
            material: Cell material.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if material is not None:
            if isinstance(material, M_0):
                material = material.suffix
            elif isinstance(material, types.Integer):
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
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._density

    @density.setter
    def density(self, density: str | int | float | types.Real) -> None:
        """
        Sets `density`.

        Parameters:
            density: Cell density.

        Raises:
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._geometry

    @geometry.setter
    def geometry(self, geometry: str | types.Geometry | Surface) -> None:
        """
        Sets `geometry`.

        Parameters:
            geometry: Cell geometry.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if geometry is not None:
            if isinstance(geometry, Surface):
                geometry = types.Geometry(str(geometry.number))
            elif isinstance(geometry, types.Geometry):
                geometry = geometry
            elif isinstance(geometry, str):
                geometry = types.Geometry.from_mcnp(geometry)

        if geometry is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, geometry)

        self._geometry: types.Geometry = geometry

    @property
    def options(self) -> types.Tuple(cell.CellOption):
        """
        Cell options.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[cell.CellOption] = None) -> None:
        """
        Sets `options`.

        Parameters:
            options: Cell options.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, cell.CellOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(cell.CellOption.from_mcnp(item))
            options = types.Tuple(cell.CellOption)(array)

        self._options: types.Tuple(cell.CellOption) = options
