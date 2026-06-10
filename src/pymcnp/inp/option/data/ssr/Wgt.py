import typing
import dataclasses

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Wgt(Ssr):
    """
    Represents wgt ssr data options.

    Attributes:
        keyword: wgt ssr data option `WGT` symbol.
        equals: wgt ssr data option `=` symbol.
        value: wgt ssr data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'WGT'] | str = abc.Terminal[r'WGT']('WGT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
