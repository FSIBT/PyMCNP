import typing
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Nrm(Sdef):
    """
    Represents nrm sdef data options.

    Attributes:
        keyword: nrm sdef data option `NRM` symbol.
        equals: nrm sdef data option `equals` parameter.
        x: nrm sdef data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NRM'] | str = abc.Terminal[r'NRM']('NRM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Integer | literal.Distribution | literal.DependentDistribution
