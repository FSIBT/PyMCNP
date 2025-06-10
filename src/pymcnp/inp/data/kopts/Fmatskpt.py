import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Fmatskpt(_option.KoptsOption):
    """
    Represents INP fmatskpt elements.

    Attributes:
        fmat_skip: fmat_skip.
    """

    _KEYWORD = 'fmatskpt'

    _ATTRS = {
        'fmat_skip': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatskpt( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fmat_skip: types.Real):
        """
        Initializes ``Fmatskpt``.

        Parameters:
            fmat_skip: fmat_skip.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fmat_skip is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_skip)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_skip,
            ]
        )

        self.fmat_skip: typing.Final[types.Real] = fmat_skip


@dataclasses.dataclass
class FmatskptBuilder(_option.KoptsOptionBuilder):
    """
    Builds ``Fmatskpt``.

    Attributes:
        fmat_skip: fmat_skip.
    """

    fmat_skip: str | float | types.Real

    def build(self):
        """
        Builds ``FmatskptBuilder`` into ``Fmatskpt``.

        Returns:
            ``Fmatskpt`` for ``FmatskptBuilder``.
        """

        fmat_skip = self.fmat_skip
        if isinstance(self.fmat_skip, types.Real):
            fmat_skip = self.fmat_skip
        elif isinstance(self.fmat_skip, float) or isinstance(self.fmat_skip, int):
            fmat_skip = types.Real(self.fmat_skip)
        elif isinstance(self.fmat_skip, str):
            fmat_skip = types.Real.from_mcnp(self.fmat_skip)

        return Fmatskpt(
            fmat_skip=fmat_skip,
        )

    @staticmethod
    def unbuild(ast: Fmatskpt):
        """
        Unbuilds ``Fmatskpt`` into ``FmatskptBuilder``

        Returns:
            ``FmatskptBuilder`` for ``Fmatskpt``.
        """

        return FmatskptBuilder(
            fmat_skip=copy.deepcopy(ast.fmat_skip),
        )
