import re

from . import _option
from ...utils import types
from ...utils import errors


class Ext(_option.DataOption):
    """
    Represents INP ext elements.

    Attributes:
        designator: Data card particle designator.
        stretching: Stretching direction for the cell.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'designator': types.Designator,
        'stretching': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Aext:(\S+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: str | types.Designator, stretching: list[str] | list[types.String]):
        """
        Initializes ``Ext``.

        Parameters:
            designator: Data card particle designator.
            stretching: Stretching direction for the cell.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.designator: types.Designator = designator
        self.stretching: types.Tuple[types.String] = stretching

    @property
    def designator(self) -> types.Designator:
        """
        Gets ``designator``.

        Returns:
            ``designator``.
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
            else:
                raise TypeError

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self._designator: types.Designator = designator

    @property
    def stretching(self) -> types.Tuple[types.String]:
        """
        Gets ``stretching``.

        Returns:
            ``stretching``.
        """

        return self._stretching

    @stretching.setter
    def stretching(self, stretching: list[str] | list[types.String]) -> None:
        """
        Sets ``stretching``.

        Parameters:
            stretching: Stretching direction for the cell.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if stretching is not None:
            array = []
            for item in stretching:
                if isinstance(item, types.String):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.String.from_mcnp(item))
                else:
                    raise TypeError
            stretching = types.Tuple(array)

        if stretching is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, stretching)

        self._stretching: types.Tuple[types.String] = stretching
