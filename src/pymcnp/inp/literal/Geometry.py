from __future__ import annotations

import re
import abc as _abc
import typing
import dataclasses

from ... import abc
from ... import _show
from .Number import Integer


@dataclasses.dataclass
class Missing(abc.Error):
    """
    Represents references to a cell or surface that is not in the file.

    Attributes:
        kind: ``'cell'`` or ``'surface'``.
        number: Number of the missing cell or surface.
    """

    kind: str = ''
    number: str = ''


def _look_up(cards: dict[str, abc.Visualization], number: str, kind: str) -> abc.Visualization:
    """
    Looks up the visualization of a cell or surface.

    Raises:
        Missing: The cell or surface is not in the file.
    """

    try:
        return cards[Integer(number)]
    except KeyError:
        raise Missing(f'{kind.capitalize()} {number} is not in the file.', number, kind=kind, number=number) from None


class _Subexpression(abc.Nonterminal):
    pass


class _Number(abc.Terminal):
    _pattern = re.compile(r'([+-]?\d+(?:\.\d+)?)', re.IGNORECASE)


class _Primary(_Subexpression):
    @_abc.abstractmethod
    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista, is_cell: bool = False) -> abc.Visualization:
        raise NotImplementedError


class _Primary_1(_Primary):
    ast: _Number

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista, is_cell: bool = False) -> abc.Visualization:
        if self.ast.startswith('-'):
            return _look_up(surfaces, self.ast[1:], 'surface')
        elif self.ast.startswith('+'):
            return ~_look_up(surfaces, self.ast[1:], 'surface')
        elif is_cell:
            return _look_up(cells, self.ast, 'cell')
        else:
            return ~_look_up(surfaces, self.ast, 'surface')


class _Complement(_Subexpression):
    operator: typing.Annotated[abc.Terminal, r'#'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    ast: _Primary

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista, is_cell: bool = False) -> abc.Visualization:
        # ``#N`` complements cell ``N`` and ``#(...)`` complements the region in parentheses.
        if self.operator != '#':
            return self.ast.to_show(surfaces, cells, shapes, False)

        return ~self.ast.to_show(surfaces, cells, shapes, isinstance(self.ast, _Primary_1))


class _IntersectionPrime(_Subexpression):
    pass


class _Intersection(_Subexpression):
    ast_left: _Complement
    ast_right: _IntersectionPrime

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista, is_cell: bool = False) -> abc.Visualization:
        if isinstance(self.ast_right, (_IntersectionPrime_0, _IntersectionPrime_1)):
            return self.ast_left.to_show(surfaces, cells, shapes, is_cell) & self.ast_right.ast.to_show(surfaces, cells, shapes, is_cell)
        else:
            return self.ast_left.to_show(surfaces, cells, shapes, is_cell)


class _UnionPrime(_Subexpression):
    pass


class _Union(_Subexpression):
    ast_left: _Intersection
    ast_right: _UnionPrime

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista, is_cell: bool = False) -> abc.Visualization:
        if isinstance(self.ast_right, _UnionPrime_0):
            return self.ast_left.to_show(surfaces, cells, shapes, is_cell) | self.ast_right.ast.to_show(surfaces, cells, shapes, is_cell)
        else:
            return self.ast_left.to_show(surfaces, cells, shapes, is_cell)


class _IntersectionPrime_0(_IntersectionPrime):
    operator: typing.Annotated[abc.Terminal, r' *(?:\$.+)?\n {1,5} *| +&(?: *\$.*)?\n +| +'] = abc.Terminal[r' *(?:\$.+)?\n {1,5} *| +&(?: *\$.*)?\n +| +'](' ')
    ast: _Intersection


class _IntersectionPrime_1(_IntersectionPrime):
    operator_left: typing.Annotated[abc.Terminal, r'\('] = abc.Terminal[r'\(']('(')
    ast: _Union
    operator_right: typing.Annotated[abc.Terminal, r'\)'] = abc.Terminal[r'\)'](')')


class _IntersectionPrime_2(_IntersectionPrime):
    pass


class _UnionPrime_0(_UnionPrime):
    operator: typing.Annotated[abc.Terminal, r' *: *'] = abc.Terminal[r' *: *'](':')
    ast: _Union


class _UnionPrime_1(_UnionPrime):
    pass


class _Primary_0(_Primary):
    operator_left: typing.Annotated[abc.Terminal, r'\('] = abc.Terminal[r'\(']('(')
    ast: _Union
    operator_right: typing.Annotated[abc.Terminal, r'\)'] = abc.Terminal[r'\)'](')')

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista, is_cell: bool = False) -> abc.Visualization:
        """
        Generates ``Visualization`` from ``_Unary``.

        Paramaters:
            surfaces: Dictionary of surfaces and visualizations.
            shapes: Collection of shapes.

        Returns:
            ``Visualization`` for ``_Unary``
        """

        return self.ast.to_show(surfaces, cells, shapes, is_cell)


def _operand(geometry: Geometry) -> str:
    text = str(geometry.ast).strip()

    depth = 0
    for char in text:
        depth += char == '('
        depth -= char == ')'
        if char == ':' and depth == 0:
            return f'({text})'

    return text


class Geometry(_Subexpression):
    """
    Represents geometry literals.

    Attributes:
        ast: geometry literal ``ast`` parameter.
    """

    ast: _Union

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista, is_cell: bool = False) -> abc.Visualization:
        """
        Visualizes geometry formulas.

        Parameters:
            surfaces: Visualizations of surface cards.
            cells: Visualizations of cell cards.
            shapes: Collection of shapes.

        Returns:
            Visualization of geometry formulas.
        """

        return self.ast.to_show(surfaces, cells, shapes, False)

    def __and__(a: Geometry, b: Geometry) -> Geometry:
        """
        Intersects geometry formulas.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            Intersections of geometry formulas.
        """

        return Geometry.from_mcnp(f'{_operand(a)} {_operand(b)}')[0]

    def __or__(a: Geometry, b: Geometry) -> Geometry:
        """
        Unites geometry formulas.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            Unions of geometry formulas.
        """

        return Geometry.from_mcnp(f'({a.ast}:{b.ast})')[0]

    def __invert__(self) -> Geometry:
        """
        Inverts geometry formulas.

        Returns:
            Complements of geomtry formulas.
        """

        return Geometry.from_mcnp(f'#({self.ast})')[0]
