import pymcnp
from .... import classes


class Test_Row(classes.Test_FromMcnp, classes.Test_ToDataframe):
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
