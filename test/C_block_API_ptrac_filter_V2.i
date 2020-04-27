DT Generator and Associated Gamma Rays from Soil  
c CELLS   
12 1 -1.30 -112 113 IMP:P,N=1 $ soil
13 2 -2.3 -113 IMP:P,N=1 $ graphite block
77 5 -0.00000125 112 113 -999 IMP:P,N=1 $ air everywhere, set to air here
99 0 999 IMP:P,N=0  
  
c SURFACES   
112 RPP 50 115 -25 25 -25 25 $ soil
113 RPP 70 95 -10 10 -10 10 $ graphite block
999 SO 200 $ world  
  
c MATERIAL DEFINITIONS  
m1 $ nlib = 60c plib = 04p pnlib = 70u $ soil
       8016     -0.51   $ O
      14028     -0.35   $ Si
      13027     -0.08   $ Al
	  026054    -0.04   $ Fe
       6012     -0.02   $ C	   
m2 6012 1   $ C	
m5 8016 -0.21  7014 -0.78 018040 -0.01 $ air  
c DATA CARDS  
mode n p  
sdef erg=14.0 x=0 y=0 z=0 par=1 vec=1 0 0 DIR=d1 $ isotropic neutron source 
SI1 -1 0.894427 1 $ histogram for cosine bin limits ---- cos(26.5651 deg)
SP1 0 0.95 0.05 $ fraction of solid angle for each bin
SB1 0. 0. 1. $ source bias for each bin
c stop ctme 1 $ computer counting time
f5:p 45 30 0 5 $ point detector at the location of the actual detector
nps 1e5 $ number of particles if not computer time used
print 
ptrac file=asc write=all event=src,bnk max=1000000000 tally=5 value=0 type=p,n $ filter=12,icl event=col,bnk  max=1000 
c ptrac file=bin write=all max=1000 coinc=lin tally=5 value=0 $