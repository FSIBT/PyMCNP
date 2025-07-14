import re

from . import ssw
from . import _option
from ...utils import types
from ...utils import errors


class Ssw(_option.DataOption):
    """
    Represents INP ssw elements.
    """

    _KEYWORD = 'ssw'

    _ATTRS = {
        'surfaces': types.Tuple[types.Integer],
        'cells': types.Tuple[types.Integer],
        'options': types.Tuple[ssw.SswOption],
    }

    _REGEX = re.compile(rf'\Assw((?: {types.Integer._REGEX.pattern[2:-2]})+?)((?: {types.Integer._REGEX.pattern[2:-2]})+?)?((?: (?:{ssw.SswOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, surfaces: list[str] | list[int] | list[types.Integer], cells: list[str] | list[int] | list[types.Integer] = None, options: list[str] | list[ssw.SswOption] = None):
        """
        Initializes ``Ssw``.

        Parameters:
            surfaces: Problem surfaces.
            cells: Problem cells.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.surfaces: types.Tuple[types.Integer] = surfaces
        self.cells: types.Tuple[types.Integer] = cells
        self.options: types.Tuple[ssw.SswOption] = options

    @property
    def surfaces(self) -> types.Tuple[types.Integer]:
        """
        Problem surfaces

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._surfaces

    @surfaces.setter
    def surfaces(self, surfaces: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``surfaces``.

        Parameters:
            surfaces: Problem surfaces.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if surfaces is not None:
            array = []
            for item in surfaces:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            surfaces = types.Tuple(array)

        if surfaces is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, surfaces)

        self._surfaces: types.Tuple[types.Integer] = surfaces

    @property
    def cells(self) -> types.Tuple[types.Integer]:
        """
        Problem cells

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cells

    @cells.setter
    def cells(self, cells: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``cells``.

        Parameters:
            cells: Problem cells.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cells is not None:
            array = []
            for item in cells:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            cells = types.Tuple(array)

        self._cells: types.Tuple[types.Integer] = cells

    @property
    def options(self) -> types.Tuple[ssw.SswOption]:
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[ssw.SswOption]) -> None:
        """
        Sets ``options``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, ssw.SswOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(ssw.SswOption.from_mcnp(item))
            options = types.Tuple(array)

        self._options: types.Tuple[ssw.SswOption] = options
