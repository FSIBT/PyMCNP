import os
import pathlib


class Test_Main:
    class Test_Main:
        def test_valid(self):
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"}')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cells')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surfaces')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cells --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surfaces --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cell=1')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surface=1')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cell=1 --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surface=1 --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cells-skip=1')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surfaces-skip=1')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cells-skip=1 --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surfaces-skip=1 --pdf')

        def test_invalid(self):
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_00.inp"}')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_01.inp"}')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_02.inp"}')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "todo_41.inp"}')
            os.system('pymcnp visualize hello')
