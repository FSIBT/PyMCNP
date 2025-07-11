import re

from . import mesh
from . import _option
from ...utils import types


class Mesh(_option.DataOption):
    """
    Represents INP mesh elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'mesh'

    _ATTRS = {
        'options': types.Tuple[mesh.MeshOption],
    }

    _REGEX = re.compile(rf'\Amesh((?: (?:{mesh.MeshOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: list[str] | list[mesh.MeshOption] = None):
        """
        Initializes ``Mesh``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.options: types.Tuple[mesh.MeshOption] = options

    @property
    def options(self) -> types.Tuple[mesh.MeshOption]:
        """
        Gets ``options``.

        Returns:
            ``options``.
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[mesh.MeshOption]) -> None:
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
                if isinstance(item, mesh.MeshOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(mesh.MeshOption.from_mcnp(item))
                else:
                    raise TypeError
            options = types.Tuple(array)

        self._options: types.Tuple[mesh.MeshOption] = options
