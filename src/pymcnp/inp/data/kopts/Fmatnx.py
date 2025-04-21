import re
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmatnx(KoptsOption, keyword='fmatnx'):
    """
    Represents INP fmatnx elements.

    Attributes:
        fmat_nx: fmat_nx.
    """

    _ATTRS = {
        'fmat_nx': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatnx( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_nx: types.RealOrJump):
        """
        Initializes ``Fmatnx``.

        Parameters:
            fmat_nx: fmat_nx.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fmat_nx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_nx)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_nx,
            ]
        )

        self.fmat_nx: typing.Final[types.RealOrJump] = fmat_nx


@dataclasses.dataclass
class FmatnxBuilder:
    """
    Builds ``Fmatnx``.

    Attributes:
        fmat_nx: fmat_nx.
    """

    fmat_nx: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FmatnxBuilder`` into ``Fmatnx``.

        Returns:
            ``Fmatnx`` for ``FmatnxBuilder``.
        """

        if isinstance(self.fmat_nx, types.Real):
            fmat_nx = self.fmat_nx
        elif isinstance(self.fmat_nx, float) or isinstance(self.fmat_nx, int):
            fmat_nx = types.RealOrJump(self.fmat_nx)
        elif isinstance(self.fmat_nx, str):
            fmat_nx = types.RealOrJump.from_mcnp(self.fmat_nx)

        return Fmatnx(
            fmat_nx=fmat_nx,
        )
