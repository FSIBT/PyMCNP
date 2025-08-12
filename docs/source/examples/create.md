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

	m1 001001 0.1118855432927602 008016 0.8859435015301171
	m1 001001 0.1118855432927602 008016 0.8859435015301171

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
	
	m21 007014 -0.797088 008016 -0.199514
	m22 008016 -0.19984179019595494 022046 -0.02472289143502082 022047 &
      	-0.02229555300321877 022048 -0.22091776443511935 022049 &
      	-0.016212223353146985 022050 -0.015522979107079737 008016 &
      	-0.03575396279808631 082206 -0.11186230536770471 082207 &
      	-0.10257912649901553 082208 -0.24321928635965673
	m23 082204 -0.014 082206 -0.241 082207 -0.221 082208 -0.524

