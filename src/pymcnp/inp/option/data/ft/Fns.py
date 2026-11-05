import typing

from ..... import abc
from .... import literal
from ..Ft import Ft


class Fns(Ft):
    """
    Represents fns ft data options.

    Attributes:
        id: fns group ``r'FNS'`` symbol.
        nt: fns group ``nt`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'FNS'] | str = abc.Terminal[r'FNS']('FNS')
    nt: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
