import pathlib
import subprocess


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp')])
            subprocess.run(['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'example_04.inp'), '--fix'])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp')])
            subprocess.run(['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_01.inp')])
            subprocess.run(['pymcnp', 'check', 'hello'])
