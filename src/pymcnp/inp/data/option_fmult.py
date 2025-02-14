import re
import typing

from . import fmult
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Fmult(_option.DataOption_, keyword='fmult'):
    """
    Represents INP data card fmult options.

    Attributes:
        zaid: Nuclide for which data are entered.
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Afmult( \S+)(( (((width)( \S+))|((sfyield)( \S+))|((watt)( \S+)( \S+))|((method)( \S+))|((data)( \S+))|((shift)( \S+))))+)?\Z'
    )

    def __init__(self, zaid: types.Zaid, options: tuple[fmult.FmultOption_] = None):
        """
        Initializes ``DataOption_Fmult``.

        Parameters:
            zaid: Nuclide for which data are entered.
            options: Dictionary of options.

        Returns:
            ``DataOption_Fmult``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, zaid)

        self.value: typing.Final[tuple[any]] = types._Tuple([zaid, options])
        self.zaid: typing.Final[types.Zaid] = zaid
        self.options: typing.Final[dict[str, fmult.FmultOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Fmult`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Fmult``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Fmult._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        zaid = types.Zaid.from_mcnp(tokens[1])
        options = (
            types._Tuple(tuple(_parser.process_inp_option(fmult.FmultOption_, tokens[2])))
            if tokens[2]
            else None
        )

        return DataOption_Fmult(zaid, options)
