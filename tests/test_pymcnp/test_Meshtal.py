import pathlib

import pytest

import pymcnp
from .. import classes


class Test_Meshtal(classes.Test_Nonterminal):
    element = pymcnp.Meshtal
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal' / 'valid_40.meshtal').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]


FILES = pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal'


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.meshtal')), ids=lambda path: path.name)
def test_valid_files_parse_completely(path: pathlib.Path) -> None:
    text = path.read_text()
    meshtal, remainder = pymcnp.Meshtal.from_mcnp(text)
    assert remainder == ''
    assert meshtal.to_mcnp() == text


@pytest.mark.parametrize('path', sorted(FILES.glob('invalid*.meshtal')), ids=lambda path: path.name)
def test_invalid_files_are_rejected(path: pathlib.Path) -> None:
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.Meshtal.from_mcnp(path.read_text())


class Test_Meshtal_Data:
    HEAD = (FILES / 'valid_40.meshtal').read_text().split('\n\n   Energy')[0] + '\n\n'

    def _parse(self, labels: str, rows: str) -> pymcnp.Meshtal:
        meshtal, remainder = pymcnp.Meshtal.from_mcnp(self.HEAD + labels + '\n' + rows)
        assert remainder == ''
        return meshtal

    def test_spatial_columns_only(self) -> None:
        meshtal = self._parse(
            '        X         Y         Z     Result     Rel Error', '    -90.000   -90.000  -149.500 3.99211E+00 3.16463E-02\n     90.000    90.000   -50.500 5.86145E+01 1.06351E-02\n'
        )
        assert meshtal.names == ['X', 'Y', 'Z', 'Result', 'Rel Error']
        frame = meshtal.to_dataframe()
        assert frame.shape == (2, 5)
        assert frame['Result'].tolist() == [3.99211, 58.6145]
        assert frame['Z'].tolist() == [-149.5, -50.5]

    def test_time_and_energy_columns_keep_total_rows(self) -> None:
        meshtal = self._parse(
            '   Energy      Time         X         Y         Z     Result     Rel Error',
            '  3.000E+00  2.000E+00  -75.000   -75.000  -137.500 0.00000E+00 0.00000E+00\n    Total     Total      75.000    75.000   -62.500 2.92742E+01 1.08373E-02\n',
        )
        frame = meshtal.to_dataframe()
        assert frame['Energy'].tolist() == ['3.000E+00', 'Total']
        assert frame['Time'].tolist() == ['2.000E+00', 'Total']
        assert frame['Rel Error'].iloc[1] == 1.08373e-02

    def test_file_without_final_newline(self) -> None:
        source = self.HEAD + '        X         Y         Z     Result     Rel Error\n    -90.000   -90.000  -149.500 3.99211E+00 3.16463E-02'
        meshtal, remainder = pymcnp.Meshtal.from_mcnp(source)
        assert remainder == ''
        assert meshtal.to_mcnp() == source

    def test_row_with_the_wrong_number_of_columns_is_rejected(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Meshtal.from_mcnp(self.HEAD + '        X         Y         Z     Result     Rel Error\n    -90.000   -90.000 3.99211E+00 3.16463E-02\n')

    def test_total_in_a_spatial_column_is_rejected(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Meshtal.from_mcnp(self.HEAD + '        X         Y         Z     Result     Rel Error\n    Total   -90.000  -149.500 3.99211E+00 3.16463E-02\n')

    def test_labels_without_rows_are_rejected(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Meshtal.from_mcnp(self.HEAD + '        X         Y         Z     Result     Rel Error\n')

    def test_full_file_row_count(self) -> None:
        meshtal, _ = pymcnp.Meshtal.from_mcnp((FILES / 'valid_40.meshtal').read_text())
        assert len(meshtal.rows) == 576 and len(meshtal.to_dataframe()) == 576
