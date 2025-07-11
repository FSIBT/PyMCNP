import re

from . import _option
from ...utils import types
from ...utils import errors


class Fc(_option.DataOption):
    """
    Represents INP fc elements.

    Attributes:
        suffix: Data card option suffix.
        info: Title for tally in output and MCTAL file.
    """

    _KEYWORD = 'fc'

    _ATTRS = {
        'suffix': types.Integer,
        'info': types.String,
    }

    _REGEX = re.compile(r'\Afc(\d+)( [\S\s]+)\Z')

    def __init__(self, suffix: str | int | types.Integer, info: str | types.String):
        """
        Initializes ``Fc``.

        Parameters:
            suffix: Data card option suffix.
            info: Title for tally in output and MCTAL file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.info: types.String = info

    @property
    def suffix(self) -> types.Integer:
        """
        Gets ``suffix``.

        Returns:
            ``suffix``.
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)
            else:
                raise TypeError

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def info(self) -> types.String:
        """
        Gets ``info``.

        Returns:
            ``info``.
        """

        return self._info

    @info.setter
    def info(self, info: str | types.String) -> None:
        """
        Sets ``info``.

        Parameters:
            info: Title for tally in output and MCTAL file.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if info is not None:
            if isinstance(info, types.String):
                info = info
            elif isinstance(info, str):
                info = types.String.from_mcnp(info)
            else:
                raise TypeError

        if info is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, info)

        self._info: types.String = info
