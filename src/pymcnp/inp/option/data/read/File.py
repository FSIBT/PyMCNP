import typing
import dataclasses

from ..... import abc
from ..Read import Read


class File(Read):
    """
    Represents file read data options.

    Attributes:
        keyword: file read data option `FILE` symbol.
        equals: file read data option `=` symbol.
        filename: file read data option `filename` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FILE'] | str = abc.Terminal[r'FILE']('FILE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str
