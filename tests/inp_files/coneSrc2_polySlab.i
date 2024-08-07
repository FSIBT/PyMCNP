MCNP test geom, CONE SRC, LaBr, NaI detector
c in a vacuum, large poly surface for plotting
c FMESH, cone source test case
c geom: CONE src test 2 LANL Tech Report
c Cell Cards
10 6 -0.93   -110           IMP:n,p=1 $ptrac cell
20 1 -5.06   -120           IMP:n,p=1 $LaBr 4
30 4 -3.667 -130            IMP:n,p=1 $NaI 5
50 5 -1.2E-6 120 130 110 -999   IMP:n,p=1 $air
99 0         999            IMP:n,p=0 $world

c Surface Cards 
110 RPP -40 40 -40 40 -84 -80   $tally surface 
120 RCC -32 0 -38   0 0 7.62 3.81 $detector 4
130 RCC  32 0 -42   0 0 12.7 6.35 $detector 5
999 SO 120  $sphere at origin radius 120 cm

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
m4  $ NaI Detector material (-3.667 g/cc)
        53127.70c  -0.844324   $ I (84.432%)
        11023.70c  -0.152956   $ Na (15.300 %)
        81203.80c  -0.000797   $ Tl (0.159%)
        81205.80c  -0.000797
m5  $ Air (US S. Atm. sea level, N, O and Ar) (-0.001225 g/cc)
        7014.80c   -0.755636  $ N
        8016.70c   -0.231475  $ O
       18000.59c   -0.012889  $ Ar 
m6 $plastic casing, polyethylene (-0.93 g/cc)
       1001 -0.143716
       6000 -0.856284
c Mode Specification 
MODE n
NPS 1e7
c photon cutoff energy 0.1 MeV
c CUT:P j 0.1
c neutron cutoff time 5 shakes
CUT:N 5
c analog capture below 20 MeV
PHYS:n j 20
print
c Source Specification 
c CONE SRC test 2 LANL
c cone source with half angle 25.8
SDEF X=0 Y=0 Z=0 DIR=D1 ERG=14.05 par=n VEC=0 0 -1
si1    -1 0.90 1  $histogram bins
sp1    0 0.0 1  $source bias 
c Tally Specification
c tally photons crossing tally surface
F1:n 110.5 110.6 $top, bottom
*C1 90 0 
E1 0.1 4095I 10
FMESH4:N GEOM=xyz ORIGIN= -40 -40 -85
        IMESH = 40 IINTS= 100
        JMESH = 40 JINTS= 100
        KMESH = -79 KINTS= 1
ptrac file=asc write=all event=src,sur max=5e6 type=n cell=10
c end file
