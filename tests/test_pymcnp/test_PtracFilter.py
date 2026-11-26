import pytest

import pymcnp
from pymcnp.Ptrac import _events


KINDS = {
    pymcnp.ptrac.EventType.SOURCE: 'source',
    pymcnp.ptrac.EventType.BANK: 'bank',
    pymcnp.ptrac.EventType.SURFACE: 'surface',
    pymcnp.ptrac.EventType.COLLISION: 'collision',
    pymcnp.ptrac.EventType.TERMINAL: 'terminal',
}


class Filter0(pymcnp.PtracFilter):
    def check_source(self, event: pymcnp.ptrac.Event) -> bool:
        return False

    def check_bank(self, event: pymcnp.ptrac.Event) -> bool:
        return False

    def check_surface(self, event: pymcnp.ptrac.Event) -> bool:
        return False

    def check_collision(self, event: pymcnp.ptrac.Event) -> bool:
        return False

    def check_terminal(self, event: pymcnp.ptrac.Event) -> bool:
        return False


class Test_PtracFilter:
    @pytest.mark.parametrize('kind', KINDS.values())
    def test_check_keeps_by_default(self, event: pymcnp.ptrac.Event, kind: str) -> None:
        assert getattr(pymcnp.PtracFilter(), f'check_{kind}')(event) is True

    def test_run_valid(self, ptrac: pymcnp.Ptrac) -> None:
        assert not list(Filter0().run(ptrac))
        assert list(pymcnp.PtracFilter().run(ptrac)) == list(_events(ptrac))

    @pytest.mark.parametrize('kind', KINDS.values())
    def test_run_checks_each_event_by_its_type(self, ptrac: pymcnp.Ptrac, kind: str) -> None:
        checked = []

        class Only(pymcnp.PtracFilter):
            def _check(self, name: str, event: pymcnp.ptrac.Event) -> bool:
                checked.append((name, KINDS[event.type]))
                return name == kind

        for name in KINDS.values():
            setattr(Only, f'check_{name}', lambda self, event, name=name: self._check(name, event))

        kept = list(Only().run(ptrac))

        events = list(_events(ptrac))
        assert kept and kept == [event for event in events if KINDS[event.type] == kind]
        assert checked == [(KINDS[event.type], KINDS[event.type]) for event in events]

    def test_run_path_matches_object(self, head) -> None:
        path = head('valid_00.ptrac')
        full, _ = pymcnp.Ptrac.from_file(path)
        assert [event.raw for event in pymcnp.PtracFilter().run(path)] == [event.raw for event in pymcnp.PtracFilter().run(full)]
