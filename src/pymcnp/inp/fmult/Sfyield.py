import re

from . import _option
from ... import types
from ... import errors


class Sfyield(_option.FmultOption):
    """
    Represents INP `sfyield` elements.
    """

    _KEYWORD = 'sfyield'

    _ATTRS = {
        'fission_yield': types.Real,
    }

    _REGEX = re.compile(rf'\Asfyield( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, fission_yield: str | int | float | types.Real):
        """
        Initializes `Sfyield`.

        Parameters:
            fission_yield: Spontaneous fission yield.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fission_yield: types.Real = fission_yield

    @property
    def fission_yield(self) -> types.Real:
        """
        Spontaneous fission yield

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fission_yield

    @fission_yield.setter
    def fission_yield(self, fission_yield: str | int | float | types.Real) -> None:
        """
        Sets `fission_yield`.

        Parameters:
            fission_yield: Spontaneous fission yield.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fission_yield is not None:
            if isinstance(fission_yield, types.Real):
                fission_yield = fission_yield
            elif isinstance(fission_yield, int) or isinstance(fission_yield, float):
                fission_yield = types.Real(fission_yield)
            elif isinstance(fission_yield, str):
                fission_yield = types.Real.from_mcnp(fission_yield)

        if fission_yield is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fission_yield)

        self._fission_yield: types.Real = fission_yield
