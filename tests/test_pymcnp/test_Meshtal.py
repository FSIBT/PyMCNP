import pathlib

import pandas
import pytest

import pymcnp
from .. import classes


PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal'


class Test_Meshtal(classes.Test_FromFileIter, classes.Test_ToDataframe):
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
        # Testing invalid space in row.
        PATH / 'invalid_07.meshtal',
        # Testing zero rows.
        PATH / 'invalid_08.meshtal',
        # Testing total in spatial column.
        PATH / 'invalid_09.meshtal',
    ]

    EXAMPLES_TO_DATAFRAME = [
        PATH / 'valid_40.meshtal',
        PATH / 'valid_41.meshtal',
        PATH / 'valid_42.meshtal',
    ]

    def test_to_dataframe(self) -> None:
        super().test_to_dataframe()

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
                    [1.000e00, -6.667, 0.000, 0.000, 3.37456e-05, 2.16359e-01],
                    [1.000e00, 0.000, 0.000, 0.000, 7.74475e-05, 1.72463e-01],
                    [1.000e00, 6.667, 0.000, 0.000, 3.12923e-05, 2.27306e-01],
                    [2.000e01, -6.667, 0.000, 0.000, 1.11810e-04, 1.04851e-01],
                    [2.000e01, 0.000, 0.000, 0.000, 2.68914e-04, 8.36333e-02],
                    [2.000e01, 6.667, 0.000, 0.000, 1.03503e-04, 1.07872e-01],
                    ['Total', -6.667, 0.000, 0.000, 1.45555e-04, 1.02591e-01],
                    ['Total', 0.000, 0.000, 0.000, 3.46361e-04, 8.51021e-02],
                    ['Total', 6.667, 0.000, 0.000, 1.34795e-04, 1.07694e-01],
                ],
                columns=meshtal.labels,
            ),
            rtol=1e-4,
        )


class Test_Meshtal_Tallies:
    MULTI = PATH / 'multi_00.meshtal'

    def test_meshtal_multi_not_truncated(self) -> None:
        assert len(list(pymcnp.Meshtal.iter_tallies(self.MULTI))) == 2

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
