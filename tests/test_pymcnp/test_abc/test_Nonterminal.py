import pymcnp

import pytest


class Nonterminal0(pymcnp.abc.Nonterminal):
    constituent0: pymcnp.abc.Array[pymcnp.inp.card.Cell, None] | pymcnp.abc.Array[pymcnp.inp.card.Surface, None]


class Test_Nonterminal:
    def test___new___valid(self) -> None:
        cell = pymcnp.inp.card.Cell_1(j='1', m=0, geom='+2.3')  # type:ignore
        assert cell.to_mcnp() == '1 0 +2.3'
        cell = pymcnp.inp.card.Cell_1(j='1', m=0, geom='+2.3', spaces={'j': pymcnp.inp.CardSpace('  '), 'm': pymcnp.inp.CardSpace('  ')})  # type:ignore
        assert cell.to_mcnp() == '1  0  +2.3'
        nonterminal = Nonterminal0(constituent0=['1 SO 1', '2 SO 2'])
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
        pymcnp.inp.card.Cell[1]
