import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Par(_option.SdefOption_, keyword='par'):
    """
    Represents INP data card data option par options.

    Attributes:
        kind: Source particle type.
    """

    _REGEX = re.compile(r'\Apar( \S+)\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``SdefOption_Par``.

        Parameters:
            kind: Source particle type.

        Returns:
            ``SdefOption_Par``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[tuple[any]] = types._Tuple([kind])
        self.kind: typing.Final[types.String] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Par`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Par``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Par._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        kind = types.String.from_mcnp(tokens[1])

        return SdefOption_Par(kind)
