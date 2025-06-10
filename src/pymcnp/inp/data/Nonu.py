import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Nonu(_option.DataOption):
    """
    Represents INP nonu elements.

    Attributes:
        settings: Tuple of fission settings.
    """

    _KEYWORD = 'nonu'

    _ATTRS = {
        'settings': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Anonu((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z')

    def __init__(self, settings: types.Tuple[types.Integer] = None):
        """
        Initializes ``Nonu``.

        Parameters:
            settings: Tuple of fission settings.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.settings: typing.Final[types.Tuple[types.Integer]] = settings


@dataclasses.dataclass
class NonuBuilder(_option.DataOptionBuilder):
    """
    Builds ``Nonu``.

    Attributes:
        settings: Tuple of fission settings.
    """

    settings: list[str] | list[int] | list[types.Integer] = None

    def build(self):
        """
        Builds ``NonuBuilder`` into ``Nonu``.

        Returns:
            ``Nonu`` for ``NonuBuilder``.
        """

        if self.settings:
            settings = []
            for item in self.settings:
                if isinstance(item, types.Integer):
                    settings.append(item)
                elif isinstance(item, int):
                    settings.append(types.Integer(item))
                elif isinstance(item, str):
                    settings.append(types.Integer.from_mcnp(item))
            settings = types.Tuple(settings)
        else:
            settings = None

        return Nonu(
            settings=settings,
        )

    @staticmethod
    def unbuild(ast: Nonu):
        """
        Unbuilds ``Nonu`` into ``NonuBuilder``

        Returns:
            ``NonuBuilder`` for ``Nonu``.
        """

        return NonuBuilder(
            settings=copy.deepcopy(ast.settings),
        )
