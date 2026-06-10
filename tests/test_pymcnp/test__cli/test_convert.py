import sys
import pathlib

import pytest

from pymcnp._cli import convert


def test_main_valid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'valid_39.outp'), '1', '--csv'])
    convert.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'valid_39.outp'), '1', '--parquet'])
    convert.main()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp'), '1', '--csv'])
    with pytest.raises(SystemExit):
        convert.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'hello', '1', '--csv'])
    with pytest.raises(SystemExit):
        convert.main()
