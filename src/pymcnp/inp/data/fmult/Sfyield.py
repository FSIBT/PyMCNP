import re
import typing
import dataclasses


from ._option import FmultOption
from ....utils import types
from ....utils import errors


class Sfyield(FmultOption, keyword='sfyield'):
    """
    Represents INP sfyield elements.

    Attributes:
        fission_yield: Spontaneous fission yield.
    """

    _ATTRS = {
        'fission_yield': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Asfyield( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fission_yield: types.RealOrJump):
        """
        Initializes ``Sfyield``.

        Parameters:
            fission_yield: Spontaneous fission yield.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fission_yield is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fission_yield)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fission_yield,
            ]
        )

        self.fission_yield: typing.Final[types.RealOrJump] = fission_yield


@dataclasses.dataclass
class SfyieldBuilder:
    """
    Builds ``Sfyield``.

    Attributes:
        fission_yield: Spontaneous fission yield.
    """

    fission_yield: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``SfyieldBuilder`` into ``Sfyield``.

        Returns:
            ``Sfyield`` for ``SfyieldBuilder``.
        """

        if isinstance(self.fission_yield, types.Real):
            fission_yield = self.fission_yield
        elif isinstance(self.fission_yield, float) or isinstance(self.fission_yield, int):
            fission_yield = types.RealOrJump(self.fission_yield)
        elif isinstance(self.fission_yield, str):
            fission_yield = types.RealOrJump.from_mcnp(self.fission_yield)

        return Sfyield(
            fission_yield=fission_yield,
        )
