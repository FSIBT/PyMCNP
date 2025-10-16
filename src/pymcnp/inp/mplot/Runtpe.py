import re

from . import _option
from ... import types
from ... import errors


class Runtpe(_option.MplotOption):
    """
    Represents INP `runtpe` elements.
    """

    _KEYWORD = 'runtpe'

    _ATTRS = {
        'filename': types.String,
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Aruntpe( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, filename: str | types.String, n: str | int | types.Integer = None):
        """
        Initializes `Runtpe`.

        Parameters:
            filename: RUNTPE file to read dump.
            n: RUNTPE read dump number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.filename: types.String = filename
        self.n: types.Integer = n

    @property
    def filename(self) -> types.String:
        """
        RUNTPE file to read dump

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
            filename: RUNTPE file to read dump.

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

    @property
    def n(self) -> types.Integer:
        """
        RUNTPE read dump number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n

    @n.setter
    def n(self, n: str | int | types.Integer) -> None:
        """
        Sets `n`.

        Parameters:
            n: RUNTPE read dump number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n is not None:
            if isinstance(n, types.Integer):
                n = n
            elif isinstance(n, int):
                n = types.Integer(n)
            elif isinstance(n, str):
                n = types.Integer.from_mcnp(n)

        self._n: types.Integer = n
