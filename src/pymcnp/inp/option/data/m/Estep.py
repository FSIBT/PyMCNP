import typing

from ..... import abc
from .... import literal
from ..M import M


class Estep(M):
    """
    Represents estep m data options.

    Attributes:
        keyword: estep m data option `ESTEP` symbol.
        equals: estep m data option `=` symbol.
        n: estep m data option `n` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ESTEP'] | str = abc.Terminal[r'ESTEP']('ESTEP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
