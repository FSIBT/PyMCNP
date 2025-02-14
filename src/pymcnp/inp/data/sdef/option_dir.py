import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Dir(_option.SdefOption_, keyword='dir'):
    """
    Represents INP data card data option dir options.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    _REGEX = re.compile(r'\Adir( \S+)\Z')

    def __init__(self, cosine: types.Real):
        """
        Initializes ``SdefOption_Dir``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Returns:
            ``SdefOption_Dir``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if cosine is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, cosine)

        self.value: typing.Final[tuple[any]] = types._Tuple([cosine])
        self.cosine: typing.Final[types.Real] = cosine

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Dir`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Dir``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Dir._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        cosine = types.Real.from_mcnp(tokens[1])

        return SdefOption_Dir(cosine)
