import pathlib

import pandas
import pytest

import pymcnp


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


class Test_File:
    def test_from_file_invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Inp.from_file('hello.hi')

    def test_to_file_writes(self, tmp_path: pathlib.Path) -> None:
        inp, _ = pymcnp.Inp.from_file(sorted((FILES / 'inp').glob('valid_*.inp'))[0])
        path = tmp_path / 'a.inp'

        inp.to_file(path)

        _, rest = pymcnp.Inp.from_file(path)
        assert rest == ''

    def test_to_file_csv_and_parquet(self, tmp_path: pathlib.Path) -> None:
        outp, _ = pymcnp.Outp.from_file(FILES / 'outp' / 'valid_39.outp')
        csv, parquet = tmp_path / 'a.csv', tmp_path / 'a.parquet'

        outp.to_file_csv(csv)
        outp.to_file_parquet(parquet)

        assert len(pandas.read_csv(csv)) == len(outp.to_dataframe())
        assert len(pandas.read_parquet(parquet)) == len(outp.to_dataframe())
