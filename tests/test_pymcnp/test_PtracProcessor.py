import pymcnp
from .. import consts


class Test_PtracProcessor:
    class Test_Dunder:
        EXAMPLES = [
            consts.ast.PTRAC,
        ]

        def test__call__(self):
            for example in self.EXAMPLES:
                pymcnp.PtracProcessor()(example)
