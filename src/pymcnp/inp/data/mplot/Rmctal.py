import re

from . import _option
from ....utils import types
from ....utils import errors


class Rmctal(_option.MplotOption):
    """
    Represents INP rmctal elements.

    Attributes:
        filename: MCTAL file to read.
    """

    _KEYWORD = 'rmctal'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Armctal( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, filename: str | types.String):
        """
        Initializes ``Rmctal``.

        Parameters:
            filename: MCTAL file to read.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.filename: types.String = filename

    @property
    def filename(self) -> types.String:
        """
        Gets ``filename``.

        Returns:
            ``filename``.
        """

        return self._filename

    @filename.setter
    def filename(self, filename: str | types.String) -> None:
        """
        Sets ``filename``.

        Parameters:
            filename: MCTAL file to read.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if filename is not None:
            if isinstance(filename, types.String):
                filename = filename
            elif isinstance(filename, str):
                filename = types.String.from_mcnp(filename)
            else:
                raise TypeError

        if filename is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, filename)

        self._filename: types.String = filename
