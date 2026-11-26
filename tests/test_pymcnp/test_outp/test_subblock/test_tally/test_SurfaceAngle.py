import pymcnp
from ..... import classes


class Test_SurfaceAngle(classes.Test_FromMcnp, classes.Test_ToDataframe):
    element = pymcnp.outp.subblock.tally.SurfaceAngle

    EXAMPLES_FROM_MCNP_VALID = [
        ' surface  2.1                                                                                                                          \n angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     \n      energy   \n    1.0000E-01   8.29996E-06 0.1098\n    1.1934E-01   3.80440E-06 0.1622\n    1.3867E-01   2.70000E-06 0.1924\n      total      1.49149E-04 0.0259\n \n',
        ' surface  2.1                                                                                                                          \n angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     \n      energy   \n\n      total      1.49149E-04 0.0259\n \n',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        ' surface  2.1                                                                                                                          \n angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     \n      energy   \n    1.0000E-01   8.29996E-06 0.1098\n    1.1934E-01   3.80440E-06 0.1622\n    1.3867E-01   2.70000E-06 0.1924\n      total      1.49149E-04 0.0259\n \n',
        ' surface  2.1                                                                                                                          \n angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     \n      energy   \n\n      total      1.49149E-04 0.0259\n \n',
    ]
