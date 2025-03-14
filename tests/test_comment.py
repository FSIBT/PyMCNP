import pymcnp
import _utils


class Test_Comment:
    """
    Tests ``Comment``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``Comment.from_mcnp``.
        """

        element = pymcnp.inp.Comment
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []
