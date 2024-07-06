MCNP Graphite Core World, CONE SRC, LaBr, NaI detector, Fe shield
c test case: lowered particles 
c fixed soil core orientation 
c in a vacuum, cylindrical soil core, brass casing, iron shielding
c geom: CONE src, core+casing, NO ALUM, LaBr, NaI, side shielding
c Cell Cards
10 3 -1.3   -110           IMP:n,p=1 $soil Core: pure silicon
11 2 -8.07 -111 110          IMP:n,p=1 $Soil Casing: Brass
20 1 -5.06   -120           IMP:n,p=1 $LaBr
c 21 7 -2.699  -121 120          IMP:n,p=1 $LaBr Casing: Alu
30 4 -3.667 -130            IMP:n,p=1 $NaI
c 31 7 -2.699  -131 130          IMP:n,p=1 $NaI Casing: Alu
50 5 -1.2E-6 111 120 130 190 191 -999   IMP:n,p=1 $air
90 8 -7.874  -190           IMP:n,p=1 $shield
91 8 -7.874  -191           IMP:n,p=1 $shield
99 0         999            IMP:n,p=0 $world

c Surface Cards 
110 RCC 0 -15 -44 0 30 0 2.54 $SOIL CORE 
111 RCC 0 -15.2 -44 0 30.4 0 2.74 $SOIL CASING
120 RCC -32 0 -38   0 0 7.62 3.81 $LaBr detector
c 121 RCC -32 0 -38.2 0 0 8.02 4.01 $LaBr casing
130 RCC  32 0 -42   0 0 12.7 6.35 $NaI detector
c 131 RCC  32 0 -42.2 0 0 13.1 6.55 $NaI Casing 
190 RPP  -39 -19 -10 10 -24 -4  $Fe shielding LaBr
191 RPP  19  39  -10 10 -24 -4  $Fe shielding NaI 
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
m2 $brass (-8.07 g/cc)
      26000 -0.000868
      29000 -0.665381
      30000 -0.325697
      50000 -0.002672
      82000 -0.005377
m3  $ Silicon
       14028.70c  1      $ Si
m4  $ NaI Detector material (-3.667 g/cc)
        53127.70c  -0.844324   $ I (84.432%)
        11023.70c  -0.152956   $ Na (15.300 %)
        81203.80c  -0.000797   $ Tl (0.159%)
        81205.80c  -0.000797
m5  $ Air (US S. Atm. sea level, N, O and Ar) (-0.001225 g/cc)
        7014.80c   -0.755636  $ N
        8016.70c   -0.231475  $ O
       18000.59c   -0.012889  $ Ar 
c m6 $plastic casing, polyethylene (-0.93 g/cc)
c       1001 -0.143716
c       6000 -0.856284
c m7 13027 1 $aluminum 
m8 26000 1 $iron
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
c cone source with half angle 28.76, alpha 5.2 cm
SDEF POS 0 0 0 DIR=D1 ERG=14.05 par=n VEC=0 0 -1
si1    -1 0.88 1  $histogram bins
sp1    0 0.95 0.05  $frac solid angle 
sb1    0. 0. 1  $source bias 
c Tally Specification
c flux tally in detector volume  
F4:P 20 30 
E4 0 1E-5 0.05 493i 10
ptrac file=asc write=all event=col,bnk,src,sur max=2e6 type=p,n cell=20,30
c end file
