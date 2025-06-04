import re
import copy
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

    _KEYWORD = 'width'

    _ATTRS = {
        'width': types.Real,
    }

    _REGEX = re.compile(rf'\Awidth( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, width: types.Real):
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

        self.width: typing.Final[types.Real] = width


@dataclasses.dataclass
class WidthBuilder:
    """
    Builds ``Width``.

    Attributes:
        width: Width for sampling spontaneous fission.
    """

    width: str | float | types.Real

    def build(self):
        """
        Builds ``WidthBuilder`` into ``Width``.

        Returns:
            ``Width`` for ``WidthBuilder``.
        """

        width = self.width
        if isinstance(self.width, types.Real):
            width = self.width
        elif isinstance(self.width, float) or isinstance(self.width, int):
            width = types.Real(self.width)
        elif isinstance(self.width, str):
            width = types.Real.from_mcnp(self.width)

        return Width(
            width=width,
        )

    @staticmethod
    def unbuild(ast: Width):
        """
        Unbuilds ``Width`` into ``WidthBuilder``

        Returns:
            ``WidthBuilder`` for ``Width``.
        """

        return Width(
            width=copy.deepcopy(ast.width),
        )
