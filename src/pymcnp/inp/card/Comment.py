import typing
import dataclasses


from ... import abc
from ..Card import Card


class Comment(Card):
    """
    Represents comment cards.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    c: typing.Annotated[abc.Terminal, r' {0,4}C'] | str = dataclasses.field(kw_only=True)
    text: typing.Annotated[abc.Terminal, r'[^\n]+'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
