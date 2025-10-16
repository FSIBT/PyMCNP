import re

from . import _option
from ... import types
from ... import errors


class Fcl(_option.LikeOption):
    """
    Represents INP `fcl` elements.
    """

    _KEYWORD = 'fcl'

    _ATTRS = {
        'designator': types.Designator,
        'control': types.Real,
    }

    _REGEX = re.compile(rf'\Afcl:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, designator: str | types.Designator, control: str | int | float | types.Real):
        """
        Initializes `Fcl`.

        Parameters:
            designator: Cell particle designator.
            control: Cell forced-collision control.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.designator: types.Designator = designator
        self.control: types.Real = control

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
    def control(self) -> types.Real:
        """
        Gets `control`.

        Returns:
            `control`.
        """

        return self._control

    @control.setter
    def control(self, control: str | int | float | types.Real) -> None:
        """
        Sets `control`.

        Parameters:
            control: Cell forced-collision control.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if control is not None:
            if isinstance(control, types.Real):
                control = control
            elif isinstance(control, int) or isinstance(control, float):
                control = types.Real(control)
            elif isinstance(control, str):
                control = types.Real.from_mcnp(control)

        if control is None or not (control >= -1 and control <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, control)

        self._control: types.Real = control
