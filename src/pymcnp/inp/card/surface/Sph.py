import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Sph(Surface):
    """
    Represents sph surface cards.

    Attributes:
        prefix: sph surface card `prefix` parameter.
        j: sph surface card `j` parameter.
        keyword: sph surface card `SPH` symbol.
        vx: sph surface card `vx` parameter.
        vy: sph surface card `vy` parameter.
        vz: sph surface card `vz` parameter.
        r: sph surface card `r` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'SPH'] | str = abc.Terminal[r'SPH']('SPH')
    vx: literal.Real | int | float | decimal.Decimal | str
    vy: literal.Real | int | float | decimal.Decimal | str
    vz: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates sph surface cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes sph surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of sph surface cards.
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.translate(numpy.array((float(self.vx), float(self.vy), float(self.vz))))

        return vis
