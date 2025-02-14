import re
import typing


from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class TrEntry_Displacement(_entry.TrEntry_):
    """
    Represents INP data card data option displacement entries.

    Attributes:
        x: Displacement vector x component.
        y: Displacement vector y component.
        z: Displacement vector z component.
    """

    _REGEX = re.compile(r'((?:\A)\S+)((?: )\S+)((?: )\S+)(?:\Z)')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``TrEntry_Displacement``.

        Parameters:
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.

        Returns:
            ``TrEntryDisplacement``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_ENTRY_VALUE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_ENTRY_VALUE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_ENTRY_VALUE, z)

        self.parameters: typing.Final[tuple[any]] = tuple([x, y, z])
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TrEntry_Displacement`` from INP.

        Parameters:
            INP for ``TrEntry_Displacement``.

        Returns:
            ``TrEntry_Displacement``.

        Raises:
            McnpError: SYNTAX_TR_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = TrEntry_Displacement._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TR_ENTRY, source)

        x = types.Real.from_mcnp(tokens[1].strip())
        y = types.Real.from_mcnp(tokens[2].strip())
        z = types.Real.from_mcnp(tokens[3].strip())

        return TrEntry_Displacement(x, y, z)
