import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Mphys(_option.DataOption_, keyword='mphys'):
    """
    Represents INP data card mphys options.

    Attributes:
        setting: Physics models on/off.
    """

    _REGEX = re.compile(r'\Amphys( \S+)?\Z')

    def __init__(self, setting: types.String = None):
        """
        Initializes ``DataOption_Mphys``.

        Parameters:
            setting: Physics models on/off.

        Returns:
            ``DataOption_Mphys``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is not None and setting not in {'on', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Mphys`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Mphys``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Mphys._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1]) if tokens[1] else None

        return DataOption_Mphys(setting)
