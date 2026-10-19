import pymcnp


class Test_Array:
    def test___str___valid(self) -> None:
        str(pymcnp.abc.Error('Hi', 'Hello'))
