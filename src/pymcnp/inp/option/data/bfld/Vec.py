import typing
import decimal
import dataclasses

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Vec(Bfld):
    """
    Represents vec bfld data options.

    Attributes:
        keyword: vec bfld data option `VEC` symbol.
        equals: vec bfld data option `=` symbol.
        uf: vec bfld data option `uf` parameter.
        vf: vec bfld data option `vf` parameter.
        wf: vec bfld data option `wf` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VEC'] | str = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    uf: literal.Real | int | float | decimal.Decimal | str
    vf: literal.Real | int | float | decimal.Decimal | str
    wf: literal.Real | int | float | decimal.Decimal | str
