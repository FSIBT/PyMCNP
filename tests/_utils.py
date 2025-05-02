import pathlib

import pytest

import pymcnp


class _Test_FromMcnp:

    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLE_VALID: list[str]
    EXAMPLE_INVALID: list[str]

    def test_valid(self):
        """
        Tests ``EXAMPLES_VALID``.
        """

        for example in self.EXAMPLES_VALID:
            self.element.from_mcnp(example)

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises(pymcnp.utils.errors.InpError):
                self.element.from_mcnp(example)


class _Test_FromMcnpFile:

    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLE_VALID: list[pathlib.Path]
    EXAMPLE_INVALID: list[pathlib.Path]

    def test_valid(self):
        """
        Tests ``EXAMPLES_VALID``.
        """

        for example in self.EXAMPLES_VALID:
            self.element.from_file(example)

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises(pymcnp.utils.errors.InpError):
                self.element.from_file(example)
