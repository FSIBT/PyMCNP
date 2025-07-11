import re

from . import _option
from ....utils import types
from ....utils import errors


class Debug(_option.EmbedOption):
    """
    Represents INP debug elements.

    Attributes:
        parameter: Debug parameter.
    """

    _KEYWORD = 'debug'

    _ATTRS = {
        'parameter': types.String,
    }

    _REGEX = re.compile(rf'\Adebug( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, parameter: str | types.String):
        """
        Initializes ``Debug``.

        Parameters:
            parameter: Debug parameter.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.parameter: types.String = parameter

    @property
    def parameter(self) -> types.String:
        """
        Gets ``parameter``.

        Returns:
            ``parameter``.
        """

        return self._parameter

    @parameter.setter
    def parameter(self, parameter: str | types.String) -> None:
        """
        Sets ``parameter``.

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
            else:
                raise TypeError

        if parameter is None or parameter not in {'echomesh'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, parameter)

        self._parameter: types.String = parameter
