import typing
import dataclasses

from ..... import abc
from ..Embee import Embee


class Atom(Embee):
    """
    Represents atom embee data options.

    Attributes:
        keyword: atom embee data option `ATOM` symbol.
        equals: atom embee data option `=` symbol.
        value: atom embee data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ATOM'] | str = abc.Terminal[r'ATOM']('ATOM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
