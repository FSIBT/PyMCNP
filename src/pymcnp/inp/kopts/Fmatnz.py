import re

from . import _option
from ... import types
from ... import errors


class Fmatnz(_option.KoptsOption):
    """
    Represents INP `fmatnz` elements.
    """

    _KEYWORD = 'fmatnz'

    _ATTRS = {
        'fmat_nz': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatnz( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, fmat_nz: str | int | float | types.Real):
        """
        Initializes `Fmatnz`.

        Parameters:
            fmat_nz: fmat_nz.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fmat_nz: types.Real = fmat_nz

    @property
    def fmat_nz(self) -> types.Real:
        """
        Fmat_nz

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fmat_nz

    @fmat_nz.setter
    def fmat_nz(self, fmat_nz: str | int | float | types.Real) -> None:
        """
        Sets `fmat_nz`.

        Parameters:
            fmat_nz: fmat_nz.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fmat_nz is not None:
            if isinstance(fmat_nz, types.Real):
                fmat_nz = fmat_nz
            elif isinstance(fmat_nz, int) or isinstance(fmat_nz, float):
                fmat_nz = types.Real(fmat_nz)
            elif isinstance(fmat_nz, str):
                fmat_nz = types.Real.from_mcnp(fmat_nz)

        if fmat_nz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_nz)

        self._fmat_nz: types.Real = fmat_nz
