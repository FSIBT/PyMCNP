import pymcnp
from .... import classes


class Test_History(classes.Test_Nonterminal):
    element = pymcnp.ptrac.block.History
    EXAMPLES_VALID = [
        '       1071      1000\n       3000         1        40        15         2\n  -0.19652E+01 -0.47816E+01 -0.20412E+00\n       3000         2     15012         9        16         1\n  -0.18262E+01 -0.47726E+01 -0.18684E+00\n       3000         3     13012       171        13         2\n  -0.11783E+01 -0.47307E+01 -0.10626E+00\n       3000         4     13012         8        16         1\n  -0.97926E+00 -0.47179E+01 -0.81516E-01\n       3000         5     10010        44        11         2\n  -0.53388E+00 -0.46891E+01 -0.26131E-01\n       3000         6      8010       163        16         1\n  -0.92519E+00 -0.35997E+01  0.98944E+00\n       9000         7     15012       169        15         2\n  -0.14671E+01 -0.28438E+01  0.11291E+01',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
