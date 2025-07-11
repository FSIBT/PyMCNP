import re

from . import _option
from ....utils import types
from ....utils import errors


class Dneb(_option.ActOption):
    """
    Represents INP dneb elements.
    """

    _KEYWORD = 'dneb'

    _ATTRS = {
        'biases': types.Tuple[types.Bias],
    }

    _REGEX = re.compile(rf'\Adneb((?: {types.Bias._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, biases: list[str] | list[types.Bias]):
        """
        Initializes ``Dneb``.

        Parameters:
            biases: Delayed neutron energy biases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.biases: types.Tuple[types.Bias] = biases

    @property
    def biases(self) -> types.Tuple[types.Bias]:
        """
        Delayed neutron energy biases

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
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

            biases = types.Tuple(array)

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self._biases: types.Tuple[types.Bias] = biases
