import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Spdtl(_option.DataOption_, keyword='spdtl'):
    """
    Represents INP data card spdtl options.

    Attributes:
        keyword: keyword in {"force", "off"}.
    """

    _REGEX = re.compile(r'\Aspdtl( \S+)\Z')

    def __init__(self, keyword: types.String):
        """
        Initializes ``DataOption_Spdtl``.

        Parameters:
            keyword: keyword in {"force", "off"}.

        Returns:
            ``DataOption_Spdtl``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if keyword is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, keyword)

        self.value: typing.Final[tuple[any]] = types._Tuple([keyword])
        self.keyword: typing.Final[types.String] = keyword

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Spdtl`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Spdtl``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Spdtl._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        keyword = types.String.from_mcnp(tokens[1])

        return DataOption_Spdtl(keyword)
