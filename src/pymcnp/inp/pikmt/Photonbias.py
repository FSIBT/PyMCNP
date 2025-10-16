import re

from . import _entry
from ... import types
from ... import errors


class Photonbias(_entry.PikmtEntry):
    """
    Represents INP `photonbias` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'zaid': types.Zaid,
        'ipiki': types.Integer,
    }

    _REGEX = re.compile(rf'\A({types.Zaid._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, zaid: str | types.Zaid, ipiki: str | int | types.Integer):
        """
        Initializes `Photonbias`.

        Parameters:
            zaid: Bias nuclide identifier.
            ipiki: Bias controls.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.zaid: types.Zaid = zaid
        self.ipiki: types.Integer = ipiki

    @property
    def zaid(self) -> types.Zaid:
        """
        Bias nuclide identifier

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._zaid

    @zaid.setter
    def zaid(self, zaid: str | types.Zaid) -> None:
        """
        Sets `zaid`.

        Parameters:
            zaid: Bias nuclide identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if zaid is not None:
            if isinstance(zaid, types.Zaid):
                zaid = zaid
            elif isinstance(zaid, str):
                zaid = types.Zaid.from_mcnp(zaid)

        if zaid is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaid)

        self._zaid: types.Zaid = zaid

    @property
    def ipiki(self) -> types.Integer:
        """
        Bias controls

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ipiki

    @ipiki.setter
    def ipiki(self, ipiki: str | int | types.Integer) -> None:
        """
        Sets `ipiki`.

        Parameters:
            ipiki: Bias controls.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ipiki is not None:
            if isinstance(ipiki, types.Integer):
                ipiki = ipiki
            elif isinstance(ipiki, int):
                ipiki = types.Integer(ipiki)
            elif isinstance(ipiki, str):
                ipiki = types.Integer.from_mcnp(ipiki)

        if ipiki is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ipiki)

        self._ipiki: types.Integer = ipiki
