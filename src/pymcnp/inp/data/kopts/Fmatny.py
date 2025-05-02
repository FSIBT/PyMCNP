import re
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmatny(KoptsOption):
    """
    Represents INP fmatny elements.

    Attributes:
        fmat_ny: fmat_ny.
    """

    _ATTRS = {
        'fmat_ny': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatny( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_ny: types.RealOrJump):
        """
        Initializes ``Fmatny``.

        Parameters:
            fmat_ny: fmat_ny.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fmat_ny is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_ny)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_ny,
            ]
        )

        self.fmat_ny: typing.Final[types.RealOrJump] = fmat_ny


@dataclasses.dataclass
class FmatnyBuilder:
    """
    Builds ``Fmatny``.

    Attributes:
        fmat_ny: fmat_ny.
    """

    fmat_ny: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FmatnyBuilder`` into ``Fmatny``.

        Returns:
            ``Fmatny`` for ``FmatnyBuilder``.
        """

        if isinstance(self.fmat_ny, types.Real):
            fmat_ny = self.fmat_ny
        elif isinstance(self.fmat_ny, float) or isinstance(self.fmat_ny, int):
            fmat_ny = types.RealOrJump(self.fmat_ny)
        elif isinstance(self.fmat_ny, str):
            fmat_ny = types.RealOrJump.from_mcnp(self.fmat_ny)

        return Fmatny(
            fmat_ny=fmat_ny,
        )
