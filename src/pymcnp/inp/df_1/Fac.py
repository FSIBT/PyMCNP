import re

from . import _option
from ... import types
from ... import errors


class Fac(_option.DfOption_1):
    """
    Represents INP `fac` elements.
    """

    _KEYWORD = 'fac'

    _ATTRS = {
        'normalization': types.Integer,
    }

    _REGEX = re.compile(rf'\Afac( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, normalization: str | int | types.Integer):
        """
        Initializes `Fac`.

        Parameters:
            normalization: Normalization factor for dose.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.normalization: types.Integer = normalization

    @property
    def normalization(self) -> types.Integer:
        """
        Normalization factor for dose

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._normalization

    @normalization.setter
    def normalization(self, normalization: str | int | types.Integer) -> None:
        """
        Sets `normalization`.

        Parameters:
            normalization: Normalization factor for dose.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if normalization is not None:
            if isinstance(normalization, types.Integer):
                normalization = normalization
            elif isinstance(normalization, int):
                normalization = types.Integer(normalization)
            elif isinstance(normalization, str):
                normalization = types.Integer.from_mcnp(normalization)

        if normalization is None or not (isinstance(normalization.value, types.Jump) or normalization >= -3):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, normalization)

        self._normalization: types.Integer = normalization
