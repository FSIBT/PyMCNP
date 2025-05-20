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
JUMP = pymcnp.utils.types.Jump()
STOCHASTIC = pymcnp.utils.types.Stochastic.from_mcnp('1 2 4 6')
ZAID = pymcnp.utils.types.Zaid.from_mcnp('002001')
SUBSTANCE = pymcnp.utils.types.Substance.from_mcnp('002001 1')
BIAS = pymcnp.utils.types.Bias.from_mcnp('1 2')
DISTRIBUTION = pymcnp.utils.types.DistributionNumber.from_mcnp('d9')
EMBEDDED_DISTRIBUTION = pymcnp.utils.types.EmbeddedDistributionNumber.from_mcnp('d9 > d1')
INDEPENDENT_DEPENDENT = pymcnp.utils.types.IndependentDependent.from_mcnp('2 3')
LOCATION = pymcnp.utils.types.Location.from_mcnp('1 4 5')
SPHERE = pymcnp.utils.types.Sphere.from_mcnp('1 4 5 3')
RING = pymcnp.utils.types.Ring.from_mcnp('1 4 5')
SHELL = pymcnp.utils.types.Shell.from_mcnp('1 2 3 4 5')
DIAGNOSTIC = pymcnp.utils.types.Diagnostic.from_mcnp('1.0 2.0')
PHOTON_BIAS = pymcnp.utils.types.PhotonBias.from_mcnp('001001 2 001001 2')
FILTER = pymcnp.utils.types.PtracFilter.from_mcnp('1,a')
FILE = pymcnp.utils.types.File.from_mcnp('1 a sequential formatted 2')


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


class _Test_Draw:
    element: pymcnp.utils._object.McnpNonterminal
    EXAMPLES: list[pathlib.Path] = []

    def test(self):
        """
        Tests ``EXAMPLES``.
        """

        for example in self.EXAMPLES:
            self.element.from_mcnp(example).draw()
