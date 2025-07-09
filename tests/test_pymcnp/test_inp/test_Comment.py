import pymcnp
from ... import consts
from ... import classes


class Test_Comment:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Comment
        EXAMPLES_VALID = [{'text': None}, {'text': consts.string.type.STRING}, {'text': consts.ast.type.STRING}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
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
            consts.string.inp.COMMENT,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]


class Test_CommentBuilder:
    class Test_Build(classes.Test_Build):
        element = pymcnp.inp.CommentBuilder
        EXAMPLES_VALID = [{'text': None}, {'text': consts.string.type.STRING}, {'text': consts.ast.type.STRING}]
        EXAMPLES_INVALID = []
