import typing
import dataclasses

from ..... import abc
from ..Ptrac import Ptrac


class File(Ptrac):
    """
    Represents file ptrac data options.

    Attributes:
        keyword: file ptrac data option `FILE` symbol.
        equals: file ptrac data option `=` symbol.
        value: file ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FILE'] | str = abc.Terminal[r'FILE']('FILE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:HDF5|ASC|BIN|AOV|BOV)'] | str
