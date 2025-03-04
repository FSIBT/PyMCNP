import re
import typing


from .option_ import Df_1Option_
from ....utils import types
from ....utils import errors


class Int(Df_1Option_, keyword='int'):
    """
    Represents INP int elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'interpolation': types.String,
    }

    _REGEX = re.compile(r'int( \S+)')

    def __init__(self, interpolation: types.String):
        """
        Initializes ``Int``.

        Parameters:
            interpolation: Energy interpolation.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if interpolation is None or interpolation not in {'log', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, interpolation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                interpolation,
            ]
        )

        self.interpolation: typing.Final[types.String] = interpolation
