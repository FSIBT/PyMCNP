import pymcnp
from .... import classes


class Test_AnalysisTallyFluctuation(classes.Test_Nonterminal):
    element = pymcnp.outp.block.AnalysisTallyFluctuation
    EXAMPLES_VALID = [
        '\n1analysis of the results in the tally fluctuation chart bin (tfc) for tally        5 with nps =  1000000000  print table 160\n\n\n normed average tally per history  = 8.13535E-06          unnormed average tally per history  = 8.13535E-06\n estimated tally relative error    = 0.0018               estimated variance of the variance  = 0.0136\n relative error from zero tallies  = 0.0006               relative error from nonzero scores  = 0.0017\n\n number of nonzero history tallies =     3134665          efficiency for the nonzero tallies  = 0.0031\n history number of largest  tally  =   128763072          largest  unnormalized history tally = 4.64070E+00\n (largest  tally)/(average tally)  = 5.70437E+05          (largest  tally)/(avg nonzero tally)= 1.78813E+03\n\n (confidence interval shift)/mean  = 0.0001               shifted confidence interval center  = 8.13577E-06\n\n\n if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:\n\n      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.\n\n      mean                            8.13535E-06             8.13999E-06                     0.000570\n      relative error                  1.80328E-03             1.89028E-03                     0.048242\n      variance of the variance        1.35589E-02             1.94788E-02                     0.436599\n      shifted center                  8.13577E-06             8.13594E-06                     0.000021\n      figure of merit                 4.46449E+03             4.06302E+03                    -0.089926\n\n the estimated inverse power slope of the 200 largest  tallies starting at 1.66171E-01 is 3.0488\n the history score probability density function appears to have an unsampled region at the largest  history scores:\n please examine. see print table 161.\n\n fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.452E+07)*( 1.754E-02)**2 = (1.452E+07)*(3.075E-04) = 4.464E+03',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
