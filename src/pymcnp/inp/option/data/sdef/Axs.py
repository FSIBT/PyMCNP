import typing
import decimal
import dataclasses

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
        keyword: axs sdef data option `AXS` symbol.
        equals: axs sdef data option `equals` parameter.
        x: axs sdef data option `x` parameter.
        y: axs sdef data option `y` parameter.
        z: axs sdef data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'AXS'] | str = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    y: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    z: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)


class Axs_1(Axs):
    """
    Represents axs sdef data options, form #1.

    Attributes:
        keyword: axs sdef data option `AXS` symbol.
        equals: axs sdef data option `equals` parameter.
        value: axs sdef data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'AXS'] | str = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Distribution | literal.DependentDistribution | str = dataclasses.field(kw_only=True)
