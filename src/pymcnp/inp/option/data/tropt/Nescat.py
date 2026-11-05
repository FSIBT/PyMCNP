import typing

from ..... import abc
from ..Tropt import Tropt


class Nescat(Tropt):
    """
    Represents nescat tropt data options.

    Attributes:
        keyword: nescat tropt data option ``r'NESCAT'`` symbol.
        equals: nescat tropt data option ``r'='`` symbol.
        value: nescat tropt data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NESCAT'] | str = abc.Terminal[r'NESCAT']('NESCAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:OFF|ON)'] | str
