import pymcnp

print(pymcnp.outp.TallyNps4._REGEX.pattern)
s = pymcnp.outp.TallyNps4.from_mcnp(
    """
1tally       14        nps =  1000000000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:      12                                                                                   
                         2.86848E+03
 
 cell  12                                                                                                                              
      energy   
    1.0000E-01   3.62214E-07 0.0025
    1.0000E+01   2.53639E-10 0.1054
      total      6.83312E-06 0.0008


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally       14

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 6.8273E-06 to 6.8389E-06; 6.8215E-06 to 6.8447E-06; 6.8157E-06 to 6.8505E-06
 estimated  symmetric confidence interval(1,2,3 sigma): 6.8273E-06 to 6.8389E-06; 6.8215E-06 to 6.8447E-06; 6.8157E-06 to 6.8505E-06

"""[1:-1]
)
print(s.to_mcnp())
