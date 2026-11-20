import typing


from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Cell(Ksen):
    """
    Represents cell ksen data options.

    Attributes:
        keyword: cell ksen data option ``r'CELL'`` symbol.
        equals: cell ksen data option ``r'='`` symbol.
        c: cell ksen data option ``c`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CELL'] = abc.Terminal[r'CELL']('CELL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
