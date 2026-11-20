import typing


from ..... import abc
from ..Ssr import Ssr
from .... import literal


class New(Ssr):
    """
    Represents new ssr data options.

    Attributes:
        keyword: new ssr data option ``r'NEW'`` symbol.
        equals: new ssr data option ``r'='`` symbol.
        s: new ssr data option ``s`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NEW'] = abc.Terminal[r'NEW']('NEW')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
