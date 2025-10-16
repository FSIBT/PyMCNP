import re

from . import _option
from ... import types
from ... import errors


class Wgt_0(_option.SdefOption):
    """
    Represents INP `wgt` elements variation #0.
    """

    _KEYWORD = 'wgt'

    _ATTRS = {
        'weight': types.Real,
    }

    _REGEX = re.compile(rf'\Awgt( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, weight: str | int | float | types.Real):
        """
        Initializes `Wgt_0`.

        Parameters:
            weight: Particle weight.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.weight: types.Real = weight

    @property
    def weight(self) -> types.Real:
        """
        Particle weight

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._weight

    @weight.setter
    def weight(self, weight: str | int | float | types.Real) -> None:
        """
        Sets `weight`.

        Parameters:
            weight: Particle weight.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if weight is not None:
            if isinstance(weight, types.Real):
                weight = weight
            elif isinstance(weight, int) or isinstance(weight, float):
                weight = types.Real(weight)
            elif isinstance(weight, str):
                weight = types.Real.from_mcnp(weight)

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight)

        self._weight: types.Real = weight
