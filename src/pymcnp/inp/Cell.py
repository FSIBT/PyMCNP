import re
import dataclasses


from . import cell
from . import data
from ._card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser
from ..utils import _visualization


class Cell(Card):
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
        'options': types.Tuple[cell.CellOption],
    }

    _REGEX = re.compile(
        rf'\A(\S+)( \S+)((?<! 0) \S+|(?<= 0))( [^a-z]+)( ({cell.CellOption._REGEX.pattern}))*\Z'
    )

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
        self.options: types.Tuple[cell.CellOption] = options

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


@dataclasses.dataclass
class CellBuilder:
    """
    Builds ``Cell``.

    Attributes:
        number: cell number.
        material: cell material.
        density: cell density.
        geometry: cell geometry.
        options: cell options.
        atoms_or_grams: density sign.
    """

    number: str | int | types.Integer
    material: str | int | types.Integer | data.MBuilder
    geometry: str | types.Geometry | types.GeometryBuilder
    options: list[str] | list[cell.CellOption] = dataclasses.field(default_factory=lambda: ({}))
    density: str | float | types.Real = None
    atoms_or_grams: bool = True

    def build(self):
        """
        Builds ``CellBuilder`` into ``Cell``.

        Returns:
            ``Cell`` for ``CellBuilder``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        if isinstance(self.material, types.Integer):
            material = self.material
        elif isinstance(self.material, int):
            material = types.Integer(self.material)
        elif isinstance(self.material, str):
            material = types.Integer.from_mcnp(self.material)
        elif isinstance(self.material, data.MBuilder):
            material = self.material.build().suffix

        density = None
        if isinstance(self.density, types.Real):
            density = self.density
        elif isinstance(self.density, int) or isinstance(self.density, float):
            density = types.Real(self.density)
        elif isinstance(self.density, str):
            density = types.Real.from_mcnp(self.density)
        if density and not self.atoms_or_grams:
            density *= -1

        if isinstance(self.geometry, types.Geometry):
            geometry = self.geometry
        elif isinstance(self.geometry, str):
            geometry = types.Geometry.from_mcnp(self.geometry)
        elif isinstance(self.geometry, types.GeometryBuilder):
            geometry = self.geometry.build()

        options = []
        for item in self.options:
            if isinstance(item, cell.CellOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(cell.CellOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Cell(
            number=number,
            material=material,
            density=density,
            geometry=geometry,
            options=options,
        )
