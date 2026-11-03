import typing

from ..... import abc
from ..Kopts import Kopts


class Kinetics(Kopts):
    """
    Represents kinetics kopts data options.

    Attributes:
        keyword: kinetics kopts data option `KINETICS` symbol.
        equals: kinetics kopts data option `=` symbol.
        value: kinetics kopts data option `value` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KINETICS'] | str = abc.Terminal[r'KINETICS']('KINETICS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
