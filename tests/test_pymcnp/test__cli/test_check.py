import sys
import pathlib

import pytest

from pymcnp._cli import check


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


def test_main_valid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / 'inp' / 'valid_00.inp')])
    check.main()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / 'inp' / 'warning_00.inp')])
    with pytest.raises(SystemExit):
        check.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit):
        check.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / 'inp' / 'invalid_01.inp')])
    with pytest.raises(SystemExit):
        check.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / 'inp' / 'invalid_02.inp')])
    with pytest.raises(SystemExit):
        check.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', 'hello'])
    with pytest.raises(SystemExit):
        check.main()
