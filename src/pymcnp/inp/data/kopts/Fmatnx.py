import re

from . import _option
from ....utils import types
from ....utils import errors


class Fmatnx(_option.KoptsOption):
    """
    Represents INP fmatnx elements.

    Attributes:
        fmat_nx: fmat_nx.
    """

    _KEYWORD = 'fmatnx'

    _ATTRS = {
        'fmat_nx': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatnx( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fmat_nx: str | int | float | types.Real):
        """
        Initializes ``Fmatnx``.

        Parameters:
            fmat_nx: fmat_nx.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fmat_nx: types.Real = fmat_nx

    @property
    def fmat_nx(self) -> types.Real:
        """
        Gets ``fmat_nx``.

        Returns:
            ``fmat_nx``.
        """

        return self._fmat_nx

    @fmat_nx.setter
    def fmat_nx(self, fmat_nx: str | int | float | types.Real) -> None:
        """
        Sets ``fmat_nx``.

        Parameters:
            fmat_nx: fmat_nx.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fmat_nx is not None:
            if isinstance(fmat_nx, types.Real):
                fmat_nx = fmat_nx
            elif isinstance(fmat_nx, int):
                fmat_nx = types.Real(fmat_nx)
            elif isinstance(fmat_nx, float):
                fmat_nx = types.Real(fmat_nx)
            elif isinstance(fmat_nx, str):
                fmat_nx = types.Real.from_mcnp(fmat_nx)
            else:
                raise TypeError

        if fmat_nx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_nx)

        self._fmat_nx: types.Real = fmat_nx
