import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ..Surface import Surface
from ... import literal


class P(Surface):
    """
    Represents p surface cards.
    """

    pass


class P_0(P):
    """
    Represents p surface cards, form #0.

    Attributes:
        prefix: p surface card `prefix` parameter.
        j: p surface card `j` parameter.
        n: p surface card `n` parameter.
        keyword: p surface card `P` symbol.
        a: p surface card `A` parameter.
        b: p surface card `B` parameter.
        c: p surface card `C` parameter.
        d: p surface card `D` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'P'] | str = abc.Terminal[r'P']('P')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
    c: literal.Real | int | float | decimal.Decimal | str
    d: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates p surface cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes p surface cards, form #0.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of p surface cards, form #0.
        """

        vis = shapes.Plane(float(self.a), float(self.b), float(self.c), float(self.d))

        return vis


class P_1(P):
    """
    Represents p surface cards, form #1.

    Attributes:
        j: p surface card `j` parameter.
        n: p surface card `n` parameter.
        keyword: p surface card `P` symbol.
        x1: p surface card `x1` parameter.
        y1: p surface card `y1` parameter.
        z1: p surface card `z1` parameter.
        x2: p surface card `x2` parameter.
        y2: p surface card `y2` parameter.
        z2: p surface card `z2` parameter.
        x3: p surface card `x3` parameter.
        y3: p surface card `y3` parameter.
        z3: p surface card `z3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'P'] | str = abc.Terminal[r'P']('P')
    x1: literal.Real | int | float | decimal.Decimal | str
    y1: literal.Real | int | float | decimal.Decimal | str
    z1: literal.Real | int | float | decimal.Decimal | str
    x2: literal.Real | int | float | decimal.Decimal | str
    y2: literal.Real | int | float | decimal.Decimal | str
    z2: literal.Real | int | float | decimal.Decimal | str
    x3: literal.Real | int | float | decimal.Decimal | str
    y3: literal.Real | int | float | decimal.Decimal | str
    z3: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates p surface cards, form #1.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes p surface cards, form #1.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of p surface cards, form #1.
        """

        a = numpy.array((float(self.x2) - float(self.x1), float(self.y2) - float(self.y1), float(self.z2) - float(self.z1)))
        b = numpy.array((float(self.x3) - float(self.x1), float(self.y3) - float(self.y1), float(self.z3) - float(self.z1)))
        n = numpy.cross(a, b)

        vis = shapes.Plane(n[0], n[1], n[2], n[0] * float(self.x1) + n[1] * float(self.y1) + n[2] * float(self.z1))

        return vis
