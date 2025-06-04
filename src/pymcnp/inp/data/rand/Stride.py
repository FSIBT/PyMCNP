import re
import copy
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

    _KEYWORD = 'stride'

    _ATTRS = {
        'stride': types.Integer,
    }

    _REGEX = re.compile(rf'\Astride( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, stride: types.Integer):
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

        self.stride: typing.Final[types.Integer] = stride


@dataclasses.dataclass
class StrideBuilder:
    """
    Builds ``Stride``.

    Attributes:
        stride: Number of random numbers between source particle.
    """

    stride: str | int | types.Integer

    def build(self):
        """
        Builds ``StrideBuilder`` into ``Stride``.

        Returns:
            ``Stride`` for ``StrideBuilder``.
        """

        stride = self.stride
        if isinstance(self.stride, types.Integer):
            stride = self.stride
        elif isinstance(self.stride, int):
            stride = types.Integer(self.stride)
        elif isinstance(self.stride, str):
            stride = types.Integer.from_mcnp(self.stride)

        return Stride(
            stride=stride,
        )

    @staticmethod
    def unbuild(ast: Stride):
        """
        Unbuilds ``Stride`` into ``StrideBuilder``

        Returns:
            ``StrideBuilder`` for ``Stride``.
        """

        return Stride(
            stride=copy.deepcopy(ast.stride),
        )
