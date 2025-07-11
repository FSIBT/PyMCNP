import re

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

    def __init__(self, biases: list[str] | list[types.Bias]):
        """
        Initializes ``Dgeb``.

        Parameters:
            biases: Delayed neutron energy biases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.biases: types.Tuple[types.Bias] = biases

    @property
    def biases(self) -> types.Tuple[types.Bias]:
        """
        Gets ``biases``.

        Returns:
            ``biases``.
        """

        return self._biases

    @biases.setter
    def biases(self, biases: list[str] | list[types.Bias]) -> None:
        """
        Sets ``biases``.

        Parameters:
            biases: Delayed neutron energy biases.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if biases is not None:
            array = []
            for item in biases:
                if isinstance(item, types.Bias):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Bias.from_mcnp(item))
                else:
                    raise TypeError
            biases = types.Tuple(array)

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self._biases: types.Tuple[types.Bias] = biases
