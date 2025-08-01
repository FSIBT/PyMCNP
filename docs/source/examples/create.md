# "Create" Examples

PyMCNP supports INP files and cards creation.

## Creating Cell Cards

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_cell.py
   :language: python
```

Output:

	1 1 0.5 #(99:3) imp:n 1.0

## Creating Material Cards

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_material.py
   :language: python
```

Output:

	m1 001001 0.1118855432927602 001002 0.000012868317335160966 008016 0.8859435015301171 008017 0.00033747860358816377 008018 0.0018206082561993046

## Creating Surface Cards

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_surface.py
   :language: python
```

Output:

	1  so 2

## Creating INP Files

Code:

```{eval-rst}
.. literalinclude:: ../../../examples/create_inp.py
   :language: python
```

Output:

	Create ``Inp``
	
	1 21 0.5 11 
	2 22 0.5 12:11 
	3 23 0.5 13:12 
	4 0  14 
	
	11  rpp -60 60 -60 60 -60 60
	11  rpp -5 5 -5 5 -5 5
	11  rpp -1 1 -1 1 -1 1
	99  so 67
	
	m21 007014 -0.797088 007015 -0.002912 008016 -0.199514 008017 -7.6e-05 008018 &
	      -0.00041000000000000005
	m22 008016 -0.19984179019595494 008017 -7.612486369323746e-05 008018 &
	      -0.00041067360676614944 022046 -0.02472289143502082 022047 &
	      -0.02229555300321877 022048 -0.22091776443511935 022049 &
	      -0.016212223353146985 022050 -0.015522979107079737 008016 &
	      -0.03575396279808631 008017 -1.361960149490542e-05 008018 &
	      -7.347416595935819e-05 082204 -0.006498225208082432 082206 &
	      -0.11186230536770471 082207 -0.10257912649901553 082208 &
	      -0.24321928635965673
	m23 082204 -0.014 082206 -0.241 082207 -0.221 082208 -0.524

