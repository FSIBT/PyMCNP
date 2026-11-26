import pymcnp
from ..... import classes


class Test_Cell(classes.Test_FromMcnp, classes.Test_ToDataframe):
    element = pymcnp.outp.subblock.tally.Cell

    EXAMPLES_FROM_MCNP_VALID = [
        ' cell  12                                                                                                                              \n      energy   \n    1.0000E-01   3.62214E-07 0.0025\n    1.9099E+00   4.26948E-09 0.0228\n    1.9198E+00   4.10659E-09 0.0231\n      total      6.83312E-06 0.0008\n \n',
        ' cell  12                                                                                                                              \n      energy   \n\n      total      6.83312E-06 0.0008\n \n',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        ' cell  12                                                                                                                              \n      energy   \n    1.0000E-01   3.62214E-07 0.0025\n    1.9099E+00   4.26948E-09 0.0228\n    1.9198E+00   4.10659E-09 0.0231\n      total      6.83312E-06 0.0008\n \n',
        ' cell  12                                                                                                                              \n      energy   \n\n      total      6.83312E-06 0.0008\n \n',
    ]
