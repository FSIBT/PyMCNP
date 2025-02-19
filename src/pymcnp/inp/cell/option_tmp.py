import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Tmp(_option.CellOption_, keyword='tmp'):
    """
    Represents INP cell card tmp options.

    Attributes:
        temperature: Cell temperature at suffix time index.
        suffix: Cell option suffix.
    """

    _REGEX = re.compile(r'\Atmp(\d+?)( \S+)\Z')

    def __init__(self, temperature: types.Real, suffix: types.Integer):
        """
        Initializes ``CellOption_Tmp``.

        Parameters:
            temperature: Cell temperature at suffix time index.
            suffix: Cell option suffix.

        Returns:
            ``CellOption_Tmp``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if temperature is None or not (temperature > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, temperature)
        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([temperature])
        self.temperature: typing.Final[types.Real] = temperature
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Tmp`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Tmp``.

        Raises:
            InpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Tmp._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        temperature = types.Real.from_mcnp(tokens[2])

        return CellOption_Tmp(temperature, suffix)
