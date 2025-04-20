import re
import typing
import dataclasses


from . import mesh
from .option_ import DataOption_
from ...utils import types


class Mesh(DataOption_, keyword='mesh'):
    """
    Represents INP mesh elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[mesh.MeshOption_],
    }

    _REGEX = re.compile(rf'\Amesh((?: (?:{mesh.MeshOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[mesh.MeshOption_] = None):
        """
        Initializes ``Mesh``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.options: typing.Final[types.Tuple[mesh.MeshOption_]] = options


@dataclasses.dataclass
class MeshBuilder:
    """
    Builds ``Mesh``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[mesh.MeshOption_] = None

    def build(self):
        """
        Builds ``MeshBuilder`` into ``Mesh``.

        Returns:
            ``Mesh`` for ``MeshBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, mesh.MeshOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(mesh.MeshOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Mesh(
            options=options,
        )
