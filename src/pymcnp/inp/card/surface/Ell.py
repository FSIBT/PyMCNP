import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Ell(Surface):
    """
    Represents ell surface cards.

    Attributes:
        prefix: ell surface card `prefix` parameter.
        j: ell surface card `j` parameter.
        keyword: ell surface card `ELL` symbol.
        v1x: ell surface card `v1x` parameter.
        v1y: ell surface card `v1y` parameter.
        v1z: ell surface card `v1z` parameter.
        v2x: ell surface card `v2x` parameter.
        v2y: ell surface card `v2y` parameter.
        v2z: ell surface card `v2z` parameter.
        r: ell surface card `r` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'ELL'] | str = abc.Terminal[r'ELL']('ELL')
    v1x: literal.Real | int | float | decimal.Decimal | str
    v1y: literal.Real | int | float | decimal.Decimal | str
    v1z: literal.Real | int | float | decimal.Decimal | str
    v2x: literal.Real | int | float | decimal.Decimal | str
    v2y: literal.Real | int | float | decimal.Decimal | str
    v2z: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates ell surface cards.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Ell`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Ell`.
        """

        assert isinstance(self.r, literal.Real)

        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))

        if self.r > 0:
            f1, f2 = v1, v2
            center = (f1 + f2) / 2.0

            f_vec = f2 - f1
            f_dist = numpy.linalg.norm(f_vec)

            c = f_dist / 2.0
            a = float(self.r)

            b = numpy.sqrt(a**2 - c**2)
            v_dir = f_vec / f_dist if f_dist > 0 else numpy.array([1.0, 0.0, 0.0])

        elif self.r < 0:
            center = v1
            a = numpy.linalg.norm(v2)

            v_dir = v2 / a
            b = abs(float(self.r))

        vis = shapes.Ellipsoid(a, b)

        x_axis = numpy.array([1.0, 0.0, 0.0])
        dot_prod = numpy.clip(numpy.dot(x_axis, v_dir), -1.0, 1.0)
        angle_deg = numpy.degrees(numpy.arccos(dot_prod))

        if angle_deg > 1e-5:
            rot_axis = numpy.cross(x_axis, v_dir)
            rot_axis /= numpy.linalg.norm(rot_axis)
            vis = vis.rotate(axis=rot_axis, angle=angle_deg, center=(0.0, 0.0, 0.0))

        vis = vis.translate(vector=center)

        return vis
