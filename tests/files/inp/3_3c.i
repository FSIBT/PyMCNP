C Cell Cards
10 1 -2.03 0 u=2 $ inferred geometry cell
11 1 -2.03 0 u=2 $ inferred geometry cell
12 1 -2.03 0 u=2 $ inferred geometry cell
13 1 -2.03 0 u=2 $ inferred geometry cell
14 1 -2.03 0 u=2 $ inferred geometry cell
15 1 -2.03 0 u=2 $ inferred geometry cell
21 0 0 u=2 $ inferred background cell
30 0 -99 fill=2 $ fill cell
40 0 99

C Surface Cards
99 sph 0. 0. 3. 10.

c Data Cards
m1 1001 -0.02 8016 -0.60 14000 -0.38
c
c embed2 meshgeo= abaqus
c        meeout= sample01.eeout
c        gmvfile= sample01.gmv
c        filetype= binary
c        background= 21
c        matcell= 1 10 2 11 3 12 4 13 5 14 6 15
c
embee4:n embed=2
embtb4 1 2 3 4 5 1e+39
embeb4 0.1 1.0 1e+10