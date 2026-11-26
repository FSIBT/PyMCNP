import inspect
import dataclasses
import pathlib
import re
import types
import warnings

import pandas
import pytest

import pymcnp
from pymcnp.Ptrac import _history_events as pymcnp_history_events
from pymcnp.ptrac.Event import _layout as pymcnp_layout
from pymcnp.ptrac.block.History import _kinds as pymcnp_history_kinds
from .. import classes


PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac'


class Test_Ptrac(classes.Test_FromFileIter):
    element = pymcnp.Ptrac

    EXAMPLES_FROM_FILE_VALID = [
        PATH / 'valid_38.ptrac',
        PATH / 'valid_39.ptrac',
        PATH / 'valid_03.ptrac',
    ]
    EXAMPLES_FROM_FILE_INVALID = [
        PATH / 'invalid_04.ptrac',
        PATH / 'hello',
    ]
    # Testing a trailing ideographic space (U+3000) after the last event.
    EXAMPLES_FROM_FILE_REMAINDER = {
        PATH / 'trailing_02.ptrac': '\u3000',
        PATH / 'trailing_03.ptrac': '\u3000',
    }


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
def test_stream_matches_parse_of_first_histories(head, path: pathlib.Path) -> None:
    path = head(path.name)
    ptrac, remainder = pymcnp.Ptrac.from_file(path)
    assert remainder == ''
    streamed = [(event.nps, event.type, event.raw) for event in pymcnp.Ptrac.stream(path)]
    assert streamed == [(nps, _type_of(kind), raw) for nps, kind, raw in _kinds(ptrac)]
    assert all(event.creation_code is not None for event in pymcnp.Ptrac.stream(path) if event.type is pymcnp.ptrac.EventType.BANK)


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.ptrac')), ids=lambda path: path.name)
def test_stream_whole_file(path: pathlib.Path) -> None:
    histories = 0
    with warnings.catch_warnings():
        warnings.simplefilter('error')  # no truncation
        for history in pymcnp.Ptrac.iter_histories(path):
            assert isinstance(history, pymcnp.ptrac.block.History)
            events = list(pymcnp_history_events(history))
            assert events
            assert events[0].type is pymcnp.ptrac.EventType.SOURCE
            assert int(events[-1].block.type) == 9000
            histories += 1
    # Some of the files only have a header.
    assert histories > 0 or len(path.read_text().splitlines()) <= 9


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


def _header() -> pymcnp.ptrac.block.Header:
    return pymcnp.Ptrac.from_file(FILES / 'valid_03.ptrac')[0].header


def test_to_dataframe_empty() -> None:
    ptrac = types.SimpleNamespace(header=_header(), histories=[])
    generator = pymcnp.Ptrac.to_dataframe_iter(ptrac, returning=True)  # type: ignore[arg-type]
    with pytest.raises(StopIteration) as stop:
        next(generator)
    assert len(stop.value.value) == 0
    assert 'nps' in stop.value.value.columns


def _lines(path: pathlib.Path) -> tuple[list[str], list[int]]:
    lines = path.read_text().split('\n')
    return lines, [i for i, line in enumerate(lines) if re.match(r' {10}\d+ +\d+$', line)]


@pytest.mark.filterwarnings('ignore::pymcnp.abc.Warning')
@pytest.mark.parametrize('cut', [1, 2, 3, 4, 5])
def test_truncated_last_history_is_kept(tmp_path: pathlib.Path, cut: int, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: starts[1] + cut]) + '\n')
    full = list(pymcnp.Ptrac.iter_histories(valid_27))
    with pytest.warns(pymcnp.abc.Warning, match='truncated'):
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
    tracks = list(pymcnp.Ptrac.tracks(path))
    assert frame['track'].tolist() == [track.index for track in tracks for _ in track.events]
    assert frame['parent_zaid'].tolist() == [track.parent_zaid if track.parent_zaid is not None else pandas.NA for track in tracks for _ in track.events]
    expected = pymcnp.ptrac.to_dataframe([event.to_dict() for event in pymcnp.Ptrac.stream(path)])
    pandas.testing.assert_frame_equal(frame.drop(columns=['track', 'parent_zaid']), expected.drop(columns=['track', 'parent_zaid']))


