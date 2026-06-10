import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Fmult(Data):
    """
    Represents fmult data cards.

    Attributes:
        keyword: fmult data card `FMULT` symbol.
        target_identifier: fmult data card `target_identifier` parameter.
        options: fmult data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMULT'] | str = abc.Terminal[r'FMULT']('FMULT')
    target_identifier: literal.Zaid | str
    options: typing.Annotated[abc.Array, option.data.Fmult, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Fmult | str] | str = abc.Terminal[r'']('')
