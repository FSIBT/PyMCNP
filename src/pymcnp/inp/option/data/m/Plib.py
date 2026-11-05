import typing

from ..... import abc
from ..M import M


class Plib(M):
    """
    Represents plib m data options.

    Attributes:
        keyword: plib m data option ``r'PLIB'`` symbol.
        equals: plib m data option ``r'='`` symbol.
        x: plib m data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PLIB'] | str = abc.Terminal[r'PLIB']('PLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str