@pytest.mark.filterwarnings('ignore::pymcnp.abc.Warning')
def test_truncated_history_tracks(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: starts[1] + 7]) + '\n')
    last = list(pymcnp.Ptrac.iter_histories(path))[-1]
    assert isinstance(last, pymcnp.ptrac.block.HistoryTruncated)
    assert [event for track in last.tracks for event in track.events] == list(pymcnp_history_events(last))


def test_truncated_warning_reports_kept_events(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, starts = _lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: starts[1] + 5]) + '\n')
    with pytest.warns(pymcnp.abc.Warning, match='kept=2'):
        list(pymcnp.Ptrac.iter_histories(path))


@pytest.mark.filterwarnings('ignore::pymcnp.abc.Warning')
@pytest.mark.parametrize('kept', [0, 1, 2])
def test_cut_in_the_middle_of_a_line(tmp_path: pathlib.Path, valid_27: pathlib.Path, kept: int) -> None:
    lines, starts = _lines(valid_27)
    # i line, then J/P pairs; cut inside the J line and inside the P line of the next event.
    for cut_line in (starts[1] + 1 + 2 * kept, starts[1] + 2 + 2 * kept):
        for column in (3, 15):
            text = '\n'.join([*lines[:cut_line], lines[cut_line][:column]])
            path = tmp_path / f'ptrac_{cut_line}_{column}'
            path.write_text(text)
            histories = list(pymcnp.Ptrac.iter_histories(path))
            assert len(histories) == 2
            assert len(histories[1].events) == kept
            assert histories[0].to_mcnp() == next(iter(pymcnp.Ptrac.iter_histories(valid_27))).to_mcnp()


@pytest.mark.parametrize('corruption', ['bad_type', 'bad_p_line', 'inserted_line'])
def test_corrupt_truncated_history_is_rejected(tmp_path: pathlib.Path, valid_27: pathlib.Path, corruption: str) -> None:
    lines, starts = _lines(valid_27)
    cut = lines[: starts[1] + 11]  # history i line and five events, then the file ends
    second_event = starts[1] + 3
    match corruption:
        case 'bad_type':
            cut[second_event] = '       7777' + cut[second_event][11:]
        case 'bad_p_line':
            cut[second_event + 1] = 'garbage'
        case _:
            cut.insert(second_event, 'garbage line')
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(cut) + '\n')
    with pytest.raises(pymcnp.abc.Error):
        list(pymcnp.Ptrac.iter_histories(path))


def _last_history_lines(valid_27: pathlib.Path) -> tuple[list[str], int, int]:
    lines, starts = _lines(valid_27)
    return lines, starts[1], starts[2] - 2  # lines, i line and the J line announcing 9000 of the second history


@pytest.mark.parametrize('variant', ['after_j', 'after_j_without_newline', 'mid_p'])
def test_cut_inside_the_final_event_is_truncated(tmp_path: pathlib.Path, valid_27: pathlib.Path, variant: str) -> None:
    lines, first, j = _last_history_lines(valid_27)
    match variant:
        case 'after_j':
            text = '\n'.join(lines[: j + 1]) + '\n'
        case 'after_j_without_newline':
            text = '\n'.join(lines[: j + 1])
        case _:
            text = '\n'.join([*lines[: j + 1], lines[j + 1][:15]])
    path = tmp_path / 'ptrac'
    path.write_text(text)
    with pytest.warns(pymcnp.abc.Warning, match='truncated'):
        histories = list(pymcnp.Ptrac.iter_histories(path))
    assert len(histories) == 2
    assert isinstance(histories[1], pymcnp.ptrac.block.HistoryTruncated)
    full = list(pymcnp.Ptrac.iter_histories(valid_27))[1]
    assert len(histories[1].events) == len(full.events) - 1
    assert [event.to_mcnp() for event in histories[1].events] == [event.to_mcnp() for event in full.events[:-1]]


def test_final_newline_missing_is_not_truncation(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, _, j = _last_history_lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: j + 2]))
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        histories = list(pymcnp.Ptrac.iter_histories(path))
    assert len(histories) == 2
    assert type(histories[1]) is pymcnp.ptrac.block.History


