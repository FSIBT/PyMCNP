import re

from . import _option
from ....utils import types


class Genxs(_option.TroptOption):
    """
    Represents INP genxs elements.

    Attributes:
        filename: Cross section generation setting.
    """

    _KEYWORD = 'genxs'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Agenxs( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, filename: str | types.String = None):
        """
        Initializes ``Genxs``.

        Parameters:
            filename: Cross section generation setting.

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
            else:
                raise TypeError

        self._filename: types.String = filename
