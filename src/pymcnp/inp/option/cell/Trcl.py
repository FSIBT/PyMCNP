import typing
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal
from ... import group


class Trcl(Cell):
    """
    Represents trcl cell options.
    """

    pass


class Trcl_0(Trcl):
    """
    Represents trcl cell options, form #0.

    Attributes:
        prefix: trcl cell option `*` symbol.
        keyword: trcl cell option `TRCL` symbol.
        equals: trcl cell option `=` symbol.
        n: trcl cell option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'TRCL'] | str = abc.Terminal[r'TRCL']('TRCL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates trcl cell options, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.n, literal.Integer)

        if not (0 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class Trcl_1(Trcl):
    """
    Represents trcl cell options, form #1.

    Attributes:
        prefix: trcl cell option `*` symbol.
        keyword: trcl cell option `TRCL` symbol.
        equals: trcl cell option `=` symbol.
        o_xyz_m: trcl cell option `o_xyz_m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'TRCL'] | str = abc.Terminal[r'TRCL']('TRCL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    o_xyz_m: group.Rotation | str


class Trcl_2(Trcl):
    """
    Represents trcl cell options, form #2.

    Attributes:
        prefix: trcl cell option `*` symbol.
        keyword: trcl cell option `TRCL` symbol.
        equals: trcl cell option `=` symbol.
        parenthesis_open: trcl cell option `(` symbol.
        o_xyz_m: trcl cell option `o_xyz_m` parameter.
        parenthesis_close: trcl cell option `)` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'TRCL'] | str = abc.Terminal[r'TRCL']('TRCL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    parenthesis_open: typing.Annotated[abc.Terminal, r'\('] | str = abc.Terminal[r'\(']('(')
    o_xyz_m: group.Rotation | str
    parenthesis_close: typing.Annotated[abc.Terminal, r'\)'] | str = abc.Terminal[r'\)'](')')
