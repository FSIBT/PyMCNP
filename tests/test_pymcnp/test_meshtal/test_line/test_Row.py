import pymcnp
from .... import classes


class Test_Row(classes.Test_FromMcnp):
    element = pymcnp.meshtal.line.Row

    EXAMPLES_FROM_MCNP_VALID = [
        '    -90.000   -90.000  -149.500 3.99211E+00 3.16463E-02',
        '  2.000E+00   -90.000   -90.000  -149.500 0.00000E+00 0.00000E+00',
        '  3.000E+00  2.000E+00  -75.000   -75.000  -137.500 0.00000E+00 0.00000E+00',
        '    Total       90.000    90.000   -52.500 5.74864E+01 3.50216E-02',
        '    Total     Total      75.000    75.000   -62.500 2.92742E+01 1.08373E-02',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
        '    -90.000   -90.000 3.99211E+00',
        '    -90.000   -90.000  -149.500 3.99211E+00 3.16463E-02 1 2 3',
        '    -90.000   -90.000  -149.500 abc 3.16463E-02',
    ]

    EXAMPLES_TO_DATAFRAME = [
        '    -90.000   -90.000  -149.500 3.99211E+00 3.16463E-02',
        '    Total       90.000    90.000   -52.500 5.74864E+01 3.50216E-02',
        '    Total     Total      75.000    75.000   -62.500 2.92742E+01 1.08373E-02',
    ]

    def test_to_dataframe_iter(self) -> None:
        """
        Tests `to_dataframe_iter` on EXAMPLES_TO_DATAFRAME`.
        """

        for example in self.EXAMPLES_TO_DATAFRAME:
            print(example)

            row, _ = self.element.from_mcnp(example)
            generator = row.to_dataframe_iter(returning=True)
            try:
                while True:
                    next(generator)
            except StopIteration as err:
                assert err.value.equals(row.to_dataframe())
