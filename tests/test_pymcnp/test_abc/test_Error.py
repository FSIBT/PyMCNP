import pymcnp


class Test_Error:
    def test___str___valid(self) -> None:
        str(pymcnp.abc.Error('Hi', 'Hello'))
