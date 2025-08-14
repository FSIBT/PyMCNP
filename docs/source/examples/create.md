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
	1 1 0.5 #(99:3) imp:n 1.0

## Creating Material Cards

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_material.py
   :language: python
```

Output:

	m1 001001 0.1118855432927602 008016 0.8859435015301171
	m1 001001 0.1118855432927602 008016 0.8859435015301171

## Creating Surface Cards

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_surface.py
   :language: python
```

Output:

	INP surface created using `__init__`:
	1  so 2

## Creating INP Files

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_inp.py
   :language: python
```

Output:

	INP file created using `__init__`:
	Create `Inp`
	
	1 0  -1 
	1 1 0.5 +1:-1 
	1 1 0.5 -1 +1:-1 
	1 0  +1 
	
	1  rpp -50 50 -50 50 -50 50
	1  rpp -10 10 -10 10 -10 10
	1  so 100
	
	m1 007014 -0.797088 008016 -0.199514
	m1 082204 -0.014 082206 -0.241 082207 -0.221 082208 -0.524
	sdef pos 0 0 0 erg 14.4 par 1
	f4:n 2
	nps 100000.0
	rand seed 1232209489
	
