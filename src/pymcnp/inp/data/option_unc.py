import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Unc(_option.DataOption_, keyword='unc'):
    """
    Represents INP data card unc options.

    Attributes:
        settings: Tuple of uncollided secondary settings.
    """

    _REGEX = re.compile(r'\Aunc(( \S+)+)\Z')

    def __init__(self, settings: tuple[types.Integer]):
        """
        Initializes ``DataOption_Unc``.

        Parameters:
            settings: Tuple of uncollided secondary settings.

        Returns:
            ``DataOption_Unc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if settings is None or not (filter(lambda entry: entry.value not in {0, 1}, settings)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, settings)

        self.value: typing.Final[tuple[any]] = types._Tuple([settings])
        self.settings: typing.Final[tuple[types.Integer]] = settings

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Unc`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Unc``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Unc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        settings = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Unc(settings)
