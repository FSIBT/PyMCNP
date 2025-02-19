import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Event(_option.PtracOption_, keyword='event'):
    """
    Represents INP data card data option event options.

    Attributes:
        setting: Specifies the type of events written to the PTRAC file.
    """

    _REGEX = re.compile(r'\Aevent( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``PtracOption_Event``.

        Parameters:
            setting: Specifies the type of events written to the PTRAC file.

        Returns:
            ``PtracOption_Event``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'src', 'bnk', 'sur', 'col', 'ter', 'cap'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Event`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Event``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Event._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return PtracOption_Event(setting)
