import pymcnp
from .. import _utils


class Test_Comment:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Comment
        EXAMPLES_VALID = [
            # 1.3
            'c cell cards for sample problem',
            'c end of cell cards for sample problem',
            # 1.3
            'C Beginning of surfaces for cube',
            'C End of cube surfaces',
            # 4.1
            'c cell cards',
            'c surface cards',
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.CommentBuilder
        EXAMPLES_VALID = [{'text': None}, {'text': _utils.string.type.STRING}, {'text': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = []
