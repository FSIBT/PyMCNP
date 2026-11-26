import pathlib

import pandas
import pytest

import pymcnp
from .. import classes


PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal'


class Test_Meshtal(classes.Test_FromFileIter):
    element = pymcnp.Meshtal

    EXAMPLES_FROM_FILE_VALID = [
        PATH / 'valid_40.meshtal',
    ]
    EXAMPLES_FROM_FILE_INVALID = [
        PATH / 'hello.hi',
        PATH / 'invalid_04.meshtal',
        PATH / 'invalid_05.meshtal',
        # Testing wrong number of columns.
        PATH / 'invalid_06.meshtal',
        # Testing zero rows.
        PATH / 'invalid_08.meshtal',
        # Testing total in spatial column.
        PATH / 'invalid_09.meshtal',
    ]
    # Testing a trailing ideographic space (U+3000) after the last row.
    EXAMPLES_FROM_FILE_REMAINDER = {
        PATH / 'trailing_07.meshtal': '\u3000\n',
    }

    def test_to_dataframe(self) -> None:
        # Testing row count.
        meshtal, _ = pymcnp.Meshtal.from_mcnp((PATH / 'valid_40.meshtal').read_text())
        assert len(meshtal.rows) == len(meshtal.to_dataframe())

        # Testing spatial columns.
        meshtal, _ = pymcnp.Meshtal.from_file(PATH / 'valid_41.meshtal')
        pandas.testing.assert_frame_equal(
            meshtal.to_dataframe(),
            pandas.DataFrame(
                [
                    [-90.0, -90.0, -149.5, 3.99211, 0.031646],
                    [-90.0, -90.0, -148.5, 4.94717, 0.031905],
                    [-90.0, -90.0, -147.5, 5.84169, 0.029744],
                    [-90.0, -90.0, -146.5, 6.68561, 0.029817],
                    [-90.0, -90.0, -145.5, 7.31142, 0.027651],
                    [-90.0, -90.0, -144.5, 8.23604, 0.027530],
                ],
                columns=meshtal.labels,
            ),
            rtol=1e-4,
        )

        # Testing time and enety columns.
        meshtal, _ = pymcnp.Meshtal.from_file(PATH / 'valid_42.meshtal')
        pandas.testing.assert_frame_equal(
            meshtal.to_dataframe(),
            pandas.DataFrame(
                [
                    ['1.000E+00', -6.667, 0.000, 0.000, 3.37456e-05, 2.16359e-01],
                    ['1.000E+00', 0.000, 0.000, 0.000, 7.74475e-05, 1.72463e-01],
                    ['1.000E+00', 6.667, 0.000, 0.000, 3.12923e-05, 2.27306e-01],
                    ['2.000E+01', -6.667, 0.000, 0.000, 1.11810e-04, 1.04851e-01],
                    ['2.000E+01', 0.000, 0.000, 0.000, 2.68914e-04, 8.36333e-02],
                    ['2.000E+01', 6.667, 0.000, 0.000, 1.03503e-04, 1.07872e-01],
                    ['Total', -6.667, 0.000, 0.000, 1.45555e-04, 1.02591e-01],
                    ['Total', 0.000, 0.000, 0.000, 3.46361e-04, 8.51021e-02],
                    ['Total', 6.667, 0.000, 0.000, 1.34795e-04, 1.07694e-01],
                ],
                columns=meshtal.labels,
            ),
            rtol=1e-4,
        )


