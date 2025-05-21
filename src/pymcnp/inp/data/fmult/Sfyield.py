import re
import copy
import typing
import dataclasses


from ._option import FmultOption
from ....utils import types
from ....utils import errors


class Sfyield(FmultOption):
    """
    Represents INP sfyield elements.

    Attributes:
        fission_yield: Spontaneous fission yield.
    """

    _KEYWORD = 'sfyield'

    _ATTRS = {
        'fission_yield': types.Real,
    }

    _REGEX = re.compile(rf'\Asfyield( {types.Real._REGEX.pattern})\Z')

    def __init__(self, fission_yield: types.Real):
        """
        Initializes ``Sfyield``.

        Parameters:
            fission_yield: Spontaneous fission yield.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fission_yield is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fission_yield)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fission_yield,
            ]
        )

        self.fission_yield: typing.Final[types.Real] = fission_yield


@dataclasses.dataclass
class SfyieldBuilder:
    """
    Builds ``Sfyield``.

    Attributes:
        fission_yield: Spontaneous fission yield.
    """

    fission_yield: str | float | types.Real

    def build(self):
        """
        Builds ``SfyieldBuilder`` into ``Sfyield``.

        Returns:
            ``Sfyield`` for ``SfyieldBuilder``.
        """

        fission_yield = self.fission_yield
        if isinstance(self.fission_yield, types.Real):
            fission_yield = self.fission_yield
        elif isinstance(self.fission_yield, float) or isinstance(self.fission_yield, int):
            fission_yield = types.Real(self.fission_yield)
        elif isinstance(self.fission_yield, str):
            fission_yield = types.Real.from_mcnp(self.fission_yield)

        return Sfyield(
            fission_yield=fission_yield,
        )

    @staticmethod
    def unbuild(ast: Sfyield):
        """
        Unbuilds ``Sfyield`` into ``SfyieldBuilder``

        Returns:
            ``SfyieldBuilder`` for ``Sfyield``.
        """

        return Sfyield(
            fission_yield=copy.deepcopy(ast.fission_yield),
        )
