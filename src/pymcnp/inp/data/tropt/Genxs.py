import re
import typing


from .option_ import TroptOption_
from ....utils import types
from ....utils import errors


class Genxs(TroptOption_, keyword='genxs'):
    """
    Represents INP genxs elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'genxs( {types.String._REGEX.pattern})')

    def __init__(self, filename: types.String):
        """
        Initializes ``Genxs``.

        Parameters:
            filename: Cross section generation setting.

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
