import re
import typing

import pytest

import pymcnp


class Nonterminal0(pymcnp.abc.Nonterminal):
    constituent0: typing.Annotated[pymcnp.abc.Array, pymcnp.inp.card.Cell, None] | typing.Annotated[pymcnp.abc.Array, pymcnp.inp.card.Surface, None]


class Test_Nonterminal:
    def test___new___valid(self) -> None:
        cell = pymcnp.inp.card.Cell_1(j='1', m=0, geom='+2.3')  # type:ignore
        assert cell.to_mcnp() == '1 0 +2.3'
        cell = pymcnp.inp.card.Cell_1(j='1', m=0, geom='+2.3', spaces={'j': pymcnp.inp.CardSpace('  '), 'm': pymcnp.inp.CardSpace('  ')})  # type:ignore
        assert cell.to_mcnp() == '1  0  +2.3'
        nonterminal = Nonterminal0(constituent0=pymcnp.abc.Array[pymcnp.inp.card.Surface, None](pymcnp.inp.card.Surface.from_mcnp('1 SO 1')[0], pymcnp.inp.card.Surface.from_mcnp('2 SO 2')[0]))
        assert nonterminal.to_mcnp() == '1 SO 1 2 SO 2'

    def test___new___invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.inp.card.Cell_1(j='A', m=0, geom='+2.3')  # type:ignore
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.inp.card.data.Vol(x=[3.1, 'J', 'A'])  # type:ignore
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.inp.option.cell.Imp.from_mcnp('imp :@')

    def test_setter_valid(self) -> None:
        vol, _ = pymcnp.inp.card.data.Vol.from_mcnp('VOL 3.1 3.1')
        assert vol.to_mcnp() == 'VOL 3.1 3.1'
        vol.no = 'no'  # type:ignore
        assert vol.to_mcnp() == 'VOL no 3.1 3.1'
        vol.no = ''  # type:ignore
        assert vol.to_mcnp() == 'VOL 3.1 3.1'

    def test___class_getitem___valid(self) -> None:
        assert pymcnp.inp.card.Cell[0] == pymcnp.inp.card.Cell_0
        assert pymcnp.inp.card.Cell[1] == pymcnp.inp.card.Cell_1

    def test_scan_valid(self) -> None:
        vol, _ = pymcnp.inp.card.data.Vol.from_mcnp('VOL 3.1 3.1')
        assert tuple(map(str, vol.scan(no=('', 'no')))) == ('VOL 3.1 3.1', 'VOL no 3.1 3.1')

    def test_scan_invalid(self) -> None:
        vol, _ = pymcnp.inp.card.data.Vol.from_mcnp('VOL 3.1 3.1')
        with pytest.raises(pymcnp.abc.Error):
            next(vol.scan(hello=('', 'no')))
        with pytest.raises(pymcnp.abc.Error):
            next(vol.scan())

    def test_scan_with(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 -1\n\n1 SO 1\n\nnps 10\n')
        copies = list(inp.scan_with([1, 2], lambda i, v: setattr(i, 'nps', v)))
        assert [c.nps for c in copies] == [1, 2]
        assert inp.nps == 10


CALLS: list[tuple[str, str]] = []


class Space(pymcnp.abc.Terminal):
    _pattern = re.compile(r'( +)')
    _default = ' '


class Nonterminal1(pymcnp.abc.Nonterminal):
    _space: typing.ClassVar = (Space,)

    a: typing.Annotated[pymcnp.abc.Terminal, r'[a-z]+']
    b: typing.Annotated[pymcnp.abc.Terminal, r'[a-z]+']

    def __post_init__(self) -> None:
        CALLS.append((self.a, self.b))

        if self.b == 'bad':
            raise pymcnp.abc.Error('Invalid value.', f'{self.b=}')


class Nonterminal2(pymcnp.abc.Nonterminal):
    _space: typing.ClassVar = (Space,)

    a: typing.Annotated[pymcnp.abc.Terminal, r'[a-z]+']
    b: typing.Annotated[pymcnp.abc.Terminal, r'[a-z]+'] = pymcnp.abc.Terminal[r'[a-z]+']('z')

    def __post_init__(self) -> None:
        CALLS.append((self.a, self.b))

        if self.a == 'x' and self.b == 'z':
            raise pymcnp.abc.Error('Invalid value.', f'{self.a=} {self.b=}')


class Test_Nonterminal_build:
    def test_build_validates_once(self) -> None:
        CALLS.clear()
        nonterminal, remainder = Nonterminal1.from_mcnp('ab  cd')
        assert CALLS == [('ab', 'cd')]
        assert remainder == ''
        assert nonterminal == Nonterminal1(a='ab', b='cd', spaces={'a': Space('  ')})
        assert nonterminal.spaces == {'a': '  '}
        assert nonterminal.to_mcnp() == 'ab  cd'
        assert vars(nonterminal) == vars(Nonterminal1(a='ab', b='cd', spaces={'a': Space('  ')}))

        # Setters still validate.
        CALLS.clear()
        nonterminal.b = 'ef'  # type: ignore
        assert CALLS == [('ab', 'ef')]
        with pytest.raises(pymcnp.abc.Error):
            nonterminal.b = '12'  # type: ignore
        with pytest.raises(pymcnp.abc.Error, match='Invalid value'):
            nonterminal.b = 'bad'  # type: ignore

    def test_build_invalid_still_raises(self) -> None:
        with pytest.raises(pymcnp.abc.Error) as err:
            Nonterminal1.from_mcnp('ab bad')
        assert str(err.value) == "Invalid value.\n self.b='bad'"

    def test_build_default_after_last_required(self) -> None:
        # Fields with defaults after the last required one: the setters validate with the defaults first.
        CALLS.clear()
        nonterminal, _ = Nonterminal2.from_mcnp('ab cd')
        assert CALLS == [('ab', 'z'), ('ab', 'cd')]
        assert nonterminal.to_mcnp() == 'ab cd'

        with pytest.raises(pymcnp.abc.Error) as err:
            Nonterminal2.from_mcnp('x cd')
        assert str(err.value) == "Invalid value.\n self.a='x' self.b='z'"
