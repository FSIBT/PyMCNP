import re

from . import _option
from ... import types
from ... import errors


class Ksental(_option.KoptsOption):
    """
    Represents INP `ksental` elements.
    """

    _KEYWORD = 'ksental'

    _ATTRS = {
        'fileopt': types.String,
    }

    _REGEX = re.compile(rf'\Aksental( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, fileopt: str | types.String):
        """
        Initializes `Ksental`.

        Parameters:
            fileopt: Format of sensity profiles output file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fileopt: types.String = fileopt

    @property
    def fileopt(self) -> types.String:
        """
        Format of sensity profiles output file

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fileopt

    @fileopt.setter
    def fileopt(self, fileopt: str | types.String) -> None:
        """
        Sets `fileopt`.

        Parameters:
            fileopt: Format of sensity profiles output file.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fileopt is not None:
            if isinstance(fileopt, types.String):
                fileopt = fileopt
            elif isinstance(fileopt, str):
                fileopt = types.String.from_mcnp(fileopt)

        if fileopt is None or fileopt.value.lower() not in {'mctal', 'tsunami-b'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fileopt)

        self._fileopt: types.String = fileopt
