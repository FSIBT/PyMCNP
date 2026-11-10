import sys
import pathlib

import pytest

from pymcnp._cli import run


def test_main_valid(monkeypatch, fake_mcnp: str) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), f'--command={fake_mcnp}'])
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
