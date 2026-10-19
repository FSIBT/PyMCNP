import sys
import pathlib

from pymcnp._cli import main


def test_main_valid(monkeypatch) -> None:
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

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp')])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'valid_39.outp'), '1', '--csv'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'valid_39.outp'), '21'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--command=echo'])
    main.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp')])
    main.main()
