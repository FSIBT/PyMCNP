import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Cosyp(_option.DataOption_, keyword='cosyp'):
    """
    Represents INP data card cosyp options.

    Attributes:
        prefix: Prefix number of the COSY map files.
        axsh: Horiztonal axis orientation.
        axsv: Vertical axis orientation.
        emaps: Tuple of operating beam energies.
    """

    _REGEX = re.compile(r'\Acosyp( \S+)( \S+)( \S+)(( \S+)+)\Z')

    def __init__(
        self,
        prefix: types.Integer,
        axsh: types.Integer,
        axsv: types.Integer,
        emaps: tuple[types.Real],
    ):
        """
        Initializes ``DataOption_Cosyp``.

        Parameters:
            prefix: Prefix number of the COSY map files.
            axsh: Horiztonal axis orientation.
            axsv: Vertical axis orientation.
            emaps: Tuple of operating beam energies.

        Returns:
            ``DataOption_Cosyp``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if prefix is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, prefix)
        if axsh is None or axsh.value not in {1, 2, 3}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, axsh)
        if axsv is None or axsv.value not in {1, 2, 3}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, axsv)
        if emaps is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, emaps)

        self.value: typing.Final[tuple[any]] = types._Tuple([prefix, axsh, axsv, emaps])
        self.prefix: typing.Final[types.Integer] = prefix
        self.axsh: typing.Final[types.Integer] = axsh
        self.axsv: typing.Final[types.Integer] = axsv
        self.emaps: typing.Final[tuple[types.Real]] = emaps

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Cosyp`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Cosyp``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Cosyp._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        prefix = types.Integer.from_mcnp(tokens[1])
        axsh = types.Integer.from_mcnp(tokens[2])
        axsv = types.Integer.from_mcnp(tokens[3])
        emaps = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[4])]
        )

        return DataOption_Cosyp(prefix, axsh, axsv, emaps)
