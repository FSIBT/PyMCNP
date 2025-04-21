import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Pikmt(DataOption, keyword='pikmt'):
    """
    Represents INP pikmt elements.

    Attributes:
        biases: Biases for proton production.
    """

    _ATTRS = {
        'biases': types.Tuple[types.PhotonBias],
    }

    _REGEX = re.compile(rf'\Apikmt((?: {types.PhotonBias._REGEX.pattern})+?)\Z')

    def __init__(self, biases: types.Tuple[types.PhotonBias]):
        """
        Initializes ``Pikmt``.

        Parameters:
            biases: Biases for proton production.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, biases)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                biases,
            ]
        )

        self.biases: typing.Final[types.Tuple[types.PhotonBias]] = biases


@dataclasses.dataclass
class PikmtBuilder:
    """
    Builds ``Pikmt``.

    Attributes:
        biases: Biases for proton production.
    """

    biases: list[str] | list[types.PhotonBias]

    def build(self):
        """
        Builds ``PikmtBuilder`` into ``Pikmt``.

        Returns:
            ``Pikmt`` for ``PikmtBuilder``.
        """

        biases = []
        for item in self.biases:
            if isinstance(item, types.PhotonBias):
                biases.append(item)
            elif isinstance(item, str):
                biases.append(types.PhotonBias.from_mcnp(item))
            else:
                biases.append(item.build())
        biases = types.Tuple(biases)

        return Pikmt(
            biases=biases,
        )
