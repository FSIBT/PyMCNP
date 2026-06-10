import pymcnp
from .... import classes


class Test_DependentDistribution(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.DependentDistribution
    EXAMPLES_VALID = [
        'FCEL=D1',
        'FSUR=D1',
        'FERG=D1',
        'FTME=D1',
        'FDIR=D1',
        'FVEC=D1',
        'FNRM=D1',
        'FPOS=D1',
        'FRAD=D1',
        'FEXT=D1',
        'FAXS=D1',
        'FX=D1',
        'FY=D1',
        'FZ=D1',
        'FCCC=D1',
        'FARA=D1',
        'FWGT=D1',
        'FTR=D1',
        'FEFF=D1',
        'FPAR=D1',
        'FDAT=D1',
        'FLOC=D1',
        'FBEM=D1',
        'FBAP=D1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
