import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_File(_option.PtracOption_, keyword='file'):
    """
    Represents INP data card data option file options.

    Attributes:
        setting: PTRAC file type.
    """

    _REGEX = re.compile(r'\Afile( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``PtracOption_File``.

        Parameters:
            setting: PTRAC file type.

        Returns:
            ``PtracOption_File``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'asc', 'bin', 'aov', 'bov'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_File`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_File``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_File._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return PtracOption_File(setting)
