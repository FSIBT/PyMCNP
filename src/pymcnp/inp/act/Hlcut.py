import re

from . import _option
from ... import types
from ... import errors


class Hlcut(_option.ActOption):
    """
    Represents INP `hlcut` elements.
    """

    _KEYWORD = 'hlcut'

    _ATTRS = {
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Ahlcut( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, cutoff: str | int | float | types.Real):
        """
        Initializes `Hlcut`.

        Parameters:
            cutoff: Spontaneous-decay half-life threshold.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cutoff: types.Real = cutoff

    @property
    def cutoff(self) -> types.Real:
        """
        Spontaneous-decay half-life threshold

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cutoff

    @cutoff.setter
    def cutoff(self, cutoff: str | int | float | types.Real) -> None:
        """
        Sets `cutoff`.

        Parameters:
            cutoff: Spontaneous-decay half-life threshold.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cutoff is not None:
            if isinstance(cutoff, types.Real):
                cutoff = cutoff
            elif isinstance(cutoff, int) or isinstance(cutoff, float):
                cutoff = types.Real(cutoff)
            elif isinstance(cutoff, str):
                cutoff = types.Real.from_mcnp(cutoff)

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff)

        self._cutoff: types.Real = cutoff
