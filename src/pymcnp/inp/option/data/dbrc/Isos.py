import typing


from ..... import abc
from ..Dbrc import Dbrc
from .... import literal


class Isos(Dbrc):
    """
    Represents isos dbrc data options.

    Attributes:
        keyword: isos dbrc data option ``r'ISOS'`` symbol.
        equals: isos dbrc data option ``r'='`` symbol.
        iso_list: isos dbrc data option ``iso_list`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ISOS'] = abc.Terminal[r'ISOS']('ISOS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    iso_list: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
