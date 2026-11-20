import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Axs(Sdef):
    """
    Represents axs sdef data options.
    """


class Axs_0(Axs):
    """
    Represents axs sdef data options, form #0.

    Attributes:
        keyword: axs sdef data option ``r'AXS'`` symbol.
        equals: axs sdef data option ``equals`` parameter.
        x: axs sdef data option ``x`` parameter.
        y: axs sdef data option ``y`` parameter.
        z: axs sdef data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AXS'] = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real


class Axs_1(Axs):
    """
    Represents axs sdef data options, form #1.

    Attributes:
        keyword: axs sdef data option ``r'AXS'`` symbol.
        equals: axs sdef data option ``equals`` parameter.
        value: axs sdef data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AXS'] = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Distribution | literal.DependentDistribution
