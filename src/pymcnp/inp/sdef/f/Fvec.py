import re

from . import _option
from .... import types
from .... import errors


class Fvec(_option.FOption):
    """
    Represents INP `fvec` elements.
    """

    _KEYWORD = 'fvec'

    _ATTRS = {
        'distribution': types.Distribution,
    }

    _REGEX = re.compile(rf'\Afvec( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, distribution: str | types.Distribution):
        """
        Initializes `Fvec`.

        Parameters:
            distribution: Dependent distribution.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.distribution: types.Distribution = distribution

    @property
    def distribution(self) -> types.Distribution:
        """
        Dependent distribution

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._distribution

    @distribution.setter
    def distribution(self, distribution: str | types.Distribution) -> None:
        """
        Sets `distribution`.

        Parameters:
            distribution: Dependent distribution.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if distribution is not None:
            if isinstance(distribution, types.Distribution):
                distribution = distribution
            elif isinstance(distribution, str):
                distribution = types.Distribution.from_mcnp(distribution)

        if distribution is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, distribution)

        self._distribution: types.Distribution = distribution
