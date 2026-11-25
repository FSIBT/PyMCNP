import pathlib
import re
import types

import pandas
import pytest

import pymcnp
from .. import classes


PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac'


class Test_Ptrac(classes.Test_FromFileIter, classes.Test_ToDataframe):
    element = pymcnp.Ptrac

    EXAMPLES_FROM_FILE_VALID = [
        PATH / 'valid_38.ptrac',
        PATH / 'valid_39.ptrac',
        PATH / 'valid_03.ptrac',
    ]
    EXAMPLES_FROM_FILE_INVALID = [
        PATH / 'invalid_02.ptrac',
        PATH / 'invalid_03.ptrac',
        PATH / 'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        PATH / 'valid_38.ptrac',
        PATH / 'valid_03.ptrac',
    ]


FILES = PATH


def _kinds(ptrac: pymcnp.Ptrac) -> list[tuple[int, str, str]]:
    result = []
    for history in ptrac.histories:
        kind = str(history.event_type).strip()
        for event in history.events:
            result.append((int(history.nps), kind, event.to_mcnp()))
            kind = str(event.type).strip()
    return result


def _type_of(code: str) -> pymcnp.ptrac.EventType:
    return pymcnp.ptrac.EventType.from_code(int(code))


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.ptrac')), ids=lambda path: path.name)
def test_stream_matches_full_parse(head, path: pathlib.Path) -> None:
    path = head(path.name)
    ptrac, remainder = pymcnp.Ptrac.from_file(path)
    assert remainder == ''
    streamed = [(event.nps, event.type, event.raw) for event in pymcnp.Ptrac.stream(path)]
    assert streamed == [(nps, _type_of(kind), raw) for nps, kind, raw in _kinds(ptrac)]
    assert all(event.creation_code is not None for event in pymcnp.Ptrac.stream(path) if event.type is pymcnp.ptrac.EventType.BANK)


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.ptrac')), ids=lambda path: path.name)
def test_stream_accessors_never_fail(head, path: pathlib.Path) -> None:
    path = head(path.name)
    for event in pymcnp.Ptrac.stream(path):
        row = event.to_dict()
        assert row['type'] == event.type.name
        assert event.type is pymcnp.ptrac.EventType.SURFACE or event.surface is None
        assert (event.energy is None) == (event.direction is None)


def test_stream_values_on_surface_and_collision(valid_27: pathlib.Path) -> None:
    events = list(pymcnp.Ptrac.stream(valid_27))
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


def test_iter_histories_matches_full_parse(head) -> None:
    path = head('valid_00.ptrac')
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


def test_tracks_group_events_and_link_parents(valid_27: pathlib.Path) -> None:
    tracks = list(pymcnp.Ptrac.tracks(valid_27))
    events = list(pymcnp.Ptrac.stream(valid_27))
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


def test_tracks_inherit_zaid_from_parent(valid_27: pathlib.Path) -> None:
    # A photon banked with ZAID 0 (made by a photon interaction) takes its parent's ZAID, `None` if there is no parent.
    for track in pymcnp.Ptrac.tracks(valid_27):
        if track.creation.type is pymcnp.ptrac.EventType.BANK and not track.creation.zaid:
            assert track.parent_zaid == (track.parent.parent_zaid if track.parent else None)


def test_to_dict_has_plain_values(valid_27: pathlib.Path) -> None:
    for event in pymcnp.Ptrac.stream(valid_27):
        for value in event.to_dict().values():
            assert value is None or type(value) in (int, float, str)


def test_tracks_filters_keep_parents(valid_27: pathlib.Path) -> None:
    path = valid_27
    everything = list(pymcnp.Ptrac.tracks(path))
    photons = list(pymcnp.Ptrac.tracks(path, particle=pymcnp.ptrac.Particle.PHOTON))
    assert photons and len(photons) < len(everything)
    assert all(track.particle is pymcnp.ptrac.Particle.PHOTON for track in photons)
    entered = list(pymcnp.Ptrac.tracks(path, entered=2))
    assert entered and all(list(track.entries(cell=2)) for track in entered)
    assert list(pymcnp.Ptrac.tracks(path, entered=99999)) == []
    by_key = {(track.nps, track.index): track.parent_zaid for track in everything}
    assert all(by_key[(track.nps, track.index)] == track.parent_zaid for track in photons)


