import pathlib

import pymcnp


class Test_Convert:
    def test_to_csv_valid(self, convert: pymcnp.Convert) -> None:
        convert.to_csv('1', pathlib.Path('hello.csv'))

    def test_to_parquet_valid(self, convert: pymcnp.Convert) -> None:
        convert.to_parquet('1', pathlib.Path('hello.parquet'))
