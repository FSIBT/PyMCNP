import re
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Hstep(MOption_0):
    """
    Represents INP hstep elements.

    Attributes:
        step: Number of proton sub-step per energy step.
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
            InpError: SEMANTICS_OPTION.
        """

        if step is None or not (step.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, step)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                step,
            ]
        )

        self.step: typing.Final[types.Integer] = step


@dataclasses.dataclass
class HstepBuilder:
    """
    Builds ``Hstep``.

    Attributes:
        step: Number of proton sub-step per energy step.
    """

    step: str | int | types.Integer

    def build(self):
        """
        Builds ``HstepBuilder`` into ``Hstep``.

        Returns:
            ``Hstep`` for ``HstepBuilder``.
        """

        step = self.step
        if isinstance(self.step, types.Integer):
            step = self.step
        elif isinstance(self.step, int):
            step = types.Integer(self.step)
        elif isinstance(self.step, str):
            step = types.Integer.from_mcnp(self.step)

        return Hstep(
            step=step,
        )
