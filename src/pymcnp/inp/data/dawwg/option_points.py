import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class DawwgOption_Points(_option.DawwgOption_, keyword='points'):
    """
    Represents INP data card data option points options.

    Attributes:
        name: Cross section library.
    """

    _REGEX = re.compile(r'\Apoints( \S+)\Z')

    def __init__(self, name: types.String):
        """
        Initializes ``DawwgOption_Points``.

        Parameters:
            name: Cross section library.

        Returns:
            ``DawwgOption_Points``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if name is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, name)

        self.value: typing.Final[tuple[any]] = types._Tuple([name])
        self.name: typing.Final[types.String] = name

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DawwgOption_Points`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``DawwgOption_Points``.

        Raises:
            InpError: SYNTAX_DAWWG_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DawwgOption_Points._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        name = types.String.from_mcnp(tokens[1])

        return DawwgOption_Points(name)
