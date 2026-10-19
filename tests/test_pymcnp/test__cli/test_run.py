import sys
import pathlib

import pytest

from pymcnp._cli import run


def test_main_valid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--command=echo'])
    run.main()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--command=""'])
    with pytest.raises(SystemExit):
        run.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit):
        run.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_01.inp')])
    with pytest.raises(SystemExit):
        run.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_02.inp')])
    with pytest.raises(SystemExit):
        run.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', 'hello'])
    with pytest.raises(SystemExit):
        run.main()
