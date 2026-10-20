import re
import pathlib

import pytest

import pymcnp
from .. import classes


class Test_Ptrac(classes.Test_Nonterminal):
    element = pymcnp.Ptrac
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac' / 'valid_38.ptrac').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]


FILES = pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac'


def _head(path: pathlib.Path, histories: int = 4) -> str:
    """Header and the first few histories, since parsing a whole 1 MB file is very slow."""

    text = path.read_text()
    starts = [match.start() for match in re.finditer(r'(?m)^ {10}\d+ +\d+$', text)]
    return text[: starts[histories]] if len(starts) > histories else text


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.ptrac')), ids=lambda path: path.name)
def test_valid_files_parse_completely(path: pathlib.Path) -> None:
    text = _head(path)
    ptrac, remainder = pymcnp.Ptrac.from_mcnp(text)
    assert remainder == ''
    assert ptrac.to_mcnp() == text


@pytest.mark.parametrize('path', sorted(FILES.glob('invalid*.ptrac')), ids=lambda path: path.name)
def test_invalid_files_are_rejected(path: pathlib.Path) -> None:
    try:
        _, remainder = pymcnp.Ptrac.from_mcnp(path.read_text())
        assert remainder
    except pymcnp.abc.Error:
        pass


def _kinds(ptrac: pymcnp.Ptrac) -> list[tuple[int, str, str]]:
    result = []
    for history in ptrac.histories:
        kind = str(history.i.event_type).strip()
        for event in history.events:
            result.append((int(history.i.nps), kind, event.to_mcnp()))
            kind = str(event.j.type).strip()
    return result


def _type_of(code: str) -> pymcnp.ptrac.EventType:
    return pymcnp.ptrac.EventType.from_code(int(code))


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.ptrac')), ids=lambda path: path.name)
def test_stream_matches_full_parse(path: pathlib.Path) -> None:
    ptrac, remainder = pymcnp.Ptrac.from_file(path)
    assert remainder == ''
    streamed = [(event.nps, event.type, event.raw) for event in pymcnp.Ptrac.stream(path)]
    assert streamed == [(nps, _type_of(kind), raw) for nps, kind, raw in _kinds(ptrac)]
    assert all(event.creation_code is not None for event in pymcnp.Ptrac.stream(path) if event.type is pymcnp.ptrac.EventType.BANK)


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.ptrac')), ids=lambda path: path.name)
def test_stream_accessors_never_fail(path: pathlib.Path) -> None:
    for event in pymcnp.Ptrac.stream(path):
        row = event.to_dict()
        assert row['type'] == event.type.name
        assert event.type is pymcnp.ptrac.EventType.SURFACE or event.surface is None
        assert (event.energy is None) == (event.direction is None)


def test_stream_values_on_surface_and_collision() -> None:
    events = list(pymcnp.Ptrac.stream(FILES / 'valid_27.ptrac'))
    surface = next(event for event in events if event.type is pymcnp.ptrac.EventType.SURFACE)
    assert surface.particle is pymcnp.ptrac.Particle.PHOTON
    assert surface.surface == pymcnp.ptrac.Surface(11, 0)
    assert surface.cell_entered == surface.cell == 2
    collision = next(event for event in events if event.type is pymcnp.ptrac.EventType.COLLISION)
    assert collision.zaid == 2000
    assert collision.surface is None
    bank = next(event for event in events if event.type is pymcnp.ptrac.EventType.BANK)
    assert bank.creation_code == 2011
    assert bank.particle is pymcnp.ptrac.Particle.ELECTRON


def test_surface_parse() -> None:
    assert pymcnp.ptrac.Surface.parse('3.1') == pymcnp.ptrac.Surface(3, 1)
    assert pymcnp.ptrac.Surface.parse('12') == pymcnp.ptrac.Surface(12, 0)
    assert pymcnp.ptrac.Surface.parse(' -5.2 ') == pymcnp.ptrac.Surface(5, 2)
    assert str(pymcnp.ptrac.Surface(3, 1)) == '3.1'


def test_iter_histories_matches_full_parse() -> None:
    path = FILES / 'valid_00.ptrac'
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    assert [history.to_mcnp() for history in pymcnp.Ptrac.iter_histories(path)] == [history.to_mcnp() for history in ptrac.histories]


def test_iter_is_lazy(tmp_path: pathlib.Path) -> None:
    text = (FILES / 'valid_00.ptrac').read_text()
    path = tmp_path / 'ptrac'
    path.write_text(text)
    generator = pymcnp.Ptrac.iter_histories(path)
    first = next(generator)
    assert first.to_mcnp()
    path.write_text(text + 'junk\n')  # the tail is never read until requested
    generator.close()


