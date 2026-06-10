import typing
import dataclasses

import collections

from ..... import abc
from .... import group
from ..Embed import Embed


class Matcell(Embed):
    """
    Represents matcell embed data options.

    Attributes:
        keyword: matcell embed data option `MATCELL` symbol.
        equals: matcell embed data option `=` symbol.
        m_c: matcell embed data option `m_c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MATCELL'] | str = abc.Terminal[r'MATCELL']('MATCELL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m_c: typing.Annotated[abc.Array, group.MatCell, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.MatCell | str] | str = abc.Terminal[r'']('')
