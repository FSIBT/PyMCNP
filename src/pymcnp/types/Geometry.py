import re
import typing

from . import _type
from .. import _show
from .. import errors


def _operand(tokens):
    """
    Parses one geometry operand (unary, parenthesized or digit).
    """

    if not tokens:
        raise SyntaxError

    if tokens[0] in {'+', '-', '#'}:
        return _Unary.from_mcnp(tokens)
    if tokens[0] == '(':
        return _Paren.from_mcnp(tokens)
    return _Digit.from_mcnp(tokens)


class _Intersection(_type._Nonterminal):
    """
    Represents MCNP geometry intersection expressions.

    Attributes:
        left: Left abstract syntax tree.
        right: Right abstract syntax tree.
    """

    def __init__(self, left: _type._Nonterminal, right: _type._Nonterminal):
        """
        Initializes `_Intersection`.

        Parameters:
            left: Left abstract syntax tree.
            right: Right abstract syntax tree.

        Returns:
            `_Intersection`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert left is not None
        assert right is not None

        self.left: typing.Final[_type._Nonterminal] = left
        self.right: typing.Final[_type._Nonterminal] = right

    @staticmethod
    def from_mcnp(tokens: list[str]):
        """
        Generates `_Intersection` from INP.

        Parameters:
            tokens: Geometry tokens.

        Returns:
            `_Intersection`, tokens

        Raises:
            SyntaxError: SYNTAX_TYPE.
        """

        left, tokens = _operand(tokens)

        while tokens and tokens[0] in {'', ' ', '('}:
            right, tokens = _operand(tokens if tokens[0] == '(' else tokens[1:])
            left = _Intersection(left, right)

        return left, tokens

    def to_mcnp(self):
        """
        Generates INP from `_Intersection`.

        Returns:
            INP for `_Intersection`.
        """

        return f'{self.left} {self.right}'

    def to_show(self, surfaces: dict[str, _show.Shape], cells: dict[str, _show.Shape], shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `_Intersection`.

        Paramaters:
            surfaces: Dictionary of surfaces and visualizations.
            shapes: Collection of shapes.

        Returns:
            `Visualization` for `_Intersection`
        """

        return self.left.to_show(surfaces, cells, shapes) & self.right.to_show(surfaces, cells, shapes)


class _Union(_type._Nonterminal):
    """
    Represents MCNP geometry union expressions.

    Attributes:
        left: Left abstract syntax tree.
        right: Right abstract syntax tree.
    """

    def __init__(self, left: _type._Nonterminal, right: _type._Nonterminal):
        """
        Initializes `_Union`.

        Parameters:
            left: Left abstract syntax tree.
            right: Right abstract syntax tree.

        Returns:
            `_Union`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert left is not None
        assert right is not None

        self.left: typing.Final[_type._Nonterminal] = left
        self.right: typing.Final[_type._Nonterminal] = right

    @staticmethod
    def from_mcnp(tokens: list[str]):
        """
        Generates `_Union` from INP.

        Parameters:
            tokens: Geometry tokens.

        Returns:
            `_Union`, tokens

        Raises:
            SyntaxError: SYNTAX_TYPE.
        """

        left, tokens = _Intersection.from_mcnp(tokens)

        while tokens and tokens[0] == ':':
            right, tokens = _Intersection.from_mcnp(tokens[1:])
            left = _Union(left, right)

        return left, tokens

    def to_mcnp(self):
        """
        Generates INP from `_Union`.

        Returns:
            INP for `_Union`.
        """

        return f'{self.left}:{self.right}'

    def to_show(self, surfaces: dict[str, _show.Shape], cells: dict[str, _show.Shape], shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `_Union`.

        Paramaters:
            surfaces: Dictionary of surfaces and visualizations.
            shapes: Collection of shapes.

        Returns:
            `Visualization` for `_Union`
        """

        return self.left.to_show(surfaces, cells, shapes) | self.right.to_show(surfaces, cells, shapes)


