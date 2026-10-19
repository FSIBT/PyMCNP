import pymcnp
from ..... import classes


class Test_Kopts(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Kopts
    EXAMPLES_VALID = [
        'blocksize 2',
        'kinetics yes',
        'precursor yes',
        'ksental mctal',
        'ksental',
        'fmat yes',
        'fmatsrc yes',
        'fmatskip 1',
        'fmatncyc 1',
        'fmatspace 1',
        'fmataccel yes',
        'fmatreduce yes',
        'fmatconvrg yes',
        'fmatnx 3.1',
        'fmatny 3.1',
        'fmatnz 3.1',
    ]
    EXAMPLES_INVALID = [
        'blocksize 1',
        'hello',
    ]