@pytest.mark.filterwarnings('ignore::pymcnp.abc.Warning')
@pytest.mark.parametrize('name', [path.name for path in sorted(FILES.glob('valid*.ptrac'))])
def test_to_dataframe_equals_concat(head, name: str) -> None:
    # The first histories only, since whole files are slow.
    path = head(name, 20)
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    frames = list(ptrac.to_dataframe_iter())
    expected = pandas.concat(frames, ignore_index=True) if frames else pymcnp.ptrac.to_dataframe([])
    frame = ptrac.to_dataframe()
    pandas.testing.assert_frame_equal(frame, expected)
    # The generic ``to_dataframe``, i.e., the result of ``to_dataframe_iter(returning=True)``.
    pandas.testing.assert_frame_equal(frame, pymcnp.abc.symbol.WithDataIter.to_dataframe(ptrac))


def test_to_dataframe_equals_concat_empty() -> None:
    ptrac = types.SimpleNamespace(header=_header(), histories=[])
    frame = pymcnp.Ptrac.to_dataframe(ptrac)  # type: ignore[arg-type]
    pandas.testing.assert_frame_equal(frame, pymcnp.ptrac.to_dataframe([]))


def test_to_dataframe_builds_one_frame(monkeypatch: pytest.MonkeyPatch, valid_27: pathlib.Path) -> None:
    ptrac, _ = pymcnp.Ptrac.from_file(valid_27)
    assert len(ptrac.histories) > 1
    calls = []
    to_dataframe = pymcnp.ptrac.to_dataframe
    monkeypatch.setattr(pymcnp.ptrac, 'to_dataframe', lambda rows: calls.append(1) or to_dataframe(rows))
    ptrac.to_dataframe()
    assert calls == [1]


def _events_per_generator(path: pathlib.Path) -> list[int]:
    return [sum(1 for _ in generator) for generator in pymcnp.Ptrac.from_file_iter(path)]


def test_from_file_iter_yields_one_generator_per_history() -> None:
    path = FILES / 'valid_31.ptrac'
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    assert _events_per_generator(path) == [len(history.events) for history in ptrac.histories]


@pytest.mark.filterwarnings('ignore::pymcnp.abc.Warning')
def test_from_file_iter_yields_one_generator_per_history_truncated(tmp_path: pathlib.Path, valid_27: pathlib.Path) -> None:
    lines, _, j = _last_history_lines(valid_27)
    path = tmp_path / 'ptrac'
    path.write_text('\n'.join(lines[: j + 1]) + '\n')  # the second (last) history is cut inside its final event
    counts = _events_per_generator(path)
    assert len(counts) == len(list(pymcnp.Ptrac.iter_histories(path))) == 2
    assert counts[0] == len(next(pymcnp.Ptrac.iter_histories(valid_27)).events)
    assert counts[1] > 0


def _block_values(event: pymcnp.ptrac.Event) -> dict:
    """
    Reads the values of ``event`` from its event block's named fields.
    """

    def number(name: str) -> int | None:
        value = getattr(event.block, name, None)
        return int(float(value)) if value is not None and value.strip() else None

    kind = event.type
    return {
        'particle': number('pbl_i_ipt'),
        'cell': number('ncl_pbl_i_icl'),
        'material': number('mat_pbl_i_icl'),
        'zaid': (number('nxs_2_iex') or None) if kind in (pymcnp.ptrac.EventType.COLLISION, pymcnp.ptrac.EventType.BANK) else None,
        'surface': number('nsf_pbl_i_jsu') if kind is pymcnp.ptrac.EventType.SURFACE else None,
    }


def _event_values(event: pymcnp.ptrac.Event) -> dict:
    particle = event.particle
    return {
        'particle': None if particle is None else int(particle),
        'cell': event.cell,
        'material': event.material,
        'zaid': event.zaid,
        'surface': None if event.surface is None else event.surface.number,
    }


