import pymcnp


class Test_Error:
    def test___str___valid(self) -> None:
        assert str(pymcnp.abc.Error('Hi', 'Hello')) == 'Hi\n Hello'
