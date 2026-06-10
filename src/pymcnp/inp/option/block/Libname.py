import typing
import dataclasses

from .... import abc
from ..Block import Block


class Libname(Block):
    """
    Represents libname block dawwg data options.

    Attributes:
        keyword: libname block suboption `LIBNAME` symbol.
        equals: libname block suboption `=` symbol.
        value: libname block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LIBNAME'] | str = abc.Terminal[r'LIBNAME']('LIBNAME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'\S+'] | str
