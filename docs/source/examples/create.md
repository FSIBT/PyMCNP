# "Create" Examples

PyMCNP supports INP files and cards creation.

## Creating Cell Cards

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_cell.py
   :language: python
```

Output:

    INP cell created using `__init__`:
    2 1 0.5 #(99:3) imp:n=1.0

## Creating Material Cards

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_material.py
   :language: python
```

Output:

    INP material created using `__init__`:
    M1 001001 0.1118855432927602 008016 0.8859435015301171
    INP material created using `from_formula`:
    M1 001001 0.66659 008016 0.3325233333333333

## Creating Surface Cards

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_surface.py
   :language: python
```

Output:

    INP surface created using `__init__`:
    1 SO 2

## Creating INP Files

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_inp.py
   :language: python
```

Output:

    INP file created using `__init__`:
    Create `Inp`
    1 0 -21 IMP:n 1
    2 32 -11.34 +21 -22 IMP:n 1
    3 31 -0.001205 +22 -99 IMP:n 1
    4 0 +99 IMP:n 0

    21 RPP -10 10 -10 10 -10 10
    22 RPP -50 50 -50 50 -50 50
    99 SO 100

    M31 007014 -0.797088 008016 -0.199514
    M32 082204 -0.014 082206 -0.241 082207 -0.221 082208 -0.524
    SDEF POS=0 0 0 ERG=14.4 PAR=1
    F4:n 2
    NPS 100000
    RAND SEED 1232209489
