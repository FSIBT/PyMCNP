import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class BfldOption_Field(_option.BfldOption_, keyword='field'):
    """
    Represents INP data card data option field options.

    Attributes:
        strength_gradient: Magnetic field strength/gradient.
    """

    _REGEX = re.compile(r'\Afield( \S+)\Z')

    def __init__(self, strength_gradient: types.Real):
        """
        Initializes ``BfldOption_Field``.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Returns:
            ``BfldOption_Field``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if strength_gradient is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, strength_gradient)

        self.value: typing.Final[tuple[any]] = types._Tuple([strength_gradient])
        self.strength_gradient: typing.Final[types.Real] = strength_gradient

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BfldOption_Field`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``BfldOption_Field``.

        Raises:
            InpError: SYNTAX_BFLD_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BfldOption_Field._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        strength_gradient = types.Real.from_mcnp(tokens[1])

        return BfldOption_Field(strength_gradient)
