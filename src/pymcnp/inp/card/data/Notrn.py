import typing
import dataclasses


from .... import abc
from ..Data import Data


class Notrn(Data):
    """
    Represents notrn data cards.

    Attributes:
        keyword: notrn data card `NOTRN` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOTRN'] | str = abc.Terminal[r'NOTRN']('NOTRN')
