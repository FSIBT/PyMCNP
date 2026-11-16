import typing
import pathlib

import pymcnp


PATH = pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac'


class Processor(pymcnp.PtracProcessor):
    def process_source(self, event: pymcnp.ptrac.block.Event) -> typing.Any:
        return event


class Test_PtracProcessor:
    def test_process_source(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_source(event)

    def test_process_bank(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_bank(event)

    def test_process_surface(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_surface(event)

    def test_process_collision(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_collision(event)

    def test_process_terminal(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_terminal(event)

    def test_run(self, ptrac: pymcnp.Ptrac) -> None:
        generator = pymcnp.PtracProcessor().run(ptrac)
        assert set(generator) == set()
        generator = Processor().run(ptrac)
        assert list(generator)

    def test_run_file(self) -> None:
        generator = pymcnp.PtracProcessor().run_file(PATH / 'valid_38.ptrac')
        assert set(generator) == set()
        generator = Processor().run_file(PATH / 'valid_38.ptrac')
        assert list(generator)
