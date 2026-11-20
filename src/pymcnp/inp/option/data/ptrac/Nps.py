import typing


from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Nps(Ptrac):
    """
    Represents nps ptrac data options.

    Attributes:
        keyword: nps ptrac data option ``r'NPS'`` symbol.
        equals: nps ptrac data option ``r'='`` symbol.
        n: nps ptrac data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NPS'] = abc.Terminal[r'NPS']('NPS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
