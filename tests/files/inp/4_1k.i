Generate a LNK3DNT rzt mesh w/ multiple materials
c upper-inner
1 1 -18.7 -11 1 2 3 imp:n=1
2 2 -0.001 -11 1 -2 3 imp:n=1
3 1 -18.7 -11 -1 -2 3 imp:n=1
4 2 -0.001 -11 -1 2 3 imp:n=1
c upper-outer
6 2 -0.001 -10 11 1 2 3 imp:n=1
7 1 -18.7 -10 11 1 -2 3 imp:n=1
8 2 -0.001 -10 11 -1 -2 3 imp:n=1
9 1 -18.7 -10 11 -1 2 3 imp:n=1
c lower-inner
11 2 -0.001 -11 1 2 -3 imp:n=1
12 1 -18.7 -11 1 -2 -3 imp:n=1
13 2 -0.001 -11 -1 -2 -3 imp:n=1
14 1 -18.7 -11 -1 2 -3 imp:n=1
c lower-outer
16 1 -18.7 -10 11 1 2 -3 imp:n=1
17 2 -0.001 -10 11 1 -2 -3 imp:n=1
18 1 -18.7 -10 11 -1 -2 -3 imp:n=1
19 2 -0.001 -10 11 -1 2 -3 imp:n=1
c
c outer void
20 0 10 imp:n=0

10 rcc 0. 0. -10. 0. 0. 20. 10. $ outer rcc
11 rcc 0 0 -10 0 0 20 5 $ inner rcc
1 py 0.0
2 px 0.0
3 pz 0.0

kcode 5000 1.0 50 250
ksrc 0.0 0.0 0.0
m1 92235.69c 1.0
m2 6012 1.0
c dm1 92235 92235.50
c mesh geom cyl
c     ref 0.0 0.0 0.0
c     origin 0.0 0.0 -10.0 $ bottom center of cylinder
c     axs 0.0 0.0 1.0
c     vec 1.0 0.0 0.0
c     imesh 10 $ cylinder radius
c     iints 2 $ 2 radial divisions
c     jmesh 20 $ axial (z) length
c     jints 2 $ 2 axial divisions
c     kmesh 1 $ azimuth-single rotation (0-2pi)
c     kints 4 $ 4 azimuthal divisions (0, pi/2, pi, 3pi/2, 2pi)
c dawwg xsec=ndilib points=10