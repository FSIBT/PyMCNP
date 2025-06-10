import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Dgeb(_option.ActOption):
    """
    Represents INP dgeb elements.

    Attributes:
        biases: Delayed neutron energy biases.
    """

    _KEYWORD = 'dgeb'

    _ATTRS = {
        'biases': types.Tuple[types.Bias],
    }

    _REGEX = re.compile(rf'\Adgeb((?: {types.Bias._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, biases: types.Tuple[types.Bias]):
        """
        Initializes ``Dgeb``.

        Parameters:
            biases: Delayed neutron energy biases.

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

        self.biases: typing.Final[types.Tuple[types.Bias]] = biases


@dataclasses.dataclass
class DgebBuilder(_option.ActOptionBuilder):
    """
    Builds ``Dgeb``.

    Attributes:
        biases: Delayed neutron energy biases.
    """

    biases: list[str] | list[types.Bias]

    def build(self):
        """
        Builds ``DgebBuilder`` into ``Dgeb``.

        Returns:
            ``Dgeb`` for ``DgebBuilder``.
        """

        if self.biases:
            biases = []
            for item in self.biases:
                if isinstance(item, types.Bias):
                    biases.append(item)
                elif isinstance(item, str):
                    biases.append(types.Bias.from_mcnp(item))
            biases = types.Tuple(biases)
        else:
            biases = None

        return Dgeb(
            biases=biases,
        )

    @staticmethod
    def unbuild(ast: Dgeb):
        """
        Unbuilds ``Dgeb`` into ``DgebBuilder``

        Returns:
            ``DgebBuilder`` for ``Dgeb``.
        """

        return DgebBuilder(
            biases=copy.deepcopy(ast.biases),
        )
