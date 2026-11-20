import typing

from ... import abc
from .Number import Real


class Qvm(abc.Nonterminal):
    """
    Represents qvm literals.
    """


class Qvm_0(Qvm):
    """
    Represents qvm literals, form #0.

    Attributes:
        sign: qvm literal ``sign`` parameter.
        q: qvm literal ``q`` parameter.
        v: qvm literal ``r'V'`` symbol.
        m: qvm literal ``m`` parameter.
    """

    sign: typing.Annotated[abc.Terminal, r'[+-]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    q: Real
    v: typing.Annotated[abc.Terminal, r'V'] = abc.Terminal[r'V']('V')
    m: Real


class Qvm_1(Qvm):
    """
    Represents qvm literals, form #1.

    Attributes:
        q: qvm literal ``q`` parameter.
        v: qvm literal ``v`` parameter.
    """

    q: Real
    v: typing.Annotated[abc.Terminal, r'X|Y|Z']


class Qvm_2(Qvm):
    """
    Represents qvm literals, form #2.

    Attributes:
        q: qvm literal ``r'0'`` symbol.
    """

    q: typing.Annotated[abc.Terminal, r'0'] = abc.Terminal[r'0']('0')
