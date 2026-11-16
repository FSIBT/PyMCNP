import pathlib

import pandas

import pymcnp
from .. import classes


PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp'


class Test_Outp(classes.Test_FromFile, classes.Test_ToDataframe):
    element = pymcnp.Outp

    EXAMPLES_FROM_FILE_VALID = [
        PATH / 'valid_39.outp',
        PATH / 'valid_06.outp',
    ]
    EXAMPLES_FROM_FILE_INVALID = [
        PATH / 'invalid_02.outp',
        PATH / 'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        PATH / 'valid_39.outp',
        PATH / 'valid_06.outp',
    ]

    def test_to_dataframe(self) -> None:
        super().test_to_dataframe()

        outp, _ = pymcnp.Outp.from_file(PATH / 'valid_00.outp')
        pandas.testing.assert_frame_equal(
            outp.to_dataframe(),
            pandas.DataFrame(
                [
                    [1.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [2.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [3.0000e00, 2.45053e-05, 0.9999, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [4.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [5.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [6.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [7.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [8.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [9.0000e00, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.0000e01, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.1000e01, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.2000e01, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.3000e01, 0.00000e00, 0.0000, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                    [1.4000e01, 3.24502e-04, 0.7074, '2', '4', '4    track length estimate of particle flux.      units   1/cm**2', 'neutrons', '10000'],
                ],
                columns=['bins', 'counts', 'errors', 'cell_number', 'number', 'type', 'particles', 'nps'],
            ),
            rtol=1e-4,
        )

    def test_version(self) -> None:
        """
        Tests `version` on `EXAMPLES_FROM_FILE_VALID`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            outp, _ = self.element.from_file(example)
            _ = outp.version

    def test_nps(self) -> None:
        """
        Tests `nps` on `EXAMPLES_FROM_FILE_VALID`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            outp, _ = self.element.from_file(example)
            _ = outp.nps

    def test_run_time(self) -> None:
        """
        Tests `run_time` on `EXAMPLES_FROM_FILE_VALID`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            outp, _ = self.element.from_file(example)
            _ = outp.run_time

    def test_terminated(self) -> None:
        """
        Tests `terminated` on `EXAMPLES_FROM_FILE_VALID`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            outp, _ = self.element.from_file(example)
            _ = outp.terminated

    def test_warnings(self) -> None:
        """
        Tests `warnings` on `EXAMPLES_FROM_FILE_VALID`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            outp, _ = self.element.from_file(example)
            _ = outp.warnings

    def test_activities(self) -> None:
        """
        Tests `activities` on `EXAMPLES_FROM_FILE_VALID`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            outp, _ = self.element.from_file(example)
            _ = outp.activities()

    def test_tallies(self) -> None:
        """
        Tests `tallies` on `EXAMPLES_FROM_FILE_VALID`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            outp, _ = self.element.from_file(example)
            _ = outp.tallies()
            _ = outp.tallies(number='1')
