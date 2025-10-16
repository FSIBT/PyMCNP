import pymcnp
from .. import consts


class Filter0(pymcnp.PtracFilter):
    def check_source(self, tally):
        return False

    def check_bank(self, tally):
        return False

    def check_surface(self, tally):
        return False

    def check_collision(self, tally):
        return False

    def check_terminal(self, tally):
        return False


class Filter1(pymcnp.PtracFilter):
    def check_source(self, tally):
        return True

    def check_bank(self, tally):
        return True

    def check_surface(self, tally):
        return True

    def check_collision(self, tally):
        return True

    def check_terminal(self, tally):
        return True


class Test_PtracFilter:
    class Test_Dunder:
        EXAMPLES = [
            consts.ast.PTRAC,
        ]

        def test__call__(self):
            for example in self.EXAMPLES:
                list(pymcnp.PtracFilter()(example))
                list(Filter0()(example))
                list(Filter1()(example))
