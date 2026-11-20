import typing


from .... import abc
from ... import group
from ..Data import Data


class Pikmt(Data):
    """
    Represents pikmt data cards.

    Attributes:
        keyword: pikmt data card ``r'PIKMT'`` symbol.
        target_identifier_ipik_mt_pmt: pikmt data card ``target_identifier_ipik_mt_pmt`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PIKMT'] = abc.Terminal[r'PIKMT']('PIKMT')
    target_identifier_ipik_mt_pmt: typing.Annotated[abc.Array, group.PhotonBias, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
