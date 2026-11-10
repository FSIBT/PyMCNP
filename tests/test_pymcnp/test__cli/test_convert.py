import sys
import pathlib

import pandas
import pytest

from pymcnp._cli import convert


def test_main_valid(monkeypatch) -> None:
    files = pathlib.Path(__file__).parent.parent.parent.parent / 'files'
    for kind, path in (('outp', files / 'outp' / 'valid_39.outp'), ('meshtal', files / 'meshtal' / 'valid_40.meshtal'), ('ptrac', files / 'ptrac' / 'valid_27.ptrac')):
        for option, read in (('--csv', pandas.read_csv), ('--parquet', pandas.read_parquet)):
            out = pathlib.Path(path.stem + '.' + option[2:])
            local = pathlib.Path(path.name)
            local.write_text(path.read_text())
            monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', kind, option, str(local)])
            convert.main()
            assert len(read(out)) > 0


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit):
        convert.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', 'hello'])
    with pytest.raises(SystemExit):
        convert.main()
