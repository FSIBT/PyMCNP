import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PertOption_Mat(_option.PertOption_, keyword='mat'):
    """
    Represents INP data card data option mat options.

    Attributes:
        material: Material number to fill cells.
    """

    _REGEX = re.compile(r'\Amat( \S+)\Z')

    def __init__(self, material: types.Integer):
        """
        Initializes ``PertOption_Mat``.

        Parameters:
            material: Material number to fill cells.

        Returns:
            ``PertOption_Mat``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, material)

        self.value: typing.Final[tuple[any]] = types._Tuple([material])
        self.material: typing.Final[types.Integer] = material

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PertOption_Mat`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PertOption_Mat``.

        Raises:
            McnpError: SYNTAX_PERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PertOption_Mat._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_PERT_OPTION, source)

        material = types.Integer.from_mcnp(tokens[1])

        return PertOption_Mat(material)
