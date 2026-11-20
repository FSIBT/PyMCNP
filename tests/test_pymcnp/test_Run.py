import pathlib

import pymcnp


PATH = pathlib.Path(__file__).parent.parent.parent / 'files'


class Test_Result:
    def test_ok(self) -> None:
        result = pymcnp.Result(
            index=0,
            directory=PATH,
            log=PATH / 'inp' / 'valid_00.log',
            inp=PATH / 'inp' / 'valid_00.inp',
            outp=PATH / 'outp' / 'valid_00.outp',
            ptrac=None,
            runtpe=None,
            returncode=0,
        )
        assert result.ok