@pytest.mark.parametrize('name', ['valid_35.ptrac', 'valid_27.ptrac', 'valid_31.ptrac'])
def test_stream_matches_block_fields(head, name: str) -> None:
    # The source J line of these files holds NODE NSR IPT NCL MAT (variable IDs 8 9 16 17 18).
    path = head(name, 5)
    events = list(pymcnp.Ptrac.stream(path))
    assert events[0].type is pymcnp.ptrac.EventType.SOURCE
    assert any(event.type is pymcnp.ptrac.EventType.SOURCE and event.particle is not None for event in events)
    for event in events:
        assert _event_values(event) == _block_values(event), event.raw
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    expected = pymcnp.ptrac.to_dataframe([event.to_dict() for event in events])
    pandas.testing.assert_frame_equal(ptrac.to_dataframe().drop(columns=['track', 'parent_zaid']), expected.drop(columns=['track', 'parent_zaid']))


def test_first_source_event_of_valid_35(head) -> None:
    event = next(pymcnp.Ptrac.stream(head('valid_35.ptrac', 1)))
    assert event.type is pymcnp.ptrac.EventType.SOURCE
    assert (event.particle, event.cell, event.material) == (pymcnp.ptrac.Particle.PHOTON, 200, 2)
    row = event.to_dict()
    assert (row['particle'], row['cell'], row['material']) == ('PHOTON', 200, 2)


def _with_header(path: pathlib.Path, tmp_path: pathlib.Path, old: str, new: str) -> pathlib.Path:
    lines = path.read_text().split('\n')
    assert old in lines[5] + '\n' + lines[6]
    lines[5:7] = (lines[5] + '\n' + lines[6]).replace(old, new, 1).split('\n')
    out = tmp_path / path.name
    out.write_text('\n'.join(lines))
    return out


# The header's source line (8 9 17 18 19, 3 P values) fits no form, which warns.
@pytest.mark.filterwarnings('ignore:PTRAC header layout has no event block form:pymcnp.abc.Warning')
def test_stream_reads_values_by_header_variable_ids(head, tmp_path: pathlib.Path) -> None:
    # The header says the source J line holds NODE NSR NCL MAT NCP (8 9 17 18 19), so the values are read that way, whatever the event block guessed.
    path = _with_header(head('valid_35.ptrac', 1), tmp_path, '   9  16  17  18', '   9  17  18  19')
    event = next(pymcnp.Ptrac.stream(path))
    assert (event.particle, event.cell, event.material) == (None, 2, 200)
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    assert ptrac.to_dataframe()[['particle', 'cell', 'material']].iloc[0].tolist() == [pandas.NA, 2, 200]
    # Without the header, e.g., for a history block on its own, the event block's fields are used.
    event = next(pymcnp_history_events(ptrac.histories[0]))
    assert (event.particle, event.cell, event.material) == (pymcnp.ptrac.Particle.PHOTON, 200, 2)


# The header's source line (8 9 17 18 19, 3 P values) fits no form, which warns.
@pytest.mark.filterwarnings('ignore:PTRAC header layout has no event block form:pymcnp.abc.Warning')
def test_event_layout_is_private(head, tmp_path: pathlib.Path) -> None:
    # The header layout is an implementation detail: it is an init-only `_layout` argument, not a field, attribute or repr entry.
    names = [field.name for field in dataclasses.fields(pymcnp.ptrac.Event)]
    assert [name for name in names if not name.startswith('_')] == ['nps', 'type', 'creation_code', 'block']
    assert 'layout' not in names and '_layout' not in names
    path = _with_header(head('valid_35.ptrac', 1), tmp_path, '   9  16  17  18', '   9  17  18  19')
    event = next(pymcnp.Ptrac.stream(path))
    assert not hasattr(event, 'layout') and '_layout' not in pymcnp.ptrac.Event.__slots__
    assert 'layout' not in repr(event)
    # The block alone gives the block's fields; `_layout` (here from the header) overrides them.
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    layout = pymcnp_layout(ptrac.header)
    plain = pymcnp.ptrac.Event(event.nps, event.type, event.creation_code, event.block)
    assert (plain.particle, plain.cell, plain.material) == (pymcnp.ptrac.Particle.PHOTON, 200, 2)
    with_layout = pymcnp.ptrac.Event(event.nps, event.type, event.creation_code, event.block, _layout=layout)
    assert (with_layout.particle, with_layout.cell, with_layout.material) == (None, 2, 200)
    assert with_layout == plain
    with pytest.raises(TypeError):
        pymcnp.ptrac.Event(event.nps, event.type, event.creation_code, event.block, layout=layout)
    # `_layout` is keyword-only and left out of the documented signature.
    with pytest.raises(TypeError):
        pymcnp.ptrac.Event(event.nps, event.type, event.creation_code, event.block, layout)
    assert list(inspect.signature(pymcnp.ptrac.Event).parameters) == ['nps', 'type', 'creation_code', 'block']


