import typing
import dataclasses

from ... import abc
from ..Block import Block
from .. import line


class Header(Block):
    """
    Represents header blocks.

    Attributes:
        magic: header block ``'   -1\\n'`` symbol.
        code: header block `code` parameter.
        version: header block `version` parameter.
        code_date: header block code `date` parameter.
        run_datetime: header block run `datetime` parameter.
        title: header block title line.
        v: header block v line.
        n: header block n line.
        l: header block l line.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    magic: typing.Annotated[abc.Terminal, r'   -1'] = dataclasses.field(kw_only=True)
    newline_0: typing.Annotated[abc.Terminal, r'\n'] = dataclasses.field(kw_only=True)
    code: typing.Annotated[abc.Terminal, r'.{8}'] = dataclasses.field(kw_only=True)
    version: typing.Annotated[abc.Terminal, r'.{25}'] = dataclasses.field(kw_only=True)
    code_date: typing.Annotated[abc.Terminal, r'.{9}'] = dataclasses.field(kw_only=True)
    run_datetime: typing.Annotated[abc.Terminal, r'.{18}'] = dataclasses.field(kw_only=True)
    newline_1: typing.Annotated[abc.Terminal, r'\n'] = dataclasses.field(kw_only=True)
    title: typing.Annotated[abc.Terminal, r'.{80}'] = dataclasses.field(kw_only=True)
    newline_2: typing.Annotated[abc.Terminal, r'\n'] = dataclasses.field(kw_only=True)
    v: line.V = dataclasses.field(kw_only=True)
    newline_3: typing.Annotated[abc.Terminal, r'\n'] = dataclasses.field(kw_only=True)
    n: line.N = dataclasses.field(kw_only=True)
    newline_4: typing.Annotated[abc.Terminal, r'\n '] = dataclasses.field(kw_only=True)
    l: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r' \d\d\d|  \d\d|   \d'], typing.Annotated[abc.Terminal, r'\n |']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    newline_5: typing.Annotated[abc.Terminal, r'\n'] = dataclasses.field(kw_only=True)
