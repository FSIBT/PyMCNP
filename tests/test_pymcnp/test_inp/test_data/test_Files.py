import pymcnp
from .... import consts
from .... import classes


class Test_Files:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Files
        EXAMPLES_VALID = [{'creations': [consts.ast.type.FILE]}]
        EXAMPLES_INVALID = [{'creations': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Files
        EXAMPLES_VALID = [consts.string.inp.data.FILES]
        EXAMPLES_INVALID = ['hello']


class Test_FilesBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FilesBuilder
        EXAMPLES_VALID = [{'creations': [consts.string.type.FILE]}, {'creations': [consts.ast.type.FILE]}]
        EXAMPLES_INVALID = [{'creations': None}]
