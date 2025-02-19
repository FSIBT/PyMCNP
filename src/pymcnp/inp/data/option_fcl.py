import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Fcl(_option.DataOption_, keyword='fcl'):
    """
    Represents INP data card fcl options.

    Attributes:
        control: Forced-collision control for cell.
        designator: Data card particle designator.
    """

    _REGEX = re.compile(r'\Afcl:(\S+?)(( \S+)+)\Z')

    def __init__(self, control: tuple[types.Real], designator: types.Designator):
        """
        Initializes ``DataOption_Fcl``.

        Parameters:
            control: Forced-collision control for cell.
            designator: Data card particle designator.

        Returns:
            ``DataOption_Fcl``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if control is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, control)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([control])
        self.control: typing.Final[tuple[types.Real]] = control
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Fcl`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Fcl``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Fcl._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        control = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Fcl(control, designator)
