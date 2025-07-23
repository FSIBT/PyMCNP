import pathlib

import pytest

import pymcnp


class Test_Init:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLES_VALID: list[str] = []
    EXAMPLES_INVALID: list[str] = []

    def test_valid(self):
        """
        Tests ``EXAMPLES_VALID`` on ``from_mcnp`` and ``to_mcnp``.
        """

        for example in self.EXAMPLES_VALID:
            self.element(**example)

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID`` on ``from_mcnp``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises((pymcnp.errors.Error)):
                self.element(**example)


class Test_Mcnp:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLES_VALID: list[str] = []
    EXAMPLES_INVALID: list[str] = []

    def test_valid(self):
        """
        Tests ``EXAMPLES_VALID`` on ``from_mcnp`` and ``to_mcnp``.
        """

        for example in self.EXAMPLES_VALID:
            a = self.element.from_mcnp(example)
            b = self.element.from_mcnp(a.to_mcnp())

            assert a == b

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID`` on ``from_mcnp``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises((pymcnp.errors.Error)):
                self.element.from_mcnp(example)


class Test_File:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLES_VALID: list[pathlib.Path] = []
    EXAMPLES_INVALID: list[pathlib.Path] = []

    def test_valid(self):
        """
        Tests ``EXAMPLES_VALID`` on ``from_file``.
        """

        for example in self.EXAMPLES_VALID:
            a = self.element.from_file(example)
            b = self.element.from_mcnp(a.to_mcnp())

            assert a == b

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID`` on ``from_file``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises((pymcnp.errors.Error)):
                self.element.from_file(example)


class Test_Draw:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLES: list[str] = []

    def test(self):
        """
        Tests ``EXAMPLES`` on ``draw``.
        """

        for example in self.EXAMPLES:
            self.element.from_mcnp(example).draw()


class Test_Dataframe:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMLPES: list[str] = []

    def test(self):
        """
        Tests ``EXAMPLES`` on ``to_dataframe``.
        """

        for example in self.EXAMPLES:
            self.element.from_mcnp(example).to_dataframe()
