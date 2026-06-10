import typing
import decimal
import dataclasses

from ... import abc
from .Number import Real


class Qvm(abc.Nonterminal):
    """
    Represents qvm literals.
    """

    pass


class Qvm_0(Qvm):
    """
    Represents qvm literals, form #0.

    Attributes:
        sign: qvm literal `sign` parameter.
        q: qvm literal `q` parameter.
        v: qvm literal `V` symbol.
        m: qvm literal `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    sign: typing.Annotated[abc.Terminal, r'[+-]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    q: Real | int | float | decimal.Decimal | str
    v: typing.Annotated[abc.Terminal, r'V'] | str = abc.Terminal[r'V']('V')
    m: Real | int | str


class Qvm_1(Qvm):
    """
    Represents qvm literals, form #1.

    Attributes:
        q: qvm literal `q` parameter.
        v: qvm literal `v` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    q: Real | int | float | decimal.Decimal | str
    v: typing.Annotated[abc.Terminal, r'X|Y|Z'] | str


class Qvm_2(Qvm):
    """
    Represents qvm literals, form #2.

    Attributes:
        q: qvm literal `0` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    q: typing.Annotated[abc.Terminal, r'0'] | str = abc.Terminal[r'0']('0')
