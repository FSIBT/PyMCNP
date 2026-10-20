import pathlib

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

    def test_run_path_matches_object(self) -> None:
        path = pathlib.Path(__file__).parents[2] / 'files' / 'ptrac' / 'valid_00.ptrac'
        ptrac, _ = pymcnp.Ptrac.from_file(path)

        class Count(pymcnp.PtracProcessor):
            def prehook(self) -> None:
                self.kinds: list[str] = []

            def process_source(self, event) -> None:
                self.kinds.append('source')

            def process_bank(self, event) -> None:
                self.kinds.append('bank')

            def process_surface(self, event) -> None:
                self.kinds.append('surface')

            def process_collision(self, event) -> None:
                self.kinds.append('collision')

            def process_terminal(self, event) -> None:
                self.kinds.append('terminal')

        from_object, from_path, from_str = Count(), Count(), Count()
        from_object.run(ptrac)
        from_path.run(path)
        from_str.run(str(path))
        assert from_object.kinds
        assert from_object.kinds == from_path.kinds == from_str.kinds
