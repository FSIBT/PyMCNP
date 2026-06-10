import typing
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Nps(Data):
    """
    Represents nps data cards.

    Attributes:
        keyword: nps data card `NPS` symbol.
        npp: nps data card `npp` parameter.
        npsmg: nps data card `npsmg` parameter.
        n_per_batch: nps data card `n_per_batch` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NPS'] | str = abc.Terminal[r'NPS']('NPS')
    npp: literal.Integer | int | str
    npsmg: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    n_per_batch: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
