import pathlib
import dataclasses

import pytest

import pymcnp


STRING = pymcnp.utils.types.String('a')
INTEGER = pymcnp.utils.types.Integer(1)
REAL = pymcnp.utils.types.Real(0.5)
DESIGNATOR = pymcnp.utils.types.Designator.from_mcnp('n')
TRANSFORMATION_0 = pymcnp.utils.types.Transformation_0.from_mcnp('1 1 1 2 2 2 3 3 3 4 4 4')
TRANSFORMATION_1 = pymcnp.utils.types.Transformation_1.from_mcnp('1 1 1 2 2 2 3 3 3')
TRANSFORMATION_2 = pymcnp.utils.types.Transformation_2.from_mcnp('1 1 1 2 2 2 3 3')
TRANSFORMATION_3 = pymcnp.utils.types.Transformation_3.from_mcnp('1 1 1 2 2 2')
TRANSFORMATION_4 = pymcnp.utils.types.Transformation_4.from_mcnp('1 1 1')
INDEX = pymcnp.utils.types.Index.from_mcnp('2:3')


class _Test_FromMcnp:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLES_VALID: list[str] = []
    EXAMPLES_INVALID: list[str] = []

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
            with pytest.raises((pymcnp.utils.errors.InpError, pymcnp.utils.errors.McnpError)):
                self.element.from_mcnp(example)


class _Test_FromMcnpFile:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLES_VALID: list[pathlib.Path] = []
    EXAMPLES_INVALID: list[pathlib.Path] = []

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
            with pytest.raises((pymcnp.utils.errors.InpError, pymcnp.utils.errors.McnpError)):
                self.element.from_file(example)


class _Test_Build:
    element: dataclasses.dataclass
    EXAMPLES_VALID: list[dict[object]] = []
    EXAMPLES_INVALID: list[dict[object]] = []

    def test_valid(self):
        """
        Tests ``EXAMPLES_VALID``.
        """

        for example in self.EXAMPLES_VALID:
            self.element(**example).build()

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises((pymcnp.utils.errors.InpError, pymcnp.utils.errors.McnpError)):
                self.element(**example).build()
