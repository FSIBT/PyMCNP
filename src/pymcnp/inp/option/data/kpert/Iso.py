import typing


from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Iso(Kpert):
    """
    Represents iso kpert data options.

    Attributes:
        keyword: iso kpert data option ``r'ISO'`` symbol.
        equals: iso kpert data option ``r'='`` symbol.
        z: iso kpert data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ISO'] = abc.Terminal[r'ISO']('ISO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    z: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
