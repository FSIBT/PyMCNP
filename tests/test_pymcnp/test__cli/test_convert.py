import sys
import shutil
import pathlib

import pandas
import pytest

import pymcnp

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

        # Both files hold the same rows, as many as the parsed file has.
        csv, parquet = pandas.read_csv(path.with_name(f'{path.name}.csv')), pandas.read_parquet(path.with_name(f'{path.name}.parquet'))
        assert len(csv) == len(parquet) > 0
        assert list(csv.columns) == list(parquet.columns)


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', str(FILES / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit) as error:
        convert.main()
    assert error.value.code == 1

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'outp', '--csv', 'hello'])
    with pytest.raises(SystemExit) as error:
        convert.main()
    assert error.value.code == 2


@pytest.mark.parametrize('flag', ['--csv', '--parquet'])
def test_main_meshtal_converts_every_tally(monkeypatch, tmp_path: pathlib.Path, flag: str) -> None:
    import pandas

    path = tmp_path / 'multi_00.meshtal'
    shutil.copy(FILES / 'meshtal' / 'multi_00.meshtal', path)

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'meshtal', flag, str(path)])
    convert.main()

    if flag == '--csv':
        frame = pandas.read_csv(tmp_path / 'multi_00.meshtal.csv')
    else:
        frame = pandas.read_parquet(tmp_path / 'multi_00.meshtal.parquet')

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


@pytest.mark.parametrize('flag, extension', [('--csv', 'csv'), ('--parquet', 'parquet')])
def test_main_partly_parsed(monkeypatch, capsys, tmp_path: pathlib.Path, flag: str, extension: str) -> None:
    # A line PyMCNP cannot parse drops the rest of the file: write what was parsed, warn, and exit 3, as `visualize` does.
    lines = (FILES / 'ptrac' / 'valid_39_noipt.ptrac').read_text().split('\n')
    path = tmp_path / 'partly.ptrac'
    path.write_text('\n'.join([*lines[: len(lines) // 2], 'garbage [here]', *lines[len(lines) // 2 :]]))
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'convert', 'ptrac', flag, str(path)])

    with pytest.raises(SystemExit) as error:
        convert.main()

    assert error.value.code == 3
    # The histories before the bad one are written.
    out_path = path.with_name(f'partly.ptrac.{extension}')
    frame = pandas.read_csv(out_path) if extension == 'csv' else pandas.read_parquet(out_path)
    assert 0 < len(frame) < len(pymcnp.Ptrac.from_file(FILES / 'ptrac' / 'valid_39_noipt.ptrac')[0].to_dataframe())
    out = ' '.join(capsys.readouterr().out.replace('│', '').split())
    # Parsing stops at the start of the history that holds the bad line.
    assert 'Warning:' in out and 'line 829: PyMCNP cannot parse the line "5 1000"' in out and 'every line after it are missing' in out and 'Done!' not in out
