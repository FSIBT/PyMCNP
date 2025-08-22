"""
Example reading PTRAC files.

This example reads an PTRAC file using two methods: `__init__` and `from_mcnp`.
First, it reads the ptrac file from a path, and second, it reads an ptrac file
from the source string directly. Finally, it prints both results.
"""

import pathlib

import pymcnp

# Reading PTRAC using `from_file`.
path = pathlib.Path('example_02.ptrac')
ptrac = pymcnp.Ptrac.from_file(path)

print(f'Reading PTRAC from `{path}`:')
print(ptrac)

# Reading PTRAC using `from_mcnp`.
ptrac = pymcnp.Ptrac.from_mcnp("""   -1
mcnp    6                        05/08/13 07/14/25 11:39:04 
Sample Problem Input Deck                                                       
   1.4000E+01  1.0000E+00  1.0000E+02  0.0000E+00  0.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00  1.0000E+00  1.0000E+04
   0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00  0.0000E+00
     2    5    3    6    3    6    3    6    3    6    3    1    4    0    0    0    0    0    0    0
    1   2   7   8   9  17  18  20  21  22   7   8  10  11  17  18  20  21  22   7   8  12  13  17  18  20  21  22   7   8
   10  11  17  18  20  21  22   7   8  14  15  17  18  20  21  22
          1      1000
       3000         1        40         1         1
   0.00000E+00 -0.40000E+01 -0.25000E+01
       4000         2         7         0         3         3
   0.25424E+00 -0.37634E+01 -0.21403E+01
       4000         2      6000        51         3         3
   0.14362E+01 -0.26632E+01 -0.46819E+00
       4000         2      6000         2         3         3
   0.13310E+01 -0.10442E+01  0.70227E-02
       3000         2      6000         2         3         3
   0.34660E+01 -0.27738E+01  0.17002E+00
       5000         3         5        55         4         0
   0.50000E+01 -0.45169E+01  0.15231E+01
       9000         3         1         1         4         0
   0.50000E+01 -0.45169E+01  0.15231E+01
       9000         1        40         1         1
   0.00000E+00 -0.40000E+01 -0.25000E+01
""")

print('Reading PTRAC file from string:')
print(ptrac)
