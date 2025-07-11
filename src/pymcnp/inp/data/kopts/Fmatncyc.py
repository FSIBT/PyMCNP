import re

from . import _option
from ....utils import types
from ....utils import errors


class Fmatncyc(_option.KoptsOption):
    """
    Represents INP fmatncyc elements.

    Attributes:
        fmat_ncyc: fmat_ncyc.
    """

    _KEYWORD = 'fmatncyc'

    _ATTRS = {
        'fmat_ncyc': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatncyc( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fmat_ncyc: str | int | float | types.Real):
        """
        Initializes ``Fmatncyc``.

        Parameters:
            fmat_ncyc: fmat_ncyc.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fmat_ncyc: types.Real = fmat_ncyc

    @property
    def fmat_ncyc(self) -> types.Real:
        """
        Gets ``fmat_ncyc``.

        Returns:
            ``fmat_ncyc``.
        """

        return self._fmat_ncyc

    @fmat_ncyc.setter
    def fmat_ncyc(self, fmat_ncyc: str | int | float | types.Real) -> None:
        """
        Sets ``fmat_ncyc``.

        Parameters:
            fmat_ncyc: fmat_ncyc.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fmat_ncyc is not None:
            if isinstance(fmat_ncyc, types.Real):
                fmat_ncyc = fmat_ncyc
            elif isinstance(fmat_ncyc, int):
                fmat_ncyc = types.Real(fmat_ncyc)
            elif isinstance(fmat_ncyc, float):
                fmat_ncyc = types.Real(fmat_ncyc)
            elif isinstance(fmat_ncyc, str):
                fmat_ncyc = types.Real.from_mcnp(fmat_ncyc)
            else:
                raise TypeError

        if fmat_ncyc is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_ncyc)

        self._fmat_ncyc: types.Real = fmat_ncyc
