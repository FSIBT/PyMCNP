import re

from . import _option
from ... import types
from ... import errors


class Stride(_option.RandOption):
    """
    Represents INP `stride` elements.
    """

    _KEYWORD = 'stride'

    _ATTRS = {
        'stride': types.Integer,
    }

    _REGEX = re.compile(rf'\Astride( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, stride: str | int | types.Integer):
        """
        Initializes `Stride`.

        Parameters:
            stride: Number of random numbers between source particle.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.stride: types.Integer = stride

    @property
    def stride(self) -> types.Integer:
        """
        Number of random numbers between source particle

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._stride

    @stride.setter
    def stride(self, stride: str | int | types.Integer) -> None:
        """
        Sets `stride`.

        Parameters:
            stride: Number of random numbers between source particle.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if stride is not None:
            if isinstance(stride, types.Integer):
                stride = stride
            elif isinstance(stride, int):
                stride = types.Integer(stride)
            elif isinstance(stride, str):
                stride = types.Integer.from_mcnp(stride)

        if stride is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, stride)

        self._stride: types.Integer = stride
