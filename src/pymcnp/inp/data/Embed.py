import re
import copy
import typing
import dataclasses


from . import embed
from ._option import DataOption
from ...utils import types


class Embed(DataOption):
    """
    Represents INP embed elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'embed'

    _ATTRS = {
        'options': types.Tuple[embed.EmbedOption],
    }

    _REGEX = re.compile(rf'\Aembed((?: (?:{embed.EmbedOption._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[embed.EmbedOption] = None):
        """
        Initializes ``Embed``.

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

        self.options: typing.Final[types.Tuple[embed.EmbedOption]] = options


@dataclasses.dataclass
class EmbedBuilder:
    """
    Builds ``Embed``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[embed.EmbedOption] = None

    def build(self):
        """
        Builds ``EmbedBuilder`` into ``Embed``.

        Returns:
            ``Embed`` for ``EmbedBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, embed.EmbedOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(embed.EmbedOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Embed(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Embed):
        """
        Unbuilds ``Embed`` into ``EmbedBuilder``

        Returns:
            ``EmbedBuilder`` for ``Embed``.
        """

        return Embed(
            options=copy.deepcopy(ast.options),
        )
