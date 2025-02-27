import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Blocksize(KoptsOption_, keyword='blocksize'):
    """
    Represents INP blocksize elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'ncy': types.Integer,
    }

    _REGEX = re.compile(r'blocksize( \S+)')

    def __init__(self, ncy: types.Integer):
        """
        Initializes ``Blocksize``.

        Parameters:
            ncy: Number of cycles in every outer iteration.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ncy is None or not (ncy >= 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ncy)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ncy,
            ]
        )

        self.ncy: typing.Final[types.Integer] = ncy
