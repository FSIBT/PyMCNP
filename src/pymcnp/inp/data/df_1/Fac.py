import re
import typing


from .option_ import Df_1Option_
from ....utils import types
from ....utils import errors


class Fac(Df_1Option_, keyword='fac'):
    """
    Represents INP fac elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'normalization': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Afac( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, normalization: types.IntegerOrJump):
        """
        Initializes ``Fac``.

        Parameters:
            normalization: Normalization factor for dose.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if normalization is None or not (normalization >= -3):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, normalization)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                normalization,
            ]
        )

        self.normalization: typing.Final[types.IntegerOrJump] = normalization
