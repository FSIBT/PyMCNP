import typing
import dataclasses

import collections
from .... import abc
from ..Cell import Cell
from ... import literal
from ... import group


class Fill(Cell):
    """
    Represents fill cell options.
    """

    pass


class Fill_0(Fill):
    """
    Represents fill cell options, form #0.

    Attributes:
        keyword: fill cell option `FILL` symbol.
        equals: fill cell option `=` symbol.
        n: fill cell option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'FILL'] | str = abc.Terminal[r'FILL']('FILL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates fill cell options, form #0.
        """

        assert isinstance(self.n, literal.Integer)

        if not (0 <= self.n <= 99_999_999):
            raise abc.Error


class Fill_1(Fill):
    """
    Represents fill cell options, form #1.

    Attributes:
        keyword: fill cell option `FILL` symbol.
        equals: fill cell option `=` symbol.
        n: fill cell option `n` parameter.
        parenthesis_open: fill cell option `(` symbol.
        q: fill cell option `q` parameter.
        parenthesis_close: fill cell option `)` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'FILL'] | str = abc.Terminal[r'FILL']('FILL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
    parenthesis_open: typing.Annotated[abc.Terminal, r'\('] | str = abc.Terminal[r'\(']('(')
    q: group.Rotation | literal.Integer | int | str
    parenthesis_close: typing.Annotated[abc.Terminal, r'\)'] | str = abc.Terminal[r'\)'](')')

    def __post_init__(self) -> None:
        """
        Validates fill cell options, form #1.
        """

        assert isinstance(self.n, literal.Integer)

        if not (0 <= self.n <= 99_999_999):
            raise abc.Error


class Fill_2(Fill):
    """
    Represents fill cell options, form #2.

    Attributes:
        keyword: fill cell option `FILL` symbol.
        equals: fill cell option `=` symbol.
        i1: fill cell option `i1` parameter.
        colon_0: fill cell option `:` symbol.
        i2: fill cell option `i2` parameter.
        j1: fill cell option `j1` parameter.
        colon_1: fill cell option `:` symbol.
        j2: fill cell option `j2` parameter.
        k1: fill cell option `k1` parameter.
        colon_2: fill cell option `:` symbol.
        k2: fill cell option `k2` parameter.
        nijk: fill cell option `nijk` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FILL'] | str = abc.Terminal[r'FILL']('FILL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    i: literal.LatticeRange | str
    j: literal.LatticeRange | str
    k: literal.LatticeRange | str
    nijk: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')


class Fill_3(Fill):
    """
    Represents fill cell options, form #3.

    Attributes:
        keyword: fill cell option `FILL` symbol.
        equals: fill cell option `=` symbol.
        i1: fill cell option `i1` parameter.
        colon_0: fill cell option `:` symbol.
        i2: fill cell option `i2` parameter.
        j1: fill cell option `j1` parameter.
        colon_1: fill cell option `:` symbol.
        j2: fill cell option `j2` parameter.
        k1: fill cell option `k1` parameter.
        colon_2: fill cell option `:` symbol.
        k2: fill cell option `k2` parameter.
        nijk: fill cell option `nijk` parameter.
        parenthesis_open: fill cell option `(` symbol.
        q: fill cell option `q` parameter.
        parenthesis_close: fill cell option `)` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FILL'] | str = abc.Terminal[r'FILL']('FILL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    i: literal.LatticeRange | str
    j: literal.LatticeRange | str
    k: literal.LatticeRange | str
    nijk: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
    parenthesis_open: typing.Annotated[abc.Terminal, r'\('] | str = abc.Terminal[r'\(']('(')
    q: group.Rotation | literal.Integer | int | str
    parenthesis_close: typing.Annotated[abc.Terminal, r'\)'] | str = abc.Terminal[r'\)'](')')
