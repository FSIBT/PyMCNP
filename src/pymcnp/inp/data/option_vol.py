import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Vol(_option.DataOption_, keyword='vol'):
    """
    Represents INP data card vol options.

    Attributes:
        no: Calculation on/off.
        volumes: Tuple of cell volumes.
    """

    _REGEX = re.compile(r'\Avol( \S+)?(( \S+)+)\Z')

    def __init__(self, volumes: tuple[types.Real], no: types.String = None):
        """
        Initializes ``DataOption_Vol``.

        Parameters:
            no: Calculation on/off.
            volumes: Tuple of cell volumes.

        Returns:
            ``DataOption_Vol``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if no is not None and not (no == 'no'):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, no)
        if volumes is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, volumes)

        self.value: typing.Final[tuple[any]] = types._Tuple([volumes, no])
        self.no: typing.Final[types.String] = no
        self.volumes: typing.Final[tuple[types.Real]] = volumes

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Vol`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Vol``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Vol._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        no = types.String.from_mcnp(tokens[1]) if tokens[1] else None
        volumes = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Vol(volumes, no)
