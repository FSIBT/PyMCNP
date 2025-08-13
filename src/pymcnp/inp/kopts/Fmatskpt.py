import re

from . import _option
from ... import types
from ... import errors


class Fmatskpt(_option.KoptsOption):
    """
    Represents INP `fmatskpt` elements.
    """

    _KEYWORD = 'fmatskpt'

    _ATTRS = {
        'fmat_skip': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatskpt( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, fmat_skip: str | int | float | types.Real):
        """
        Initializes `Fmatskpt`.

        Parameters:
            fmat_skip: fmat_skip.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fmat_skip: types.Real = fmat_skip

    @property
    def fmat_skip(self) -> types.Real:
        """
        Fmat_skip

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fmat_skip

    @fmat_skip.setter
    def fmat_skip(self, fmat_skip: str | int | float | types.Real) -> None:
        """
        Sets `fmat_skip`.

        Parameters:
            fmat_skip: fmat_skip.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fmat_skip is not None:
            if isinstance(fmat_skip, types.Real):
                fmat_skip = fmat_skip
            elif isinstance(fmat_skip, int) or isinstance(fmat_skip, float):
                fmat_skip = types.Real(fmat_skip)
            elif isinstance(fmat_skip, str):
                fmat_skip = types.Real.from_mcnp(fmat_skip)

        if fmat_skip is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_skip)

        self._fmat_skip: types.Real = fmat_skip
