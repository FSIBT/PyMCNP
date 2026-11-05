import typing

import collections

from ..... import abc
from .... import group
from ..Embed import Embed


class Matcell(Embed):
    """
    Represents matcell embed data options.

    Attributes:
        keyword: matcell embed data option ``r'MATCELL'`` symbol.
        equals: matcell embed data option ``r'='`` symbol.
        m_c: matcell embed data option ``m_c`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MATCELL'] | str = abc.Terminal[r'MATCELL']('MATCELL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m_c: typing.Annotated[abc.Array, group.MatCell, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.MatCell | str] | str = abc.Terminal[r'']('')
