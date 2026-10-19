import pymcnp


class Test_PtracProcessor:
    def test_process_source_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_source(event)

    def test_process_bank_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_bank(event)

    def test_process_surface_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_surface(event)

    def test_process_collision_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_collision(event)

    def test_process_terminal_valid(self, event: pymcnp.ptrac.block.Event) -> None:
        pymcnp.PtracProcessor().process_terminal(event)

    def test_run_valid(self, ptrac: pymcnp.Ptrac):
        pymcnp.PtracProcessor().run(ptrac)
