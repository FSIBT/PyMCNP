import sys
import shutil
import pathlib
import matplotlib.pyplot

import pytest

import pymcnp
from pymcnp._cli import main


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


# valid_39.outp holds a tally PyMCNP cannot parse.
@pytest.mark.filterwarnings('ignore:Tally not parsed:pymcnp.abc.Warning')
def test_main_valid(monkeypatch, fake_mcnp: str, tmp_path: pathlib.Path) -> None:
    outp = tmp_path / 'valid_39.outp'
    shutil.copy(FILES / 'outp' / 'valid_39.outp', outp)

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help', 'check'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help', 'convert'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help', 'plot'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help', 'run'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help', 'visualize'])
    main.main()

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / 'inp' / 'valid_00.inp')])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', str(outp)])
    main.main()
    assert outp.with_name('valid_39.outp.csv').stat().st_size > 1
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(outp), '21'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'valid_00.inp'), f'--command={fake_mcnp}'])
    main.main()

    matplotlib.pyplot.close()


@pytest.mark.render
def test_main_valid_render(monkeypatch, tmp_path: pathlib.Path) -> None:
    inp = tmp_path / 'valid_00.inp'
    shutil.copy(FILES / 'inp' / 'valid_00.inp', inp)

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp)])
    main.main()


def test_main_invalid(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['pymcnp', '--version'])
    try:
        main.main()
    except SystemExit:
        pass
    assert capsys.readouterr().out.strip() == f'pymcnp {pymcnp.__version__}'


def test_main_prints_warnings_as_panels(monkeypatch, capsys, recwarn, tmp_path: pathlib.Path) -> None:
    import warnings

    outp = tmp_path / 'valid_39.outp'
    shutil.copy(FILES / 'outp' / 'valid_39.outp', outp)
    showwarning = warnings.showwarning

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', str(outp)])
    main.main()

    out = capsys.readouterr()
    assert '╭' in out.out
    # The panel wraps long lines.
    text = ' '.join(out.out.replace('│', ' ').split())
    assert 'Warning: Tally not parsed.' in text and 'tally 1 (type 1)' in text
    # Not Python's own format, which prints the source line of the warning.
    assert 'warnings.warn' not in out.out + out.err
    assert not [w for w in recwarn if 'Tally not parsed' in str(w.message)]
    assert warnings.showwarning is showwarning


def test_main_prints_other_warnings_with_their_category(monkeypatch, capsys) -> None:
    import warnings

    from pymcnp._cli import convert

    monkeypatch.setattr(convert, 'main', lambda: warnings.warn('bins [1, 2] are empty', RuntimeWarning))
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert'])
    main.main()

    assert 'Warning: RuntimeWarning: bins [1, 2] are empty' in capsys.readouterr().out
