import os
import pathlib


class Test_Main:
    class Test_Main:
        def test_valid(self):
            os.system(f"pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'} --cells")
            os.system(f"pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'} --surfaces")
            os.system(f"pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'} --cells --pdf")
            os.system(f"pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'} --surfaces --pdf")

        def test_invalid(self):
            os.system(f"pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp'}")
            os.system('pymcnp visualize hello')
