import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Fc(_option.DataOption_, keyword='fc'):
    """
    Represents INP data card fc options.

    Attributes:
        info: Title for tally in output and MCTAL file.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Afc(\d+?)( \S+)\Z')

    def __init__(self, info: types.String, suffix: types.Integer):
        """
        Initializes ``DataOption_Fc``.

        Parameters:
            info: Title for tally in output and MCTAL file.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Fc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if info is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, info)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([info])
        self.info: typing.Final[types.String] = info
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Fc`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Fc``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Fc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        info = types.String.from_mcnp(tokens[2])

        return DataOption_Fc(info, suffix)
