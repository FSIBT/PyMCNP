import pymcnp
from .... import classes


class Test_NeutronActivity(classes.Test_Nonterminal):
    element = pymcnp.outp.block.NeutronActivity
    EXAMPLES_VALID = [
        '\n1neutron  activity in each cell                                                                         print table 126\n\n                       tracks     population   collisions   collisions     number        flux        average      average\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp\n                                                          (per history)    energy       energy     (relative)      (cm)\n\n        1        1      998401      1003380      5426818    3.2659E+00   8.0494E-01   1.4170E+00   6.2420E-01   2.6321E+00\n\n           total        998401      1003380      5426818    3.2659E+00'
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
