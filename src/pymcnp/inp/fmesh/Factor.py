import re

from . import _option
from ... import types
from ... import errors


class Factor(_option.FmeshOption):
    """
    Represents INP `factor` elements.
    """

    _KEYWORD = 'factor'

    _ATTRS = {
        'multiple': types.Real,
    }

    _REGEX = re.compile(rf'\Afactor( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, multiple: str | int | float | types.Real):
        """
        Initializes `Factor`.

        Parameters:
            multiple: Multiplicative factor for each mesh.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.multiple: types.Real = multiple

    @property
    def multiple(self) -> types.Real:
        """
        Multiplicative factor for each mesh

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._multiple

    @multiple.setter
    def multiple(self, multiple: str | int | float | types.Real) -> None:
        """
        Sets `multiple`.

        Parameters:
            multiple: Multiplicative factor for each mesh.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if multiple is not None:
            if isinstance(multiple, types.Real):
                multiple = multiple
            elif isinstance(multiple, int) or isinstance(multiple, float):
                multiple = types.Real(multiple)
            elif isinstance(multiple, str):
                multiple = types.Real.from_mcnp(multiple)

        if multiple is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, multiple)

        self._multiple: types.Real = multiple
