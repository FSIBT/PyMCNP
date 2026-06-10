import pymcnp
from ..... import classes


class Test_Embed(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Embed
    EXAMPLES_VALID = [
        'background 1',
        'matcell 1 2 1 2 1 2',
        'meshgeo lnk3dnt',
        'mgeoin hello',
        'meeout hello',
        'meein hello',
        'calc_vols yes',
        'debug echomesh',
        'elementchk= yes',
        'filetype ascii',
        'gmvfile hello',
        'hdf5file hello',
        'length 1',
        'mcnpumfile hello',
        'overlap exit',
        'overlap exit average',
        'overlap exit average 1 2 1 2',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