def test_iter_header_only(tmp_path: pathlib.Path) -> None:
    text = (FILES / 'valid_00.ptrac').read_text()
    starts = [match.start() for match in re.finditer(r'(?m)^ {10}\d+ +\d+$', text)]
    path = tmp_path / 'ptrac'
    path.write_text(text[: starts[0]])
    assert list(pymcnp.Ptrac.iter_histories(path)) == []


def test_iter_missing_file(tmp_path: pathlib.Path) -> None:
    with pytest.raises(pymcnp.abc.Error):
        list(pymcnp.Ptrac.iter_histories(tmp_path / 'missing'))


def test_iter_junk_is_rejected(tmp_path: pathlib.Path) -> None:
    path = tmp_path / 'ptrac'
    path.write_text('hello\nworld\n')
    with pytest.raises(pymcnp.abc.Error):
        list(pymcnp.Ptrac.iter_histories(path))


def test_tracks_group_events_and_link_parents() -> None:
    tracks = list(pymcnp.Ptrac.tracks(FILES / 'valid_27.ptrac'))
    events = list(pymcnp.Ptrac.stream(FILES / 'valid_27.ptrac'))
    assert [event for track in tracks for event in track.events] == events
    for track in tracks:
        assert track.creation.type in (pymcnp.ptrac.EventType.SOURCE, pymcnp.ptrac.EventType.BANK)
        assert track.events[0] is track.creation
        assert {event.nps for event in track.events} == {track.nps}
        if track.parent is not None:
            assert track.parent.index < track.index
            assert track.parent.nps == track.nps
        if track.creation.zaid:
            assert track.parent_zaid == track.creation.zaid


def test_tracks_inherit_zaid_from_parent() -> None:
    # A photon banked with ZAID 0 (made by a photon interaction) takes its parent's ZAID, `None` if there is no parent.
    for track in pymcnp.Ptrac.tracks(FILES / 'valid_27.ptrac'):
        if track.creation.type is pymcnp.ptrac.EventType.BANK and not track.creation.zaid:
            assert track.parent_zaid == (track.parent.parent_zaid if track.parent else None)


def test_to_dict_has_plain_values() -> None:
    for event in pymcnp.Ptrac.stream(FILES / 'valid_27.ptrac'):
        for value in event.to_dict().values():
            assert value is None or type(value) in (int, float, str)


def test_tracks_filters_keep_parents() -> None:
    path = FILES / 'valid_27.ptrac'
    everything = list(pymcnp.Ptrac.tracks(path))
    photons = list(pymcnp.Ptrac.tracks(path, particle=pymcnp.ptrac.Particle.PHOTON))
    assert photons and len(photons) < len(everything)
    assert all(track.particle is pymcnp.ptrac.Particle.PHOTON for track in photons)
    entered = list(pymcnp.Ptrac.tracks(path, entered=2))
    assert entered and all(list(track.entries(cell=2)) for track in entered)
    assert list(pymcnp.Ptrac.tracks(path, entered=99999)) == []
    by_key = {(track.nps, track.index): track.parent_zaid for track in everything}
    assert all(by_key[(track.nps, track.index)] == track.parent_zaid for track in photons)


def test_to_parquet(tmp_path: pathlib.Path) -> None:
    pandas = pytest.importorskip('pandas')
    path = FILES / 'valid_27.ptrac'
    out = tmp_path / 'out.parquet'
    count = pymcnp.Ptrac.to_parquet(path, out, chunk=7)
    frame = pandas.read_parquet(out)
    assert count == len(frame) == len(list(pymcnp.Ptrac.stream(path)))
    assert str(frame['nps'].dtype) == 'Int64' and str(frame['zaid'].dtype) == 'Int64' and str(frame['type'].dtype) in ('string', 'str', 'object')
    assert {'track', 'parent_zaid'} <= set(frame.columns)
    assert not list(tmp_path.glob('*.partial'))

    photons = pymcnp.Ptrac.to_parquet(path, out, particle=pymcnp.ptrac.Particle.PHOTON, types={pymcnp.ptrac.EventType.SURFACE}, cell_entered=2)
    frame = pandas.read_parquet(out)
    assert photons == len(frame)
    assert set(frame['type']) <= {'SURFACE'} and set(frame['particle']) <= {'PHOTON'} and set(frame['cell']) <= {2}


def test_to_parquet_empty_and_invalid(tmp_path: pathlib.Path) -> None:
    pandas = pytest.importorskip('pandas')
    out = tmp_path / 'out.parquet'
    assert pymcnp.Ptrac.to_parquet(FILES / 'valid_27.ptrac', out, cell_entered=99999) == 0
    assert len(pandas.read_parquet(out)) == 0
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.Ptrac.to_parquet(FILES / 'valid_27.ptrac', out, chunk=0)
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.Ptrac.to_parquet(tmp_path / 'missing', tmp_path / 'never.parquet')
    assert not (tmp_path / 'never.parquet').exists() and not list(tmp_path.glob('*.partial'))
