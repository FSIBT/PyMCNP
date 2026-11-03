import typing


from ... import abc
from ..Card import Card


class Comment(Card):
    """
    Represents comment cards.
    """

    c: typing.Annotated[abc.Terminal, r' {0,4}C'] | str
    text: typing.Annotated[abc.Terminal, r'[^\n]+'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
