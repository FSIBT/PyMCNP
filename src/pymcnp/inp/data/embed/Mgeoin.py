import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Mgeoin(EmbedOption_, keyword='mgeoin'):
    """
    Represents INP mgeoin elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'mgeoin( {types.String._REGEX.pattern})')

    def __init__(self, filename: types.String):
        """
        Initializes ``Mgeoin``.

        Parameters:
            filename: Name of the input file containing the mesh description.

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
