import pytest

import pymcnp
from pymcnp.Ptrac import _events

from .test_PtracFilter import KINDS


class Count(pymcnp.PtracProcessor):
    """
    Records the type of every processed event, by the method that processed it.
    """

    def prehook(self) -> None:
        self.kinds: list[tuple[str, pymcnp.ptrac.EventType]] = []

    def posthook(self) -> None:
        self.done = True

    def _process(self, name: str, event: pymcnp.ptrac.Event) -> None:
        self.kinds.append((name, event.type))


for _name in KINDS.values():
    setattr(Count, f'process_{_name}', lambda self, event, name=_name: self._process(name, event))


class Test_PtracProcessor:
    @pytest.mark.parametrize('kind', KINDS.values())
    def test_process_returns_none_by_default(self, event: pymcnp.ptrac.Event, kind: str) -> None:
        assert getattr(pymcnp.PtracProcessor(), f'process_{kind}')(event) is None

    def test_run_processes_each_event_by_its_type(self, ptrac: pymcnp.Ptrac) -> None:
        count = Count()

        assert count.run(ptrac) == []
        assert count.done
        assert count.kinds == [(KINDS[event.type], event.type) for event in _events(ptrac)]
        assert {name for name, _ in count.kinds} == set(KINDS.values())

    def test_run_path_matches_object(self, head) -> None:
        path = head('valid_00.ptrac')
        ptrac, _ = pymcnp.Ptrac.from_file(path)

        from_object, from_path, from_str = Count(), Count(), Count()
        from_object.run(ptrac)
        from_path.run(path)
        from_str.run(str(path))
        assert from_object.kinds
        assert from_object.kinds == from_path.kinds == from_str.kinds

    def test_run_collects_results(self, ptrac: pymcnp.Ptrac) -> None:
        class Collect(pymcnp.PtracProcessor):
            def process_source(self, event) -> int:
                return 1

        assert pymcnp.PtracProcessor().run(ptrac) == []
        assert Collect().run(ptrac) == [1] * sum(1 for event in _events(ptrac) if event.type is pymcnp.ptrac.EventType.SOURCE)
