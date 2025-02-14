import re
import typing

from . import ksen
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ksen(_option.DataOption_, keyword='ksen'):
    """
    Represents INP data card ksen options.

    Attributes:
        sen: Type of sensitivity.
        options: Dictionary of options.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(
        r'\Aksen(\d+?)( \S+)(( (((iso)(( \S+)+))|((rxn)(( \S+)+))|((mt)(( \S+)+))|((erg)(( \S+)+))|((ein)(( \S+)+))|((legendre)( \S+))|((cos)(( \S+)+))|((constrain)( \S+))))+)?\Z'
    )

    def __init__(
        self, sen: types.String, suffix: types.Integer, options: tuple[ksen.KsenOption_] = None
    ):
        """
        Initializes ``DataOption_Ksen``.

        Parameters:
            sen: Type of sensitivity.
            options: Dictionary of options.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Ksen``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if sen is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, sen)
        if suffix is None or not (0 < suffix <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([sen, options])
        self.sen: typing.Final[types.String] = sen
        self.options: typing.Final[dict[str, ksen.KsenOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ksen`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ksen``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ksen._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        sen = types.String.from_mcnp(tokens[2])
        options = (
            types._Tuple(tuple(_parser.process_inp_option(ksen.KsenOption_, tokens[3])))
            if tokens[3]
            else None
        )

        return DataOption_Ksen(sen, suffix, options)