def test_to_parquet(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    path = valid_27
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


def test_to_parquet_empty_and_invalid(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    out = tmp_path / 'out.parquet'
    assert pymcnp.Ptrac.to_parquet(valid_27, out, cell_entered=99999) == 0
    assert len(pandas.read_parquet(out)) == 0
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.Ptrac.to_parquet(valid_27, out, chunk=0)
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.Ptrac.to_parquet(tmp_path / 'missing', tmp_path / 'never.parquet')
    assert not (tmp_path / 'never.parquet').exists() and not list(tmp_path.glob('*.partial'))


def test_history_tracks_links_bank_parent() -> None:
    history = next(history for history in pymcnp.Ptrac.iter_histories(FILES / 'valid_01.ptrac') if int(history.nps) == 646)
    tracks = list(history.tracks)
    assert len(tracks) == 2
    assert tracks[1].parent is tracks[0]


def test_stream_matches_from_file_events(head) -> None:
    path = head('valid_00.ptrac')
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    assert sum(1 for _ in pymcnp.Ptrac.stream(path)) == sum(len(history.events) for history in ptrac.histories)
    list(pymcnp.Ptrac.tracks(path))


def test_stream_does_not_read_whole_file(monkeypatch: pytest.MonkeyPatch) -> None:
    def boom(*args, **kwargs):
        raise AssertionError('read_text')

    monkeypatch.setattr(pathlib.Path, 'read_text', boom)
    assert next(pymcnp.Ptrac.stream(FILES / 'valid_00.ptrac')) is not None


def test_to_dataframe_typed(head) -> None:
    ptrac, _ = pymcnp.Ptrac.from_file(head('valid_01.ptrac'))
    frame = ptrac.to_dataframe()
    assert str(frame['nps'].dtype) == 'Int64'
    assert not [column for column in frame.columns if frame[column].dtype == object]


def test_to_dataframe_empty() -> None:
    ptrac = types.SimpleNamespace(histories=[])
    generator = pymcnp.Ptrac.to_dataframe_iter(ptrac, returning=True)  # type: ignore[arg-type]
    with pytest.raises(StopIteration) as stop:
        next(generator)
    assert len(stop.value.value) == 0
    assert 'nps' in stop.value.value.columns


def _lines(path: pathlib.Path) -> tuple[list[str], list[int]]:
    lines = path.read_text().split('\n')
    return lines, [i for i, line in enumerate(lines) if re.match(r' {10}\d+ +\d+$', line)]


@pytest.mark.parametrize('cut', [1, 2, 3, 4, 5])
def test_truncated_last_history_is_kept(tmp_path: pathlib.Path, cut: int, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: starts[1] + cut]) + '\n')
    full = list(pymcnp.Ptrac.iter_histories(valid_27))
    histories = list(pymcnp.Ptrac.iter_histories(path))
    assert len(histories) == 2
    assert histories[0].to_mcnp() == full[0].to_mcnp()
    assert int(histories[1].nps) == int(full[1].nps)
    assert len(histories[1].events) == (cut - 1) // 2
    assert [event.nps for event in pymcnp.Ptrac.stream(path)] == [int(histories[0].nps)] * len(histories[0].events) + [int(histories[1].nps)] * len(histories[1].events)
    list(pymcnp.Ptrac.tracks(path))
    out = tmp_path / 'out.parquet'
    assert pymcnp.Ptrac.to_parquet(path, out) == len(histories[0].events) + len(histories[1].events)


