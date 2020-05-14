Basalt and Poly 1 with Litho Scanner Using Richard's VR Techniques
c
c  Simulation of a measurement of the composition of the 
c  GNT facility basalt monument with a polyethylene layer using the 
c  Schlumberger Litho Scanner tool with its 2.5” x 3” LaBr3 detector.
c  Set up by Ann Parsons originally on August 4, 2016.
c
c  The origin of the coordinate system is centered on the basalt 
c  monument with z=0 at the top surface. The basalt monument is a 
c  182 cm x 182 cm x 91 cm rectangular paralellpiped (RPP). The 
c  HD polyethylene layer is directly on top of the basalt monument and 
c  is also a RPP with thickness t.
c
c  The Litho Scanner tool is mounted over the top of the monument at height
c  D between the bottom of the tool and the top of the polyethylene, 
c  oriented diagonally (at 45 degrees) in the XY plane. 
c  For now, consider it as a point neutron source.
c
c  The LaBr3 detector is a right circular cylinder (RCC) mounted inside the 
c  Litho Scanner tool so that it is aligned along the tool axis with the 
c  top face a distance l from the PNG target. As with the Litho Scanner 
c  tool, the detector is rotated 45 degrees in the XY plane.  The detector 
c  has radius R and height h so that the back face is (l+h) from the origin 
c  in the XY plane. The definition of the RCC surface for the detector is
c  # RCC Vx Vy Vz Hz Hy Hz R where # is the surface number, Vx = -0.7071*(l+h),
c  Vy = -0.7071*(l+h) Vz = t+D+Rh, Hx = = 0.7071*h, Hy = = 0.7071*h and
c  Hz = t+D+Rh and R is the radius of the detector.
c 
c
c  The basalt composition is taken from the Columbia River basalt 
c  composition used in Julia Bodnarik’s and Suzanne Nowicki’s GGAO 
c  simulations - specifically from the file bas3.txt.
c
c
c ---------------------------------------------------------------
c CELL DESCRIPTIONS
c --------------------------------------------------------------
100    100   -2.69   -10            $ basalt monument
150	   150   -0.93   -15            $ poly layer
200    200   -5.06   -20            $ LaBr3 detector
300    300   -1.2E-3  10 15 20 -99      $ air
400    0              99                $ void

c --------------------------------------------------------------
c SURFACE DESCRIPTIONS
c --------------------------------------------------------------
10  RPP -91.0 +91.0 -91.0 +91.0 -91.0 0.0       $ basalt monument
15  RPP -90.9 +90.9 -90.9 +90.9 0.0 2.54        $ poly layer
20  RCC -33.67 -33.67 18.42 5.39 5.39 0 3.18    $ LaBr3 detector
99  RCC 0 0 -100 0 0 200 150        		$ universe boundary

c --------------------------------------------------------------
c DATA SECTION
c --------------------------------------------------------------
c
c 
c ----- Physics Modes -----
MPHYS
MODE N P  $ photon and neutron transport
PHYS:N  $ neutron physics - use defaults
PHYS:P  $ photon physics - use defaults
c
c
c --- Material Cards
c
c Columbia River Basalt (2.69 g/cc)
m100   8016.70c   -45.97   $O 
      14028.70c   -22.05   $Si-28 
      14029.70c   -1.12    $Si-29 
      14030.70c   -0.74    $Si-30    
      13027.62c   -7.99    $Al 
      19000.62c   -1.27    $K
      11023.70c   -2.68    $Na 
      26054.70c   -0.44    $Fe-54 
      26056.70c   -6.94    $Fe-56 
      26057.70c   -0.17    $Fe-57 
      26058.70c   -0.02    $Fe-58 
      20000.62c   -5.24    $Ca 
      12000.62c   -3.99    $Mg 
      22000.62c   -1.12    $Ti 
      15031.70c   -0.24    $P 
      1001.70c    -0.05    $H
      25055.70c   -0.13    $Mn 
      37085.70c   -1e-003  $Rb 
      6000.70c    -0.04    $C
      56138.70c   -0.0484  $Ba 
      17035.70c   -0.02    $Cl 
      40090.70c   -0.0201  $Zr 
      58000.70c   -7.0e-003 $Ce
      7014.70c    -0.01      $N 
      30000.70c   -0.1       $Zn
      38088.70c   -0.0753    $Sr
      16000.62c   -0.01         $S
      5000.70c    -0.50E-004    $B 
      21045.70c   -27.0E-004    $Sc 
      4009.70c    -2.00E-004   $Be 
      23000.70c   -271E-004    $V 
      24000.70c   -310E-004    $Cr
      27059.70c   -39.0E-004    $Co 
      28000.70c   -180E-004    $Ni
      29000.70c   -70.0E-004    $Cu 
      31000.70c   -21.0E-004    $Ga 
      32000.70c   -1.20E-004    $Ge
      33000.70c   -5.0E-004     $As 
      37000.70c   -12.00E-004   $Rb
      38000.70c   -753.0E-004   $Sr 
      39089.70c   -26.0E-004    $Y 
      41093.70c   -24.90E-004   $Nb 
      42000.70c   -2.0E-004     $Mo 
      47000.70c   -0.5E-004     $Ag 
      49000.70c   -0.1E-004     $In 
      50000.70c   -2.00E-004    $Sn
      51000.70c   -0.4E-004     $Sb
      55133.70c   -0.1E-004     $Cs 
      57000.70c   -32.6E-004    $La
      59000.70c   -9.12E-004    $Pr
      60000.70c   -37.2E-004    $Nd 
      62000.70c   -7.42E-004    $Sm 
      63000.70c   -2.23E-004    $Eu 
      64000.70c   -5.90E-004    $Gd
      65000.70c   -0.85E-004    $Tb
      66000.70c   -4.94E-004    $Dy
      67165.70c   -0.93E-004    $Ho 
      68000.70c   -2.65E-004    $Er
      69000.70c   -0.373E-004   $Tm
      70000.70c   -2.35E-004    $Yb
      71000.70c   -0.351E-004   $Lu  
      72000.70c   -4.50e-004    $Hf 
      73181.70c   -1.34e-004    $Ta
      74000.70c   -0.5e-004     $W  
      81000.70c   -0.05e-004    $Tl 
      82000.70c   -7.0e-004     $Pb 
      83209.70c   -0.1e-004     $Bi 
      90232.70c   -4.07e-004    $Th 
      92238.70c   -0.53e-004    $U 
