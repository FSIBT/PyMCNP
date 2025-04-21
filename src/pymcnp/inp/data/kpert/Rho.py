import re
import typing
import dataclasses


from ._option import KpertOption
from ....utils import types
from ....utils import errors


class Rho(KpertOption, keyword='rho'):
    """
    Represents INP rho elements.

    Attributes:
        densities: List of densities.
    """

    _ATTRS = {
        'densities': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Arho((?: {types.Zaid._REGEX.pattern})+?)\Z')

    def __init__(self, densities: types.Tuple[types.Zaid]):
        """
        Initializes ``Rho``.

        Parameters:
            densities: List of densities.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if densities is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, densities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                densities,
            ]
        )

        self.densities: typing.Final[types.Tuple[types.Zaid]] = densities


@dataclasses.dataclass
class RhoBuilder:
    """
    Builds ``Rho``.

    Attributes:
        densities: List of densities.
    """

    densities: list[str] | list[types.Zaid]

    def build(self):
        """
        Builds ``RhoBuilder`` into ``Rho``.

        Returns:
            ``Rho`` for ``RhoBuilder``.
        """

        densities = []
        for item in self.densities:
            if isinstance(item, types.Zaid):
                densities.append(item)
            elif isinstance(item, str):
                densities.append(types.Zaid.from_mcnp(item))
            else:
                densities.append(item.build())
        densities = types.Tuple(densities)

        return Rho(
            densities=densities,
        )
