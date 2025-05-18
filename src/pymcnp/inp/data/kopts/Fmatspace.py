import re
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmatspace(KoptsOption):
    """
    Represents INP fmatspace elements.

    Attributes:
        fmat_space: fmat_space.
    """

    _ATTRS = {
        'fmat_space': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatspace( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_space: types.RealOrJump):
        """
        Initializes ``Fmatspace``.

        Parameters:
            fmat_space: fmat_space.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fmat_space is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_space)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_space,
            ]
        )

        self.fmat_space: typing.Final[types.RealOrJump] = fmat_space


@dataclasses.dataclass
class FmatspaceBuilder:
    """
    Builds ``Fmatspace``.

    Attributes:
        fmat_space: fmat_space.
    """

    fmat_space: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FmatspaceBuilder`` into ``Fmatspace``.

        Returns:
            ``Fmatspace`` for ``FmatspaceBuilder``.
        """

        fmat_space = self.fmat_space
        if isinstance(self.fmat_space, types.Real):
            fmat_space = self.fmat_space
        elif isinstance(self.fmat_space, float) or isinstance(self.fmat_space, int):
            fmat_space = types.RealOrJump(self.fmat_space)
        elif isinstance(self.fmat_space, str):
            fmat_space = types.RealOrJump.from_mcnp(self.fmat_space)

        return Fmatspace(
            fmat_space=fmat_space,
        )
