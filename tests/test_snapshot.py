import json

import pytest

from . import snapshot

EXPECTED = json.loads(snapshot.SNAPSHOT.read_text())


def test_snapshot_covers_every_fixture() -> None:
    assert sorted(EXPECTED) == [p.relative_to(snapshot.FILES).as_posix() for p in snapshot.fixtures()]


@pytest.mark.parametrize('key', sorted(EXPECTED))
def test_snapshot(key: str) -> None:
    assert snapshot.record(snapshot.FILES / key) == EXPECTED[key]


def test_record_all_matches_snapshot(monkeypatch: pytest.MonkeyPatch) -> None:
    # ``record_all`` regenerates files/snapshot.json; check it on a few fixtures, one per kind.
    keys = ['inp/valid_00.inp', 'outp/valid_00.outp', 'meshtal/multi_00.meshtal', 'ptrac/valid_38.ptrac']
    monkeypatch.setattr(snapshot, 'fixtures', lambda: [snapshot.FILES / key for key in keys])
    assert snapshot.record_all() == {key: EXPECTED[key] for key in keys}


def _same_parse(a: dict, b: dict) -> bool:
    # Error messages name the file, which differs; everything else must match.
    return {k: v for k, v in a.items() if k != 'error'} == {k: v for k, v in b.items() if k != 'error'}


@pytest.mark.parametrize('key', sorted(EXPECTED))
def test_snapshot_crlf(key: str, tmp_path) -> None:
    # Windows editors write CRLF line ends: every reader gives the same result for them.
    path = tmp_path / key
    path.parent.mkdir()
    path.write_bytes((snapshot.FILES / key).read_bytes().replace(b'\n', b'\r\n'))
    assert _same_parse(snapshot.record(path), EXPECTED[key])
