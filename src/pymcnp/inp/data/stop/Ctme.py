import re

from . import _option
from ....utils import types
from ....utils import errors


class Ctme(_option.StopOption):
    """
    Represents INP ctme elements.

    Attributes:
        tme: Computer time before stop.
    """

    _KEYWORD = 'ctme'

    _ATTRS = {
        'tme': types.Real,
    }

    _REGEX = re.compile(rf'\Actme( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, tme: str | int | float | types.Real):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: Computer time before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.tme: types.Real = tme

    @property
    def tme(self) -> types.Real:
        """
        Gets ``tme``.

        Returns:
            ``tme``.
        """

        return self._tme

    @tme.setter
    def tme(self, tme: str | int | float | types.Real) -> None:
        """
        Sets ``tme``.

        Parameters:
            tme: Computer time before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if tme is not None:
            if isinstance(tme, types.Real):
                tme = tme
            elif isinstance(tme, int):
                tme = types.Real(tme)
            elif isinstance(tme, float):
                tme = types.Real(tme)
            elif isinstance(tme, str):
                tme = types.Real.from_mcnp(tme)
            else:
                raise TypeError

        if tme is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tme)

        self._tme: types.Real = tme
