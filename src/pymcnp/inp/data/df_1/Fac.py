import re
import typing
import dataclasses


from ._option import DfOption_1
from ....utils import types
from ....utils import errors


class Fac(DfOption_1):
    """
    Represents INP fac elements.

    Attributes:
        normalization: Normalization factor for dose.
    """

    _ATTRS = {
        'normalization': types.Integer,
    }

    _REGEX = re.compile(rf'\Afac( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, normalization: types.Integer):
        """
        Initializes ``Fac``.

        Parameters:
            normalization: Normalization factor for dose.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if normalization is None or not (
            isinstance(normalization, types.Jump) or normalization.value >= -3
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, normalization)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                normalization,
            ]
        )

        self.normalization: typing.Final[types.Integer] = normalization


@dataclasses.dataclass
class FacBuilder:
    """
    Builds ``Fac``.

    Attributes:
        normalization: Normalization factor for dose.
    """

    normalization: str | int | types.Integer

    def build(self):
        """
        Builds ``FacBuilder`` into ``Fac``.

        Returns:
            ``Fac`` for ``FacBuilder``.
        """

        normalization = self.normalization
        if isinstance(self.normalization, types.Integer):
            normalization = self.normalization
        elif isinstance(self.normalization, int):
            normalization = types.Integer(self.normalization)
        elif isinstance(self.normalization, str):
            normalization = types.Integer.from_mcnp(self.normalization)

        return Fac(
            normalization=normalization,
        )
