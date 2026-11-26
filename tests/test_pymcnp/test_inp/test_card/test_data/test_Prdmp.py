import pymcnp


def test_prdmp_entries_may_be_left_out() -> None:
    # Every entry may be a jump, and trailing entries may be left out.
    card, remainder = pymcnp.inp.card.Data.from_mcnp('prdmp j j -1')
    assert remainder == ''
    assert isinstance(card, pymcnp.inp.card.data.Prdmp)
    assert isinstance(card.ndp, pymcnp.inp.literal.Jump)
    assert card.mct == -1
    assert card.ndmp == ''
    assert pymcnp.inp.card.data.Prdmp(mct=1).to_mcnp() == 'PRDMP J J 1 J J'


def test_prdmp_in_file_keeps_later_cards() -> None:
    source = 'title\n1 0 -1\n2 0 1\n\n1 so 1\n\nprdmp 2j 1\nnps 10\n'
    inp, remainder = pymcnp.Inp.from_mcnp(source)
    assert remainder == ''
    prdmp, nps = inp.data_cards()
    assert (prdmp.ndp, prdmp.ndm, prdmp.mct) == ('j', 'j', 1)
    assert nps.to_mcnp() == 'nps 10'
    assert pymcnp.Inp.from_mcnp(inp.to_mcnp())[1] == ''
