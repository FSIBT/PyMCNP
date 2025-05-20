import re
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmatnx(KoptsOption):
    """
    Represents INP fmatnx elements.

    Attributes:
        fmat_nx: fmat_nx.
    """

    _ATTRS = {
        'fmat_nx': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatnx( {types.Real._REGEX.pattern})\Z')

    def __init__(self, fmat_nx: types.Real):
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

        self.fmat_nx: typing.Final[types.Real] = fmat_nx


@dataclasses.dataclass
class FmatnxBuilder:
    """
    Builds ``Fmatnx``.

    Attributes:
        fmat_nx: fmat_nx.
    """

    fmat_nx: str | float | types.Real

    def build(self):
        """
        Builds ``FmatnxBuilder`` into ``Fmatnx``.

        Returns:
            ``Fmatnx`` for ``FmatnxBuilder``.
        """

        fmat_nx = self.fmat_nx
        if isinstance(self.fmat_nx, types.Real):
            fmat_nx = self.fmat_nx
        elif isinstance(self.fmat_nx, float) or isinstance(self.fmat_nx, int):
            fmat_nx = types.Real(self.fmat_nx)
        elif isinstance(self.fmat_nx, str):
            fmat_nx = types.Real.from_mcnp(self.fmat_nx)

        return Fmatnx(
            fmat_nx=fmat_nx,
        )
