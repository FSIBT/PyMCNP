import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Bap(SdefOption, keyword='bap'):
    """
    Represents INP bap elements.

    Attributes:
        ba1: Beam aperture half-width in the x transverse direction.
        ba2: Beam aperture half-width in the y transverse direction.
        u: Unused, arrbirary value.
    """

    _ATTRS = {
        'ba1': types.RealOrJump,
        'ba2': types.RealOrJump,
        'u': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Abap( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, ba1: types.RealOrJump, ba2: types.RealOrJump, u: types.RealOrJump):
        """
        Initializes ``Bap``.

        Parameters:
            ba1: Beam aperture half-width in the x transverse direction.
            ba2: Beam aperture half-width in the y transverse direction.
            u: Unused, arrbirary value.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ba1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ba1)
        if ba2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ba2)
        if u is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, u)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ba1,
                ba2,
                u,
            ]
        )

        self.ba1: typing.Final[types.RealOrJump] = ba1
        self.ba2: typing.Final[types.RealOrJump] = ba2
        self.u: typing.Final[types.RealOrJump] = u


@dataclasses.dataclass
class BapBuilder:
    """
    Builds ``Bap``.

    Attributes:
        ba1: Beam aperture half-width in the x transverse direction.
        ba2: Beam aperture half-width in the y transverse direction.
        u: Unused, arrbirary value.
    """

    ba1: str | float | types.RealOrJump
    ba2: str | float | types.RealOrJump
    u: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``BapBuilder`` into ``Bap``.

        Returns:
            ``Bap`` for ``BapBuilder``.
        """

        if isinstance(self.ba1, types.Real):
            ba1 = self.ba1
        elif isinstance(self.ba1, float) or isinstance(self.ba1, int):
            ba1 = types.RealOrJump(self.ba1)
        elif isinstance(self.ba1, str):
            ba1 = types.RealOrJump.from_mcnp(self.ba1)

        if isinstance(self.ba2, types.Real):
            ba2 = self.ba2
        elif isinstance(self.ba2, float) or isinstance(self.ba2, int):
            ba2 = types.RealOrJump(self.ba2)
        elif isinstance(self.ba2, str):
            ba2 = types.RealOrJump.from_mcnp(self.ba2)

        if isinstance(self.u, types.Real):
            u = self.u
        elif isinstance(self.u, float) or isinstance(self.u, int):
            u = types.RealOrJump(self.u)
        elif isinstance(self.u, str):
            u = types.RealOrJump.from_mcnp(self.u)

        return Bap(
            ba1=ba1,
            ba2=ba2,
            u=u,
        )
