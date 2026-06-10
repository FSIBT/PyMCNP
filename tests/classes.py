import collections

import pymcnp


class Test_Nonterminal:
    element: pymcnp.abc.Nonterminal
    EXAMPLES_VALID: collections.abc.Sequence[str] = []
    EXAMPLES_INVALID: collections.abc.Sequence[str] = []

    def test_from_mcnp_valid(self) -> None:
        """
        Tests `EXAMPLES_VALID` on `from_mcnp` and `to_mcnp`.
        """

        for example in self.EXAMPLES_VALID:
            a, _ = self.element.from_mcnp(example)
            b, _ = self.element.from_mcnp(a.to_mcnp())
            assert a.to_mcnp() == b.to_mcnp()
            assert example == a.to_mcnp()

    def test_from_mcnp_invalid(self) -> None:
        """
        Tests `EXAMPLES_INVALID` on `from_mcnp`.
        """

        for example in self.EXAMPLES_INVALID:
            print(example)
            try:
                _, source = self.element.from_mcnp(example)
                assert source
            except pymcnp.abc.Error:
                assert True
