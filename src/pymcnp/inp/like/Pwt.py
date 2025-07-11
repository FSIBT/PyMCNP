import re

from . import _option
from ...utils import types
from ...utils import errors


class Pwt(_option.LikeOption):
    """
    Represents INP pwt elements.

    Attributes:
        weight: Cell weight of photons produced at neutron collisions.
    """

    _KEYWORD = 'pwt'

    _ATTRS = {
        'weight': types.Real,
    }

    _REGEX = re.compile(rf'\Apwt( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, weight: str | int | float | types.Real):
        """
        Initializes ``Pwt``.

        Parameters:
            weight: Cell weight of photons produced at neutron collisions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.weight: types.Real = weight

    @property
    def weight(self) -> types.Real:
        """
        Gets ``weight``.

        Returns:
            ``weight``.
        """

        return self._weight

    @weight.setter
    def weight(self, weight: str | int | float | types.Real) -> None:
        """
        Sets ``weight``.

        Parameters:
            weight: Cell weight of photons produced at neutron collisions.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if weight is not None:
            if isinstance(weight, types.Real):
                weight = weight
            elif isinstance(weight, int):
                weight = types.Real(weight)
            elif isinstance(weight, float):
                weight = types.Real(weight)
            elif isinstance(weight, str):
                weight = types.Real.from_mcnp(weight)
            else:
                raise TypeError

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight)

        self._weight: types.Real = weight
