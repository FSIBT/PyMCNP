# Examples

For examples using the command line, see the [Comand Line Interface](cli.rst).

## Loading a file

    import pymcnp
	
	filename = "/path/to/data/input.i'
	data = pymcnp.read_input(filename)

## Loading a file, modyfing it and saving it again

We load a file and change the number of particles to 100,000.

    import pymcnp
	
	filename = "/path/to/data/input.i'
	data = pymcnp.read_input(filename)
	
	pymcnp.modify(x.data._cards['nps'], npp=100_000)

	data.to_mcnp_file('/path/to/data/new_file_name.i')

