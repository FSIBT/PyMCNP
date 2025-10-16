import abc

from .. import _symbol


class _Nonterminal(_symbol.Nonterminal):
    @classmethod
    @abc.abstractmethod
    def from_mcnp(cls, source: str) -> tuple[object, str]:  # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def to_mcnp(self) -> str:  # pragma: no cover
        raise NotImplementedError

    def __str__(self):
        return self.to_mcnp()


class Type(_symbol.Nonterminal):
    pass
