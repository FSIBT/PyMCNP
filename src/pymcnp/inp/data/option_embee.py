import re
import typing

from . import embee
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Embee(_option.DataOption_, keyword='embee'):
    """
    Represents INP data card embee options.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Aembee(\d+?)(( (((embed)( \S+))|((energy)( \S+))|((time)( \S+))|((atom)( \S+))|((factor)( \S+))|((list)( \S+))|((mat)( \S+))|((mtype)( \S+))))+)?\Z'
    )

    def __init__(self, suffix: types.Integer, options: tuple[embee.EmbeeOption_] = None):
        """
        Initializes ``DataOption_Embee``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Returns:
            ``DataOption_Embee``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[dict[str, embee.EmbeeOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Embee`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Embee``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Embee._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        options = (
            types._Tuple(tuple(_parser.process_inp_option(embee.EmbeeOption_, tokens[3])))
            if tokens[3]
            else None
        )

        return DataOption_Embee(suffix, options)
