import typing

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Tz(Surface):
    """
    Represents tz surface cards.

    Attributes:
        prefix: tz surface card ``prefix`` parameter.
        j: tz surface card ``j`` parameter.
        n: tz surface card ``n`` parameter.
        keyword: tz surface card ``r'TZ'`` symbol.
        x: tz surface card ``x`` parameter.
        y: tz surface card ``y`` parameter.
        z: tz surface card ``z`` parameter.
        a: tz surface card ``A`` parameter.
        b: tz surface card ``B`` parameter.
        c: tz surface card ``C`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'TZ'] = abc.Terminal[r'TZ']('TZ')
    x: literal.Real
    y: literal.Real
    z: literal.Real
    a: literal.Real
    b: literal.Real
    c: literal.Real

    def __post_init__(self) -> None:
        """
        Validates tz surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes tz surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of tz surface cards.
        """

        vis = shapes.Torus(float(self.b), float(self.c), float(self.a))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
