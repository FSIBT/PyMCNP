import re

from . import cell
from . import _field
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

SURFACES = (
    Arb,
    Box,
    C_x,
    C_y,
    C_z,
    Cx,
    Cy,
    Cz,
    Ell,
    Gq,
    K_x,
    K_y,
    K_z,
    Kx,
    Ky,
    Kz,
    P_0,
    P_1,
    Px,
    Py,
    Pz,
    Rcc,
    Rec,
    Rhp,
    Rpp,
    S,
    So,
    Sph,
    Sq,
    Sx,
    Sy,
    Sz,
    Trc,
    Tx,
    Ty,
    Tz,
    Wed,
    X,
    Y,
    Z,
)


class Cell(_field.Fields, _card.Card):
    """
    Represents INP cell cards.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD
    _ORDER = ('material', 'geometry', 'density', 'number', 'options')

    number = _field.Field(types.Integer, 'Cell number', required=True, default=lambda card: next(NUMBER), numeric=int, invalid=lambda self, value: not 1 <= value <= 99_999_999)
    material = _field.Field(
        types.Integer,
        'Cell material',
        required=True,
        numeric=int,
        before=lambda value: value.suffix if isinstance(value, M_0) else value,
        invalid=lambda self, value: not 0 <= value <= 99_999_999,
    )
    density = _field.Field(
        types.Real,
        'Cell density',
        invalid=lambda self, value: (value is not None and self.material == 0) or (value is None and self.material != 0),
    )
    geometry = _field.Field(types.Geometry, 'Cell geometry', required=True, numeric=(), before=lambda value: types.Geometry(str(value.number)) if isinstance(value, SURFACES) else value)
    options = _field.Field.tuple(cell.CellOption, 'Cell options', numeric=())

    _REGEX = re.compile(rf'\A(\S+)( \S+)((?<! 0) \S+|(?<= 0))( [^a-z]+)((?: (?:{cell.CellOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

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
