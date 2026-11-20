import typing
import dataclasses


from .... import abc
from ... import literal
from ..Data import Data


class U(Data):
    """
    Represents u data cards.

    Attributes:
        keyword: u data card ``r'U'`` symbol.
        n: u data card ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'U'] = abc.Terminal[r'U']('U')
    n: typing.Annotated[abc.Array, literal.Integer | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] = dataclasses.field(kw_only=True)
