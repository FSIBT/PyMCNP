import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Nonu(_option.DataOption_, keyword='nonu'):
    """
    Represents INP data card nonu options.

    Attributes:
        settings: Tuple of fission settings.
    """

    _REGEX = re.compile(r'\Anonu(( \S+)+)?\Z')

    def __init__(self, settings: tuple[types.Integer] = None):
        """
        Initializes ``DataOption_Nonu``.

        Parameters:
            settings: Tuple of fission settings.

        Returns:
            ``DataOption_Nonu``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if settings is not None and not (
            filter(lambda entry: not (entry == 0 or entry == 1 or entry == 2), settings)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, settings)

        self.value: typing.Final[tuple[any]] = types._Tuple([settings])
        self.settings: typing.Final[tuple[types.Integer]] = settings

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Nonu`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Nonu``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Nonu._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        settings = (
            types._Tuple(
                [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
            )
            if tokens[1]
            else None
        )

        return DataOption_Nonu(settings)
