import pymcnp
from .... import classes


class Test_Activity(classes.Test_FromMcnp):
    element = pymcnp.outp.line.Activity

    EXAMPLES_FROM_MCNP_VALID = [
        '        1        1        8171         7669         4634    8.0865E-01   2.4970E+00   3.5628E+00   1.6163E+00   2.3400E+01',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        '        1        1        8171         7669         4634    8.0865E-01   2.4970E+00   3.5628E+00   1.6163E+00   2.3400E+01',
    ]

    def test_to_dataframe_iter(self) -> None:
        """
        Tests `to_dataframe_iter` on EXAMPLES_TO_DATAFRAME`.
        """

        for example in self.EXAMPLES_TO_DATAFRAME:
            print(example)

            activity, _ = self.element.from_mcnp(example)
            generator = activity.to_dataframe_iter(returning=True)
            try:
                while True:
                    next(generator)
            except StopIteration as err:
                assert err.value.equals(activity.to_dataframe())
