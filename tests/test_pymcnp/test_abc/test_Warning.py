import pathlib
import warnings

import pymcnp


PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp'


class Test_Warning:
    def test___str___valid(self) -> None:
        assert str(pymcnp.abc.Warning('Hi', 'Hello')) == 'Hi\n Hello'

    def test_warning_is_shown(self) -> None:
        source = (PATH / 'warning_00.inp').read_text()

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            try:
                pymcnp.Inp.from_mcnp(source)
            except pymcnp.abc.Error:
                pass

        assert any(issubclass(w.category, pymcnp.abc.Warning) for w in caught)
        assert warnings.showwarning.__module__ in ('warnings', '_py_warnings')
