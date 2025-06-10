import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Pikmt(_option.DataOption):
    """
    Represents INP pikmt elements.

    Attributes:
        biases: Biases for proton production.
    """

    _KEYWORD = 'pikmt'

    _ATTRS = {
        'biases': types.Tuple[types.PhotonBias],
    }

    _REGEX = re.compile(rf'\Apikmt((?: {types.PhotonBias._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, biases: types.Tuple[types.PhotonBias]):
        """
        Initializes ``Pikmt``.

        Parameters:
            biases: Biases for proton production.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                biases,
            ]
        )

        self.biases: typing.Final[types.Tuple[types.PhotonBias]] = biases


@dataclasses.dataclass
class PikmtBuilder(_option.DataOptionBuilder):
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

        if self.biases:
            biases = []
            for item in self.biases:
                if isinstance(item, types.PhotonBias):
                    biases.append(item)
                elif isinstance(item, str):
                    biases.append(types.PhotonBias.from_mcnp(item))
            biases = types.Tuple(biases)
        else:
            biases = None

        return Pikmt(
            biases=biases,
        )

    @staticmethod
    def unbuild(ast: Pikmt):
        """
        Unbuilds ``Pikmt`` into ``PikmtBuilder``

        Returns:
            ``PikmtBuilder`` for ``Pikmt``.
        """

        return PikmtBuilder(
            biases=copy.deepcopy(ast.biases),
        )
