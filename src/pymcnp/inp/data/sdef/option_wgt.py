import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Wgt(_option.SdefOption_, keyword='wgt'):
    """
    Represents INP data card data option wgt options.

    Attributes:
        weight: Particle weight.
    """

    _REGEX = re.compile(r'\Awgt( \S+)\Z')

    def __init__(self, weight: types.Real):
        """
        Initializes ``SdefOption_Wgt``.

        Parameters:
            weight: Particle weight.

        Returns:
            ``SdefOption_Wgt``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight)

        self.value: typing.Final[tuple[any]] = types._Tuple([weight])
        self.weight: typing.Final[types.Real] = weight

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Wgt`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Wgt``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Wgt._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        weight = types.Real.from_mcnp(tokens[1])

        return SdefOption_Wgt(weight)
