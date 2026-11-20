import sys
import pathlib

import pytest

from pymcnp._cli import convert


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


def test_main_valid(monkeypatch) -> None:
    for kind, path in (('outp', FILES / 'outp' / 'valid_39.outp'), ('meshtal', FILES / 'meshtal' / 'valid_40.meshtal'), ('ptrac', FILES / 'ptrac' / 'valid_38.ptrac')):
        monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', kind, '--csv', str(path)])
        convert.main()

        monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', kind, '--parquet', str(path)])
        convert.main()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit):
        convert.main()

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', 'hello'])
    with pytest.raises(SystemExit):
        convert.main()
