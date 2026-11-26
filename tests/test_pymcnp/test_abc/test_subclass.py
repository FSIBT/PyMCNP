import sys
import copy
import typing
import pathlib

import pytest

import pymcnp

from . import _subclasses

FILES = pathlib.Path(__file__).parents[3] / 'files'
HISTORY = '          9      1000\n       3000         1        40        10         1\n   0.00000E+00  0.00000E+00  0.00000E+00\n       9000         4         1         2        12         0\n  -0.14320E+01  0.55289E+01 -0.18385E+01'
PARENTS = [
    (pymcnp.Inp, FILES / 'inp' / 'valid_00.inp'),
    (pymcnp.Outp, FILES / 'outp' / 'valid_02.outp'),
    (pymcnp.Meshtal, FILES / 'meshtal' / 'valid_38.meshtal'),
    (pymcnp.Ptrac, FILES / 'ptrac' / 'valid_00.ptrac'),
]


@pytest.mark.parametrize('parent, path', PARENTS)
def test_file_subclass_reads_its_own_type(parent: type, path: pathlib.Path) -> None:
    forms = parent._forms
    subclass = type(f'My{parent.__name__}', (parent,), {})
    assert parent._forms == forms
    assert subclass._fields == parent._fields
    mine, _ = subclass.from_file(path)
    theirs, _ = parent.from_file(path)
    assert type(mine) is subclass
    assert type(theirs) is parent
    assert mine.to_mcnp() == theirs.to_mcnp()
    assert mine != theirs
    assert type(copy.deepcopy(mine)) is subclass


def test_history_subclass_from_mcnp_returns_subclass() -> None:
    class MyHistory(pymcnp.ptrac.block.History):
        def count(self) -> int:
            return len(self.events)

    history, _ = MyHistory.from_mcnp(HISTORY)
    parent, _ = pymcnp.ptrac.block.History.from_mcnp(HISTORY)
    assert type(history) is MyHistory
    assert type(parent) is pymcnp.ptrac.block.History
    assert history.count() == 2
    assert history.to_mcnp() == parent.to_mcnp()
    assert type(pymcnp.Ptrac.from_file(FILES / 'ptrac' / 'valid_00.ptrac')[0].histories[0]) is pymcnp.ptrac.block.History


def test_card_subclass() -> None:
    class MyCell(pymcnp.inp.card.Cell_1):
        pass

    cell, remainder = MyCell.from_mcnp('1 0 +2.3')
    assert type(cell) is MyCell
    assert remainder == ''
    assert cell.j.to_mcnp() == '1'
    assert MyCell(j='1', m=0, geom='+2.3').to_mcnp() == '1 0 +2.3'  # type:ignore
    assert MyCell not in pymcnp.inp.card.Cell._forms
    assert type(pymcnp.inp.card.Cell.from_mcnp('1 0 +2.3')[0]) is pymcnp.inp.card.Cell_1


def test_subclass_of_subclass() -> None:
    class MyHistory(pymcnp.ptrac.block.History):
        pass

    class OurHistory(MyHistory):
        pass

    history, _ = OurHistory.from_mcnp(HISTORY)
    assert type(history) is OurHistory
    assert MyHistory._forms == ()
    assert type(MyHistory.from_mcnp(HISTORY)[0]) is MyHistory


def test_subclass_with_string_annotations() -> None:
    history, _ = _subclasses.FutureHistory.from_mcnp(HISTORY)
    assert type(history) is _subclasses.FutureHistory
    assert history.count() == 2
    assert _subclasses.FutureHistory._fields == pymcnp.ptrac.block.History._fields
    inp, _ = _subclasses.FutureInp.from_file(FILES / 'inp' / 'valid_00.inp')
    assert type(inp) is _subclasses.FutureInp


def test_subclass_keyword_construction_uses_inherited_defaults() -> None:
    class MyHistory(pymcnp.ptrac.block.History):
        pass

    parent, _ = pymcnp.ptrac.block.History.from_mcnp(HISTORY)
    history = MyHistory(blank=' ', nps=parent.nps, event_type=parent.event_type, newline='\n', events=parent.events)  # type:ignore
    assert history.to_mcnp() == parent.to_mcnp()
    assert history.number == parent.number
    assert history.tfc == ''


def test_subclass_adding_a_field_raises() -> None:
    with pytest.raises(pymcnp.abc.Error):

        class MyHistory(pymcnp.ptrac.block.History):
            extra: typing.Annotated[pymcnp.abc.Terminal, r'.*']

    with pytest.raises(pymcnp.abc.Error):

        class MyInp(pymcnp.Inp):
            title: typing.Annotated[pymcnp.abc.Terminal, r'.+\n']


def test_subclass_adding_a_field_raises_with_string_annotations() -> None:
    with pytest.raises(pymcnp.abc.Error):
        exec('from __future__ import annotations\nimport pymcnp\nclass MyInp(pymcnp.Inp):\n    extra: int', {})


def test_subclass_shadowing_a_field_raises() -> None:
    # A class attribute named like an inherited field would replace the field's property.
    with pytest.raises(pymcnp.abc.Error):

        class MyInp(pymcnp.Inp):
            title = 'abc'

    with pytest.raises(pymcnp.abc.Error):

        class MyHistory(pymcnp.ptrac.block.History):
            def events(self) -> None:
                """Replaces the field."""


# Skipped before Python 3.14, so its body runs, and counts for coverage, only from 3.14 on.
@pytest.mark.skipif(sys.version_info < (3, 14), reason='annotations are evaluated lazily from Python 3.14')
def test_subclass_with_lazy_forward_references() -> None:  # pragma: no cover
    # Names defined later, or never, in private and class-variable annotations do not stop the class.
    class MyHistory(pymcnp.ptrac.block.History):
        _cache: Later  # noqa: F821
        tag: typing.ClassVar[Later]  # noqa: F821

    history, _ = MyHistory.from_mcnp(HISTORY)
    assert type(history) is MyHistory
    with pytest.raises(pymcnp.abc.Error):

        class OurHistory(pymcnp.ptrac.block.History):
            extra: Later  # noqa: F821