class _Unary(_type._Nonterminal):
    """
    Represents MCNP geometry unary expressions.

    Attributes:
        operator: Unary operator.
        operand: Operand abstract syntax tree.
    """

    def __init__(self, operator: str, operand: _type._Nonterminal):
        """
        Initializes `_Unary`.

        Parameters:
            operator: Unary operator.
            operand: Operand abstract syntax tree.

        Returns:
            `_Unary`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert operator is not None and operator in {'+', '-', '#'}
        assert operand is not None

        self.operator: typing.Final[str] = operator
        self.operand: typing.Final[_type._Nonterminal] = operand

    @staticmethod
    def from_mcnp(tokens: list[str]):
        """
        Generates `_Unary` from INP.

        Parameters:
            tokens: Geometry tokens.

        Returns:
            `_Unary`, tokens

        Raises:
            SyntaxError: SYNTAX_TYPE.
        """

        assert tokens[0] in {'+', '-', '#'}

        operator = tokens[0]
        if operator == '#' and tokens[1:] and tokens[1] == '(':
            ast, tokens = _Paren.from_mcnp(tokens[1:])
        elif tokens[1:] and _Digit._REGEX.match(tokens[1]):
            ast, tokens = _Digit.from_mcnp(tokens[1:])
        else:
            raise SyntaxError

        return _Unary(operator, ast), tokens

    def to_mcnp(self):
        """
        Generates INP from `_Unary`.

        Returns:
            INP for `_Unary`.
        """

        return f'{self.operator}{self.operand}'

    def to_show(self, surfaces: dict[str, _show.Shape], cells: dict[str, _show.Shape], shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `_Unary`.

        Paramaters:
            surfaces: Dictionary of surfaces and visualizations.
            shapes: Collection of shapes.

        Returns:
            `Visualization` for `_Unary`
        """

        if self.operator == '+':
            return self.operand.to_show(surfaces, cells, shapes)
        elif self.operator == '-':
            return ~self.operand.to_show(surfaces, cells, shapes)
        else:
            if isinstance(self.operand, _Digit):
                if self.operand.value in cells:
                    return cells[self.operand.value]
                elif self.operand.value in surfaces:
                    return surfaces[self.operand.value]
                else:
                    raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, self.operand.value)
            else:
                return ~self.operand.to_show(surfaces, cells, shapes)


class _Paren(_type._Nonterminal):
    """
    Represents MCNP geometry parenthesized expressions.

    Attributes:
        ast: Geometry abstract syntax tree.
    """

    def __init__(self, ast: _type._Nonterminal):
        """
        Initializes `_Paren`.

        Parameters:
            ast: Geometry abstract syntax tree.

        Returns:
            `_Paren`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert ast is not None

        self.ast: typing.Final[_type._Nonterminal] = ast

    @staticmethod
    def from_mcnp(tokens: list[str]):
        """
        Generates `_Paren` from INP.

        Parameters:
            tokens: Geometry tokens.

        Returns:
            `_Paren`, tokens

        Raises:
            SyntaxError.
        """

        assert tokens[0] == '('

        ast, tokens = _Union.from_mcnp(tokens[1:])

        if not tokens or tokens[0] != ')':
            raise SyntaxError

        return _Paren(ast), tokens[1:]

    def to_mcnp(self):
        """
        Generates INP from `_Paren`.

        Returns:
            INP for `_Paren`.
        """

        return f'({self.ast})'

    def to_show(self, surfaces: dict[str, _show.Shape], cells: dict[str, _show.Shape], shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `_Paren`.

        Paramaters:
            surfaces: Dictionary of surfaces and visualizations.
            shapes: Collection of shapes.

        Returns:
            `Visualization` for `_Paren`
        """

        return self.ast.to_show(surfaces, cells, shapes)


