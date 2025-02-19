import re
import typing

from . import bias
from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PikmtEntry_Bias(_entry.PikmtEntry_):
    """
    Represents INP data card data option bias entries.

    Attributes:
        zaid: Bias nuclide identifier.
        ipiki: Bias controls.
        reactions: Bias MT reactions.
    """

    _REGEX = re.compile(r'( \S+)( \S+)((( \S+)( \S+))+)')

    def __init__(
        self, zaid: types.Zaid, ipiki: types.Integer, reactions: tuple[bias.BiasEntry_Reaction]
    ):
        """
        Initializes ``PikmtEntry_Bias``.

        Parameters:
            zaid: Bias nuclide identifier.
            ipiki: Bias controls.
            reactions: Bias MT reactions.

        Returns:
            ``PikmtEntryBias``.

        Raises:
            InpError: SEMANTICS_ENTRY_VALUE.
        """

        if zaid is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, zaid)
        if ipiki is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, ipiki)
        if reactions is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, reactions)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([zaid, ipiki, reactions])
        self.zaid: typing.Final[types.Zaid] = zaid
        self.ipiki: typing.Final[types.Integer] = ipiki
        self.reactions: typing.Final[tuple[bias.BiasEntry_Reaction]] = reactions

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PikmtEntry_Bias`` from INP.

        Parameters:
            INP for ``PikmtEntry_Bias``.

        Returns:
            ``PikmtEntry_Bias``.

        Raises:
            InpError: SYNTAX_PIKMT_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PikmtEntry_Bias._REGEX.match(' ' + source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_ENTRY, source)

        zaid = types.Zaid.from_mcnp(tokens[1])
        ipiki = types.Integer.from_mcnp(tokens[2])
        reactions = types._Tuple(
            [
                bias.BiasEntry_Reaction.from_mcnp(token[0])
                for token in bias.BiasEntry_Reaction._REGEX.finditer(tokens[3])
            ]
        )

        return PikmtEntry_Bias(zaid, ipiki, reactions)
