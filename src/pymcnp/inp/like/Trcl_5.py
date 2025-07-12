import re

from . import _option
from ...utils import types
from ...utils import errors


class Trcl_5(_option.LikeOption):
    """
    Represents INP trcl variation #5 elements.
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'prefix': types.String,
        'transformation': types.Transformation_4,
    }

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Transformation_4._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: str | types.Transformation_4, prefix: str | types.String = None):
        """
        Initializes ``Trcl_5``.

        Parameters:
            prefix: Star prefix.
            transformation: Cell transformation..

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.prefix: types.String = prefix
        self.transformation: types.Transformation_4 = transformation

    @property
    def prefix(self) -> types.String:
        """
        Gets ``prefix``.

        Returns:
            ``prefix``.
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets ``prefix``.

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

        if prefix is not None and prefix not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)

        self._prefix: types.String = prefix

    @property
    def transformation(self) -> types.Transformation_4:
        """
        Gets ``transformation``.

        Returns:
            ``transformation``.
        """

        return self._transformation

    @transformation.setter
    def transformation(self, transformation: str | types.Transformation_4) -> None:
        """
        Sets ``transformation``.

        Parameters:
            transformation: Cell transformation..

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if transformation is not None:
            if isinstance(transformation, types.Transformation_4):
                transformation = transformation
            elif isinstance(transformation, str):
                transformation = types.Transformation_4.from_mcnp(transformation)

        if transformation is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformation)

        self._transformation: types.Transformation_4 = transformation
