import pymcnp
from .... import classes


class Test_Activity(classes.Test_FromMcnp, classes.Test_ToDataframe):
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
