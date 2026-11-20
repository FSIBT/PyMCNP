import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Erg(Sdef):
    """
    Represents erg sdef data options.

    Attributes:
        keyword: erg sdef data option ``r'ERG'`` symbol.
        equals: erg sdef data option ``equals`` parameter.
        e: erg sdef data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ERG'] = abc.Terminal[r'ERG']('ERG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    e: literal.Real | literal.Distribution | literal.DependentDistribution | literal.EmbeddedDistribution
