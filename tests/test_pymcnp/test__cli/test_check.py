import os
import pathlib


class Test_Main:
    class Test_Main:
        def test_valid(self):
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"}')
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --fix')

        def test_invalid(self):
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_00.inp"}')
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_01.inp"}')
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_02.inp"}')
            os.system('pymcnp check hello')
