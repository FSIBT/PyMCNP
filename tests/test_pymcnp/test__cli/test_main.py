import sys
import shutil
import pathlib
import matplotlib.pyplot

import pytest

import pymcnp
from pymcnp._cli import main


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


def test_main_valid(monkeypatch, fake_mcnp: str, tmp_path: pathlib.Path) -> None:
    outp = tmp_path / 'valid_39.outp'
    shutil.copy(FILES / 'outp' / 'valid_39.outp', outp)

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help', 'hello'])
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
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'help', 'hello'])
    main.main()

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / 'inp' / 'valid_00.inp')])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', str(outp)])
    main.main()
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
