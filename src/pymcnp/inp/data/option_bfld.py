import re
import typing

from . import bfld
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Bfld(_option.DataOption_, keyword='bfld'):
    """
    Represents INP data card bfld options.

    Attributes:
        kind: Magnetic field type.
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Abfld(\d+?)( \S+)(( (((field)( \S+))|((vec)(( \S+)+))|((maxdeflc)( \S+))|((maxstep)( \S+))|((axs)(( \S+)+))|((ffedges)(( \S+)+))|((refpnt)(( \S+)+))))+)?\Z'
    )

    def __init__(
        self, kind: types.String, suffix: types.Integer, options: tuple[bfld.BfldOption_] = None
    ):
        """
        Initializes ``DataOption_Bfld``.

        Parameters:
            kind: Magnetic field type.
            suffix: Data card option suffix.
            options: Dictionary of options.

        Returns:
            ``DataOption_Bfld``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None or type not in {'const', 'quad', 'quadff'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)
        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([kind, options])
        self.kind: typing.Final[types.String] = kind
        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[dict[str, bfld.BfldOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Bfld`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Bfld``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Bfld._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        kind = types.String.from_mcnp(tokens[2])
        options = (
            types._Tuple(tuple(_parser.process_inp_option(bfld.BfldOption_, tokens[4])))
            if tokens[4]
            else None
        )

        return DataOption_Bfld(kind, suffix, options)
