import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Estep(_option.MOption_0):
    """
    Represents INP estep elements.

    Attributes:
        step: Number of electron sub-step per energy step.
    """

    _KEYWORD = 'estep'

    _ATTRS = {
        'step': types.Integer,
    }

    _REGEX = re.compile(rf'\Aestep( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, step: types.Integer):
        """
        Initializes ``Estep``.

        Parameters:
            step: Number of electron sub-step per energy step.

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
class EstepBuilder(_option.MOptionBuilder_0):
    """
    Builds ``Estep``.

    Attributes:
        step: Number of electron sub-step per energy step.
    """

    step: str | int | types.Integer

    def build(self):
        """
        Builds ``EstepBuilder`` into ``Estep``.

        Returns:
            ``Estep`` for ``EstepBuilder``.
        """

        step = self.step
        if isinstance(self.step, types.Integer):
            step = self.step
        elif isinstance(self.step, int):
            step = types.Integer(self.step)
        elif isinstance(self.step, str):
            step = types.Integer.from_mcnp(self.step)

        return Estep(
            step=step,
        )

    @staticmethod
    def unbuild(ast: Estep):
        """
        Unbuilds ``Estep`` into ``EstepBuilder``

        Returns:
            ``EstepBuilder`` for ``Estep``.
        """

        return EstepBuilder(
            step=copy.deepcopy(ast.step),
        )
