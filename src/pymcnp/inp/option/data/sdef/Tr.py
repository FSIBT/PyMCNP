import typing
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Tr(Sdef):
    """
    Represents tr sdef data options.

    Attributes:
        keyword: tr sdef data option `TR` symbol.
        equals: tr sdef data option `equals` parameter.
        n: tr sdef data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'TR'] | str = abc.Terminal[r'TR']('TR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | literal.Distribution | int | str = dataclasses.field(kw_only=True)
