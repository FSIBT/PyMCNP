import re

from . import _option
from ....utils import types
from ....utils import errors


class Blocksize(_option.KoptsOption):
    """
    Represents INP blocksize elements.

    Attributes:
        ncy: Number of cycles in every outer iteration.
    """

    _KEYWORD = 'blocksize'

    _ATTRS = {
        'ncy': types.Integer,
    }

    _REGEX = re.compile(rf'\Ablocksize( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, ncy: str | int | types.Integer):
        """
        Initializes ``Blocksize``.

        Parameters:
            ncy: Number of cycles in every outer iteration.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.ncy: types.Integer = ncy

    @property
    def ncy(self) -> types.Integer:
        """
        Gets ``ncy``.

        Returns:
            ``ncy``.
        """

        return self._ncy

    @ncy.setter
    def ncy(self, ncy: str | int | types.Integer) -> None:
        """
        Sets ``ncy``.

        Parameters:
            ncy: Number of cycles in every outer iteration.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ncy is not None:
            if isinstance(ncy, types.Integer):
                ncy = ncy
            elif isinstance(ncy, int):
                ncy = types.Integer(ncy)
            elif isinstance(ncy, str):
                ncy = types.Integer.from_mcnp(ncy)
            else:
                raise TypeError

        if ncy is None or not (ncy >= 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ncy)

        self._ncy: types.Integer = ncy
