import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Ksental(KoptsOption_, keyword='ksental'):
    """
    Represents INP ksental elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fileopt': types.String,
    }

    _REGEX = re.compile(r'ksental( \S+)')

    def __init__(self, fileopt: types.String):
        """
        Initializes ``Ksental``.

        Parameters:
            fileopt: Format of sensity profiles output file.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fileopt is None or fileopt not in {
            'mctal',
        }:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fileopt)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fileopt,
            ]
        )

        self.fileopt: typing.Final[types.String] = fileopt
