import typing


from .... import abc
from ..Data import Data


class Notrn(Data):
    """
    Represents notrn data cards.

    Attributes:
        keyword: notrn data card ``r'NOTRN'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOTRN'] | str = abc.Terminal[r'NOTRN']('NOTRN')
