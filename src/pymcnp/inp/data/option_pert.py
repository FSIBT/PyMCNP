import re
import typing

from . import pert
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Pert(_option.DataOption_, keyword='pert'):
    """
    Represents INP data card pert options.

    Attributes:
        options: Dictionary of options.
        suffix: Data card option suffix.
        designator: Data card particle designator.
    """

    _REGEX = re.compile(
        r'\Apert(\d+?):(\S+?)(( (((cell)(( \S+)+))|((mat)( \S+))|((rho)( \S+))|((method)( \S+))|((erg)( \S+)( \S+))|((rxn)(( \S+)+))))+)?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        options: tuple[pert.PertOption_] = None,
    ):
        """
        Initializes ``DataOption_Pert``.

        Parameters:
            options: Dictionary of options.
            suffix: Data card option suffix.
            designator: Data card particle designator.

        Returns:
            ``DataOption_Pert``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, pert.PertOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )
        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Pert`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Pert``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Pert._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        designator = types.Designator.from_mcnp(tokens[2])
        options = (
            types._Tuple(tuple(_parser.process_inp_option(pert.PertOption_, tokens[3])))
            if tokens[3]
            else None
        )

        return DataOption_Pert(suffix, designator, options)
