import re

from . import _option
from ... import types
from ... import errors


class Debug(_option.EmbedOption):
    """
    Represents INP `debug` elements.
    """

    _KEYWORD = 'debug'

    _ATTRS = {
        'parameter': types.String,
    }

    _REGEX = re.compile(rf'\Adebug( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, parameter: str | types.String):
        """
        Initializes `Debug`.

        Parameters:
            parameter: Debug parameter.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.parameter: types.String = parameter

    @property
    def parameter(self) -> types.String:
        """
        Debug parameter

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._parameter

    @parameter.setter
    def parameter(self, parameter: str | types.String) -> None:
        """
        Sets `parameter`.

        Parameters:
            parameter: Debug parameter.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if parameter is not None:
            if isinstance(parameter, types.String):
                parameter = parameter
            elif isinstance(parameter, str):
                parameter = types.String.from_mcnp(parameter)

        if parameter is None or parameter.value.lower() not in {'echomesh'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, parameter)

        self._parameter: types.String = parameter
