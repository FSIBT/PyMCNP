import re

from . import _option
from ... import types
from ... import errors


class Fmatspace(_option.KoptsOption):
    """
    Represents INP `fmatspace` elements.
    """

    _KEYWORD = 'fmatspace'

    _ATTRS = {
        'fmat_space': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatspace( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, fmat_space: str | int | float | types.Real):
        """
        Initializes `Fmatspace`.

        Parameters:
            fmat_space: fmat_space.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fmat_space: types.Real = fmat_space

    @property
    def fmat_space(self) -> types.Real:
        """
        Fmat_space

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fmat_space

    @fmat_space.setter
    def fmat_space(self, fmat_space: str | int | float | types.Real) -> None:
        """
        Sets `fmat_space`.

        Parameters:
            fmat_space: fmat_space.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fmat_space is not None:
            if isinstance(fmat_space, types.Real):
                fmat_space = fmat_space
            elif isinstance(fmat_space, int) or isinstance(fmat_space, float):
                fmat_space = types.Real(fmat_space)
            elif isinstance(fmat_space, str):
                fmat_space = types.Real.from_mcnp(fmat_space)

        if fmat_space is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_space)

        self._fmat_space: types.Real = fmat_space
