import json

import pytest

from . import snapshot

EXPECTED = json.loads(snapshot.SNAPSHOT.read_text())


def test_snapshot_covers_every_fixture() -> None:
    assert sorted(EXPECTED) == [str(p.relative_to(snapshot.FILES)) for p in snapshot.fixtures()]


@pytest.mark.parametrize('key', sorted(EXPECTED))
def test_snapshot(key: str) -> None:
    assert snapshot.record(snapshot.FILES / key) == EXPECTED[key]
