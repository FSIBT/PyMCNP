import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Buffer(_option.PtracOption_, keyword='buffer'):
    """
    Represents INP data card data option buffer options.

    Attributes:
        storage: Amount of storage available for filtered events.
    """

    _REGEX = re.compile(r'\Abuffer( \S+)\Z')

    def __init__(self, storage: types.Integer):
        """
        Initializes ``PtracOption_Buffer``.

        Parameters:
            storage: Amount of storage available for filtered events.

        Returns:
            ``PtracOption_Buffer``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if storage is None or not (storage > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, storage)

        self.value: typing.Final[tuple[any]] = types._Tuple([storage])
        self.storage: typing.Final[types.Integer] = storage

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Buffer`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Buffer``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Buffer._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        storage = types.Integer.from_mcnp(tokens[1])

        return PtracOption_Buffer(storage)
