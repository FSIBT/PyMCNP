import typing

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Vec(Bfld):
    """
    Represents vec bfld data options.

    Attributes:
        keyword: vec bfld data option ``r'VEC'`` symbol.
        equals: vec bfld data option ``r'='`` symbol.
        uf: vec bfld data option ``uf`` parameter.
        vf: vec bfld data option ``vf`` parameter.
        wf: vec bfld data option ``wf`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VEC'] = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    uf: literal.Real
    vf: literal.Real
    wf: literal.Real
