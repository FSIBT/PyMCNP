import re

from . import _option
from ... import types
from ... import errors


class Value(_option.PtracOption):
    """
    Represents INP `value` elements.
    """

    _KEYWORD = 'value'

    _ATTRS = {
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Avalue( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, cutoff: str | int | float | types.Real):
        """
        Initializes `Value`.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cutoff: types.Real = cutoff

    @property
    def cutoff(self) -> types.Real:
        """
        Specifies tally cutoff above which history events will be written.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cutoff

    @cutoff.setter
    def cutoff(self, cutoff: str | int | float | types.Real) -> None:
        """
        Sets `cutoff`.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cutoff is not None:
            if isinstance(cutoff, types.Real):
                cutoff = cutoff
            elif isinstance(cutoff, int) or isinstance(cutoff, float):
                cutoff = types.Real(cutoff)
            elif isinstance(cutoff, str):
                cutoff = types.Real.from_mcnp(cutoff)

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff)

        self._cutoff: types.Real = cutoff