class Test_Meshtal_Data:
    HEAD = (PATH / 'valid_40.meshtal').read_text().split('\n\n   Energy')[0] + '\n\n'

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
        assert all(dtype == 'float64' for dtype in frame.dtypes)

    def test_time_and_energy_columns_keep_total_rows(self) -> None:
        meshtal = self._parse(
            '   Energy      Time         X         Y         Z     Result     Rel Error',
            '  3.000E+00  2.000E+00  -75.000   -75.000  -137.500 0.00000E+00 0.00000E+00\n    Total     Total      75.000    75.000   -62.500 2.92742E+01 1.08373E-02\n',
        )
        frame = meshtal.to_dataframe()
        assert frame['Energy'].tolist() == ['3.000E+00', 'Total']
        assert frame['Time'].tolist() == ['2.000E+00', 'Total']
        assert frame['Rel Error'].iloc[1] == 1.08373e-02
        assert frame['Result'].dtype == 'float64' and frame['X'].dtype == 'float64'

    def test_energy_is_float_without_total_row(self) -> None:
        meshtal = self._parse(
            '   Energy         X         Y         Z     Result     Rel Error',
            '  1.000E+00    -6.667     0.000     0.000 3.37456E-05 2.16359E-01\n  2.000E+01     0.000     0.000     0.000 7.74475E-05 1.72463E-01\n',
        )
        frame = meshtal.to_dataframe()
        assert frame['Energy'].dtype == 'float64' and frame['Energy'].tolist() == [1.0, 20.0]
        assert (frame['Energy'] > 1).tolist() == [False, True]

    def test_to_dataframe_iter_returning(self) -> None:
        meshtal, _ = pymcnp.Meshtal.from_file(PATH / 'valid_41.meshtal')
        generator = meshtal.to_dataframe_iter(returning=True)
        first = next(generator)
        with pytest.raises(StopIteration) as stop:
            next(generator)
        assert stop.value.value.equals(first)

    def test_parquet_stringifies_mixed_object_columns(self, tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
        meshtal, _ = pymcnp.Meshtal.from_file(PATH / 'valid_41.meshtal')
        monkeypatch.setattr(pymcnp.Meshtal, 'to_dataframe', lambda self: pandas.DataFrame({'a': pandas.Series([1.0, 'x', None], dtype=object)}))
        meshtal.to_file_parquet(tmp_path / 'out.parquet')
        assert pandas.read_parquet(tmp_path / 'out.parquet')['a'].tolist()[:2] == ['1.0', 'x']

    def test_names_are_plain_strings(self) -> None:
        meshtal, _ = pymcnp.Meshtal.from_file(PATH / 'valid_42.meshtal')
        assert all(type(name) is str for name in meshtal.names)
        assert type(meshtal.particle_name) is str


class Test_Meshtal_Tallies:
    MULTI = PATH / 'multi_00.meshtal'

    def test_iter_tallies_reads_every_tally(self) -> None:
        tallies = list(pymcnp.Meshtal.iter_tallies(self.MULTI))
        assert [tally.tally_number for tally in tallies] == [4, 14]
        assert [tally.particle_name for tally in tallies] == ['neutron', 'photon']
        assert [tally.names for tally in tallies] == [['X', 'Y', 'Z', 'Result', 'Rel Error'], ['Energy', 'X', 'Y', 'Z', 'Result', 'Rel Error']]
        assert [len(tally.to_dataframe()) for tally in tallies] == [8, 9]
        assert all('two mesh tallies' in str(tally.title) for tally in tallies)

    def test_iter_tallies_single_tally_file(self) -> None:
        tallies = list(pymcnp.Meshtal.iter_tallies(PATH / 'valid_41.meshtal'))
        whole, _ = pymcnp.Meshtal.from_file(PATH / 'valid_41.meshtal')
        assert len(tallies) == 1
        assert tallies[0].to_mcnp() == whole.to_mcnp()

    def test_iter_tallies_values_match_the_file(self) -> None:
        frame = list(pymcnp.Meshtal.iter_tallies(self.MULTI))[1].to_dataframe()
        assert frame['Energy'].tolist()[-1] == 'Total'
        assert frame['Result'].iloc[0] == pytest.approx(3.37456e-05)

    def test_iter_tallies_errors(self, tmp_path: pathlib.Path) -> None:
        with pytest.raises(pymcnp.abc.Error):
            list(pymcnp.Meshtal.iter_tallies(tmp_path / 'missing'))
        path = tmp_path / 'junk.mesh'
        path.write_text('hello\nworld\n')
        with pytest.raises(pymcnp.abc.Error):
            list(pymcnp.Meshtal.iter_tallies(path))

    def test_iter_tallies_rejects_trailing_junk(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'junk.mesh'
        path.write_text(self.MULTI.read_text() + 'junk\n')
        with pytest.raises(pymcnp.abc.Error):
            list(pymcnp.Meshtal.iter_tallies(path))

    def test_iter_tallies_file_without_final_newline(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'short.mesh'
        path.write_text(self.MULTI.read_text().rstrip('\n'))
        assert len(list(pymcnp.Meshtal.iter_tallies(path))) == 2
