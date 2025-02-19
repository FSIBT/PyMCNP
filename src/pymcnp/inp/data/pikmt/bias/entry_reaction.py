import re
import typing

from . import _entry
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BiasEntry_Reaction(_entry.BiasEntry_):
    """
    Represents INP data card data option pikmt entry reaction entries.

    Attributes:
        mt: MT reaction identifiers.
        pmt: MT reaction frequency control.
    """

    _REGEX = re.compile(r'( \S+)( \S+)')

    def __init__(self, mt: types.Zaid, pmt: types.Integer):
        """
        Initializes ``BiasEntry_Reaction``.

        Parameters:
            mt: MT reaction identifiers.
            pmt: MT reaction frequency control.

        Returns:
            ``BiasEntryReaction``.

        Raises:
            InpError: SEMANTICS_ENTRY_VALUE.
        """

        if mt is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, mt)
        if pmt is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, pmt)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([mt, pmt])
        self.mt: typing.Final[types.Zaid] = mt
        self.pmt: typing.Final[types.Integer] = pmt

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BiasEntry_Reaction`` from INP.

        Parameters:
            INP for ``BiasEntry_Reaction``.

        Returns:
            ``BiasEntry_Reaction``.

        Raises:
            InpError: SYNTAX_BIAS_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BiasEntry_Reaction._REGEX.match(' ' + source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_ENTRY, source)

        mt = types.Zaid.from_mcnp(tokens[1])
        pmt = types.Integer.from_mcnp(tokens[2])

        return BiasEntry_Reaction(mt, pmt)
