import re
import typing

from . import kpert
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Kpert(_option.DataOption_, keyword='kpert'):
    """
    Represents INP data card kpert options.

    Attributes:
        options: Dictionary of options.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(
        r'\Akpert(\d+?)(( (((cell)(( \S+)+))|((mat)(( \S+)+))|((rho)(( \S+)+))|((iso)(( \S+)+))|((rxn)(( \S+)+))|((erg)(( \S+)+))|((linear)( \S+))))+)?\Z'
    )

    def __init__(self, suffix: types.Integer, options: tuple[kpert.KpertOption_] = None):
        """
        Initializes ``DataOption_Kpert``.

        Parameters:
            options: Dictionary of options.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Kpert``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if suffix is None or not (0 < suffix <= 10_000):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, kpert.KpertOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Kpert`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Kpert``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Kpert._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        options = (
            types._Tuple(tuple(_parser.process_inp_option(kpert.KpertOption_, tokens[2])))
            if tokens[2]
            else None
        )

        return DataOption_Kpert(suffix, options)
