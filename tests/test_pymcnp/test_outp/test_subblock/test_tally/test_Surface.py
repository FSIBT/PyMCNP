import pymcnp
from ..... import classes


class Test_Surface(classes.Test_FromMcnp, classes.Test_ToDataframe):
    element = pymcnp.outp.subblock.tally.Surface

    EXAMPLES_FROM_MCNP_VALID = [
        '      surface:           8                                                                                         \n        time   \n    0.0000E+00   0.00000E+00 0.0000\n    1.0000E+02   7.79859E-05 0.1010\n    2.0000E+02   8.51479E-05 0.0966\n      total      7.95775E-02 0.0000\n \n',
        '      surface:           8                                                                                         \n        time   \n\n      total      7.95775E-02 0.0000\n \n',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        '      surface:           8                                                                                         \n        time   \n    0.0000E+00   0.00000E+00 0.0000\n    1.0000E+02   7.79859E-05 0.1010\n    2.0000E+02   8.51479E-05 0.0966\n      total      7.95775E-02 0.0000\n \n',
        '      surface:           8                                                                                         \n        time   \n\n      total      7.95775E-02 0.0000\n \n',
    ]
    # Totals are not data rows: this example has only a total.
    EXAMPLES_TO_DATAFRAME_EMPTY = EXAMPLES_TO_DATAFRAME[1:]
