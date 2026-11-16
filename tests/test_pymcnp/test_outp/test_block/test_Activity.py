import pymcnp
from .... import classes


class Test_Activity(classes.Test_FromMcnp):
    element = pymcnp.outp.block.Activity

    EXAMPLES_FROM_MCNP_VALID = [
        '\n1neutron  activity in each cell                                                                         print table 126\n\n                       tracks     population   collisions   collisions     number        flux        average      average\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp\n                                                          (per history)    energy       energy     (relative)      (cm)\n\n        1        1      998401      1003380      5426818    3.2659E+00   8.0494E-01   1.4170E+00   6.2420E-01   2.6321E+00\n\n           total        998401      1003380      5426818    3.2659E+00',
        '\n1photon   activity in each cell                                                                         print table 126\n\n                       tracks     population   collisions   collisions     number        flux        average      average\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp\n                                                          (per history)    energy       energy     (relative)      (cm)\n\n        1        1       10572        10434           26    2.6000E-03   2.3555E+00   2.3555E+00   1.0000E+00   2.1683E+04\n        2        2       10571        32576        46943    4.6943E+00   1.9269E+00   1.9269E+00   1.0000E+00   1.6948E+00\n\n           total         21143        43010        46969    4.6969E+00',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        '\n1neutron  activity in each cell                                                                         print table 126\n\n                       tracks     population   collisions   collisions     number        flux        average      average\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp\n                                                          (per history)    energy       energy     (relative)      (cm)\n\n        1        1      998401      1003380      5426818    3.2659E+00   8.0494E-01   1.4170E+00   6.2420E-01   2.6321E+00\n\n           total        998401      1003380      5426818    3.2659E+00',
        '\n1photon   activity in each cell                                                                         print table 126\n\n                       tracks     population   collisions   collisions     number        flux        average      average\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp\n                                                          (per history)    energy       energy     (relative)      (cm)\n\n        1        1       10572        10434           26    2.6000E-03   2.3555E+00   2.3555E+00   1.0000E+00   2.1683E+04\n        2        2       10571        32576        46943    4.6943E+00   1.9269E+00   1.9269E+00   1.0000E+00   1.6948E+00\n\n           total         21143        43010        46969    4.6969E+00',
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
