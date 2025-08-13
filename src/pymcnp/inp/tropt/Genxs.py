import re

from . import _option
from ... import types


class Genxs(_option.TroptOption):
    """
    Represents INP `genxs` elements.
    """

    _KEYWORD = 'genxs'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Agenxs( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, filename: str | types.String = None):
        """
        Initializes `Genxs`.

        Parameters:
            filename: Cross section generation setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.filename: types.String = filename

    @property
    def filename(self) -> types.String:
        """
        Cross section generation setting

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
            filename: Cross section generation setting.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if filename is not None:
            if isinstance(filename, types.String):
                filename = filename
            elif isinstance(filename, str):
                filename = types.String.from_mcnp(filename)

        self._filename: types.String = filename
