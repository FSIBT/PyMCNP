import re

from . import cell
from . import _card
from .M_0 import M_0
from .Arb import Arb
from .Box import Box
from .C_x import C_x
from .C_y import C_y
from .C_z import C_z
from .Cx import Cx
from .Cy import Cy
from .Cz import Cz
from .Ell import Ell
from .Gq import Gq
from .K_x import K_x
from .K_y import K_y
from .K_z import K_z
from .Kx import Kx
from .Ky import Ky
from .Kz import Kz
from .P_0 import P_0
from .P_1 import P_1
from .Px import Px
from .Py import Py
from .Pz import Pz
from .Rcc import Rcc
from .Rec import Rec
from .Rhp import Rhp
from .Rpp import Rpp
from .S import S
from .So import So
from .Sph import Sph
from .Sq import Sq
from .Sx import Sx
from .Sy import Sy
from .Sz import Sz
from .Trc import Trc
from .Tx import Tx
from .Ty import Ty
from .Tz import Tz
from .Wed import Wed
from .X import X
from .Y import Y
from .Z import Z
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
        number: types.Integer = None,
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

        if number is None:
            number = next(NUMBER)

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
    def geometry(
        self,
        geometry: str
        | types.Geometry
        | Arb
        | Box
        | C_x
        | C_y
        | C_z
        | Cx
        | Cy
        | Cz
        | Ell
        | Gq
        | K_x
        | K_y
        | K_z
        | Kx
        | Ky
        | Kz
        | P_0
        | P_1
        | Px
        | Py
        | Pz
        | Rcc
        | Rec
        | Rhp
        | Rpp
        | S
        | So
        | Sph
        | Sq
        | Sx
        | Sy
        | Sz
        | Trc
        | Tx
        | Ty
        | Tz
        | Wed
        | X
        | Y
        | Z,
    ) -> None:
        """
        Sets `geometry`.

        Parameters:
            geometry: Cell geometry.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if geometry is not None:
            if any(
                (
                    isinstance(geometry, Arb),
                    isinstance(geometry, Box),
                    isinstance(geometry, C_x),
                    isinstance(geometry, C_y),
                    isinstance(geometry, C_z),
                    isinstance(geometry, Cx),
                    isinstance(geometry, Cy),
                    isinstance(geometry, Cz),
                    isinstance(geometry, Ell),
                    isinstance(geometry, Gq),
                    isinstance(geometry, K_x),
                    isinstance(geometry, K_y),
                    isinstance(geometry, K_z),
                    isinstance(geometry, Kx),
                    isinstance(geometry, Ky),
                    isinstance(geometry, Kz),
                    isinstance(geometry, P_0),
                    isinstance(geometry, P_1),
                    isinstance(geometry, Px),
                    isinstance(geometry, Py),
                    isinstance(geometry, Pz),
                    isinstance(geometry, Rcc),
                    isinstance(geometry, Rec),
                    isinstance(geometry, Rhp),
                    isinstance(geometry, Rpp),
                    isinstance(geometry, S),
                    isinstance(geometry, So),
                    isinstance(geometry, Sph),
                    isinstance(geometry, Sq),
                    isinstance(geometry, Sx),
                    isinstance(geometry, Sy),
                    isinstance(geometry, Sz),
                    isinstance(geometry, Trc),
                    isinstance(geometry, Tx),
                    isinstance(geometry, Ty),
                    isinstance(geometry, Tz),
                    isinstance(geometry, Wed),
                    isinstance(geometry, X),
                    isinstance(geometry, Y),
                    isinstance(geometry, Z),
                )
            ):
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
