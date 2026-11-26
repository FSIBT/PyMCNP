import functools
import pathlib

import pandas
import pytest

import pymcnp
from .. import classes


# The OUTP fixtures hold tallies PyMCNP cannot parse; the tests of that warning catch it themselves.
pytestmark = pytest.mark.filterwarnings('ignore:Tally not parsed:pymcnp.abc.Warning')

PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp'


class Test_Outp(classes.Test_FromFile):
    element = pymcnp.Outp

    EXAMPLES_FROM_FILE_VALID = [
        PATH / 'valid_39.outp',
        PATH / 'valid_06.outp',
    ]
    EXAMPLES_FROM_FILE_INVALID = [
        PATH / 'invalid_02.outp',
        PATH / 'hello',
    ]

    def test_to_dataframe(self) -> None:
        outp, _ = pymcnp.Outp.from_file(PATH / 'valid_00.outp')
        pandas.testing.assert_frame_equal(
            outp.to_dataframe(),
            pandas.DataFrame(
                [
                    [1.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [2.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [3.0000e00, 2.45053e-05, 0.9999, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [4.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [5.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [6.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [7.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [8.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [9.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.0000e01, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.1000e01, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.2000e01, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.3000e01, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.4000e01, 3.24502e-04, 0.7074, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                ],
                columns=['bins', 'counts', 'errors', 'cell_number', 'number', 'type', 'particles', 'nps'],
            ),
            rtol=1e-4,
        )

    def test_footer_properties(self) -> None:
        outp, _ = self.element.from_file(PATH / 'valid_39.outp')

        assert outp.version == 'MCNP_6.20, 6.2.0'
        assert outp.nps.strip() == '1000000'
        assert outp.run_time.strip() == '0.79'
        assert outp.terminated.strip() == '1000000  particle histories were done.'
        assert outp.warnings.strip() == '15'

    def test_footer_properties_without_footer(self) -> None:
        outp, _ = self.element.from_file(PATH / 'valid_06.outp')

        assert outp.version == 'MCNP6, 1.0'
        assert (outp.nps, outp.run_time, outp.terminated, outp.warnings) == (None, None, None, None)
        assert outp.activities() == () and outp.tallies() == ()

    def test_activities(self) -> None:
        outp, _ = self.element.from_file(PATH / 'valid_39.outp')

        assert [type(block) for block in outp.activities()] == [pymcnp.outp.block.NeutronActivity, pymcnp.outp.block.PhotonActivity]
        assert outp.activities(pymcnp.outp.block.PhotonActivity) == outp.activities()[1:]

    def test_tallies(self) -> None:
        outp, _ = self.element.from_file(PATH / 'valid_39.outp')

        tallies = outp.tallies()
        assert [str(tally.number).strip() for tally in tallies] == ['21']
        assert outp.tallies(number=21) == tallies
        assert outp.tallies(number='1') == ()


@functools.cache
def _parsed(name: str) -> pymcnp.Outp:
    outp, _ = pymcnp.Outp.from_file(PATH / name)
    return outp


def test_fatal_errors() -> None:
    from pymcnp.Outp import _fatal_errors

    text = '  comment.  fine\n  fatal error.  surface        -7 not found for cell         2 card.\n \n  fatal error.  surface -7 of cell 2 is not defined.\n  warning.  nothing\n'
    assert _fatal_errors(text) == ['surface        -7 not found for cell         2 card.', 'surface -7 of cell 2 is not defined.']
    assert _fatal_errors('  warning.  no fatal error here\n') == []


@pytest.mark.parametrize('name', ['valid_38.outp', 'valid_39.outp'])
@pytest.mark.parametrize('particle', ['neutron', 'photon'])
def test_activity_rows_add_up_to_the_total(name: str, particle: str) -> None:
    frame = _parsed(name).activity(particle)

    cells, total = frame.iloc[:-1], frame.iloc[-1]
    assert list(frame.columns)[:3] == ['cell', 'tracks', 'population']
    assert pandas.isna(total['cell']) and not cells.empty
    assert cells['tracks'].sum() == total['tracks']
    assert cells['population'].sum() == total['population']
    assert cells['collisions'].sum() == total['collisions']


def test_activity_values() -> None:
    text = (PATH / 'valid_38.outp').read_text()
    frame = _parsed('valid_38.outp').activity('photon')
    first = next(line.split() for line in text.split('1photon')[1].splitlines() if line.split()[:1] == ['1'])

    assert int(frame.iloc[0]['cell']) == int(first[1])
    assert int(frame.iloc[0]['tracks']) == int(first[2])
    assert float(frame.iloc[0]['average_track_mfp']) == float(first[9])


def test_activity_invalid() -> None:
    outp = _parsed('valid_01.outp')  # neutron table only
    with pytest.raises(pymcnp.abc.Error):
        outp.activity('electron')
    with pytest.raises(pymcnp.abc.Error):
        outp.activity('photon')


class Test_Outp_Summary:
    def _summary(self, name: str) -> pymcnp.outp.Summary:
        return pymcnp.outp.Summary.from_text((PATH / name).read_text())

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
        outp = _parsed('valid_03.outp')
        summary = outp.summary
        assert summary.terminated == 'fatal errors' and not summary.ok
        assert summary.fatal_errors == outp.fatal_errors and summary.fatal_errors

    def test_summary_property_matches_text(self) -> None:
        outp = _parsed('valid_38.outp')
        assert outp.summary == pymcnp.outp.Summary.from_text((PATH / 'valid_38.outp').read_text(), outp.fatal_errors)

    def test_no_checks_and_empty_text(self) -> None:
        empty = pymcnp.outp.Summary.from_text('')
        assert empty == pymcnp.outp.Summary()
        assert empty.checks_passed is None and not empty.ok


class Test_Outp_Tally:
    def test_quantity_without_units(self) -> None:
        assert _parsed('valid_00.outp').tally(4).quantity[0] == 'track length estimate of particle flux.'

    def test_typed_surface_tally(self) -> None:
        frame = _parsed('valid_38.outp').tally(21)
        assert list(frame.columns) == ['bins', 'counts', 'errors', 'angle_from', 'angle_to', 'surface', 'facet', 'number', 'quantity', 'particles', 'nps']
        assert frame.angle_from.dtype == float and str(frame.surface.dtype) == 'Int64'
        assert set(frame.surface) == {2, 3} and set(frame.number) == {21}
        assert frame.nps.dtype == int

    def test_tally_by_string_and_missing(self) -> None:
        outp = _parsed('valid_00.outp')
        assert outp.tally('4').equals(outp.tally(4))
        assert 'cell' in outp.tally(4)
        with pytest.raises(pymcnp.abc.Error):
            outp.tally(99)

    def test_blocks_methods_stay(self) -> None:
        outp = _parsed('valid_38.outp')
        assert outp.tallies() and outp.activities()


def test_surface_helper() -> None:
    from pymcnp.Outp import _surface

    assert _surface(' 12.3 ') == (12, 3)
    assert _surface('12') == (12, 0)
    assert _surface('total') == (None, None)


def test_activity_malformed_row_is_rejected() -> None:
    text = (PATH / 'valid_01.outp').read_text()
    line = next(line for line in text.splitlines() if line.split()[:1] == ['1'] and len(line.split()) == 10 and '.' in line)
    broken = text.replace(line, line[:-13] + ' ' * 13, 1)
    outp, _ = pymcnp.Outp.from_mcnp(broken)
    with pytest.raises(pymcnp.abc.Error, match='Invalid table row'):
        outp.activity('neutron')


EXAMPLES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'examples'


def _skipped(path: pathlib.Path) -> list[str]:
    import warnings

    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter('always')
        pymcnp.Outp.from_file(path)
    return [str(w.message) for w in record if isinstance(w.message, pymcnp.abc.Warning) and w.message.title == 'Tally not parsed.']


@pytest.mark.parametrize(
    'path, expected',
    [
        (PATH / 'valid_00.outp', [('2', '2')]),
        (EXAMPLES / 'example_01.outp', [('8', '8')]),
        (EXAMPLES / 'example_02.outp', [('4', '4'), ('5', '5')]),
        (PATH / 'valid_39.outp', [('1', '1')]),
        # Tally 4 is printed twice; it is reported once.
        (PATH / 'valid_10.outp', [('4', '4')]),
    ],
    ids=lambda value: value.name if isinstance(value, pathlib.Path) else '',
)
def test_skipped_tally_warns(path: pathlib.Path, expected: list[tuple[str, str]]) -> None:
    messages = _skipped(path)
    assert len(messages) == len(expected)
    for message, (number, kind) in zip(messages, expected):
        assert f'tally {number} (type {kind})' in message


def test_parsed_tallies_do_not_warn() -> None:
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter('error')
        pymcnp.Outp.from_file(EXAMPLES / 'example_00.outp')


@pytest.mark.parametrize('path', sorted(PATH.glob('valid_*.outp')) + sorted(EXAMPLES.glob('*.outp')), ids=lambda path: path.name)
def test_every_unparsed_tally_warns(path: pathlib.Path) -> None:
    import re
    import warnings

    printed = set(re.findall(r'^1tally +(\d+) +nps =', path.read_text(), re.M))
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter('always')
        outp, _ = pymcnp.Outp.from_file(path)
    parsed = {tally.number.strip() for tally in outp.tallies()}
    warned = {re.search(r'tally (\S+) \(type', w.message.body)[1] for w in record if isinstance(w.message, pymcnp.abc.Warning) and w.message.title == 'Tally not parsed.'}
    assert warned == printed - parsed


def test_unparsed_tally_warns_for_every_file() -> None:
    import warnings

    paths = [PATH / 'valid_00.outp', PATH / 'valid_39.outp', PATH / 'valid_00.outp']
    with warnings.catch_warnings(record=True) as record:
        # Default filters show a warning once per text and location; each file must still warn.
        warnings.simplefilter('default')
        for path in paths:
            pymcnp.Outp.from_file(path)
    bodies = [w.message.body for w in record if isinstance(w.message, pymcnp.abc.Warning) and w.message.title == 'Tally not parsed.']
    assert len(bodies) == len(paths)
    for body, path in zip(bodies, paths):
        assert body.startswith(f'{path=} tally ')


def test_unparsed_tally_warning_from_text_has_no_path() -> None:
    import warnings

    source = (PATH / 'valid_00.outp').read_text()
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter('default')
        pymcnp.Outp.from_mcnp(source)
        pymcnp.Outp.from_mcnp(source)
    bodies = [w.message.body for w in record if isinstance(w.message, pymcnp.abc.Warning) and w.message.title == 'Tally not parsed.']
    assert bodies == ['tally 2 (type 2) is in the file, but PyMCNP cannot parse its layout, so it is missing from the result'] * 2


def test_tally_of_unparsed_tally_says_so() -> None:
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        outp = _parsed('valid_00.outp')
    with pytest.raises(pymcnp.abc.Error, match='not parsed') as error:
        outp.tally(2)
    assert 'type 2' in str(error.value)
    with pytest.raises(pymcnp.abc.Error, match='Tally not found'):
        outp.tally(99)
