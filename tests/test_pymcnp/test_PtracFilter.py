import pathlib

import pymcnp


PATH = pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac'


class Filter(pymcnp.PtracFilter):
    def check_source(self, event: pymcnp.ptrac.block.Event) -> bool:
        return False

    def check_bank(self, event: pymcnp.ptrac.block.Event) -> bool:
        return False

    def check_surface(self, event: pymcnp.ptrac.block.Event) -> bool:
        return False

    def check_collision(self, event: pymcnp.ptrac.block.Event) -> bool:
        return False

    def check_terminal(self, event: pymcnp.ptrac.block.Event) -> bool:
        return False


class Test_PtracFilter:
    def test_check_source(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter().check_source(event)
        pymcnp.PtracFilter().check_source(event)

    def test_check_bank(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter().check_bank(event)
        pymcnp.PtracFilter().check_bank(event)

    def test_check_surface(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter().check_surface(event)
        pymcnp.PtracFilter().check_surface(event)

    def test_check_collision(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter().check_collision(event)
        pymcnp.PtracFilter().check_collision(event)

    def test_check_terminal(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter().check_terminal(event)
        pymcnp.PtracFilter().check_terminal(event)

    def test_run(self, ptrac: pymcnp.Ptrac) -> None:
        generator = Filter().run(ptrac)
        assert not list(generator)
        generator = pymcnp.PtracFilter().run(ptrac)
        assert list(generator)

    def test_run_file(self, ptrac: pymcnp.Ptrac) -> None:
        generator = Filter().run_file(PATH / 'valid_38.ptrac')
        assert not list(generator)
        generator = pymcnp.PtracFilter().run_file(PATH / 'valid_38.ptrac')
        assert list(generator)
