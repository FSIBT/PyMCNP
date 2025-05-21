import re
import copy
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

    _KEYWORD = 'fmatny'

    _ATTRS = {
        'fmat_ny': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatny( {types.Real._REGEX.pattern})\Z')

    def __init__(self, fmat_ny: types.Real):
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

        self.fmat_ny: typing.Final[types.Real] = fmat_ny


@dataclasses.dataclass
class FmatnyBuilder:
    """
    Builds ``Fmatny``.

    Attributes:
        fmat_ny: fmat_ny.
    """

    fmat_ny: str | float | types.Real

    def build(self):
        """
        Builds ``FmatnyBuilder`` into ``Fmatny``.

        Returns:
            ``Fmatny`` for ``FmatnyBuilder``.
        """

        fmat_ny = self.fmat_ny
        if isinstance(self.fmat_ny, types.Real):
            fmat_ny = self.fmat_ny
        elif isinstance(self.fmat_ny, float) or isinstance(self.fmat_ny, int):
            fmat_ny = types.Real(self.fmat_ny)
        elif isinstance(self.fmat_ny, str):
            fmat_ny = types.Real.from_mcnp(self.fmat_ny)

        return Fmatny(
            fmat_ny=fmat_ny,
        )

    @staticmethod
    def unbuild(ast: Fmatny):
        """
        Unbuilds ``Fmatny`` into ``FmatnyBuilder``

        Returns:
            ``FmatnyBuilder`` for ``Fmatny``.
        """

        return Fmatny(
            fmat_ny=copy.deepcopy(ast.fmat_ny),
        )
