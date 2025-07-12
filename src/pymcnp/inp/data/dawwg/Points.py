import re

from . import _option
from ....utils import types
from ....utils import errors


class Points(_option.DawwgOption):
    """
    Represents INP points elements.
    """

    _KEYWORD = 'points'

    _ATTRS = {
        'name': types.String,
    }

    _REGEX = re.compile(rf'\Apoints( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, name: str | types.String):
        """
        Initializes ``Points``.

        Parameters:
            name: Cross section library.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.name: types.String = name

    @property
    def name(self) -> types.String:
        """
        Cross section library

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._name

    @name.setter
    def name(self, name: str | types.String) -> None:
        """
        Sets ``name``.

        Parameters:
            name: Cross section library.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if name is not None:
            if isinstance(name, types.String):
                name = name
            elif isinstance(name, str):
                name = types.String.from_mcnp(name)

        if name is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, name)

        self._name: types.String = name
