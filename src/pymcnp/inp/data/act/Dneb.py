import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Dneb(_option.ActOption):
    """
    Represents INP dneb elements.

    Attributes:
        biases: Delayed neutron energy biases.
    """

    _KEYWORD = 'dneb'

    _ATTRS = {
        'biases': types.Tuple[types.Bias],
    }

    _REGEX = re.compile(rf'\Adneb((?: {types.Bias._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, biases: types.Tuple[types.Bias]):
        """
        Initializes ``Dneb``.

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
class DnebBuilder(_option.ActOptionBuilder):
    """
    Builds ``Dneb``.

    Attributes:
        biases: Delayed neutron energy biases.
    """

    biases: list[str] | list[types.Bias]

    def build(self):
        """
        Builds ``DnebBuilder`` into ``Dneb``.

        Returns:
            ``Dneb`` for ``DnebBuilder``.
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

        return Dneb(
            biases=biases,
        )

    @staticmethod
    def unbuild(ast: Dneb):
        """
        Unbuilds ``Dneb`` into ``DnebBuilder``

        Returns:
            ``DnebBuilder`` for ``Dneb``.
        """

        return DnebBuilder(
            biases=copy.deepcopy(ast.biases),
        )
