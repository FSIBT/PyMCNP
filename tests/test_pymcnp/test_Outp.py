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


class Test_Outp_Summary:
    def _summary(self, name: str) -> pymcnp.outp.Summary:
        return pymcnp.outp.Summary.from_text((FILES_OUTP / name).read_text())

    def test_fixed_source_run(self) -> None:
        summary = self._summary('valid_38.outp')
        assert summary.version == 'MCNP_6.20, 6.2.0'
        assert (summary.nps, summary.run_time, summary.terminated) == (1_000_000, 0.79, 'histories')
        assert summary.keff is None and summary.keff_sd is None
        assert summary.ok and summary.fatal_errors == []
        assert '35081.80c lacks gamma-ray production cross sections.' in summary.warnings
        assert len(summary.warnings) == len(set(summary.warnings))

    def test_statistical_checks(self) -> None:
        summary = self._summary('valid_38.outp')
        assert set(summary.checks) == {1, 21}
        assert (summary.checks[1].passed, summary.checks[1].failed) == (False, 1)
        assert summary.checks[21].failed == 2
        assert 'tfc bin' in summary.checks[1].message
        assert summary.checks_passed is False

        passing = self._summary('valid_01.outp')
        assert passing.checks[4].passed and passing.checks[4].message == '' and passing.checks_passed is True

    def test_kcode_run(self) -> None:
        summary = self._summary('valid_01.outp')
        assert (summary.keff, summary.keff_sd) == (1.28609, 0.00069)
        assert summary.terminated == 'cycles' and summary.nps == 1_250_166

    def test_fatal_errors_fail_the_run(self) -> None:
        text = (FILES_OUTP / 'valid_03.outp').read_text()
        outp, _ = pymcnp.Outp.from_mcnp(text)
        summary = outp.summary
        assert summary.terminated == 'fatal errors' and not summary.ok
        assert summary.fatal_errors == outp.fatal_errors and summary.fatal_errors

    def test_summary_property_matches_text(self) -> None:
        text = (FILES_OUTP / 'valid_38.outp').read_text()
        outp, _ = pymcnp.Outp.from_mcnp(text)
        assert outp.summary == pymcnp.outp.Summary.from_text(text, outp.fatal_errors)

    def test_no_checks_and_empty_text(self) -> None:
        empty = pymcnp.outp.Summary.from_text('')
        assert empty == pymcnp.outp.Summary()
        assert empty.checks_passed is None and not empty.ok


class Test_Outp_Tallies:
    def _outp(self, name: str) -> pymcnp.Outp:
        outp, _ = pymcnp.Outp.from_file(FILES_OUTP / name)
        return outp

    def test_table(self) -> None:
        table = self._outp('valid_38.outp').tallies()
        assert list(table.number) == [1, 21]
        assert set(table.quantity) == {'number of particles crossing a surface.'}
        assert set(table.particles) == {'photons'}
        assert list(table.nps) == [1_000_000, 1_000_000]
        assert list(table.checks_passed) == [False, False]

    def test_quantity_without_units(self) -> None:
        table = self._outp('valid_00.outp').tallies()
        assert table.quantity[0] == 'track length estimate of particle flux.'

    def test_no_tallies(self) -> None:
        assert self._outp('valid_01.outp').tallies().empty

    def test_typed_surface_tally(self) -> None:
        frame = self._outp('valid_38.outp').tally(21)
        assert list(frame.columns) == ['bins', 'counts', 'errors', 'angle_from', 'angle_to', 'surface', 'facet', 'number', 'quantity', 'particles', 'nps']
        assert frame.angle_from.dtype == float and str(frame.surface.dtype) == 'Int64'
        assert set(frame.surface) == {2, 3} and set(frame.number) == {21}
        assert frame.nps.dtype == int

    def test_tally_by_string_and_missing(self) -> None:
        outp = self._outp('valid_00.outp')
        assert outp.tally('4').equals(outp.tally(4))
        assert 'cell' in outp.tally(4)
        with pytest.raises(pymcnp.abc.Error):
            outp.tally(99)
