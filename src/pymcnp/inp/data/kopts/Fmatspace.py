import re
import copy
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

    _KEYWORD = 'fmatspace'

    _ATTRS = {
        'fmat_space': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatspace( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fmat_space: types.Real):
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

        self.fmat_space: typing.Final[types.Real] = fmat_space


@dataclasses.dataclass
class FmatspaceBuilder:
    """
    Builds ``Fmatspace``.

    Attributes:
        fmat_space: fmat_space.
    """

    fmat_space: str | float | types.Real

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
            fmat_space = types.Real(self.fmat_space)
        elif isinstance(self.fmat_space, str):
            fmat_space = types.Real.from_mcnp(self.fmat_space)

        return Fmatspace(
            fmat_space=fmat_space,
        )

    @staticmethod
    def unbuild(ast: Fmatspace):
        """
        Unbuilds ``Fmatspace`` into ``FmatspaceBuilder``

        Returns:
            ``FmatspaceBuilder`` for ``Fmatspace``.
        """

        return Fmatspace(
            fmat_space=copy.deepcopy(ast.fmat_space),
        )
