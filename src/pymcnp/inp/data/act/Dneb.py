import re
import typing
import dataclasses


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Dneb(ActOption_, keyword='dneb'):
    """
    Represents INP dneb elements.

    Attributes:
        biases: Delayed neutron energy biases.
    """

    _ATTRS = {
        'biases': types.Tuple[types.Bias],
    }

    _REGEX = re.compile(rf'\Adneb((?: {types.Bias._REGEX.pattern})+?)\Z')

    def __init__(self, biases: types.Tuple[types.Bias]):
        """
        Initializes ``Dneb``.

        Parameters:
            biases: Delayed neutron energy biases.

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

        self.biases: typing.Final[types.Tuple[types.Bias]] = biases


@dataclasses.dataclass
class DnebBuilder:
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

        biases = []
        for item in self.biases:
            if isinstance(item, types.Bias):
                biases.append(item)
            elif isinstance(item, str):
                biases.append(types.Bias.from_mcnp(item))
            else:
                biases.append(item.build())
        biases = types.Tuple(biases)

        return Dneb(
            biases=biases,
        )
