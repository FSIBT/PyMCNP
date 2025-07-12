import re

from . import _option
from ...utils import types
from ...utils import errors


class Fcl(_option.DataOption):
    """
    Represents INP fcl elements.
    """

    _KEYWORD = 'fcl'

    _ATTRS = {
        'designator': types.Designator,
        'control': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Afcl:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: str | types.Designator, control: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Fcl``.

        Parameters:
            designator: Data card particle designator.
            control: Forced-collision control for cell.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.designator: types.Designator = designator
        self.control: types.Tuple[types.Real] = control

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets ``designator``.

        Parameters:
            designator: Data card particle designator.

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
    def control(self) -> types.Tuple[types.Real]:
        """
        Forced-collision control for cell

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._control

    @control.setter
    def control(self, control: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``control``.

        Parameters:
            control: Forced-collision control for cell.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if control is not None:
            array = []
            for item in control:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))

            control = types.Tuple(array)

        if control is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, control)

        self._control: types.Tuple[types.Real] = control
