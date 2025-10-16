import re

from . import dgeb
from . import _option
from ... import types
from ... import errors


class Dgeb(_option.ActOption):
    """
    Represents INP `dgeb` elements.
    """

    _KEYWORD = 'dgeb'

    _ATTRS = {
        'biases': types.Tuple(dgeb.Bias),
    }

    _REGEX = re.compile(rf'\Adgeb((?: {dgeb.Bias._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, biases: list[str] | list[dgeb.Bias]):
        """
        Initializes `Dgeb`.

        Parameters:
            biases: Delayed neutron energy biases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.biases: types.Tuple(dgeb.Bias) = biases

    @property
    def biases(self) -> types.Tuple(dgeb.Bias):
        """
        Delayed neutron energy biases

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._biases

    @biases.setter
    def biases(self, biases: list[str] | list[dgeb.Bias]) -> None:
        """
        Sets `biases`.

        Parameters:
            biases: Delayed neutron energy biases.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if biases is not None:
            array = []
            for item in biases:
                if isinstance(item, dgeb.Bias):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(dgeb.Bias.from_mcnp(item))
            biases = types.Tuple(dgeb.Bias)(array)

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self._biases: types.Tuple(dgeb.Bias) = biases
