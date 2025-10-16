import re

from . import _option
from ... import types
from ... import errors


class Cz(_option.SurfaceOption):
    """
    Represents INP `cz` elements.
    """

    _KEYWORD = 'cz'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Acz( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, r: str | int | float | types.Real):
        """
        Initializes `Cz`.

        Parameters:
            r: On-z-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.r: types.Real = r

    @property
    def r(self) -> types.Real:
        """
        On-z-axis cylinder radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r

    @r.setter
    def r(self, r: str | int | float | types.Real) -> None:
        """
        Sets `r`.

        Parameters:
            r: On-z-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r is not None:
            if isinstance(r, types.Real):
                r = r
            elif isinstance(r, int) or isinstance(r, float):
                r = types.Real(r)
            elif isinstance(r, str):
                r = types.Real.from_mcnp(r)

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self._r: types.Real = r
