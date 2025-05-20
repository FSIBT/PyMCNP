import pathlib

import pymcnp
from . import _utils


class Test_Inp:
    """
    Tests ``Inp``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``Inp.from_mcnp``.
        """

        element = pymcnp.Inp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_FromMcnpFile(_utils._Test_FromMcnpFile):
        """
        Tests ``Inp.from_file``.
        """

        element = pymcnp.Inp
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent / 'files/inp').glob('*.i'),
        ]
        EXAMPLES_INVALID = []


def test_comments():
    line = 'area -0.02 0.044 0.117\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(line)
    assert source == 'area -0.02 0.044 0.117'
    assert comments == []

    comment_line = 'area -0.02 0.044 0.117 $ hi\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(comment_line)
    assert source == 'area -0.02 0.044 0.117'
    assert comments == [' hi']

    doubled_comment_line = 'area -0.02 0.044 0.117 $ hi $ hello\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(doubled_comment_line)
    assert source == 'area -0.02 0.044 0.117'
    assert comments == [' hi $ hello']

    continuation_line = 'm300 8016 -0.2094897 $ o-016\n     7014 -0.7771608 $ n-014\n     18040 -0.00996035 $ ar-040\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(continuation_line)
    assert source == 'm300 8016 -0.2094897 7014 -0.7771608 18040 -0.00996035'
    assert comments == [' o-016', ' n-014', ' ar-040']

    doubled_continuation_line = 'm300 8016 -0.2094897 $ o-016 $ hello\n     7014 -0.7771608 $ n-014\n     18040 -0.00996035 $ ar-040 $ hi\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(doubled_continuation_line)
    assert source == 'm300 8016 -0.2094897 7014 -0.7771608 18040 -0.00996035'
    assert comments == [' o-016 $ hello', ' n-014', ' ar-040 $ hi']
