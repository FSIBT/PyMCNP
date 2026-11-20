import typing


from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Iso(Ksen):
    """
    Represents iso ksen data options.

    Attributes:
        keyword: iso ksen data option ``r'ISO'`` symbol.
        equals: iso ksen data option ``r'='`` symbol.
        z: iso ksen data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ISO'] = abc.Terminal[r'ISO']('ISO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    z: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
