MCNP Graphite Core World, LaBr, NaI detector, Fe shield
c test case: lowered particles 
c fixed soil core orientation
c in a vacuum, cylindrical soil core, NO brass, iron shielding
c geom: src, core, NO casing, NO ALUM, LaBr, NaI, side shielding
c --Begin Cells--
c Cell Cards
10 3 -1.3   -110           IMP:n,p=1 $soil Core: natural soil
c 11 2 -8.07 -111 110          IMP:n,p=1 $Soil Casing: Brass
20 1 -5.06   -120           IMP:n,p=1 $LaBr
c 21 7 -2.699  -121 120          IMP:n,p=1 $LaBr Casing: Alu
30 4 -3.667 -130            IMP:n,p=1 $NaI
c 31 7 -2.699  -131 130          IMP:n,p=1 $NaI Casing: Alu
50 5 -1.2E-6 110 120 130 190 191 -999   IMP:n,p=1 $air
90 8 -7.874  -190           IMP:n,p=1 $shield
91 8 -7.874  -191           IMP:n,p=1 $shield
99 0         999            IMP:n,p=0 $world

c --Begin Surfaces-- 
110 RCC 0 -15 -44 0 30 0 2.54 $SOIL CORE 
111 RCC 0 -15.2 -44 0 30.4 0 2.74 $SOIL CASING
120 RCC -32 0 -38   0 0 7.62 3.81 $LaBr cylinder
c 121 RCC -32 0 -38.2 0 0 8.02 4.01 $LaBr casing
130 RCC  32 0 -42   0 0 12.7 6.35 $NaI detector
c 131 RCC  32 0 -42.2 0 0 13.1 6.55 $NaI Casing 
190 RPP  -39 -19 -10 10 -24 -4  $Fe shielding LaBr
191 RPP  19  39  -10 10 -24 -4  $Fe shielding NaI 
999 SO 120  $sphere at origin radius 120 cm

c --Begin Options--
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
c m2 $brass (-8.07 g/cc)
c      26000 -0.000868
c      29000 -0.665381
c      30000 -0.325697
c      50000 -0.002672
c      82000 -0.005377
m3  $ Natural Soil Worldwide
        8016.70c  -0.4901223345347        $ O
       14028.70c  -0.330082388564186      $ Si
       13027.70c  -0.07101772602441570    $ Al
       26054.70c  -0.0400099864926286     $ Fe
        6000.60c  -0.0200049932463143     $ C
       19039.70c  -0.01400349527242       $ K
       11023.70c  -0.00500124831157857    $ Na
       20040.70c  -0.0150037449347357     $ Ca
       12024.70c  -0.00500124831157857    $ Mg
       22048.70c  -0.00500124831157857    $ Ti
        7014.80c  -0.00200049932463143    $ N
       15031.70c  -0.000800199729852571   $ P
       25055.70c  -0.00100024966231571    $ Mn
       56137.80c  -0.000500124831157857   $ Ba*
       23000.70c  -0.0000300074898694714  $ V
       38088.80c  -0.000250062415578929   $ Sr*
       30000.42c  -0.0000900224696084143  $ Zn
       29063.70c  -0.0000207561807427134  $ Cu
       29065.70c  -0.00000925130912675803
       28058.70c  -0.0000500124831157857  $ Ni
       34080.80c  -4.00099864926286E-07   $ Se*
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
c spherical neutron source radius 1 cm 
SDEF POS 0 0 0 rad=D1 ERG=14.05 par=n
si1      0 1
sp1    -21 2
c Tally Specification
c tally photon flux in detector 
F4:P 20 30 
E4 0 1E-5 0.05 493i 10
ptrac file=asc write=all event=col,bnk,src,sur max=2e6 type=p,n cell=20,30
c end file
