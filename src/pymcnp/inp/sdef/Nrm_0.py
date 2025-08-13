import re

from . import _option
from ... import types
from ... import errors


class Nrm_0(_option.SdefOption):
    """
    Represents INP `nrm` elements variation #0.
    """

    _KEYWORD = 'nrm'

    _ATTRS = {
        'sign': types.Integer,
    }

    _REGEX = re.compile(rf'\Anrm( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, sign: str | int | types.Integer):
        """
        Initializes `Nrm_0`.

        Parameters:
            sign: Sign of the surface normal.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.sign: types.Integer = sign

    @property
    def sign(self) -> types.Integer:
        """
        Sign of the surface normal

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._sign

    @sign.setter
    def sign(self, sign: str | int | types.Integer) -> None:
        """
        Sets `sign`.

        Parameters:
            sign: Sign of the surface normal.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if sign is not None:
            if isinstance(sign, types.Integer):
                sign = sign
            elif isinstance(sign, int):
                sign = types.Integer(sign)
            elif isinstance(sign, str):
                sign = types.Integer.from_mcnp(sign)

        if sign is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, sign)

        self._sign: types.Integer = sign
