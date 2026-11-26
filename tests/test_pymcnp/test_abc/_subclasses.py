"""
Subclasses of library nonterminals defined in a module with string annotations.
"""

from __future__ import annotations

import typing

import pymcnp


class FutureHistory(pymcnp.ptrac.block.History):
    _note: str = 'private'
    tag: typing.ClassVar[str] = 'future'

    def count(self) -> int:
        return len(self.events)


class FutureInp(pymcnp.Inp):
    pass
