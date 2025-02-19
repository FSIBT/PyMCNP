import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Ksental(_option.KoptsOption_, keyword='ksental'):
    """
    Represents INP data card data option ksental options.

    Attributes:
        fileopt: Format of sensity profiles output file.
    """

    _REGEX = re.compile(r'\Aksental( \S+)\Z')

    def __init__(self, fileopt: types.String):
        """
        Initializes ``KoptsOption_Ksental``.

        Parameters:
            fileopt: Format of sensity profiles output file.

        Returns:
            ``KoptsOption_Ksental``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fileopt is None or fileopt not in {
            'mctal',
        }:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fileopt)

        self.value: typing.Final[tuple[any]] = types._Tuple([fileopt])
        self.fileopt: typing.Final[types.String] = fileopt

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Ksental`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Ksental``.

        Raises:
            InpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Ksental._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        fileopt = types.String.from_mcnp(tokens[1])

        return KoptsOption_Ksental(fileopt)
