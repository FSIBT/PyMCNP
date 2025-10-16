import re

from . import _option
from ... import types
from ... import errors


class Hstep(_option.MOption_0):
    """
    Represents INP `hstep` elements.
    """

    _KEYWORD = 'hstep'

    _ATTRS = {
        'step': types.Integer,
    }

    _REGEX = re.compile(rf'\Ahstep( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, step: str | int | types.Integer):
        """
        Initializes `Hstep`.

        Parameters:
            step: Number of proton sub-step per energy step.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.step: types.Integer = step

    @property
    def step(self) -> types.Integer:
        """
        Number of proton sub-step per energy step

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
            step: Number of proton sub-step per energy step.

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
