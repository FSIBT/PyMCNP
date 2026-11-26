import sys
import shutil
import pathlib

import pytest

from pymcnp._cli import convert


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


# valid_39.outp holds a tally PyMCNP cannot parse.
@pytest.mark.filterwarnings('ignore:Tally not parsed:pymcnp.abc.Warning')
def test_main_valid(monkeypatch, tmp_path: pathlib.Path) -> None:
    for kind, source in (('outp', FILES / 'outp' / 'valid_39.outp'), ('meshtal', FILES / 'meshtal' / 'valid_40.meshtal'), ('ptrac', FILES / 'ptrac' / 'valid_38.ptrac')):
        path = tmp_path / source.name
        shutil.copy(source, path)

        monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', kind, '--csv', str(path)])
        convert.main()

        monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', kind, '--parquet', str(path)])
        convert.main()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', str(FILES / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit):
        convert.main()

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', 'hello'])
    with pytest.raises(SystemExit):
        convert.main()


@pytest.mark.parametrize('flag', ['--csv', '--parquet'])
def test_main_meshtal_converts_every_tally(monkeypatch, tmp_path: pathlib.Path, flag: str) -> None:
    import pandas

    path = tmp_path / 'multi_00.meshtal'
    shutil.copy(FILES / 'meshtal' / 'multi_00.meshtal', path)

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'meshtal', flag, str(path)])
    convert.main()

    if flag == '--csv':
        frame = pandas.read_csv(tmp_path / 'multi_00.csv')
    else:
        frame = pandas.read_parquet(tmp_path / 'multi_00.parquet')

    assert len(frame) == 8 + 9
    assert frame.columns[0] == 'number'
    assert frame['number'].tolist() == [4] * 8 + [14] * 9
    assert list(frame.columns) == ['number', 'X', 'Y', 'Z', 'Result', 'Rel Error', 'Energy']
    assert frame['Result'].iloc[0] == pytest.approx(0.002874, rel=1e-3)
    assert pandas.isna(frame['Energy'].iloc[0])
    assert str(frame['Energy'].iloc[-1]) == 'Total'


def test_main_file_without_extension(monkeypatch, tmp_path: pathlib.Path) -> None:
    # MCNP names its files `meshtal`, `outp` and `ptrac` by default.
    path = tmp_path / 'meshtal'
    shutil.copy(FILES / 'meshtal' / 'multi_00.meshtal', path)

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'meshtal', '--csv', str(path)])
    convert.main()

    assert (tmp_path / 'meshtal.csv').exists()
