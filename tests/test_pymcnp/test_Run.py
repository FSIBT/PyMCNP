import pathlib

import pytest

import pymcnp


class Test_Run:
    def test___post_init___invalid(self, inp: pymcnp.Inp) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run((inp,), '')

    def test_prehook_file_valid(self, run: pymcnp.Run) -> None:
        run.prehook_file(pathlib.Path('.'), 0)

    def test_posthook_file_valid(self, run: pymcnp.Run) -> None:
        run.posthook_file(pathlib.Path('.'), 0)

    def test_prehook_batch_valid(self, run: pymcnp.Run) -> None:
        run.prehook_batch(pathlib.Path('.'))

    def test_posthook_batch_valid(self, run: pymcnp.Run) -> None:
        run.posthook_batch(pathlib.Path('.'))

    def test_run_valid(self, run: pymcnp.Run) -> None:
        run.run(pathlib.Path('.'))
