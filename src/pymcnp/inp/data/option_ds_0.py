import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ds0(_option.DataOption_, keyword='ds'):
    """
    Represents INP data card ds_0 options.

    Attributes:
        option: Dependent variable setting.
        js: Depdented source dependent variables.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Ads(\d+?)( \S+)(( \S+)+)\Z')

    def __init__(self, option: types.String, js: tuple[types.Real], suffix: types.Integer):
        """
        Initializes ``DataOption_Ds0``.

        Parameters:
            option: Dependent variable setting.
            js: Depdented source dependent variables.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Ds0``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if option is None or option not in {'h', 'l', 's'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if js is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, js)
        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([option, js])
        self.option: typing.Final[types.String] = option
        self.js: typing.Final[tuple[types.Real]] = js
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ds0`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ds0``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ds0._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        option = types.String.from_mcnp(tokens[2])
        js = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[3])]
        )

        return DataOption_Ds0(option, js, suffix)
