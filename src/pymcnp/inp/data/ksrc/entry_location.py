import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KsrcEntry_Location(_entry.KsrcEntry_):
    """
    Represents INP data card data option location entries.

    Attributes:
        x: Location x-coordinate.
        y: Location y-coordinate.
        z: Location z-coordinate.
    """

    _REGEX = re.compile(r'( \S+)( \S+)( \S+)')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``KsrcEntry_Location``.

        Parameters:
            x: Location x-coordinate.
            y: Location y-coordinate.
            z: Location z-coordinate.

        Returns:
            ``KsrcEntryLocation``.

        Raises:
            InpError: SEMANTICS_ENTRY_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, z)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([x, y, z])
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KsrcEntry_Location`` from INP.

        Parameters:
            INP for ``KsrcEntry_Location``.

        Returns:
            ``KsrcEntry_Location``.

        Raises:
            InpError: SYNTAX_KSRC_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KsrcEntry_Location._REGEX.match(' ' + source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_ENTRY, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])

        return KsrcEntry_Location(x, y, z)
