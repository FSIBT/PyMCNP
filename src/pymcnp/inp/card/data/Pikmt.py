import typing
import dataclasses

import collections

from .... import abc
from ... import group
from ..Data import Data


class Pikmt(Data):
    """
    Represents pikmt data cards.

    Attributes:
        keyword: pikmt data card `PIKMT` symbol.
        target_identifier_ipik_mt_pmt: pikmt data card `target_identifier_ipik_mt_pmt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PIKMT'] | str = abc.Terminal[r'PIKMT']('PIKMT')
    target_identifier_ipik_mt_pmt: typing.Annotated[abc.Array, group.PhotonBias, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.PhotonBias | str] | str = abc.Terminal[
        r''
    ]('')
