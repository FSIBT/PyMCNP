import typing

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Refpnt(Bfld):
    """
    Represents refpnt bfld data options.

    Attributes:
        keyword: refpnt bfld data option ``r'REFPNT'`` symbol.
        equals: refpnt bfld data option ``r'='`` symbol.
        x: refpnt bfld data option ``x`` parameter.
        y: refpnt bfld data option ``y`` parameter.
        z: refpnt bfld data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'REFPNT'] = abc.Terminal[r'REFPNT']('REFPNT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real
