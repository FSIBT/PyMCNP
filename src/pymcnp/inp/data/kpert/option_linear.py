import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KpertOption_Linear(_option.KpertOption_, keyword='linear'):
    """
    Represents INP data card data option linear options.

    Attributes:
        setting: Pertubated fission source on/off.
    """

    _REGEX = re.compile(r'\Alinear( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``KpertOption_Linear``.

        Parameters:
            setting: Pertubated fission source on/off.

        Returns:
            ``KpertOption_Linear``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KpertOption_Linear`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KpertOption_Linear``.

        Raises:
            McnpError: SYNTAX_KPERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KpertOption_Linear._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KPERT_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return KpertOption_Linear(setting)
