import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Fmatnz(_option.KoptsOption):
    """
    Represents INP fmatnz elements.

    Attributes:
        fmat_nz: fmat_nz.
    """

    _KEYWORD = 'fmatnz'

    _ATTRS = {
        'fmat_nz': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatnz( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fmat_nz: types.Real):
        """
        Initializes ``Fmatnz``.

        Parameters:
            fmat_nz: fmat_nz.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fmat_nz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_nz)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_nz,
            ]
        )

        self.fmat_nz: typing.Final[types.Real] = fmat_nz


@dataclasses.dataclass
class FmatnzBuilder(_option.KoptsOptionBuilder):
    """
    Builds ``Fmatnz``.

    Attributes:
        fmat_nz: fmat_nz.
    """

    fmat_nz: str | float | types.Real

    def build(self):
        """
        Builds ``FmatnzBuilder`` into ``Fmatnz``.

        Returns:
            ``Fmatnz`` for ``FmatnzBuilder``.
        """

        fmat_nz = self.fmat_nz
        if isinstance(self.fmat_nz, types.Real):
            fmat_nz = self.fmat_nz
        elif isinstance(self.fmat_nz, float) or isinstance(self.fmat_nz, int):
            fmat_nz = types.Real(self.fmat_nz)
        elif isinstance(self.fmat_nz, str):
            fmat_nz = types.Real.from_mcnp(self.fmat_nz)

        return Fmatnz(
            fmat_nz=fmat_nz,
        )

    @staticmethod
    def unbuild(ast: Fmatnz):
        """
        Unbuilds ``Fmatnz`` into ``FmatnzBuilder``

        Returns:
            ``FmatnzBuilder`` for ``Fmatnz``.
        """

        return FmatnzBuilder(
            fmat_nz=copy.deepcopy(ast.fmat_nz),
        )
