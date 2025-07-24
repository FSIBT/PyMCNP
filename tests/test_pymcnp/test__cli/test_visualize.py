import pathlib
import subprocess


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cells'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surfaces'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cells', '--pdf'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surfaces', '--pdf'])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp')])
            subprocess.run(['pymcnp', 'visualize', 'hello'])
