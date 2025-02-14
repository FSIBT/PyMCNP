import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Wwn(_option.DataOption_, keyword='wwn'):
    """
    Represents INP data card wwn options.

    Attributes:
        bounds: Lower weight bound.
        suffix: Data card option suffix.
        designator: Data card particle designator.
    """

    _REGEX = re.compile(r'\Awwn(\d+?):(\S+?)(( \S+)+)\Z')

    def __init__(
        self, bounds: tuple[types.Real], suffix: types.Integer, designator: types.Designator
    ):
        """
        Initializes ``DataOption_Wwn``.

        Parameters:
            bounds: Lower weight bound.
            suffix: Data card option suffix.
            designator: Data card particle designator.

        Returns:
            ``DataOption_Wwn``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
            McnpError: SEMANTICS_DATA_OPTION_DESIGNATOR.
        """

        if bounds is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, bounds)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([bounds])
        self.bounds: typing.Final[tuple[types.Real]] = bounds
        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Wwn`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Wwn``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Wwn._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        designator = types.Designator.from_mcnp(tokens[2])
        bounds = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[3])]
        )

        return DataOption_Wwn(bounds, suffix, designator)
