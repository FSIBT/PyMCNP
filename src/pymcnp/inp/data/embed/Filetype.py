import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Filetype(EmbedOption_, keyword='filetype'):
    """
    Represents INP filetype elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'filetype( {types.String._REGEX.pattern})')

    def __init__(self, kind: types.String):
        """
        Initializes ``Filetype``.

        Parameters:
            kind: File type for the elemental edit output file.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None or type not in {'ascii', 'binary'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind
