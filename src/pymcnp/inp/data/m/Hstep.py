import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Hstep(MOption_, keyword='hstep'):
    """
    Represents INP hstep elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'step': types.Integer,
    }

    _REGEX = re.compile(rf'\Ahstep( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, step: types.Integer):
        """
        Initializes ``Hstep``.

        Parameters:
            step: Number of proton sub-step per energy step.

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