@pytest.mark.parametrize(
    'old, new',
    [
        # Counts that are not numbers.
        ('     2    6    3', '     2    x    3'),
        # Counts that do not add up to the number of variable IDs.
        ('     2    6    3', '     2    5    3'),
        # A J line whose IDs do not start with the event type (ID 7).
        ('   2   7   8   9', '   2   6   8   9'),
        # A J line with another number of values than the event has.
        pytest.param('     2    6    3', '     2    5    4', marks=pytest.mark.filterwarnings('ignore:PTRAC header layout has no event block form:pymcnp.abc.Warning')),
    ],
    ids=['number', 'counts', 'type', 'length'],
)
def test_stream_with_inconsistent_header_reads_block_fields(head, tmp_path: pathlib.Path, old: str, new: str) -> None:
    path = _with_header(head('valid_35.ptrac', 1), tmp_path, old, new)
    event = next(pymcnp.Ptrac.stream(path))
    assert (event.particle, event.cell, event.material) == (pymcnp.ptrac.Particle.PHOTON, 200, 2)


# valid_39_noipt.ptrac is valid_39.ptrac (MODE N P, WRITE=ALL) cut to 8 histories, with the particle type (variable ID
# 16, IPT) dropped from the header and from every J line, as MCNP writes it for a single particle type.
NOIPT = FILES / 'valid_39_noipt.ptrac'


def test_header_chooses_event_block_forms() -> None:
    # Each event type's form is the one whose J-line variable IDs and number of P-line values are the header's.
    kinds = {
        'valid_00.ptrac': '_1',  # 8 9 17 18, 3 P values
        'valid_27.ptrac': '_2',  # 8 9 16 17 18, 3 P values
        'valid_39_noipt.ptrac': '_3',  # 8 9 17 18 19, 9 P values
        'valid_39.ptrac': '_4',  # 8 9 16 17 18 19, 9 P values
    }
    for name, suffix in kinds.items():
        header = next(_read_header(FILES / name))
        assert [form.__name__ for form in pymcnp_history_kinds(header).values()] == [f'{base}{suffix}' for base in ('EventSource', 'EventBank', 'EventSurface', 'EventCollision', 'EventTermination')]


def _read_header(path: pathlib.Path):
    from pymcnp.Ptrac import _read

    yield next(_read(path))


def _with_headers(path: pathlib.Path, tmp_path: pathlib.Path, *changes: tuple[str, str]) -> pathlib.Path:
    for old, new in changes:
        path = _with_header(path, tmp_path, old, new)
    return path


@pytest.mark.parametrize(
    'changes, warned',
    [
        # A source J line `8 9 17 18 19` with 3 P values, which no form has: one warning.
        ([('    2    5', '    2    6'), ('   9  17  18', '   9  17  18  19')], True),
        # Counts that are not numbers: the header describes no lines, so nothing to warn about.
        ([('    2    5', '    x    5')], False),
    ],
)
def test_header_without_a_matching_form_keeps_the_trial_parse(head, tmp_path: pathlib.Path, changes: list[tuple[str, str]], warned: bool) -> None:
    # Event types no form fits are left to the parse by length, as without a header.
    path = head('valid_00.ptrac', 1)
    changed = _with_headers(path, tmp_path, *changes)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        header = next(_read_header(changed))
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        kinds = pymcnp_history_kinds(header)
    assert kinds['      1000'] is pymcnp.ptrac.block.EventSource
    messages = [str(warning.message) for warning in caught if issubclass(warning.category, pymcnp.abc.Warning)]
    if warned:
        assert len(messages) == 1
        assert 'source' in messages[0] and 'ptrac.block' in messages[0] and 'stream' in messages[0]
    else:
        assert messages == []
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        ptrac, remainder = pymcnp.Ptrac.from_file(changed)
        events = list(pymcnp.Ptrac.stream(changed))
    assert len([warning for warning in caught if issubclass(warning.category, pymcnp.abc.Warning)]) == 2 * warned
    assert events
    assert remainder == ''
    assert ptrac.histories.to_mcnp() == pymcnp.Ptrac.from_file(path)[0].histories.to_mcnp()


