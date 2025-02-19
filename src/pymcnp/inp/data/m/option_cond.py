import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Cond(_option.MOption_, keyword='cond'):
    """
    Represents INP data card data option cond options.

    Attributes:
        setting: Conduction state for EL03 electron-transport evaluation.
    """

    _REGEX = re.compile(r'\Acond( \S+)\Z')

    def __init__(self, setting: types.Real):
        """
        Initializes ``MOption_Cond``.

        Parameters:
            setting: Conduction state for EL03 electron-transport evaluation.

        Returns:
            ``MOption_Cond``.

        Raises:
            InpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Real] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MOption_Cond`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Cond``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Cond._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        setting = types.Real.from_mcnp(tokens[1])

        return MOption_Cond(setting)
