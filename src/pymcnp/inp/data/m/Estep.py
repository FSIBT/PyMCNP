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
        'step': types.Integer,
    }

    _REGEX = re.compile(rf'estep( {types.Integer._REGEX.pattern})')

    def __init__(self, step: types.Integer):
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

        self.step: typing.Final[types.Integer] = step
