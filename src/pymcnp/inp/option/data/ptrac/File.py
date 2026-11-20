import typing

from ..... import abc
from ..Ptrac import Ptrac


class File(Ptrac):
    """
    Represents file ptrac data options.

    Attributes:
        keyword: file ptrac data option ``r'FILE'`` symbol.
        equals: file ptrac data option ``r'='`` symbol.
        value: file ptrac data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FILE'] = abc.Terminal[r'FILE']('FILE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:HDF5|ASC|BIN|AOV|BOV)']
