import re

from . import _option
from ....utils import types
from ....utils import errors


class Nps(_option.StopOption):
    """
    Represents INP nps elements.

    Attributes:
        npp: Total number of histories before stop.
        npsmg: Number of histories before stop.
    """

    _KEYWORD = 'nps'

    _ATTRS = {
        'npp': types.Integer,
        'npsmg': types.Integer,
    }

    _REGEX = re.compile(rf'\Anps( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, npp: str | int | types.Integer, npsmg: str | int | types.Integer = None):
        """
        Initializes ``Nps``.

        Parameters:
            npp: Total number of histories before stop.
            npsmg: Number of histories before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.npp: types.Integer = npp
        self.npsmg: types.Integer = npsmg

    @property
    def npp(self) -> types.Integer:
        """
        Gets ``npp``.

        Returns:
            ``npp``.
        """

        return self._npp

    @npp.setter
    def npp(self, npp: str | int | types.Integer) -> None:
        """
        Sets ``npp``.

        Parameters:
            npp: Total number of histories before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if npp is not None:
            if isinstance(npp, types.Integer):
                npp = npp
            elif isinstance(npp, int):
                npp = types.Integer(npp)
            elif isinstance(npp, str):
                npp = types.Integer.from_mcnp(npp)
            else:
                raise TypeError

        if npp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, npp)

        self._npp: types.Integer = npp

    @property
    def npsmg(self) -> types.Integer:
        """
        Gets ``npsmg``.

        Returns:
            ``npsmg``.
        """

        return self._npsmg

    @npsmg.setter
    def npsmg(self, npsmg: str | int | types.Integer) -> None:
        """
        Sets ``npsmg``.

        Parameters:
            npsmg: Number of histories before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if npsmg is not None:
            if isinstance(npsmg, types.Integer):
                npsmg = npsmg
            elif isinstance(npsmg, int):
                npsmg = types.Integer(npsmg)
            elif isinstance(npsmg, str):
                npsmg = types.Integer.from_mcnp(npsmg)
            else:
                raise TypeError

        self._npsmg: types.Integer = npsmg
