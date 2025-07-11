import re

from . import _option
from ...utils import types
from ...utils import errors


class Totnu(_option.DataOption):
    """
    Represents INP totnu elements.

    Attributes:
        no: Delay fission sampling on/off.
    """

    _KEYWORD = 'totnu'

    _ATTRS = {
        'no': types.String,
    }

    _REGEX = re.compile(rf'\Atotnu( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, no: str | types.String = None):
        """
        Initializes ``Totnu``.

        Parameters:
            no: Delay fission sampling on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.no: types.String = no

    @property
    def no(self) -> types.String:
        """
        Gets ``no``.

        Returns:
            ``no``.
        """

        return self._no

    @no.setter
    def no(self, no: str | types.String) -> None:
        """
        Sets ``no``.

        Parameters:
            no: Delay fission sampling on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if no is not None:
            if isinstance(no, types.String):
                no = no
            elif isinstance(no, str):
                no = types.String.from_mcnp(no)
            else:
                raise TypeError

        if no is not None and not (no == 'no'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, no)

        self._no: types.String = no
