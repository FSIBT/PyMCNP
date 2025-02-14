import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class Ds2Entry_Qpair(_entry.Ds2Entry_):
    """
    Represents INP data card data option qpair entries.

    Attributes:
        distribution_dependent: Distribution number for dependent variable.
    """

    _REGEX = re.compile(r'(( \S+)+)')

    def __init__(self, distribution_dependent: tuple[types.Real]):
        """
        Initializes ``Ds2Entry_Qpair``.

        Parameters:
            distribution_dependent: Distribution number for dependent variable.

        Returns:
            ``Ds2EntryQpair``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if distribution_dependent is None:
            raise errors.McnpError(
                errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, distribution_dependent
            )

        self.parameters: typing.Final[tuple[any]] = types._Tuple([distribution_dependent])
        self.distribution_dependent: typing.Final[tuple[types.Real]] = distribution_dependent

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ds2Entry_Qpair`` from INP.

        Parameters:
            INP for ``Ds2Entry_Qpair``.

        Returns:
            ``Ds2Entry_Qpair``.

        Raises:
            McnpError: SYNTAX_DS_2_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Ds2Entry_Qpair._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DS_2_ENTRY, source)

        distribution_dependent = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return Ds2Entry_Qpair(distribution_dependent)
