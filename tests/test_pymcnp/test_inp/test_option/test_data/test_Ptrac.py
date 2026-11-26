import pymcnp
from ..... import classes


class Test_Ptrac(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Ptrac

    EXAMPLES_FROM_MCNP_VALID = [
        'buffer 1',
        'file asc',
        'flushnps 1',
        'max 1',
        'meph 1',
        'write pos',
        'coinc col',
        'event src',
        'event src,col,bnk',
        'event=sur,col',
        'event sur col',
        'event src , col',
        # 'filter 3.1,hello,3.1 3.1,hello,3.1 3.1,hello,3.1',
        'type @ @ @',
        'nps 1 1 1',
        'cell 1 1 1',
        'surface 1 1 1',
        'surface 3.1 3.2 3.3',
        'cell 3,4',
        'cell=3,4,5',
        'surface 3.1,4',
        'tally 1 1 1',
        'value 3.1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]


def test_event_cell_surface_lists() -> None:
    event, rest = pymcnp.inp.option.data.Ptrac.from_mcnp('event=src,col,bnk')
    assert rest == ''
    assert [str(item) for item in event.value] == ['src', 'col', 'bnk']

    cell, rest = pymcnp.inp.option.data.Ptrac.from_mcnp('cell=3,4')
    assert rest == ''
    assert [int(item) for item in cell.c] == [3, 4]

    surface, rest = pymcnp.inp.option.data.Ptrac.from_mcnp('surface=3.1,4')
    assert rest == ''
    assert [float(item) for item in surface.s] == [3.1, 4.0]

    # Items added in Python are written with commas, as MCNP's manual does.
    event.value.append(type(event.value[0])('TER'))
    assert event.to_mcnp() == 'event=src,col,bnk,TER'


def test_inp_with_multi_event_ptrac() -> None:
    text = 'title\n1 0 -1\n2 0 1\n\n1 so 1\n\nnps 10\nptrac event=sur,col write=all\n'
    inp, rest = pymcnp.Inp.from_mcnp(text)
    assert rest == ''
    assert inp.to_mcnp() == text
