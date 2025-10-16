import re

from . import _option
from ... import types
from ... import errors


class Fmatnx(_option.KoptsOption):
    """
    Represents INP `fmatnx` elements.
    """

    _KEYWORD = 'fmatnx'

    _ATTRS = {
        'fmat_nx': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatnx( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, fmat_nx: str | int | float | types.Real):
        """
        Initializes `Fmatnx`.

        Parameters:
            fmat_nx: fmat_nx.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fmat_nx: types.Real = fmat_nx

    @property
    def fmat_nx(self) -> types.Real:
        """
        Fmat_nx

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fmat_nx

    @fmat_nx.setter
    def fmat_nx(self, fmat_nx: str | int | float | types.Real) -> None:
        """
        Sets `fmat_nx`.

        Parameters:
            fmat_nx: fmat_nx.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fmat_nx is not None:
            if isinstance(fmat_nx, types.Real):
                fmat_nx = fmat_nx
            elif isinstance(fmat_nx, int) or isinstance(fmat_nx, float):
                fmat_nx = types.Real(fmat_nx)
            elif isinstance(fmat_nx, str):
                fmat_nx = types.Real.from_mcnp(fmat_nx)

        if fmat_nx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_nx)

        self._fmat_nx: types.Real = fmat_nx
