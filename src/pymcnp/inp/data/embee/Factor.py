import re

from . import _option
from ....utils import types
from ....utils import errors


class Factor(_option.EmbeeOption):
    """
    Represents INP factor elements.

    Attributes:
        constant: Multiplicative constant.
    """

    _KEYWORD = 'factor'

    _ATTRS = {
        'constant': types.Real,
    }

    _REGEX = re.compile(rf'\Afactor( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, constant: str | int | float | types.Real):
        """
        Initializes ``Factor``.

        Parameters:
            constant: Multiplicative constant.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.constant: types.Real = constant

    @property
    def constant(self) -> types.Real:
        """
        Gets ``constant``.

        Returns:
            ``constant``.
        """

        return self._constant

    @constant.setter
    def constant(self, constant: str | int | float | types.Real) -> None:
        """
        Sets ``constant``.

        Parameters:
            constant: Multiplicative constant.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if constant is not None:
            if isinstance(constant, types.Real):
                constant = constant
            elif isinstance(constant, int):
                constant = types.Real(constant)
            elif isinstance(constant, float):
                constant = types.Real(constant)
            elif isinstance(constant, str):
                constant = types.Real.from_mcnp(constant)
            else:
                raise TypeError

        if constant is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, constant)

        self._constant: types.Real = constant
