import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Mt(DataOption_, keyword='mt'):
    """
    Represents INP mt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'identifier': types.String,
    }

    _REGEX = re.compile(r'mt(\S+)( \S+)')

    def __init__(self, suffix: types.Integer, identifier: types.String):
        """
        Initializes ``Mt``.

        Parameters:
            suffix: Data card option suffix.
            identifier: Corresponding S(α,β) identifier.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if identifier is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, identifier)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                identifier,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.identifier: typing.Final[types.String] = identifier
