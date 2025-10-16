import re

from . import _option
from ... import types
from ... import errors


class Fmatny(_option.KoptsOption):
    """
    Represents INP `fmatny` elements.
    """

    _KEYWORD = 'fmatny'

    _ATTRS = {
        'fmat_ny': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatny( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, fmat_ny: str | int | float | types.Real):
        """
        Initializes `Fmatny`.

        Parameters:
            fmat_ny: fmat_ny.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fmat_ny: types.Real = fmat_ny

    @property
    def fmat_ny(self) -> types.Real:
        """
        Fmat_ny

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fmat_ny

    @fmat_ny.setter
    def fmat_ny(self, fmat_ny: str | int | float | types.Real) -> None:
        """
        Sets `fmat_ny`.

        Parameters:
            fmat_ny: fmat_ny.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fmat_ny is not None:
            if isinstance(fmat_ny, types.Real):
                fmat_ny = fmat_ny
            elif isinstance(fmat_ny, int) or isinstance(fmat_ny, float):
                fmat_ny = types.Real(fmat_ny)
            elif isinstance(fmat_ny, str):
                fmat_ny = types.Real.from_mcnp(fmat_ny)

        if fmat_ny is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_ny)

        self._fmat_ny: types.Real = fmat_ny
