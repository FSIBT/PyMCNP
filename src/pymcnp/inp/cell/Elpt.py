import re

from . import _option
from ... import types
from ... import errors


class Elpt(_option.CellOption):
    """
    Represents INP `elpt` elements.
    """

    _KEYWORD = 'elpt'

    _ATTRS = {
        'designator': types.Designator,
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Aelpt:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, designator: str | types.Designator, cutoff: str | int | float | types.Real):
        """
        Initializes `Elpt`.

        Parameters:
            designator: Cell particle designator.
            cutoff: Cell energy cutoff.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.designator: types.Designator = designator
        self.cutoff: types.Real = cutoff

    @property
    def designator(self) -> types.Designator:
        """
        Cell particle designator

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Cell particle designator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self._designator: types.Designator = designator

    @property
    def cutoff(self) -> types.Real:
        """
        Cell energy cutoff

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
            cutoff: Cell energy cutoff.

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
