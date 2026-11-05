import typing

from ..... import abc
from ..M import M


class Pnlib(M):
    """
    Represents pnlib m data options.

    Attributes:
        keyword: pnlib m data option ``r'PNLIB'`` symbol.
        equals: pnlib m data option ``r'='`` symbol.
        x: pnlib m data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PNLIB'] | str = abc.Terminal[r'PNLIB']('PNLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str
