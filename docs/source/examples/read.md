# "Read" Examples

PyMCNP reads MCNP input (INP), output (OUTP), and particle track (PTRAC) files. The example files are in the
[examples directory](https://github.com/FSIBT/PyMCNP/tree/main/examples) of the repository; they are not installed
with the package, so download them or clone the repository. Run the scripts from that directory.

## Reading INP

```{eval-rst}
.. note:: 
   This example requires `example_00.inp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_00.inp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_inp.py
   :language: python
```

Output:

    Reading INP from `example_00.inp`:
    Isotropic neutron source over lunar regolith with two gamma detectors
    c
    c cell cards
    c
    100 100 -1.54 -1 imp:P,N 1
    200 300 -5.06 -2 imp:P,N 1
    201 200 -5.1 -3 imp:P,N 1
    777 900 -0.000001 1 2 3 -99 imp:P,N 1
    999 0  99 imp:P,N 0

    c
    c surface cards
    c
    1  rpp -300 300 -300 300 -150 -50
    2  rcc 50 0 0 0 0 7.62 3.81
    3  rcc -50 0 0 0 0 5.08 2.54
    99  so 600

    c
    c material cards
    c
    c Lunar Highlands:
    m100 013027 -0.1701 020040 -0.131742819 020042 -0.000879273 020044 &
          -0.002834874 026054 -0.00086506 026056 -0.013579592 026057 -0.000313612 &
          008016 -0.45489192 019039 -0.0001865162 019041 -0.0000134604 012024 &
          -0.00402849 012025 -0.00051 012026 -0.00056151 011023 -0.0045 014028 &
          -0.190532718 014029 -0.00967921 014030 -0.006388072 090232 -0.006 022046 &
          -0.000066 022047 -0.00005952 022048 -0.00058976 022049 -0.00004328 &
          022050 -0.00004144
    c CeBr3:
    m200 035079 -0.3199072536 035081 -0.3111980011 058140 -0.3262874023 058142 &
          -0.040998962
    c LaBr3:
    m300 035079 -0.3209300771 035081 -0.3121929789 057139 -0.3665511205
    c Air:
    m900 008016 -0.2094897 007014 -0.7771608 018040 -0.00996035
    c
    c
    c source cards
    c
    mode n p
    nps 1000000
    rand seed 71129329235055
    c source definition
    sdef par n erg 14.05
    c tally information
    c
    f1:p 2.1 2.2 2.3
    *c1 90 0
    e1 0.1 0.1193359375 0.138671875 0.1580078125 0.17734375000000002 0.1966796875 &
         0.21601562500000002 0.2353515625 0.2546875 0.2740234375 0.293359375 &
         0.31269531250000004 0.33203125 0.35136718750000007 0.370703125 &
         ... (512 energies in all)
    f21:p 3.1 3.2
    *c21 90 0
    e21 0.1 0.1193359375 0.138671875 0.1580078125 0.17734375000000002 0.1966796875 &
         0.21601562500000002 0.2353515625 0.2546875 0.2740234375 0.293359375 &
         0.31269531250000004 0.33203125 0.35136718750000007 0.370703125 &
         ... (512 energies in all)
    c
    c end of file


    Reading INP file from string:
    Create `Inp`
    1 0  -12 imp:n=1
    2 23 0.5 +12:-13 imp:n=1
    3 21 0.5 -12 +13:-14 imp:n=1
    4 0  +14 imp:n=1

    12  rpp -5 5 -5 5 -5 5
    13  rpp -1 1 -1 1 -1 1
    14  so 60

    m21 007014 -0.797088 008016 -0.199514
    m23 082204 -0.014 082206 -0.241 082207 -0.221 082208 -0.524

Printing an `Inp` writes it as MCNP input. The `511i` shorthand of `e1` and `e21` is written as 512 explicit energies,
wrapped with `&` to fit in 80 columns (shortened above).

## Reading INP Cell

```{eval-rst}
.. note:: 
   This example requires `example_00.inp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_00.inp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_cell.py
   :language: python
```

Output:

    Reading cell from `example_00.inp`:
    100 100 -1.54 -1 imp:P,N 1

## Reading INP Material

```{eval-rst}
.. note:: 
   This example requires `example_00.inp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_00.inp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_material.py
   :language: python
```

Output:

    Reading material from `example_00.inp`:
    m100 013027 -0.1701 020040 -0.131742819 020042 -0.000879273 020044 &
          -0.002834874 026054 -0.00086506 026056 -0.013579592 026057 -0.000313612 &
          008016 -0.45489192 019039 -0.0001865162 019041 -0.0000134604 012024 &
          -0.00402849 012025 -0.00051 012026 -0.00056151 011023 -0.0045 014028 &
          -0.190532718 014029 -0.00967921 014030 -0.006388072 090232 -0.006 022046 &
          -0.000066 022047 -0.00005952 022048 -0.00058976 022049 -0.00004328 &
          022050 -0.00004144

## Reading INP Surface

```{eval-rst}
.. note:: 
   This example requires `example_00.inp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_00.inp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_surface.py
   :language: python
```

Output:

    Reading surface from `example_00.inp`:
    2  rcc 50 0 0 0 0 7.62 3.81

## Reading OUTP

```{eval-rst}
.. note:: 
   This example requires `example_00.outp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_00.outp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_outp.py
   :language: python
```

Output:

    Reading OUTP from `example_00.outp`:
              Code Name & Version = MCNP_6.20, 6.2.0

         _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/ 
        _/_/  _/_/      _/             _/_/    _/       _/    _/     _/        
       _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/     
      _/      _/      _/             _/    _/_/       _/           _/    _/    
     _/      _/        _/_/_/       _/      _/       _/             _/_/       

      +-----------------------------------------------------------------------+
      | Copyright (2018).  Los Alamos National Security, LLC.  All rights     !
      | reserved.                                                             !
      |  This material was produced under U.S. Government contract            !
      | DE-AC52-06NA25396 for Los Alamos National Laboratory, which is        !
      | operated by Los Alamos National Security, LLC for the U.S.            !
      | Department of Energy. The Government is granted for itself and        !
      | others acting on its behalf a paid-up, nonexclusive, irrevocable      !
      | worldwide license in this material to reproduce, prepare derivative   !
      | works, and perform publicly and display publicly. Beginning five (5)  !
      | years after February 14, 2018, subject to additional five-year        !
      | worldwide renewals, the Government is granted for itself and others   !
      | acting on its behalf a paid-up, nonexclusive, irrevocable worldwide   !
      | license in this material to reproduce, prepare derivative works,      !
      | distribute copies to the public, perform publicly and display         !
      | publicly, and to permit others to do so. NEITHER THE UNITED STATES    !
      | NOR THE UNITED STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL   !
      | SECURITY, LLC, NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY,        !
      | EXPRESS OR IMPLIED, OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY  !
      | FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS OF ANY INFORMATION,     !
      | APPARATUS, PRODUCT, OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE  !
      | WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS.                            !
      +-----------------------------------------------------------------------+

    1mcnp     version 6     ld=02/20/18                     10/21/24 12:25:31 

    ...

    Reading OUTP file from string:
              Code Name & Version = MCNP_6.20, 6.2.0

         _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/ 
        _/_/  _/_/      _/             _/_/    _/       _/    _/     _/        
       _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/     
      _/      _/      _/             _/    _/_/       _/           _/    _/    
     _/      _/        _/_/_/       _/      _/       _/             _/_/       

      +-----------------------------------------------------------------------+
      | Copyright (2018).  Los Alamos National Security, LLC.  All rights     !
      | reserved.                                                             !
      |  This material was produced under U.S. Government contract            !
      | DE-AC52-06NA25396 for Los Alamos National Laboratory, which is        !
      | operated by Los Alamos National Security, LLC for the U.S.            !
      | Department of Energy. The Government is granted for itself and        !
      | others acting on its behalf a paid-up, nonexclusive, irrevocable      !
      | worldwide license in this material to reproduce, prepare derivative   !
      | works, and perform publicly and display publicly. Beginning five (5)  !
      | years after February 14, 2018, subject to additional five-year        !
      | worldwide renewals, the Government is granted for itself and others   !
      | acting on its behalf a paid-up, nonexclusive, irrevocable worldwide   !
      | license in this material to reproduce, prepare derivative works,      !
      | distribute copies to the public, perform publicly and display         !
      | publicly, and to permit others to do so. NEITHER THE UNITED STATES    !
      | NOR THE UNITED STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL   !
      | SECURITY, LLC, NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY,        !
      | EXPRESS OR IMPLIED, OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY  !
      | FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS OF ANY INFORMATION,     !
      | APPARATUS, PRODUCT, OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE  !
      | WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS.                            !
      +-----------------------------------------------------------------------+

    1mcnp     version 6     ld=02/20/18                     06/17/25 16:52:59 
     *************************************************************************                 probid =  06/17/25 16:52:59 
     i=valid_3_3g.i


     bad trouble in subroutine oldcd1 of imcn                             

     too many entries on fill card.

## Reading OUTP Tally 1

```{eval-rst}
.. note:: 
   This example requires `example_00.outp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_00.outp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_tally1.py
   :language: python
```

Output:

    Reading tally #1 surface #2 from `example_00.outp`:
             bins    counts  errors  angle_from  angle_to  surface  facet  number                                 quantity particles      nps
    0     0.10000  0.000010  0.3177       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    1     0.11934  0.000003  0.5773       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    2     0.13867  0.000005  0.4472       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    3     0.15801  0.000002  0.7071       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    4     0.17734  0.000002  0.7072       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    ..        ...       ...     ...         ...       ...      ...    ...     ...                                      ...       ...      ...
    508   9.92270  0.000000  0.0000       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    509   9.94200  0.000000  0.0000       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    510   9.96130  0.000000  0.0000       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    511   9.98070  0.000000  0.0000       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000
    512  10.00000  0.000000  0.0000       180.0      90.0        2      1       1  number of particles crossing a surface.   photons  1000000

    [513 rows x 11 columns]

## Reading OUTP Tally 2

```{eval-rst}
.. note:: 
   This example requires `example_03.outp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_03.outp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_tally2.py
   :language: python
```

Output:

    Reading tally #2 surface #8 from `example_03.outp`:
              bins    counts  errors  surface  facet  number                                quantity particles     nps
    0          0.0  0.000000  0.0000        8      0       2  particle flux averaged over a surface.  neutrons  100000
    1        100.0  0.000078  0.1010        8      0       2  particle flux averaged over a surface.  neutrons  100000
    2        200.0  0.000085  0.0966        8      0       2  particle flux averaged over a surface.  neutrons  100000
    3        300.0  0.000080  0.0999        8      0       2  particle flux averaged over a surface.  neutrons  100000
    4        400.0  0.000085  0.0966        8      0       2  particle flux averaged over a surface.  neutrons  100000
    ...        ...       ...     ...      ...    ...     ...                                     ...       ...     ...
    4496  449600.0  0.000000  0.0000        8      0       2  particle flux averaged over a surface.  neutrons  100000
    4497  449700.0  0.000000  0.0000        8      0       2  particle flux averaged over a surface.  neutrons  100000
    4498  449800.0  0.000000  0.0000        8      0       2  particle flux averaged over a surface.  neutrons  100000
    4499  449900.0  0.000000  0.0000        8      0       2  particle flux averaged over a surface.  neutrons  100000
    4500  450000.0  0.000000  0.0000        8      0       2  particle flux averaged over a surface.  neutrons  100000

    [4501 rows x 9 columns]

## Reading OUTP Tally 4

```{eval-rst}
.. note:: 
   This example requires `example_02.outp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_02.outp>`_.
   ``example_02.outp`` also holds tallies 4 and 5 in a layout PyMCNP cannot parse yet, so ``Outp.from_file`` issues a
   ``pymcnp.abc.Warning`` ("Tally not parsed.") for each of them; tally 14 is parsed.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_tally4.py
   :language: python
```

Output:

    Reading tally #14 cell #12 from `example_02.outp`:
              bins        counts  errors  cell  number                                 quantity particles         nps
    0      0.10000  3.622140e-07  0.0025    12      14  track length estimate of particle flux.   photons  1000000000
    1      0.10989  6.949680e-08  0.0045    12      14  track length estimate of particle flux.   photons  1000000000
    2      0.11978  6.931230e-08  0.0045    12      14  track length estimate of particle flux.   photons  1000000000
    3      0.12967  6.818310e-08  0.0045    12      14  track length estimate of particle flux.   photons  1000000000
    4      0.13956  6.641000e-08  0.0046    12      14  track length estimate of particle flux.   photons  1000000000
    ...        ...           ...     ...   ...     ...                                      ...       ...         ...
    997    9.96040  2.980820e-10  0.0862    12      14  track length estimate of particle flux.   photons  1000000000
    998    9.97030  2.593030e-10  0.0989    12      14  track length estimate of particle flux.   photons  1000000000
    999    9.98020  2.353170e-10  0.1060    12      14  track length estimate of particle flux.   photons  1000000000
    1000   9.99010  2.747060e-10  0.1015    12      14  track length estimate of particle flux.   photons  1000000000
    1001  10.00000  2.536390e-10  0.1054    12      14  track length estimate of particle flux.   photons  1000000000

    [1002 rows x 8 columns]

## Reading OUTP Tally 8

```{eval-rst}
.. note:: 
   This example requires `example_01.outp <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_01.outp>`_.
   ``example_01.outp`` also holds tally 8 in a layout PyMCNP cannot parse yet, so ``Outp.from_file``
   issues a ``pymcnp.abc.Warning`` ("Tally not parsed.") for it; tally 18 is parsed.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_tally8.py
   :language: python
```

Output:

    Reading tally #18 cell #200 from `example_01.outp`:
             bins    counts  errors  cell  number                    quantity particles       nps
    0     0.10000  0.000109  0.0303   200      18  pulse height distribution.   photons  10000000
    1     0.11934  0.000008  0.1098   200      18  pulse height distribution.   photons  10000000
    2     0.13867  0.000008  0.1132   200      18  pulse height distribution.   photons  10000000
    3     0.15801  0.000007  0.1204   200      18  pulse height distribution.   photons  10000000
    4     0.17734  0.000006  0.1270   200      18  pulse height distribution.   photons  10000000
    ..        ...       ...     ...   ...     ...                         ...       ...       ...
    508   9.92270  0.000000  0.0000   200      18  pulse height distribution.   photons  10000000
    509   9.94200  0.000000  0.0000   200      18  pulse height distribution.   photons  10000000
    510   9.96130  0.000000  0.0000   200      18  pulse height distribution.   photons  10000000
    511   9.98070  0.000000  0.0000   200      18  pulse height distribution.   photons  10000000
    512  10.00000  0.000000  0.0000   200      18  pulse height distribution.   photons  10000000

    [513 rows x 8 columns]

## Reading PTRAC

```{eval-rst}
.. note:: 
   This example requires `example_00.ptrac <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_00.ptrac>`_ and
   `example_02.ptrac <https://github.com/FSIBT/PyMCNP/blob/main/examples/example_02.ptrac>`_. ``example_00.ptrac`` holds
   only the PTRAC header and no histories, which is why the first part prints only the header; ``example_02.ptrac`` has
   histories.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_ptrac.py
   :language: python
```

Output:

    Reading PTRAC from `example_00.ptrac`:
       -1
    mcnp    6                        05/08/13 07/14/25 11:39:04 
    Isotropic neutron source over lunar regolith with two gamma detectors           
       1.4000E+01  1.0000E+00  1.0000E+02  0.0000E+00  0.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00  1.0000E+00  1.0000E+04
       0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00  0.0000E+00
         2    6    3    7    3    7    3    7    3    7    3    0    4    0    0    0    0    0    0    0
        1   2   7   8   9  16  17  18  20  21  22   7   8  10  11  16  17  18  20  21  22   7   8  12  13  16  17  18  20  21
       22   7   8  10  11  16  17  18  20  21  22   7   8  14  15  16  17  18  20  21  22

    Reading PTRAC from `example_02.ptrac`, event by event:
    1 SOURCE None 1 (0.0, 0.0, 0.0)
    1 SURFACE 1 99 (101.7, 94.656, 143.87)
    1 TERMINAL 1 99 (101.7, 94.656, 143.87)
    2 SOURCE None 1 (0.0, 0.0, 0.0)
    2 SURFACE 1 99 (179.04, -88.936, -5.8889)
    Reading PTRAC file from string:
       -1
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
