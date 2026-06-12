import typing
import dataclasses

from ... import abc
from ..Block import Block
from .. import line


class Header(Block):
    """
    Represents header blocks.

    Attributes:
        magic: header block `   -1\n` symbol.
        code: header block `code` parameter.
        version: header block `version` parameter.
        code_date: header block code `date` parameter.
        run_datetime: header block run `datetime` parameter.
        title: header block title line.
        v: header block v line.
        n: header block n line.
        l: header block l line.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    magic: typing.Annotated[abc.Terminal, r'   -1']
    newline_0: typing.Annotated[abc.Terminal, r'\n']
    code: typing.Annotated[abc.Terminal, r'.{8}']
    version: typing.Annotated[abc.Terminal, r'.{25}']
    code_date: typing.Annotated[abc.Terminal, r'.{9}']
    run_datetime: typing.Annotated[abc.Terminal, r'.{18}']
    newline_1: typing.Annotated[abc.Terminal, r'\n']
    title: typing.Annotated[abc.Terminal, r'.{80}']
    newline_2: typing.Annotated[abc.Terminal, r'\n']
    v: line.V
    newline_3: typing.Annotated[abc.Terminal, r'\n']
    n: line.N
    newline_4: typing.Annotated[abc.Terminal, r'\n ']
    l: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r' \d\d\d|  \d\d|   \d'], typing.Annotated[abc.Terminal, r'\n |']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    newline_5: typing.Annotated[abc.Terminal, r'\n']
