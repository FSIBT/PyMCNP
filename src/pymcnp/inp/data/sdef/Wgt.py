import re

from . import _option
from ....utils import types
from ....utils import errors


class Wgt(_option.SdefOption):
    """
    Represents INP wgt elements.
    """

    _KEYWORD = 'wgt'

    _ATTRS = {
        'weight': types.Real,
    }

    _REGEX = re.compile(rf'\Awgt( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, weight: str | int | float | types.Real):
        """
        Initializes ``Wgt``.

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
        Sets ``weight``.

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
