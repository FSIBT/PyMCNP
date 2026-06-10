import pymcnp


class Filter0(pymcnp.PtracFilter):
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
    def test_check_source_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter0().check_source(event)
        pymcnp.PtracFilter().check_source(event)

    def test_check_bank_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter0().check_bank(event)
        pymcnp.PtracFilter().check_bank(event)

    def test_check_surface_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter0().check_surface(event)
        pymcnp.PtracFilter().check_surface(event)

    def test_check_collision_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter0().check_collision(event)
        pymcnp.PtracFilter().check_collision(event)

    def test_check_terminal_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        Filter0().check_terminal(event)
        pymcnp.PtracFilter().check_terminal(event)

    def test_run_valid(self, ptrac: pymcnp.Ptrac) -> None:
        generator = Filter0().run(ptrac)
        assert not list(generator)
        generator = pymcnp.PtracFilter().run(ptrac)
        assert list(generator)