class _Digit(_type._Nonterminal):
    """
    Represents MCNP geometry digits.

    Attributes:
        value: Surface or facet number.
    """

    _REGEX = re.compile(r'\A(\d+(?:[.]\d+)?)\Z')

    def __init__(self, value: str):
        """
        Initializes `_Digit`.

        Parameters:
            value: Surface or facet number.

        Returns:
            `_Digit`, tokens

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert value is not None and self._REGEX.match(value)

        self.value: typing.Final[str] = value

    @staticmethod
    def from_mcnp(tokens: list[str]):
        """
        Generates `_Digit` from INP.

        Parameters:
            tokens: Geometry tokens.

        Returns:
            `_Digit`, tokens

        Raises:
            SyntaxError.
        """

        assert _Digit._REGEX.match(tokens[0])

        return _Digit(tokens[0]), tokens[1:]

    def to_mcnp(self):
        """
        Generates INP from `_Digit`.

        Returns:
            INP for `_Digit`.
        """

        return self.value

    def to_show(self, surfaces: dict[str, _show.Shape], cells: dict[str, _show.Shape], shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `_Digit`.

        Paramaters:
            surfaces: Dictionary of surfaces and visualizations.
            shapes: Collection of shapes.

        Returns:
            `Visualization` for `_Digit`
        """

        if self.value in surfaces:
            return surfaces[self.value]
        else:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, self.value)


class Geometry(_type.Type):
    """
    Represents MCNP geometries.

    Attributes:
        ast: Geometry abstract syntax tree.
    """

    _REGEX = re.compile(r'\A((?:\s*[:]\s*|\s+|\d+(?:\.\d+)?|[(+#-]\s*|\s*[)])+)\Z', re.IGNORECASE)

    def __init__(self, ast: _type._Nonterminal):
        """
        Initializes `Geometry`.

        Parameters:
            ast: Geometry abstract syntax tree.

        Returns:
            `Geometry`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if ast is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, ast)

        self.ast: typing.Final[_type._Nonterminal] = ast

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Geometry` from INP.

        Parameters:
            INP for `Geometry`.

        Returns:
            `Geometry`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        source = source.strip()

        tokens = [token[0] for token in re.finditer(Geometry._REGEX.pattern[6:-5], source)]

        if ''.join(tokens) != source:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        tokens = [(token.strip() or ' ') for token in tokens]

        try:
            ast, tokens = _Union.from_mcnp(tokens)
        except SyntaxError as err:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source) from err

        assert not tokens

        return Geometry(ast)

    def to_mcnp(self):
        """
        Generates INP from `Geometry`.

        Returns:
            INP for `Geometry`.
        """

        return self.ast.to_mcnp()

    @staticmethod
    def _ast(other):
        if isinstance(other, Geometry):
            return other.ast
        if hasattr(other, 'number'):
            return _Digit(str(other.number))
        return None

    def __and__(a, b):
        """
        Intersects `Geometry` (MCNP: space).

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Geometry` intersection.
        """

        if (right := Geometry._ast(b)) is None:
            return NotImplemented

        wrap = lambda ast: _Paren(ast) if isinstance(ast, _Union) else ast
        return Geometry(_Intersection(wrap(a.ast), wrap(right)))

    def __or__(a, b):
        """
        Unites `Geometry` (MCNP: colon).

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Geometry` union.
        """

        if (right := Geometry._ast(b)) is None:
            return NotImplemented

        return Geometry(_Union(a.ast, right))

    def __rand__(a, b):
        return Geometry(_Digit(str(b.number))) & a if hasattr(b, 'number') else NotImplemented

    def __ror__(a, b):
        return Geometry(_Digit(str(b.number))) | a if hasattr(b, 'number') else NotImplemented

    def _signed(self, operator):
        if not isinstance(self.ast, _Digit):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, self.to_mcnp())

        return Geometry(_Unary(operator, self.ast))

    def __neg__(self):
        """
        Negatives `Geometry` (negative sense of a surface).

        Returns:
            `Geometry` negative.

        Raises:
            TypesError: SEMANTICS_TYPE, if not a single surface.
        """

        return self._signed('-')

    def __pos__(self):
        """
        Positives `Geometry` (positive sense of a surface).

        Returns:
            `Geometry` positive.

        Raises:
            TypesError: SEMANTICS_TYPE, if not a single surface.
        """

        return self._signed('+')

    def __invert__(self):
        """
        Complements `Geometry` (MCNP: `#(...)`).

        Returns:
            `Geometry` complement.
        """

        return Geometry(_Unary('#', _Paren(self.ast) if not isinstance(self.ast, (_Paren, _Digit)) else self.ast))
