import re

from . import _option
from ... import types
from ... import errors


class Gmvfile(_option.EmbedOption):
    """
    Represents INP `gmvfile` elements.
    """

    _KEYWORD = 'gmvfile'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Agmvfile( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, filename: str | types.String):
        """
        Initializes `Gmvfile`.

        Parameters:
            filename: Name of the GMV output file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.filename: types.String = filename

    @property
    def filename(self) -> types.String:
        """
        Name of the GMV output file

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._filename

    @filename.setter
    def filename(self, filename: str | types.String) -> None:
        """
        Sets `filename`.

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

        if filename is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, filename)

        self._filename: types.String = filename
