import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Nrm(SdefOption_, keyword='nrm'):
    """
    Represents INP nrm elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'sign': types.Integer,
    }

    _REGEX = re.compile(rf'\Anrm( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, sign: types.Integer):
        """
        Initializes ``Nrm``.

        Parameters:
            sign: Sign of the surface normal.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if sign is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, sign)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                sign,
            ]
        )

        self.sign: typing.Final[types.Integer] = sign
