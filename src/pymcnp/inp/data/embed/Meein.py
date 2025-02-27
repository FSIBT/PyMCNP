import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Meein(EmbedOption_, keyword='meein'):
    """
    Represents INP meein elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(r'meein( \S+)')

    def __init__(self, filename: types.String):
        """
        Initializes ``Meein``.

        Parameters:
            filename: Name of the EEOUT results file to read.

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
