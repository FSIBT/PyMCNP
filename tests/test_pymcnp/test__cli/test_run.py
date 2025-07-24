import pathlib
import subprocess


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp')])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp')])
            subprocess.run(['pymcnp', 'run', 'hello'])
