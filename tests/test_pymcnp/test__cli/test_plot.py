import os
import pathlib

import matplotlib.pyplot


class Test_Main:
    class Test_Main:
        def test_valid(self):
            os.system(f'pymcnp plot {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "outp" / "valid_38.outp"} 1')
            os.system(f'pymcnp plot {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "outp" / "valid_38.outp"} 1 --pdf')
            matplotlib.pyplot.close()

        def test_invalid(self):
            os.system(f'pymcnp plot {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "outp" / "invalid_02.outp"} 1')
            os.system(f'pymcnp plot {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "outp" / "valid_38.outp"} 123')
            os.system('pymcnp plot hello 1')
            matplotlib.pyplot.close()