c
c Polyethylene   CH2 (H:2., C:1.) (0.93 g/cc)
m150   1001.70c 0.666590
       1002.70c 0.000077
       6000.70c 0.333333
c mt150 poly.60t
c
c LaBr3 Detector material (5.06 g/cc)
m200   35079.70c  0.375208        $ Br (74.026%)
       35081.70c  0.365052 
       57138.70c  0.000222        $ La (24.675%)
       57139.70c  0.246531 
       58136.70c  0.000024        $ Ce (1.299%)
       58138.70c  0.000033 
       58140.70c  0.011487 
       58142.70c  0.001443 
c
c Air (US S. Atm at sea level, N, O and Ar), rho = -0.001225 g/cc
m300  7014.70c      -0.755636  $ Air
      8016.70c      -0.231475 18000.59      -0.012889
c
c
c
c ----- Neutron Source Definition -----
c
SDEF  PAR=N              $ generate neutrons
      POS =  0.0 0.0 +13.27
      ERG = D1
      TME=D11<D12
SP1   -4 0.006 14
SI11  0  8E2  30E2
SP11  0  1    0
SI12  0  300E2  
SP12  0  1
c
c
c ----- Tally Definitions -----
c
c 
F11:P  20.1 20.2 20.3      $ check this
C11 -0.9 -0.8 -0.7 -0.6 -0.5 -0.4 -0.3 -0.2 -0.1 0.0  0.1 0.2 0.3 
        0.4 0.5 0.6 0.7 0.8 0.9 1.0                                                                                                                                                                                                                                 
E11 1.636E-2 508i 10.40
T11 8E2 30E2 38E2 60E2 68E2 90E2 98E2
        120E2 128E2 150E2 158E2 180E2 188E2 
        210E2 218E2 240E2 248E2 270E2 278E2 300E2
FT11 TAG 4
FU11 00000.00102 1E10
c 
c ----- Variance Reduction Code -----
c Crude tally of photon flux in the crystal
c
FC4  Simple photon flux target for WW generation
F4:p 200
E4  .1 98i 10  20  $ unrealistically coarse 100-keV energy bins
T4  10e2 20e2 1e7  $ invented time gates
FQ4   E T          $ tabular display
TF4   7j 3   $ WW optimized for TFC bin:  latest time gate
c
c --------  WW Usage/Gen for spectroscopy  ------------
imp:n,p  1 1 8 1 0
c
dxt:p -30.975 -30.975 18.42 5.0 7.5
c wwp:X WUPN WSURVN MXSPLN MWHERE SWITCHN
c   ... where SWITCHN: neg=wwimp, 0=wwn card, pos=inverse imp.
c wwg: tallyNumber  cell 0->mesh
c
wwp:n 5 3 5 0 -1
wwp:p 5 3 5 0 -1
c
wwg   4 0       $ optimize for crystal flux
c
c
c Crude cylindrical mesh:
c
c ref set to the src point, origin set to bottom center, just outside the universe
c
MESH   GEOM=cyl  REF= 0.0 0.0 +13.27  ORIGIN=1e-6 1e-6 -100.1
       AXS= 0 0 1  VEC= 1 0 0   $ theta measured from X  axis
       IMESH= 30.0  50.0  200.1    IINTS=5 10 1
       JMESH= 30.0  50.0  200.1    JINTS=5 10 1
       KMESH= 1                    KINTS=4
PRDMP 2j 1
c 
c ----- Number of Particles -----
NPS 1E7