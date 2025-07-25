import re
import abc
import enum


class classproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func(owner)


class TerminalMeta(enum.EnumMeta, abc.ABCMeta):
    pass


class Terminal(enum.Enum, metaclass=TerminalMeta):
    """
    Represents generic MCNP terminal symbols.
    """

    @classmethod
    @abc.abstractmethod
    def from_mcnp(cls, source: str):  # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def to_mcnp(self):  # pragma: no cover
        raise NotImplementedError

    def __str__(self):
        return self.to_mcnp()

    def __eq__(a, b):
        return (str(a) if a else None) == (str(b) if b else None)


class Nonterminal(metaclass=abc.ABCMeta):
    """
    Represents generic MCNP nonterminal symbols.
    """

    @classproperty
    def _REGEX(cls):
        return re.compile(
            rf'\A{r"|".join(map(lambda subclass: subclass._REGEX.pattern[2:-2], sorted(cls.__subclasses__(), reverse=True, key=lambda subclass: len(subclass.__name__))))}\Z', re.IGNORECASE
        )

    @classmethod
    @abc.abstractmethod
    def from_mcnp(cls, source: str):  # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def to_mcnp(self):  # pragma: no cover
        raise NotImplementedError

    def __str__(self):
        return self.to_mcnp()

    def __eq__(a, b):
        return (str(a) if a else None) == (str(b) if b else None)
