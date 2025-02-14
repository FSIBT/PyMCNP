import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class Ds1Entry_Tpair(_entry.Ds1Entry_):
    """
    Represents INP data card data option tpair entries.

    Attributes:
        independent: Independent source dependent variable.
        dependent: Dependent source dependent variable.
    """

    _REGEX = re.compile(r'( \S+)( \S+)')

    def __init__(self, independent: types.Real, dependent: types.Real):
        """
        Initializes ``Ds1Entry_Tpair``.

        Parameters:
            independent: Independent source dependent variable.
            dependent: Dependent source dependent variable.

        Returns:
            ``Ds1EntryTpair``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if independent is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, independent)
        if dependent is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, dependent)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([independent, dependent])
        self.independent: typing.Final[types.Real] = independent
        self.dependent: typing.Final[types.Real] = dependent

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ds1Entry_Tpair`` from INP.

        Parameters:
            INP for ``Ds1Entry_Tpair``.

        Returns:
            ``Ds1Entry_Tpair``.

        Raises:
            McnpError: SYNTAX_DS_1_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Ds1Entry_Tpair._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DS_1_ENTRY, source)

        independent = types.Real.from_mcnp(tokens[1])
        dependent = types.Real.from_mcnp(tokens[2])

        return Ds1Entry_Tpair(independent, dependent)
