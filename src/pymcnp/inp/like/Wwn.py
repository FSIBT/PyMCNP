import re

from . import _option
from ... import types
from ... import errors


class Wwn(_option.LikeOption):
    """
    Represents INP `wwn` elements.
    """

    _KEYWORD = 'wwn'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'bound': types.Real,
    }

    _REGEX = re.compile(rf'\Awwn(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, designator: str | types.Designator, bound: str | int | float | types.Real):
        """
        Initializes `Wwn`.

        Parameters:
            suffix: Cell option suffix.
            designator: Cell particle designator.
            bound: Cell weight-window space, time, or energy lower bound.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.designator: types.Designator = designator
        self.bound: types.Real = bound

    @property
    def suffix(self) -> types.Integer:
        """
        Gets `suffix`.

        Returns:
            `suffix`.
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Cell option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def designator(self) -> types.Designator:
        """
        Gets `designator`.

        Returns:
            `designator`.
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
    def bound(self) -> types.Real:
        """
        Gets `bound`.

        Returns:
            `bound`.
        """

        return self._bound

    @bound.setter
    def bound(self, bound: str | int | float | types.Real) -> None:
        """
        Sets `bound`.

        Parameters:
            bound: Cell weight-window space, time, or energy lower bound.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if bound is not None:
            if isinstance(bound, types.Real):
                bound = bound
            elif isinstance(bound, int) or isinstance(bound, float):
                bound = types.Real(bound)
            elif isinstance(bound, str):
                bound = types.Real.from_mcnp(bound)

        if bound is None or not (bound == -1 or bound >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bound)

        self._bound: types.Real = bound
