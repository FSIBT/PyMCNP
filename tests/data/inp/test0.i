MCNP Test Model for MOAA
C cells
c
1 1 20
         -1000  $ dollar comment
     imp:n,p=1 trcl=5
     u=1
2 2 8
      -1005
     imp:n=1
     imp:p=0.5
     lat 1 
     fill= 0:1 0:1 0:0 1 0 1 5
3 3 -1
      1000 1005 -1010
     imp:n,p=1
99 0
      1010
     imp:n,p=0
     fill=1
5 0 
      #99
      imp:n,p=3
c foo end comment

C surfaces
1000 SO 1
1005 RCC 0 1.5 -0.5 0 0 1 0.25
1010 SO 3

C data
C materials
C UO2 5 atpt enriched
m1        92235           5 &
     92238          95
c testing comments
sc1 This is a high quality source comment
Fc5 Such a good tally comment.
C Iron
m2        26054        5.85
          26056       91.75
          26057       2.12
          26058       0.28
C water
m3        1001          2
           8016         1
MT3 lwtr
TR5 0.0 0.0 1.0 1 1 2 3 4 5 2 1 3 1
C execution
ksrc 0 0 0
mode n p
vol NO 2J 1 1.5 J
E0 1 10 100
