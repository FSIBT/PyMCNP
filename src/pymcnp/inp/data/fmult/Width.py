import re
import typing
import dataclasses


from ._option import FmultOption
from ....utils import types
from ....utils import errors


class Width(FmultOption):
    """
    Represents INP width elements.

    Attributes:
        width: Width for sampling spontaneous fission.
    """

    _ATTRS = {
        'width': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Awidth( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, width: types.RealOrJump):
        """
        Initializes ``Width``.

        Parameters:
            width: Width for sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if width is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, width)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                width,
            ]
        )

        self.width: typing.Final[types.RealOrJump] = width


@dataclasses.dataclass
class WidthBuilder:
    """
    Builds ``Width``.

    Attributes:
        width: Width for sampling spontaneous fission.
    """

    width: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``WidthBuilder`` into ``Width``.

        Returns:
            ``Width`` for ``WidthBuilder``.
        """

        if isinstance(self.width, types.Real):
            width = self.width
        elif isinstance(self.width, float) or isinstance(self.width, int):
            width = types.RealOrJump(self.width)
        elif isinstance(self.width, str):
            width = types.RealOrJump.from_mcnp(self.width)

        return Width(
            width=width,
        )
