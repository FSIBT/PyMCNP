import pymcnp


class Test_Warning:
    def test___str___valid(self) -> None:
        str(pymcnp.abc.Warning('Hi', 'Hello'))
