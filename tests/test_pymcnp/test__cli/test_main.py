import sys
import pathlib

import pymcnp
from pymcnp._cli import main


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


def test_main_valid(monkeypatch, fake_mcnp: str) -> None:
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
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', str(FILES / 'outp' / 'valid_39.outp')])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(FILES / 'outp' / 'valid_39.outp'), '21'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'valid_00.inp'), f'--command={fake_mcnp}'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(FILES / 'inp' / 'valid_00.inp')])
    main.main()


def test_main_invalid(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['pymcnp', '--version'])
    try:
        main.main()
    except SystemExit:
        pass
    assert capsys.readouterr().out.strip() == f'pymcnp {pymcnp.__version__}'
