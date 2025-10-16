import re
import typing

from . import _type
from .. import errors


class _Embedded(_type._Nonterminal):
    """
    Represents MCNP lattice embedded expressions.

    Attributes:
        left: Left abstract syntax tree.
        right: Right abstract syntax tree.
    """

    def __init__(self, left: _type._Nonterminal, right: _type._Nonterminal):
        """
        Initializes `_Embedded`.

        Parameters:
            left: Left abstract syntax tree.
            right: Right abstract syntax tree.

        Returns:
            `_Embedded`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert left is not None
        assert right is not None

        self.left = left
        self.right = right

    @staticmethod
    def from_mcnp(tokens):
        """
        Initializes _Embedded`.

        Parameters:
            left: Left _Embedded syntax tree.
            right: Right abstract syntax tree.

        _Embeddedns:
            `_Embedded`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if not tokens:
            raise SyntaxError

        if tokens[0] == '(':
            left, tokens = _Paren.from_mcnp(tokens)
        elif tokens[1:] and tokens[1] == '[':
            left, tokens = _Range.from_mcnp(tokens)
        else:
            left, tokens = _Digit.from_mcnp(tokens)

        while tokens and tokens[0] == '<':
            tokens = tokens[1:]

            if tokens and tokens[0] == '(':
                right, tokens = _Paren.from_mcnp(tokens)
            elif tokens[1:] and tokens[1] == '[':
                right, tokens = _Range.from_mcnp(tokens)
            else:
                right, tokens = _Digit.from_mcnp(tokens)

            left = _Embedded(left, right)

        return left, tokens

    def to_mcnp(self):
        """
        Generates INP from `_Embedded`.

        Returns:
            INP for `_Embedded`.
        """

        return f'{self.left}<{self.right}'


class _Range(_type._Nonterminal):
    """
    Represents MCNP lattice range expressions.

    Attributes:
        cell: Cell number.
        i: Index in the i-direction.
        k: Index in the j-direction.
        j: Index in the k-direction.
    """

    def __init__(self, cell: _type._Nonterminal, i: _type._Nonterminal, j: _type._Nonterminal, k: _type._Nonterminal):
        """
        Initializes `_Range`.

        Parameters:
            cell: Cell number.
            i: Index in the i-direction.
            k: Index in the j-direction.
            j: Index in the k-direction.

        Returns:
            `_Range`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert cell is not None
        assert i is not None
        assert j is not None
        assert k is not None

        self.cell: typing.Final[_type._Nonterminal] = cell
        self.i: typing.Final[_type._Nonterminal] = i
        self.j: typing.Final[_type._Nonterminal] = j
        self.k: typing.Final[_type._Nonterminal] = k

    @staticmethod
    def from_mcnp(tokens):
        """
        Generates `_Range` from INP.

        Parameters:
            INP for `_Range`.

        Returns:
            `_Range`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        cell, tokens = _Digit.from_mcnp(tokens)

        assert tokens and tokens[0] == '['

        if (tokens[1:] and tokens[1] == ':') or (tokens[2:] and tokens[2] == ':'):
            i, tokens = _Index.from_mcnp(tokens[1:])
        else:
            i, tokens = _Digit.from_mcnp(tokens[1:])

        if (tokens[1:] and tokens[1] == ':') or (tokens[2:] and tokens[2] == ':'):
            j, tokens = _Index.from_mcnp(tokens)
        else:
            j, tokens = _Digit.from_mcnp(tokens)

        if (tokens[1:] and tokens[1] == ':') or (tokens[2:] and tokens[2] == ':'):
            k, tokens = _Index.from_mcnp(tokens)
        else:
            k, tokens = _Digit.from_mcnp(tokens)

        if not tokens or tokens[0] != ']':
            raise SyntaxError

        return _Range(cell, i, j, k), tokens[1:]

    def to_mcnp(self):
        """
        Generates INP from `_Range`.

        Returns:
            INP for `_Range`.
        """

        return f'{self.cell}[{self.i} {self.j} {self.k}]'


class _Paren(_type._Nonterminal):
    """
    Represents MCNP lattice parenthesized expressions.

    Attributes:
        ast: Lattice abstract syntax tree.
    """

    def __init__(self, ast):
        """
        Initializes `_Paren`.

        Parameters:
            ast: Lattice abstract syntax tree.

        Returns:
            `_Paren`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert ast is not None

        self.ast: typing.Final[_type._Nonterminal] = ast

    @staticmethod
    def from_mcnp(tokens):
        """
        Generates `_Paren` from INP.

        Parameters:
            INP for `_Paren`.

        Returns:
            `_Paren`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        assert tokens[0] == '('

        ast, tokens = _Embedded.from_mcnp(tokens[1:])

        assert tokens[0] == ')'

        return _Paren(ast), tokens[1:]

    def to_mcnp(self):
        """
        Generates INP from `_Paren`.

        Returns:
            INP for `_Paren`.
        """

        return f'({self.ast})'


class _Index(_type._Nonterminal):
    """
    Represents MCNP lattice digits.

    Attributes:
        lower: Lower bound.
        upper: Upper bound.
    """

    _REGEX = re.compile(r'\A(\d+?)\Z')

    def __init__(self, lower: _type._Nonterminal, upper: _type._Nonterminal):
        """
        Initializes `_Index`.

        Parameters:
            lower: Lower bound.
            upper: Upper bound.

        Returns:
            `_Index`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert lower is not None
        assert upper is not None

        self.lower: typing.Final[_type._Nonterminal] = lower
        self.upper: typing.Final[_type._Nonterminal] = upper

    @staticmethod
    def from_mcnp(tokens):
        """
        Generates `_Index` from INP.

        Parameters:
            INP for `_Index`.

        Returns:
            `_Index`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        lower, tokens = _Digit.from_mcnp(tokens)

        assert tokens[0] == ':'

        upper, tokens = _Digit.from_mcnp(tokens[1:])

        return _Index(lower, upper), tokens

    def to_mcnp(self):
        """
        Generates INP from `_Index`.

        Returns:
            INP for `_Index`.
        """

        return f'{self.lower}:{self.upper}'


class _Digit(_type._Nonterminal):
    """
    Represents MCNP lattice digits.

    Attributes:
        value: Surface or facet number.
    """

    _REGEX = re.compile(r'\A([+-]?\d+?)\Z')

    def __init__(self, value: str):
        """
        Initializes `_Digit`.

        Parameters:
            value: Surface or facet number.

        Returns:
            `_Digit`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        assert value is not None and self._REGEX.match(value)

        self.value: typing.Final[str] = value

    @staticmethod
    def from_mcnp(tokens):
        """
        Generates `_Digit` from INP.

        Parameters:
            INP for `_Digit`.

        Returns:
            `_Digit`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        if not tokens or not (value := _Digit._REGEX.match(tokens[0])):
            raise SyntaxError

        return _Digit(value[0]), tokens[1:]

    def to_mcnp(self):
        """
        Generates INP from `_Digit`.

        Returns:
            INP for `_Digit`.
        """

        return self.value


class Lattice(_type.Type):
    """
    Represents MCNP lattices.

    Attributes:
        ast: Lattice abstract syntax tree.
    """

    _REGEX = re.compile(r'\A((?:\s+|[+-]?\d+|\s*[:<)(\[\]|]\s*)+)\Z', re.IGNORECASE)

    def __init__(self, ast: _type._Nonterminal):
        """
        Initializes `Lattice`.

        Parameters:
            ast: Lattice abstract syntax tree.

        Returns:
            `Lattice`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if ast is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, ast)

        self.ast: typing.Final[_type._Nonterminal] = ast

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Lattice` from INP.

        Parameters:
            INP for `Lattice`.

        Returns:
            `Lattice`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        source = source.strip()

        tokens = [token[0] for token in re.finditer(Lattice._REGEX.pattern[6:-5], source)]

        if ''.join(tokens) != source:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        tokens = [token.strip() for token in tokens if token.strip()]

        try:
            left, tokens = _Embedded.from_mcnp(tokens)
            while tokens:
                right, tokens = _Embedded.from_mcnp(tokens)
                left = _Embedded(left, right)
        except SyntaxError:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        return Lattice(left)

    def to_mcnp(self):
        """
        Generates INP from `Lattice`.

        Returns:
            INP for `Lattice`.
        """

        return self.ast.to_mcnp()
