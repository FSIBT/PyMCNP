import re
import typing
import dataclasses


from ._option import MOption
from ....utils import types
from ....utils import errors


class Estep(MOption, keyword='estep'):
    """
    Represents INP estep elements.

    Attributes:
        step: Number of electron sub-step per energy step.
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
            InpError: SEMANTICS_OPTION.
        """

        if step is None or not (step >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, step)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                step,
            ]
        )

        self.step: typing.Final[types.IntegerOrJump] = step


@dataclasses.dataclass
class EstepBuilder:
    """
    Builds ``Estep``.

    Attributes:
        step: Number of electron sub-step per energy step.
    """

    step: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``EstepBuilder`` into ``Estep``.

        Returns:
            ``Estep`` for ``EstepBuilder``.
        """

        if isinstance(self.step, types.Integer):
            step = self.step
        elif isinstance(self.step, int):
            step = types.IntegerOrJump(self.step)
        elif isinstance(self.step, str):
            step = types.IntegerOrJump.from_mcnp(self.step)

        return Estep(
            step=step,
        )
