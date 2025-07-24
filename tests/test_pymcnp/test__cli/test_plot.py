import pathlib
import subprocess

import matplotlib.pyplot


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'example_00.outp'), '1'])
            subprocess.run(['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'example_00.outp'), '1', '--pdf'])
            matplotlib.pyplot.close()

        def test_invalid(self):
            subprocess.run(['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'invalid_02.outp'), '1'])
            subprocess.run(['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'example_00.outp'), '132423'])
            subprocess.run(['pymcnp', 'plot', 'hello', '1'])
            matplotlib.pyplot.close()
