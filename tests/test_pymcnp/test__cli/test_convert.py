import os
import pathlib


class Test_Main:
    class Test_Main:
        def test_valid(self):
            os.system(f'pymcnp convert {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "outp" / "valid_38.outp"} 1 --csv')
            os.system(f'pymcnp convert {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "outp" / "valid_38.outp"} 1 --parquet')

        def test_invalid(self):
            os.system(f'pymcnp convert {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_00.inp"} 1 --csv')
            os.system('pymcnp convert hello 1 --csv')
