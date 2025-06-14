import re
import copy
import typing
import dataclasses


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

    def __init__(self, options: types.Tuple[mesh.MeshOption] = None):
        """
        Initializes ``Mesh``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.options: typing.Final[types.Tuple[mesh.MeshOption]] = options


@dataclasses.dataclass
class MeshBuilder(_option.DataOptionBuilder):
    """
    Builds ``Mesh``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[mesh.MeshOption] = None

    def build(self):
        """
        Builds ``MeshBuilder`` into ``Mesh``.

        Returns:
            ``Mesh`` for ``MeshBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, mesh.MeshOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(mesh.MeshOption.from_mcnp(item))
                elif isinstance(item, mesh.MeshOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Mesh(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Mesh):
        """
        Unbuilds ``Mesh`` into ``MeshBuilder``

        Returns:
            ``MeshBuilder`` for ``Mesh``.
        """

        return MeshBuilder(
            options=copy.deepcopy(ast.options),
        )
