import re

from . import _option
from ....utils import types
from ....utils import errors


class Value(_option.PtracOption):
    """
    Represents INP value elements.

    Attributes:
        cutoff: Specifies tally cutoff above which history events will be written..
    """

    _KEYWORD = 'value'

    _ATTRS = {
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Avalue( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, cutoff: str | int | float | types.Real):
        """
        Initializes ``Value``.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cutoff: types.Real = cutoff

    @property
    def cutoff(self) -> types.Real:
        """
        Gets ``cutoff``.

        Returns:
            ``cutoff``.
        """

        return self._cutoff

    @cutoff.setter
    def cutoff(self, cutoff: str | int | float | types.Real) -> None:
        """
        Sets ``cutoff``.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cutoff is not None:
            if isinstance(cutoff, types.Real):
                cutoff = cutoff
            elif isinstance(cutoff, int):
                cutoff = types.Real(cutoff)
            elif isinstance(cutoff, float):
                cutoff = types.Real(cutoff)
            elif isinstance(cutoff, str):
                cutoff = types.Real.from_mcnp(cutoff)
            else:
                raise TypeError

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff)

        self._cutoff: types.Real = cutoff
