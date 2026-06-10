import typing
import dataclasses

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Psc(Ssr):
    """
    Represents psc ssr data options.

    Attributes:
        keyword: psc ssr data option `PSC` symbol.
        equals: psc ssr data option `=` symbol.
        c: psc ssr data option `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PSC'] | str = abc.Terminal[r'PSC']('PSC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: literal.Integer | int | str
