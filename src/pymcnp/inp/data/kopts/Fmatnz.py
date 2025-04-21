import re
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmatnz(KoptsOption, keyword='fmatnz'):
    """
    Represents INP fmatnz elements.

    Attributes:
        fmat_nz: fmat_nz.
    """

    _ATTRS = {
        'fmat_nz': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatnz( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_nz: types.RealOrJump):
        """
        Initializes ``Fmatnz``.

        Parameters:
            fmat_nz: fmat_nz.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_nz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_nz)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_nz,
            ]
        )

        self.fmat_nz: typing.Final[types.RealOrJump] = fmat_nz


@dataclasses.dataclass
class FmatnzBuilder:
    """
    Builds ``Fmatnz``.

    Attributes:
        fmat_nz: fmat_nz.
    """

    fmat_nz: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FmatnzBuilder`` into ``Fmatnz``.

        Returns:
            ``Fmatnz`` for ``FmatnzBuilder``.
        """

        if isinstance(self.fmat_nz, types.Real):
            fmat_nz = self.fmat_nz
        elif isinstance(self.fmat_nz, float) or isinstance(self.fmat_nz, int):
            fmat_nz = types.RealOrJump(self.fmat_nz)
        elif isinstance(self.fmat_nz, str):
            fmat_nz = types.RealOrJump.from_mcnp(self.fmat_nz)

        return Fmatnz(
            fmat_nz=fmat_nz,
        )
