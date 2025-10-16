import pymcnp
from .. import consts


class Test_MeshtalProcessor:
    class Test_Dunder:
        EXAMPLES = [
            consts.ast.MESHTAL,
        ]

        def test__call__(self):
            for example in self.EXAMPLES:
                pymcnp.MeshtalProcessor()(example)
