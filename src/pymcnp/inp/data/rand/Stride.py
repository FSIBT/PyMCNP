import re
import typing
import dataclasses


from ._option import RandOption
from ....utils import types
from ....utils import errors


class Stride(RandOption):
    """
    Represents INP stride elements.

    Attributes:
        stride: Number of random numbers between source particle.
    """

    _ATTRS = {
        'stride': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Astride( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, stride: types.IntegerOrJump):
        """
        Initializes ``Stride``.

        Parameters:
            stride: Number of random numbers between source particle.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if stride is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, stride)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                stride,
            ]
        )

        self.stride: typing.Final[types.IntegerOrJump] = stride


@dataclasses.dataclass
class StrideBuilder:
    """
    Builds ``Stride``.

    Attributes:
        stride: Number of random numbers between source particle.
    """

    stride: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``StrideBuilder`` into ``Stride``.

        Returns:
            ``Stride`` for ``StrideBuilder``.
        """

        if isinstance(self.stride, types.Integer):
            stride = self.stride
        elif isinstance(self.stride, int):
            stride = types.IntegerOrJump(self.stride)
        elif isinstance(self.stride, str):
            stride = types.IntegerOrJump.from_mcnp(self.stride)

        return Stride(
            stride=stride,
        )