def test_header_that_disagrees_with_the_lines_falls_back_to_the_trial_parse(head, tmp_path: pathlib.Path) -> None:
    # valid_27's header without IPT (16) on the bank line names form _1, but its bank J lines hold IPT: they are parsed by
    # length, as without a header.
    path = head('valid_27.ptrac', 4)
    changed = _with_headers(path, tmp_path, ('    2    6    3    7', '    2    6    3    6'), ('   8  10  11  16  17  18', '   8  10  11  17  18'))
    header = next(_read_header(changed))
    assert pymcnp_history_kinds(header)['bank'] is pymcnp.ptrac.block.EventBank_1
    ptrac, remainder = pymcnp.Ptrac.from_file(changed)
    assert remainder == ''
    banks = [event for history in ptrac.histories for event in history.events if isinstance(event, pymcnp.ptrac.block.EventBank)]
    assert banks and all(isinstance(event, pymcnp.ptrac.block.EventBank_2) for event in banks)
    assert [history.to_mcnp() for history in pymcnp.Ptrac.iter_histories(changed)] == [history.to_mcnp() for history in ptrac.histories]


def test_no_ipt_header_block_fields_and_tracks() -> None:
    # Without IPT the blocks are forms _3: the same values as valid_39's forms _4, less the particle type.
    ptrac, remainder = pymcnp.Ptrac.from_file(NOIPT)
    assert remainder == ''
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        full = list(pymcnp.Ptrac.iter_histories(FILES / 'valid_39.ptrac'))[: len(ptrac.histories)]
    assert len(ptrac.histories) == 8
    for history, other in zip(ptrac.histories, full):
        assert len(history.events) == len(other.events)
        for event, original in zip(history.events, other.events):
            assert type(event).__name__ == type(original).__name__.replace('_4', '_3')
            assert not hasattr(event, 'pbl_i_ipt')
            assert {name: getattr(event, name) for name in type(event)._fields} == {name: getattr(original, name) for name in type(event)._fields}
        tracks = list(history.tracks)
        expected = list(other.tracks)
        assert [len(track.events) for track in tracks] == [len(track.events) for track in expected]
        assert all(track.particle is None for track in tracks)
        assert [[(event.cell, event.material, event.position) for event in track.events] for track in tracks] == [
            [(event.cell, event.material, event.position) for event in track.events] for track in expected
        ]
    # The streaming parse reads the same blocks.
    assert [history.to_mcnp() for history in pymcnp.Ptrac.iter_histories(NOIPT)] == [history.to_mcnp() for history in ptrac.histories]


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.ptrac')), ids=lambda path: path.name)
def test_block_events_agree_with_stream(path: pathlib.Path) -> None:
    # Every event read by the block's field names (no header) equals the streamed event read by the header's IDs.
    streamed = pymcnp.Ptrac.stream(path)
    count = 0
    for history in pymcnp.Ptrac.iter_histories(path):
        for event in pymcnp_history_events(history):
            assert event.to_dict() == next(streamed).to_dict(), event.raw
            count += 1
    assert next(streamed, None) is None
    assert count > 0 or len(path.read_text().splitlines()) <= 9


def test_public_signatures_have_no_private_parameters() -> None:
    # Private parameters belong in private functions, so that the documented signatures stay as they were.
    classes = [pymcnp.Ptrac, pymcnp.ptrac.block.History, pymcnp.ptrac.block.HistoryTruncated, pymcnp.ptrac.Event]
    for cls in classes:
        for name, member in [('', cls), *inspect.getmembers(cls, callable)]:
            if name.startswith('_'):
                continue
            parameters = inspect.signature(member).parameters
            assert not [p for p in parameters if p.startswith('_')], f'{cls.__name__}.{name}'


