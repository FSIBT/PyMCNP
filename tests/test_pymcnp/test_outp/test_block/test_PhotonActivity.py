import pymcnp
from .... import classes


class Test_PhotonActivity(classes.Test_Nonterminal):
    element = pymcnp.outp.block.PhotonActivity
    EXAMPLES_VALID = [
        '\n1photon   activity in each cell                                                                         print table 126\n\n                       tracks     population   collisions   collisions     number        flux        average      average\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp\n                                                          (per history)    energy       energy     (relative)      (cm)\n\n        1        1       10572        10434           26    2.6000E-03   2.3555E+00   2.3555E+00   1.0000E+00   2.1683E+04\n        2        2       10571        32576        46943    4.6943E+00   1.9269E+00   1.9269E+00   1.0000E+00   1.6948E+00\n\n           total         21143        43010        46969    4.6969E+00',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
