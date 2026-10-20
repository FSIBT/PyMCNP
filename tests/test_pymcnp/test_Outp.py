import pathlib

import pandas
import pytest

import pymcnp
from .. import classes


class Test_Outp(classes.Test_Nonterminal):
    element = pymcnp.Outp
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_39.outp').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]


def test_fatal_errors() -> None:
    from pymcnp.Outp import _fatal_errors

    text = '  comment.  fine\n  fatal error.  surface        -7 not found for cell         2 card.\n \n  fatal error.  surface -7 of cell 2 is not defined.\n  warning.  nothing\n'
    assert _fatal_errors(text) == ['surface        -7 not found for cell         2 card.', 'surface -7 of cell 2 is not defined.']
    assert _fatal_errors('  warning.  no fatal error here\n') == []


FILES_OUTP = pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp'


@pytest.mark.parametrize('name', ['valid_38.outp', 'valid_39.outp'])
@pytest.mark.parametrize('particle', ['neutron', 'photon'])
def test_activity_rows_add_up_to_the_total(name: str, particle: str) -> None:
    outp, _ = pymcnp.Outp.from_file(FILES_OUTP / name)
    frame = outp.activity(particle)

    cells, total = frame.iloc[:-1], frame.iloc[-1]
    assert list(frame.columns)[:3] == ['cell', 'tracks', 'population']
    assert pandas.isna(total['cell']) and not cells.empty
    assert cells['tracks'].sum() == total['tracks']
    assert cells['population'].sum() == total['population']
    assert cells['collisions'].sum() == total['collisions']


def test_activity_values() -> None:
    text = (FILES_OUTP / 'valid_38.outp').read_text()
    outp, _ = pymcnp.Outp.from_mcnp(text)
    frame = outp.activity('photon')
    first = next(line.split() for line in text.split('1photon')[1].splitlines() if line.split()[:1] == ['1'])

    assert int(frame.iloc[0]['cell']) == int(first[1])
    assert int(frame.iloc[0]['tracks']) == int(first[2])
    assert float(frame.iloc[0]['average_track_mfp']) == float(first[9])


def test_activity_invalid() -> None:
    outp, _ = pymcnp.Outp.from_file(FILES_OUTP / 'valid_01.outp')  # neutron table only
    with pytest.raises(pymcnp.abc.Error):
        outp.activity('electron')
    with pytest.raises(pymcnp.abc.Error):
        outp.activity('photon')
