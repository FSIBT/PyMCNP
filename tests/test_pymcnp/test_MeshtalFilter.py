import pymcnp
from .. import consts


class Filter0(pymcnp.MeshtalFilter):
    def check(self, tally):
        return False


class Filter1(pymcnp.MeshtalFilter):
    def check(self, tally):
        return True


class Test_MeshtalFilter:
    class Test_Dunder:
        EXAMPLES = [
            consts.ast.MESHTAL,
        ]

        def test__call__(self):
            for example in self.EXAMPLES:
                list(pymcnp.MeshtalFilter()(example))
                list(Filter0()(example))
                list(Filter1()(example))
