import typing


from .... import abc
from ..Data import Data
from ... import group


class Uran(Data):
    """
    Represents uran data cards.

    Attributes:
        keyword: uran data card ``r'URAN'`` symbol.
        nj_dx_dy_dz: uran data card ``nj_dx_dy_dz`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'URAN'] = abc.Terminal[r'URAN']('URAN')
    nj_dx_dy_dz: typing.Annotated[abc.Array, group.Stochastic, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
