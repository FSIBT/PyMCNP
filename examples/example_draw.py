import pathlib

import pymcnp


inp = pymcnp.Inp.from_file(pathlib.Path(__file__).parent / 'data/input_files/png.i')
vista = inp.draw()
vista.plot()
