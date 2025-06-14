import re
import copy
import typing
import dataclasses


from . import sdef
from . import _option
from ...utils import types


class Sdef(_option.DataOption):
    """
    Represents INP sdef elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'sdef'

    _ATTRS = {
        'options': types.Tuple[sdef.SdefOption],
    }

    _REGEX = re.compile(rf'\Asdef((?: (?:{sdef.SdefOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: types.Tuple[sdef.SdefOption] = None):
        """
        Initializes ``Sdef``.

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

        self.options: typing.Final[types.Tuple[sdef.SdefOption]] = options


@dataclasses.dataclass
class SdefBuilder(_option.DataOptionBuilder):
    """
    Builds ``Sdef``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[sdef.SdefOption] = None

    def build(self):
        """
        Builds ``SdefBuilder`` into ``Sdef``.

        Returns:
            ``Sdef`` for ``SdefBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, sdef.SdefOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(sdef.SdefOption.from_mcnp(item))
                elif isinstance(item, sdef.SdefOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Sdef(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Sdef):
        """
        Unbuilds ``Sdef`` into ``SdefBuilder``

        Returns:
            ``SdefBuilder`` for ``Sdef``.
        """

        return SdefBuilder(
            options=copy.deepcopy(ast.options),
        )
