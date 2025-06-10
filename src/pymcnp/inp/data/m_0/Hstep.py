import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Hstep(_option.MOption_0):
    """
    Represents INP hstep elements.

    Attributes:
        step: Number of proton sub-step per energy step.
    """

    _KEYWORD = 'hstep'

    _ATTRS = {
        'step': types.Integer,
    }

    _REGEX = re.compile(rf'\Ahstep( {types.Integer._REGEX.pattern[2:-2]})\Z')

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
class HstepBuilder(_option.MOptionBuilder_0):
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

    @staticmethod
    def unbuild(ast: Hstep):
        """
        Unbuilds ``Hstep`` into ``HstepBuilder``

        Returns:
            ``HstepBuilder`` for ``Hstep``.
        """

        return HstepBuilder(
            step=copy.deepcopy(ast.step),
        )
