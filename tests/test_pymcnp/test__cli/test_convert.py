import pathlib
import subprocess


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'example_00.outp'), '1', '--csv'])
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'example_00.outp'), '1', '--parquet'])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp'), '1', '--csv'])
            subprocess.run(['pymcnp', 'convert', 'hello', '1', '--csv'])
