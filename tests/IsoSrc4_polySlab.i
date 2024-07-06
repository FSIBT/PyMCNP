MCNP INPUT Polyethelene SLAB WITH LaBr DETECTOR
c test case: reduced particles 
c based on MCNP-Intro Examples 1&2
c three part geom: slab, cylinder, sph world+source
c Cell Cards
10 3 -0.96   -110           IMP:n,p=1 $poly slab
20 5 -1.2E-3 110 120 -999   IMP:n,p=1 $air
30 1 -5.06   -120           IMP:n,p=1 $LaBr
99 0         999            IMP:n,p=0 $world

c Surface Cards 
110 RPP -7 7 -12 12 -33 -27 $ ENLARGED slab 30 cm below source
120 RCC -33.8 0 -30 7.62 0 0 3.81 $LaBr cylinder level with slab
999 SO 90  $sphere at origin radius 90 cm

c Data Block
c Material Specification
m1  $ LaBr Detector material (-5.06 g/cc)
      35079    -0.375208   $ Br (74.026%)
      35081    -0.365052
      57138    -0.000222   $ La (24.675%)
      57139    -0.246531
      58136    -0.000024   $ Ce (1.299%)
      58138    -0.000033
      58140    -0.011487
      58142    -0.001443
m3 6012 1 1001 2  $polyethelene C2H4
m5 8016 -0.21  7014 -0.78 018040 -0.01 $ air  
c Mode Specification 
c Mode Specification 
MODE n p
NPS 4E6
c photon cutoff energy 0.1 MeV
CUT:P j 0.1
c neutron cutoff time 10 shakes
CUT:N 10
c analog capture below 15 MeV
PHYS:n j 15
print
c Source Specification 
c spherical neutron source radius 1 cm 
SDEF POS 0 0 0 rad=D1 ERG=14.05 par=n
si1      0 1
sp1    -21 2
c Tally Specification
c tally photon flux in detector 
F4:P 30 
E4 0 1E-5 0.05 493i 10
ptrac file=asc write=all event=col,bnk,src,sur max=2E6 type=p,n cell=30
c end file