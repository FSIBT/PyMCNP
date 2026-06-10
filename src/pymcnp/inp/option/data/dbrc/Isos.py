import typing
import dataclasses

import collections

from ..... import abc
from ..Dbrc import Dbrc
from .... import literal


class Isos(Dbrc):
    """
    Represents isos dbrc data options.

    Attributes:
        keyword: isos dbrc data option `ISOS` symbol.
        equals: isos dbrc data option `=` symbol.
        iso_list: isos dbrc data option `iso_list` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ISOS'] | str = abc.Terminal[r'ISOS']('ISOS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    iso_list: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Zaid | str] | str = abc.Terminal[r'']('')
