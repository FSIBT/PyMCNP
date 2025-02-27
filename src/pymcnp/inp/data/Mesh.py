import re
import typing


from . import mesh
from .option_ import DataOption_
from ...utils import types


class Mesh(DataOption_, keyword='mesh'):
    """
    Represents INP mesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[mesh.MeshOption_],
    }

    _REGEX = re.compile(rf'mesh(( ({mesh.MeshOption_._REGEX.pattern}))+)?')

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
