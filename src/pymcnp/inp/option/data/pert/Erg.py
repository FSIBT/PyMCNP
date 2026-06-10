import typing
import decimal
import dataclasses

from ..... import abc
from ..Pert import Pert
from .... import literal


class Erg(Pert):
    """
    Represents erg pert data options.

    Attributes:
        keyword: erg pert data option `ERG` symbol.
        equals: erg pert data option `=` symbol.
        elb: erg pert data option `elb` parameter.
        eub: erg pert data option `eub` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ERG'] | str = abc.Terminal[r'ERG']('ERG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    elb: literal.Real | int | float | decimal.Decimal | str
    eub: literal.Real | int | float | decimal.Decimal | str