def test_malformed_inner_history_is_rejected(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    lines[starts[0] + 3] = '       7777' + lines[starts[0] + 3][11:]
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: starts[2]]) + '\n')
    with pytest.raises(pymcnp.abc.Error):
        list(pymcnp.Ptrac.iter_histories(path))


def test_history_without_events_is_rejected() -> None:
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.ptrac.block.History.from_mcnp('         12      1000\n')


def test_iter_complete_history_then_end(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: starts[1]]) + '\n')
    assert len(list(pymcnp.Ptrac.iter_histories(path))) == 1


def test_iter_empty_and_bad_header(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('')
    with pytest.raises(pymcnp.abc.Error):
        list(pymcnp.Ptrac.iter_histories(path))
    path.write_text('\n'.join([*lines[: starts[0]], 'extra', *lines[starts[0] : starts[1]]]) + '\n')
    with pytest.raises(pymcnp.abc.Error):
        list(pymcnp.Ptrac.iter_histories(path))


def test_iter_trailing_junk_is_rejected(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: starts[1]]) + '\njunk\n')
    with pytest.raises(pymcnp.abc.Error):
        list(pymcnp.Ptrac.iter_histories(path))
    out = tmp_path / 'out.parquet'
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.Ptrac.to_parquet(path, out, chunk=1)
    assert not out.exists() and not list(tmp_path.glob('*.partial'))


def test_to_parquet_types_only(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    out = tmp_path / 'out.parquet'
    count = pymcnp.Ptrac.to_parquet(valid_27, out, types={pymcnp.ptrac.EventType.COLLISION})
    frame = pandas.read_parquet(out)
    assert count == len(frame) > 0
    assert set(frame['type']) == {'COLLISION'}


def test_unknown_particle_number(valid_27: pathlib.Path) -> None:
    event = next(pymcnp.Ptrac.stream(valid_27))
    event._j = ['0', '0', '99', '0', '0', '0']
    assert event.type is pymcnp.ptrac.EventType.SOURCE
    assert event.particle == 99


def test_track_entries_and_creation_code(valid_27: pathlib.Path) -> None:
    tracks = list(pymcnp.Ptrac.tracks(valid_27))
    bank = next(track for track in tracks if track.creation.type is pymcnp.ptrac.EventType.BANK)
    assert bank.creation_code == bank.creation.creation_code is not None
    assert next(track for track in tracks if track.creation.type is pymcnp.ptrac.EventType.SOURCE).creation_code is None
    entries = list(bank.entries())
    assert all(event.type is pymcnp.ptrac.EventType.SURFACE for event in entries)
    crossing = next(track for track in tracks if list(track.entries()))
    assert list(crossing.entries(surface=99999)) == []
    assert list(crossing.entries(cell=99999)) == []


def test_tracks_skip_events_before_a_source(valid_27: pathlib.Path) -> None:
    events = list(pymcnp.Ptrac.stream(valid_27))
    assert events[0].type is pymcnp.ptrac.EventType.SOURCE
    tracks = list(pymcnp.ptrac.tracks(events[1:]))
    assert all(track.creation.type in (pymcnp.ptrac.EventType.SOURCE, pymcnp.ptrac.EventType.BANK) for track in tracks)


def test_iter_history_with_trailing_text_is_rejected(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    lines[starts[1] - 1] += ' extra'
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: starts[1]]) + '\n')
    with pytest.raises(pymcnp.abc.Error):
        list(pymcnp.Ptrac.iter_histories(path))


def test_to_dataframe_rows_match_stream(head) -> None:
    path = head('valid_27.ptrac', 4)
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    frame = ptrac.to_dataframe()
    assert frame['track'].notna().all()
    assert frame['track'].max() > 0
    expected = pymcnp.ptrac.to_dataframe([event.to_dict() for event in pymcnp.Ptrac.stream(path)])
    pandas.testing.assert_frame_equal(frame.drop(columns=['track', 'parent_zaid']), expected.drop(columns=['track', 'parent_zaid']))
