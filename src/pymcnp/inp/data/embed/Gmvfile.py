import re

from . import _option
from ....utils import types
from ....utils import errors


class Gmvfile(_option.EmbedOption):
    """
    Represents INP gmvfile elements.

    Attributes:
        filename: Name of the GMV output file.
    """

    _KEYWORD = 'gmvfile'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Agmvfile( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, filename: str | types.String):
        """
        Initializes ``Gmvfile``.

        Parameters:
            filename: Name of the GMV output file.

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
            filename: Name of the GMV output file.

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
