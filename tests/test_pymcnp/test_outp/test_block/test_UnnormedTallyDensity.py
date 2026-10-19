import pymcnp
from .... import classes


class Test_UnnormedTallyDensity(classes.Test_Nonterminal):
    element = pymcnp.outp.block.UnnormedTallyDensity
    EXAMPLES_VALID = [
        '\n1unnormed tally density for tally        2          nonzero tally mean(m) = 3.375E+00   nps =       10000  print table 161\n\n abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 0.0)\n  tally  number num den log den:d---------------------------------------------------------------------------------------------------\n 2.51+00      2 3.87-04  -3.412 ****************************************************************************************************\n 3.16+00      0 0.00+00   0.000                                                                                                     \n 3.98+00      0 0.00+00   0.000                                                                                                     \n 5.01+00      0 0.00+00   0.000                                                                                                     \n 6.31+00      1 7.71-05  -4.113 *                                                                                                   \n  total       3 3.00-04         d---------------------------------------------------------------------------------------------------\n',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
