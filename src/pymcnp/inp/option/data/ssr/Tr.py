import typing
import dataclasses

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Tr(Ssr):
    """
    Represents tr ssr data options.

    Attributes:
        keyword: tr ssr data option `TR` symbol.
        equals: tr ssr data option `=` symbol.
        n: tr ssr data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'TR'] | str = abc.Terminal[r'TR']('TR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | literal.Distribution | int | str = dataclasses.field(kw_only=True)
