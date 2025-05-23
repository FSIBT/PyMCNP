import re
import copy
import typing
import dataclasses


from . import dawwg
from ._option import DataOption
from ...utils import types


class Dawwg(DataOption):
    """
    Represents INP dawwg elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'dawwg'

    _ATTRS = {
        'options': types.Tuple[dawwg.DawwgOption],
    }

    _REGEX = re.compile(rf'\Adawwg((?: (?:{dawwg.DawwgOption._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[dawwg.DawwgOption] = None):
        """
        Initializes ``Dawwg``.

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

        self.options: typing.Final[types.Tuple[dawwg.DawwgOption]] = options


@dataclasses.dataclass
class DawwgBuilder:
    """
    Builds ``Dawwg``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[dawwg.DawwgOption] = None

    def build(self):
        """
        Builds ``DawwgBuilder`` into ``Dawwg``.

        Returns:
            ``Dawwg`` for ``DawwgBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, dawwg.DawwgOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(dawwg.DawwgOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Dawwg(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Dawwg):
        """
        Unbuilds ``Dawwg`` into ``DawwgBuilder``

        Returns:
            ``DawwgBuilder`` for ``Dawwg``.
        """

        return Dawwg(
            options=copy.deepcopy(ast.options),
        )
