import re

from . import _option
from ... import types
from ... import errors


class Estep(_option.MOption_0):
    """
    Represents INP `estep` elements.
    """

    _KEYWORD = 'estep'

    _ATTRS = {
        'step': types.Integer,
    }

    _REGEX = re.compile(rf'\Aestep( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, step: str | int | types.Integer):
        """
        Initializes `Estep`.

        Parameters:
            step: Number of electron sub-step per energy step.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.step: types.Integer = step

    @property
    def step(self) -> types.Integer:
        """
        Number of electron sub-step per energy step

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._step

    @step.setter
    def step(self, step: str | int | types.Integer) -> None:
        """
        Sets `step`.

        Parameters:
            step: Number of electron sub-step per energy step.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if step is not None:
            if isinstance(step, types.Integer):
                step = step
            elif isinstance(step, int):
                step = types.Integer(step)
            elif isinstance(step, str):
                step = types.Integer.from_mcnp(step)

        if step is None or not (step >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, step)

        self._step: types.Integer = step
