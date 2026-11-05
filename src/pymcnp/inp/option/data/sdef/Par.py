import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Par(Sdef):
    """
    Represents par sdef data options.

    Attributes:
        keyword: par sdef data option ``r'PAR'`` symbol.
        equals: par sdef data option ``equals`` parameter.
        m: par sdef data option ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PAR'] | str = abc.Terminal[r'PAR']('PAR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m: (
        literal.Particle
        | literal.Distribution
        | literal.DependentDistribution
        | typing.Annotated[
            abc.Terminal, r'(?:-?CR)|(?:-?CH)|(?:-?C1001)|(?:-?CA)|(?:-?C2004)|(?:-?C7014)|(?:-?C14028)|(?:-?C26056)|(?:-?BG)|(?:-?BN)|(?:-?BP)|(?:-?SF)|(?:SN)|(?:SP)|(?:SB)|(?:ST)|(?:SA)|(?:SD)'
        ]
        | str
    )
