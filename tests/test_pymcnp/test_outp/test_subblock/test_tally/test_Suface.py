import pymcnp
from ..... import classes


class Test_Surface(classes.Test_Nonterminal):
    element = pymcnp.outp.subblock.tally.Surface
    EXAMPLES_VALID = [
        '      surface:           8                                                                                         \n        time   \n    0.0000E+00   0.00000E+00 0.0000\n    1.0000E+02   7.79859E-05 0.1010\n    2.0000E+02   8.51479E-05 0.0966\n      total      7.95775E-02 0.0000\n \n',
        '      surface:           8                                                                                         \n        time   \n\n      total      7.95775E-02 0.0000\n \n',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]

    def test_to_dataframe_valid(self) -> None:
        for example in self.EXAMPLES_VALID:
            pymcnp.outp.subblock.tally.Surface.from_mcnp(example)[0].to_dataframe()
