import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data
from ... import group


class Uran(Data):
    """
    Represents uran data cards.

    Attributes:
        keyword: uran data card `URAN` symbol.
        nj_dx_dy_dz: uran data card `nj_dx_dy_dz` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'URAN'] | str = abc.Terminal[r'URAN']('URAN')
    nj_dx_dy_dz: typing.Annotated[abc.Array, group.Stochastic, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Stochastic | str] | str = abc.Terminal[r'']('')
