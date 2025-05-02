import re
import typing
import dataclasses


from . import mesh
from ._option import DataOption
from ...utils import types


class Mesh(DataOption):
    """
    Represents INP mesh elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[mesh.MeshOption],
    }

    _REGEX = re.compile(rf'\Amesh((?: (?:{mesh.MeshOption._REGEX.pattern}))+?)?\Z')

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
class MeshBuilder:
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

        options = []
        for item in self.options:
            if isinstance(item, mesh.MeshOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(mesh.MeshOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Mesh(
            options=options,
        )
