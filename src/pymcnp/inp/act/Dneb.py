import re

from . import dneb
from . import _option
from ... import types
from ... import errors


class Dneb(_option.ActOption):
    """
    Represents INP `dneb` elements.
    """

    _KEYWORD = 'dneb'

    _ATTRS = {
        'biases': types.Tuple(dneb.Bias),
    }

    _REGEX = re.compile(rf'\Adneb((?: {dneb.Bias._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, biases: list[str] | list[dneb.Bias]):
        """
        Initializes `Dneb`.

        Parameters:
            biases: Delayed neutron energy biases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.biases: types.Tuple(dneb.Bias) = biases

    @property
    def biases(self) -> types.Tuple(dneb.Bias):
        """
        Delayed neutron energy biases

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._biases

    @biases.setter
    def biases(self, biases: list[str] | list[dneb.Bias]) -> None:
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
                if isinstance(item, dneb.Bias):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(dneb.Bias.from_mcnp(item))
            biases = types.Tuple(dneb.Bias)(array)

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self._biases: types.Tuple(dneb.Bias) = biases
