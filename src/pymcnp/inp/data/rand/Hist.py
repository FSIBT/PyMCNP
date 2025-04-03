import re
import typing


from .option_ import RandOption_
from ....utils import types
from ....utils import errors


class Hist(RandOption_, keyword='hist'):
    """
    Represents INP hist elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'hist': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Ahist( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, hist: types.IntegerOrJump):
        """
        Initializes ``Hist``.

        Parameters:
            hist: Starting pseudorandom number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if hist is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hist)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                hist,
            ]
        )

        self.hist: typing.Final[types.IntegerOrJump] = hist
