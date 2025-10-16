# "Read" Examples

PyMCNP provides endpoints to read MCNP files.

## Reading INP

```{eval-rst}
.. note:: 
   This example requires `example_00.inp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_00.inp>`_.
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
    ...

## Reading INP Cell

```{eval-rst}
.. note:: 
   This example requires `example_00.inp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_00.inp>`_.
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
   This example requires `example_00.inp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_00.inp>`_.
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
          -0.000066 022047 -0.00005952 022048 -0.00058976 022049 -0.00004328 022050 &
          -0.00004144

## Reading INP Surface

```{eval-rst}
.. note:: 
   This example requires `example_00.inp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_00.inp>`_.
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
   This example requires `example_00.outp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_00.outp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_outp.py
   :language: python
```

Output:

    Reading OUTP from `PyMCNP/files/outp/example_00.outp`:
              Code Name & Version = MCNP_6.20, 6.2.0
      
         _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/ 
        _/_/  _/_/      _/             _/_/    _/       _/    _/     _/        
       _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/     
      _/      _/      _/             _/    _/_/       _/           _/    _/    
     _/      _/        _/_/_/       _/      _/       _/             _/_/       
     ... 

## Reading OUTP Tally 1

```{eval-rst}
.. note:: 
   This example requires `example_00.outp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_00.outp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_tally1.py
   :language: python
```

Output:

    Reading tally #1 cell #2.1 from `PyMCNP/files/outp/example_00.outp`:
             bins    counts  ...  particles      nps
    0     0.10000  0.000010  ...    photons  1000000
    1     0.11934  0.000003  ...    photons  1000000
    2     0.13867  0.000005  ...    photons  1000000
    3     0.15801  0.000002  ...    photons  1000000
    4     0.17734  0.000002  ...    photons  1000000
    ..        ...       ...  ...        ...      ...
    508   9.92270  0.000000  ...    photons  1000000
    509   9.94200  0.000000  ...    photons  1000000
    510   9.96130  0.000000  ...    photons  1000000
    511   9.98070  0.000000  ...    photons  1000000
    512  10.00000  0.000000  ...    photons  1000000
    
    [513 rows x 10 columns]

## Reading OUTP Tally 2

```{eval-rst}
.. note:: 
   This example requires `example_03.outp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_03.outp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_tally2.py
   :language: python
```

Output:

    Reading tally #2 cell #8 from `PyMCNP/files/outp/example_03.outp`:
              bins    counts  ...  particles     nps
    0          0.0  0.000000  ...   neutrons  100000
    1        100.0  0.000078  ...   neutrons  100000
    2        200.0  0.000085  ...   neutrons  100000
    3        300.0  0.000080  ...   neutrons  100000
    4        400.0  0.000085  ...   neutrons  100000
    ...        ...       ...  ...        ...     ...
    4496  449600.0  0.000000  ...   neutrons  100000
    4497  449700.0  0.000000  ...   neutrons  100000
    4498  449800.0  0.000000  ...   neutrons  100000
    4499  449900.0  0.000000  ...   neutrons  100000
    4500  450000.0  0.000000  ...   neutrons  100000
    
    [4501 rows x 8 columns]

## Reading OUTP Tally 4

```{eval-rst}
.. note:: 
   This example requires `example_02.outp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_02.outp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_tally4.py
   :language: python
```

Output:

    Reading tally #14 cell #12 from `PyMCNP/files/outp/example_02.outp`:
              bins        counts  ...  particles         nps
    0      0.10000  3.622140e-07  ...    photons  1000000000
    1      0.10989  6.949680e-08  ...    photons  1000000000
    2      0.11978  6.931230e-08  ...    photons  1000000000
    3      0.12967  6.818310e-08  ...    photons  1000000000
    4      0.13956  6.641000e-08  ...    photons  1000000000
    ...        ...           ...  ...        ...         ...
    997    9.96040  2.980820e-10  ...    photons  1000000000
    998    9.97030  2.593030e-10  ...    photons  1000000000
    999    9.98020  2.353170e-10  ...    photons  1000000000
    1000   9.99010  2.747060e-10  ...    photons  1000000000
    1001  10.00000  2.536390e-10  ...    photons  1000000000
    
    [1002 rows x 8 columns]

## Reading OUTP Tally 8

```{eval-rst}
.. note:: 
   This example requires `example_01.outp <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_01.outp>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_tally8.py
   :language: python
```

Output:

    Reading tally #18 cell #200 from `PyMCNP/files/outp/example_01.outp`:
             bins    counts  ...  particles       nps
    0     0.10000  0.000109  ...    photons  10000000
    1     0.11934  0.000008  ...    photons  10000000
    2     0.13867  0.000008  ...    photons  10000000
    3     0.15801  0.000007  ...    photons  10000000
    4     0.17734  0.000006  ...    photons  10000000
    ..        ...       ...  ...        ...       ...
    508   9.92270  0.000000  ...    photons  10000000
    509   9.94200  0.000000  ...    photons  10000000
    510   9.96130  0.000000  ...    photons  10000000
    511   9.98070  0.000000  ...    photons  10000000
    512  10.00000  0.000000  ...    photons  10000000
    
    [513 rows x 8 columns]

## Reading PTRAC

```{eval-rst}
.. note:: 
   This example requires `example_02.ptrac <https://github.com/FSIBT/PyMCNP/blob/master/examples/example_02.ptrac>`_.
```

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/read_ptrac.py
   :language: python
```

Output:

    Reading PTRAC from `PyMCNP/files/ptrac/example_02.ptrac`:
       -1
    mcnp    6                        05/08/13 07/14/25 11:39:04 
    Detector response single carbon block                                           
       1.4000E+01  1.0000E+00  1.0000E+02  0.0000E+00  0.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00  1.0000E+00  1.0000E+04
       0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00  0.0000E+00
         2    6    3    7    3    7    3    7    3    7    3    0    4    0    0    0    0    0    0    0
        1   2   7   8   9  16  17  18  20  21  22   7   8  10  11  16  17  18  20  21  22   7   8  12  13  16  17  18  20  21
       22   7   8  10  11  16  17  18  20  21  22   7   8  14  15  16  17  18  20  21  22
              1      1000
    ...
           9000         1        40         1        77         1
       0.00000E+00  0.00000E+00  0.00000E+00
    
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
           9000         1        40         1         1
       0.00000E+00 -0.40000E+01 -0.25000E+01

