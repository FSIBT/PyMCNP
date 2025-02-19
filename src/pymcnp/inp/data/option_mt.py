import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Mt(_option.DataOption_, keyword='mt'):
    """
    Represents INP data card mt options.

    Attributes:
        identifier: Corresponding S(α,β) identifier.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Amt(\d+?)( \S+)\Z')

    def __init__(self, identifier: types.String, suffix: types.Integer):
        """
        Initializes ``DataOption_Mt``.

        Parameters:
            identifier: Corresponding S(α,β) identifier.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Mt``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if identifier is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, identifier)
        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([identifier])
        self.identifier: typing.Final[types.String] = identifier
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Mt`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Mt``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Mt._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        identifier = types.String.from_mcnp(tokens[2])

        return DataOption_Mt(identifier, suffix)
