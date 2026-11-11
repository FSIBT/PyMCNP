import collections

import pymcnp


class Test_FromMcnp:
    element: pymcnp.abc.Nonterminal

    EXAMPLES_FROM_MCNP_VALID: collections.abc.Sequence[str] = []
    EXAMPLES_FROM_MCNP_INVALID: collections.abc.Sequence[str] = []

    def test_from_mcnp_valid(self) -> None:
        """
        Tests `EXAMPLES_FROM_MCNP_VALID` on `from_mcnp` and `to_mcnp`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)
            a, _ = self.element.from_mcnp(example)
            b, _ = self.element.from_mcnp(a.to_mcnp())
            assert a.to_mcnp() == b.to_mcnp()
            assert example == a.to_mcnp()

    def test_from_mcnp_invalid(self) -> None:
        """
        Tests `EXAMPLES_FROM_MCNP_INVALID` on `from_mcnp`.
        """

        for example in self.EXAMPLES_FROM_MCNP_INVALID:
            print(example)
            try:
                _, source = self.element.from_mcnp(example)
                assert source
            except pymcnp.abc.Error:
                assert True

class Test_FromFile(Test_FromMcnp):
    element: pymcnp.abc.Nonterminal

    EXAMPLES_FROM_FILE_VALID: collections.abc.Sequence[str] = []
    EXAMPLES_FROM_FILE_INVALID: collections.abc.Sequence[str] = []

    def test_from_file_valid(self) -> None:
        """
        Tests `EXAMPLES_FROM_MCNP_VALID` on `from_file` and `to_mcnp`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)
            a, _ = self.element.from_file(example)
            b, _ = self.element.from_mcnp(a.to_mcnp())
            assert a.to_mcnp() == b.to_mcnp()
            assert example.read_text() == a.to_mcnp()

    def test_from_file_invalid(self) -> None:
        """
        Tests `EXAMPLES_FROM_MCNP_INVALID` on `from_file`.
        """

        for example in self.EXAMPLES_FROM_FILE_INVALID:
            print(example)
            try:
                _, source = self.element.from_file(example)
                assert source
            except pymcnp.abc.Error:
                assert True
