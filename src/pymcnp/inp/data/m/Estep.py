import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Estep(MOption_, keyword='estep'):
    """
    Represents INP estep elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'step': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aestep( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, step: types.IntegerOrJump):
        """
        Initializes ``Estep``.

        Parameters:
            step: Number of electron sub-step per energy step.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if step is None or not (step >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, step)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                step,
            ]
        )

        self.step: typing.Final[types.IntegerOrJump] = step
