import pymcnp
from ... import consts
from ... import classes


class Test_Files:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Files
        EXAMPLES_VALID = [{'creations': [consts.string.inp.files.FILE]}, {'creations': [consts.ast.inp.files.FILE]}]
        EXAMPLES_INVALID = [{'creations': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Files
        EXAMPLES_VALID = [consts.string.inp.FILES]
        EXAMPLES_INVALID = ['hello']
