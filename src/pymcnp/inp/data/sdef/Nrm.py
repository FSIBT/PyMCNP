import re

from . import _option
from ....utils import types
from ....utils import errors


class Nrm(_option.SdefOption):
    """
    Represents INP nrm elements.

    Attributes:
        sign: Sign of the surface normal.
    """

    _KEYWORD = 'nrm'

    _ATTRS = {
        'sign': types.Integer,
    }

    _REGEX = re.compile(rf'\Anrm( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, sign: str | int | types.Integer):
        """
        Initializes ``Nrm``.

        Parameters:
            sign: Sign of the surface normal.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.sign: types.Integer = sign

    @property
    def sign(self) -> types.Integer:
        """
        Gets ``sign``.

        Returns:
            ``sign``.
        """

        return self._sign

    @sign.setter
    def sign(self, sign: str | int | types.Integer) -> None:
        """
        Sets ``sign``.

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
            else:
                raise TypeError

        if sign is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, sign)

        self._sign: types.Integer = sign
