import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Bap(SdefOption):
    """
    Represents INP bap elements.

    Attributes:
        ba1: Beam aperture half-width in the x transverse direction.
        ba2: Beam aperture half-width in the y transverse direction.
        u: Unused, arrbirary value.
    """

    _ATTRS = {
        'ba1': types.Real,
        'ba2': types.Real,
        'u': types.Real,
    }

    _REGEX = re.compile(
        rf'\Abap( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(self, ba1: types.Real, ba2: types.Real, u: types.Real):
        """
        Initializes ``Bap``.

        Parameters:
            ba1: Beam aperture half-width in the x transverse direction.
            ba2: Beam aperture half-width in the y transverse direction.
            u: Unused, arrbirary value.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if ba1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ba1)
        if ba2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ba2)
        if u is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, u)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ba1,
                ba2,
                u,
            ]
        )

        self.ba1: typing.Final[types.Real] = ba1
        self.ba2: typing.Final[types.Real] = ba2
        self.u: typing.Final[types.Real] = u


@dataclasses.dataclass
class BapBuilder:
    """
    Builds ``Bap``.

    Attributes:
        ba1: Beam aperture half-width in the x transverse direction.
        ba2: Beam aperture half-width in the y transverse direction.
        u: Unused, arrbirary value.
    """

    ba1: str | float | types.Real
    ba2: str | float | types.Real
    u: str | float | types.Real

    def build(self):
        """
        Builds ``BapBuilder`` into ``Bap``.

        Returns:
            ``Bap`` for ``BapBuilder``.
        """

        ba1 = self.ba1
        if isinstance(self.ba1, types.Real):
            ba1 = self.ba1
        elif isinstance(self.ba1, float) or isinstance(self.ba1, int):
            ba1 = types.Real(self.ba1)
        elif isinstance(self.ba1, str):
            ba1 = types.Real.from_mcnp(self.ba1)

        ba2 = self.ba2
        if isinstance(self.ba2, types.Real):
            ba2 = self.ba2
        elif isinstance(self.ba2, float) or isinstance(self.ba2, int):
            ba2 = types.Real(self.ba2)
        elif isinstance(self.ba2, str):
            ba2 = types.Real.from_mcnp(self.ba2)

        u = self.u
        if isinstance(self.u, types.Real):
            u = self.u
        elif isinstance(self.u, float) or isinstance(self.u, int):
            u = types.Real(self.u)
        elif isinstance(self.u, str):
            u = types.Real.from_mcnp(self.u)

        return Bap(
            ba1=ba1,
            ba2=ba2,
            u=u,
        )
