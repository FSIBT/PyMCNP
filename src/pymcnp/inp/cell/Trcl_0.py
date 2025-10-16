import re

from . import _option
from ... import types
from ... import errors


class Trcl_0(_option.CellOption):
    """
    Represents INP `trcl` elements variation #0.
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'prefix': types.String,
        'transformation': types.Integer,
    }

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, transformation: str | int | types.Integer, prefix: str | types.String = None):
        """
        Initializes `Trcl_0`.

        Parameters:
            prefix: Star prefix.
            transformation: Cell transformation number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.prefix: types.String = prefix
        self.transformation: types.Integer = transformation

    @property
    def prefix(self) -> types.String:
        """
        Star prefix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)

        self._prefix: types.String = prefix

    @property
    def transformation(self) -> types.Integer:
        """
        Cell transformation number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._transformation

    @transformation.setter
    def transformation(self, transformation: str | int | types.Integer) -> None:
        """
        Sets `transformation`.

        Parameters:
            transformation: Cell transformation number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if transformation is not None:
            if isinstance(transformation, types.Integer):
                transformation = transformation
            elif isinstance(transformation, int):
                transformation = types.Integer(transformation)
            elif isinstance(transformation, str):
                transformation = types.Integer.from_mcnp(transformation)

        if transformation is None or not (transformation >= 0 and transformation <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformation)

        self._transformation: types.Integer = transformation
