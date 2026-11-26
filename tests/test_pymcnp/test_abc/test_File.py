import types
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

    # valid_39.outp holds a tally PyMCNP cannot parse.
    @pytest.mark.filterwarnings('ignore:Tally not parsed:pymcnp.abc.Warning')
    def test_to_file_csv_and_parquet(self, tmp_path: pathlib.Path) -> None:
        outp, _ = pymcnp.Outp.from_file(FILES / 'outp' / 'valid_39.outp')
        csv, parquet = tmp_path / 'a.csv', tmp_path / 'a.parquet'

        outp.to_file_csv(csv)
        outp.to_file_parquet(parquet)

        assert len(pandas.read_csv(csv)) == len(outp.to_dataframe())
        assert len(pandas.read_parquet(parquet)) == len(outp.to_dataframe())


def _items(iterator):
    items = []
    try:
        while True:
            item = next(iterator)
            items.append(list(item) if isinstance(item, types.GeneratorType) else item)
    except StopIteration as stop:
        return items, stop.value


@pytest.mark.filterwarnings('ignore::pymcnp.abc.Warning')
@pytest.mark.parametrize(
    'kind, path',
    [
        (pymcnp.Inp, FILES / 'inp' / 'valid_36.inp'),
        (pymcnp.Outp, FILES / 'outp' / 'valid_00.outp'),
        (pymcnp.Meshtal, FILES / 'meshtal' / 'valid_38.meshtal'),
        (pymcnp.Ptrac, FILES / 'ptrac' / 'valid_00.ptrac'),
    ],
)
def test_from_mcnp_reads_crlf(kind, path) -> None:
    # Text with Windows line ends parses as `from_file` reads it, which translates them.
    text = path.read_text()
    crlf = text.replace('\n', '\r\n')

    assert kind.from_mcnp(crlf) == kind.from_file(path)
    if hasattr(kind, 'from_mcnp_iter'):
        assert _items(kind.from_mcnp_iter(crlf, returning=True)) == _items(kind.from_mcnp_iter(text, returning=True))


def test_card_from_mcnp_reads_crlf() -> None:
    assert pymcnp.inp.card.Data.from_mcnp('m1 1001 2\r\n     8016 1') == pymcnp.inp.card.Data.from_mcnp('m1 1001 2\n     8016 1')
