import typing


from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Cell(Kpert):
    """
    Represents cell kpert data options.

    Attributes:
        keyword: cell kpert data option ``r'CELL'`` symbol.
        equals: cell kpert data option ``r'='`` symbol.
        c: cell kpert data option ``c`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CELL'] = abc.Terminal[r'CELL']('CELL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
