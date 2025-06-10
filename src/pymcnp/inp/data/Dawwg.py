import re
import copy
import typing
import dataclasses


from . import dawwg
from . import _option
from ...utils import types


class Dawwg(_option.DataOption):
    """
    Represents INP dawwg elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'dawwg'

    _ATTRS = {
        'options': types.Tuple[dawwg.DawwgOption],
    }

    _REGEX = re.compile(rf'\Adawwg((?: (?:{dawwg.DawwgOption._REGEX.pattern[2:-2]}))+?)?\Z')

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
class DawwgBuilder(_option.DataOptionBuilder):
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
                elif isinstance(item, dawwg.DawwgOptionBuilder):
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

        return DawwgBuilder(
            options=copy.deepcopy(ast.options),
        )
