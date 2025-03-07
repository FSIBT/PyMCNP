import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Meeout(EmbedOption_, keyword='meeout'):
    """
    Represents INP meeout elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'meeout( {types.String._REGEX.pattern})')

    def __init__(self, filename: types.String):
        """
        Initializes ``Meeout``.

        Parameters:
            filename: Name assigned to EEOUT, the elemental edit output file.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if filename is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, filename)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                filename,
            ]
        )

        self.filename: typing.Final[types.String] = filename
