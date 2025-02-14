import re
import typing

from . import ds_1
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ds1(_option.DataOption_, keyword='ds'):
    """
    Represents INP data card ds_1 options.

    Attributes:
        t: Dependent source T option.
        ijs: Dependent source independent & dependent variables.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Ads(\d+?)( \S+)((( \S+)( \S+))+)\Z')

    def __init__(self, t: types.String, ijs: tuple[ds_1.Ds1Entry_Tpair], suffix: types.Integer):
        """
        Initializes ``DataOption_Ds1``.

        Parameters:
            t: Dependent source T option.
            ijs: Dependent source independent & dependent variables.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Ds1``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if t is None or t not in {'t'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, t)
        if ijs is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ijs)
        if suffix is None or not (1 <= suffix <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([t, ijs])
        self.t: typing.Final[types.String] = t
        self.ijs: typing.Final[tuple[ds_1.Ds1Entry_Tpair]] = ijs
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ds1`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ds1``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ds1._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        t = types.String.from_mcnp(tokens[2])
        ijs = types._Tuple(
            [
                ds_1.Ds1Entry_Tpair.from_mcnp(token[0])
                for token in ds_1.Ds1Entry_Tpair._REGEX.finditer(tokens[3])
            ]
        )

        return DataOption_Ds1(t, ijs, suffix)
