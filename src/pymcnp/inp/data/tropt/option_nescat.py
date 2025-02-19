import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class TroptOption_Nescat(_option.TroptOption_, keyword='nescat'):
    """
    Represents INP data card data option nescat options.

    Attributes:
        setting: Nuclear elastic scattering setting.
    """

    _REGEX = re.compile(r'\Anescat( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``TroptOption_Nescat``.

        Parameters:
            setting: Nuclear elastic scattering setting.

        Returns:
            ``TroptOption_Nescat``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'off', 'on'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TroptOption_Nescat`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``TroptOption_Nescat``.

        Raises:
            InpError: SYNTAX_TROPT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = TroptOption_Nescat._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return TroptOption_Nescat(setting)
