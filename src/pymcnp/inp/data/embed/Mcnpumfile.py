import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Mcnpumfile(EmbedOption_, keyword='mcnpumfile'):
    """
    Represents INP mcnpumfile elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(r'mcnpumfile( \S+)')

    def __init__(self, filename: types.String):
        """
        Initializes ``Mcnpumfile``.

        Parameters:
            filename: Name of the MCNPUM output file.

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
