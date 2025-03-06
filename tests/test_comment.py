import pymcnp

import pytest


class _Test_FromMcnp:
    """
    Tests ``McnpElement_.from_mcnp``.
    """

    element: pymcnp.utils._object.McnpElement_
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


class Test_Comment:
    """
    Tests ``Comment``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``Comment.from_mcnp``.
        """

        element = pymcnp.inp.Comment
        EXAMPLES_VALID = [
            'c',
            'C',
            'c sdjfhasdkfj',
            'C sdfjhskdjfa',
        ]
        EXAMPLES_INVALID = [
            'sadkfjhajskd',
            '',
        ]
