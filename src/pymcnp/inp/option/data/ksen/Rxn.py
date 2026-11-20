import typing


from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Rxn(Ksen):
    """
    Represents rxn ksen data options.

    Attributes:
        keyword: rxn ksen data option ``r'RXN'`` symbol.
        equals: rxn ksen data option ``r'='`` symbol.
        rx: rxn ksen data option ``rx`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RXN'] = abc.Terminal[r'RXN']('RXN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    rx: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
