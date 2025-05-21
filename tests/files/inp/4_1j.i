Lattice/Rotation example of pwrlat
1 0 -1 -19 29 fill=1 imp:n=1
c 2 2 -1 -301 302 -303 304 lat=1 u=1 imp:n=1 fill=-3:3 -3:3 0:0
c     1 1 1 1 1 1 1 1 1 2 2 2 1 1 1 2 2 2 2 2 1 1 2 2 2 2 2 1
c     1 2 2 2 2 2 1 1 1 2 2 2 1 1 1 1 1 1 1 1 1
3 1 -18 -10 u=2 imp:n=1
4 2 -1 #3 #5 #6 #7 #8 #9 #10 #11 #12 #13 #14 #15 #16 #17 #18
    #19 #20 #21 #22 #23 #24 #25 #26 #27 #28 imp:n=1 u=2
c 5 like 3 but trcl=(-6 6 0)
c 6 like 3 but trcl=(-3 6 0)
c 7 like 3 but trcl=(0 6 0)
c 8 like 3 but trcl=(3 6 0)
c 9 like 3 but trcl=(6 6 0)
c 10 like 3 but trcl=(-6 3 0)
c 11 like 3 but trcl=(0 3 0)
c 12 like 3 but trcl=(6 3 0)
c 13 like 3 but trcl=(-6 0 0)
c 14 like 3 but trcl=(-3 0 0)
c 15 like 3 but trcl=(3 0 0)
c 16 like 3 but trcl=(6 0 0)
c 17 like 3 but trcl=(-6 -3 0)
c 18 like 3 but trcl=(0 -3 0)
c 19 like 3 but trcl=(6 -3 0)
c 20 like 3 but trcl=(-6 -6 0)
c 21 like 3 but trcl=(-3 -6 0)
c 22 like 3 but trcl=(0 -6 0)
c 23 like 3 but trcl=(3 -6 0)
c 24 like 3 but trcl=(6 -6 0)
c 25 like 3 but mat=3 rho=-9 trcl=(-3 3 0)
c 26 like 25 but trcl=(3 3 0)
c 27 like 25 but trcl=(-3 -3 0)
c 28 like 25 but trcl=(3 -3 0)
50 0 1:19:-29 imp:n=0

1 cz 60
10 cz 1.4
19 pz 60
29 pz -60
301 px 10
302 px -10
303 py 10
304 py -10

kcode 1000 1 5 10
ksrc 0 0 0
m1 92235 0.02 92238 0.98
m2 1001 2 8016 1
m3 48000 1