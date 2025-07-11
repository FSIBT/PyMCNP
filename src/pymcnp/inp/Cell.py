import re
import copy
import dataclasses


from . import cell
from ._card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Cell(Card):
    """
    Represents INP cell cards.

    Attributes:
        number: cell number.
        material: cell material.
        density: cell density.
        geometry: cell geometry.
        options: cell options.
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
            number: cell number.
            material: cell material.
            density: cell density.
            geometry: cell geometry.
            options: cell options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)
        if material is None or not (0 <= material <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, material)
        if (density is not None and material == 0) or (density is None and material != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, density)
        if geometry is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, geometry)

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
    material: str | int | types.Integer
    geometry: str | types.Geometry | types.GeometryBuilder
    options: list[str] | list[cell.CellOption] | list[cell.CellOptionBuilder] = None
    density: str | float | types.Real = None

    def build(self):
        """
        Builds ``CellBuilder`` into ``Cell``.

        Returns:
            ``Cell`` for ``CellBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        material = self.material
        if isinstance(self.material, types.Integer):
            material = self.material
        elif isinstance(self.material, int):
            material = types.Integer(self.material)
        elif isinstance(self.material, str):
            material = types.Integer.from_mcnp(self.material)

        density = self.density
        if isinstance(self.density, types.Real):
            density = self.density
        elif isinstance(self.density, int) or isinstance(self.density, float):
            density = types.Real(self.density)
        elif isinstance(self.density, str):
            density = types.Real.from_mcnp(self.density)

        geometry = self.geometry
        if isinstance(self.geometry, types.Geometry):
            geometry = self.geometry
        elif isinstance(self.geometry, str):
            geometry = types.Geometry.from_mcnp(self.geometry)
        elif isinstance(self.geometry, types.GeometryBuilder):
            geometry = self.geometry.build()

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, cell.CellOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(cell.CellOption.from_mcnp(item))
                elif isinstance(item, cell.CellOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Cell(
            number=number,
            material=material,
            density=density,
            geometry=geometry,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Cell):
        """
        Unbuilds ``Cell`` into ``CellBuilder``

        Returns:
            ``CellBuilder`` for ``Cell``.
        """

        return CellBuilder(
            number=copy.deepcopy(ast.number),
            material=copy.deepcopy(ast.material),
            density=copy.deepcopy(ast.density),
            geometry=copy.deepcopy(ast.geometry),
            options=copy.deepcopy(ast.options),
        )
