import pathlib
import dataclasses

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
            print(repr(example))

            element = self.element(**example)

            for key, value in example.items():
                assert getattr(element, key) == value

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID`` on ``from_mcnp``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises((pymcnp.utils.errors.Error)):
                print(repr(example))

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
            print(repr(example))

            a = self.element.from_mcnp(example)
            print(repr(a.to_mcnp()))
            b = self.element.from_mcnp(a.to_mcnp())
            print(repr(b.to_mcnp()))

            assert a.to_mcnp() == b.to_mcnp()

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID`` on ``from_mcnp``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises((pymcnp.utils.errors.Error)):
                print(repr(example))

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
            print(repr(example))

            print(repr(example.read_text()))
            a = self.element.from_file(example)
            print(repr(a.to_mcnp()))
            b = self.element.from_mcnp(a.to_mcnp())
            print(repr(b.to_mcnp()))

            assert a.to_mcnp() == b.to_mcnp()

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID`` on ``from_file``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises((pymcnp.utils.errors.Error)):
                print(repr(example))
                self.element.from_file(example)


class Test_Build:
    element: dataclasses.dataclass
    EXAMPLES_VALID: list[dict[object]] = []
    EXAMPLES_INVALID: list[dict[object]] = []

    def test_valid(self):
        """
        Tests ``EXAMPLES_VALID`` on ``build`` and ``unbuild``.
        """

        for example in self.EXAMPLES_VALID:
            print(repr(example))

            a = self.element(**example)
            b = a.build()
            c = self.element.unbuild(b)
            d = c.build()

            assert b.to_mcnp() == d.to_mcnp()

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID`` on `build``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises((pymcnp.utils.errors.Error)):
                print(repr(example))

                self.element(**example).build()


class Test_Draw:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLES: list[str] = []

    def test(self):
        """
        Tests ``EXAMPLES`` on ``draw``.
        """

        for example in self.EXAMPLES:
            print(repr(example))
            self.element.from_mcnp(example).draw()


class Test_Dataframe:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMLPES: list[str] = []

    def test(self):
        """
        Tests ``EXAMPLES`` on ``to_dataframe``.
        """

        for example in self.EXAMPLES:
            print(repr(example))
            self.element.from_mcnp(example).to_dataframe()