# Events of the first history of valid_39 (`PTRAC ... WRITE=ALL`), one of each type, written out by hand from the file:
# the J line holds the header's variables for the type (e.g., source: next type, node, NSR, IPT, NCL, MAT, NCP), the
# P line x y z u v w energy weight time. A bank event's creation code is the type its previous event announced.
VALID_39_EVENTS = {
    # 3000 1 40 1 4 4 0 / 0 0 0 -0.23578 0.0082756 -0.97177 14.1 1 0
    0: {
        'nps': 1,
        'type': 'SOURCE',
        'creation_code': None,
        'particle': 'NEUTRON',
        'cell': 4,
        'material': 4,
        'surface': None,
        'facet': None,
        'zaid': None,
        'x': 0.0,
        'y': 0.0,
        'z': 0.0,
        'u': -0.23578,
        'v': 0.0082756,
        'w': -0.97177,
        'energy': 14.1,
        'weight': 1.0,
        'time': 0.0,
    },
    # 3000 2 1.5 166 1 1 1 0 / ... 0.40071
    1: {
        'nps': 1,
        'type': 'SURFACE',
        'creation_code': None,
        'particle': 'NEUTRON',
        'cell': 1,
        'material': 1,
        'surface': 1,
        'facet': 5,
        'zaid': None,
        'x': -4.8527,
        'y': 0.17032,
        'z': -20.0,
        'u': -0.23578,
        'v': 0.0082756,
        'w': -0.97177,
        'energy': 14.1,
        'weight': 1.0,
        'time': 0.40071,
    },
    # 4000 4 8016 22 1 2 2 1
    4: {
        'nps': 1,
        'type': 'COLLISION',
        'creation_code': None,
        'particle': 'NEUTRON',
        'cell': 2,
        'material': 2,
        'surface': None,
        'facet': None,
        'zaid': 8016,
        'x': -24.601,
        'y': 0.86344,
        'z': -101.39,
        'u': -0.92844,
        'v': -0.2709,
        'w': -0.2542,
        'energy': 2.0635,
        'weight': 0.87134,
        'time': 2.0314,
    },
    # 2008 6 1 1 1 5 0 30
    36: {
        'nps': 1,
        'type': 'TERMINAL',
        'creation_code': None,
        'particle': 'NEUTRON',
        'cell': 5,
        'material': 0,
        'surface': None,
        'facet': None,
        'zaid': None,
        'x': 31.745,
        'y': -373.69,
        'z': 330.68,
        'u': 0.094981,
        'v': -0.6493,
        'w': 0.75458,
        'energy': 1.8947e-07,
        'weight': 0.82901,
        'time': 96127.0,
    },
    # 4000 5 8016 0 2 2 2 0, after the terminal event announced 2008
    37: {
        'nps': 1,
        'type': 'BANK',
        'creation_code': 2008,
        'particle': 'PHOTON',
        'cell': 2,
        'material': 2,
        'surface': None,
        'facet': None,
        'zaid': 8016,
        'x': -24.601,
        'y': 0.86344,
        'z': -101.39,
        'u': -0.10228,
        'v': -0.0084908,
        'w': -0.99472,
        'energy': 3.6845,
        'weight': 1.0,
        'time': 2.0314,
    },
}


def test_event_values_of_valid_39_by_hand(head) -> None:
    path = head('valid_39.ptrac', 1)
    events = list(pymcnp.Ptrac.stream(path))

    for index, expected in VALID_39_EVENTS.items():
        assert events[index].to_dict() == expected, events[index].raw

    # The dataframe has the same values in the same columns.
    ptrac, _ = pymcnp.Ptrac.from_file(path)
    frame = ptrac.to_dataframe()
    for index, expected in VALID_39_EVENTS.items():
        row = frame.iloc[index]
        assert {name: (None if pandas.isna(row[name]) else row[name]) for name in expected} == expected
