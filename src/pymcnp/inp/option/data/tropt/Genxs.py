import typing

from ..... import abc
from ..Tropt import Tropt


class Genxs(Tropt):
    """
    Represents genxs tropt data options.
    """


class Genxs_0(Genxs):
    """
    Represents genxs tropt data options, form #0.

    Attributes:
        keyword: genxs tropt data option `GENXS` symbol.
        equals: genxs tropt data option `=` symbol.
        filename: genxs tropt data option `filename` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'GENXS'] | str = abc.Terminal[r'GENXS']('GENXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str


class Genxs_1(Genxs):
    """
    Represents genxs tropt data options, form #1.

    Attributes:
        keyword: genxs tropt data option `GENXS` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'GENXS'] | str = abc.Terminal[r'GENXS']('GENXS')
