import re
import typing


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Field(BfldOption_, keyword='field'):
    """
    Represents INP field elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'strength_gradient': types.Real,
    }

    _REGEX = re.compile(r'field( \S+)')

    def __init__(self, strength_gradient: types.Real):
        """
        Initializes ``Field``.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if strength_gradient is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, strength_gradient)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                strength_gradient,
            ]
        )

        self.strength_gradient: typing.Final[types.Real] = strength_gradient
