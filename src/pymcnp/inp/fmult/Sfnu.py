import re

from . import _option
from ... import types
from ... import errors


class Sfnu(_option.FmultOption):
    """
    Represents INP `sfnu` elements.
    """

    _KEYWORD = 'sfnu'

    _ATTRS = {
        'distribution': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Asfnu((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, distribution: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Sfnu`.

        Parameters:
            distribution: V bar for or of cumulative distribution the sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.distribution: types.Tuple(types.Real) = distribution

    @property
    def distribution(self) -> types.Tuple(types.Real):
        """
        V bar for or of cumulative distribution the sampling spontaneous fission

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._distribution

    @distribution.setter
    def distribution(self, distribution: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `distribution`.

        Parameters:
            distribution: V bar for or of cumulative distribution the sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if distribution is not None:
            array = []
            for item in distribution:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            distribution = types.Tuple(types.Real)(array)

        if distribution is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, distribution)

        self._distribution: types.Tuple(types.Real) = distribution
