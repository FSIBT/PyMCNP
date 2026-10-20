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
