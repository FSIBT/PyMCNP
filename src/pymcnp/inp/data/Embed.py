import re
import typing
import dataclasses


from . import embed
from .option_ import DataOption_
from ...utils import types


class Embed(DataOption_, keyword='embed'):
    """
    Represents INP embed elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[embed.EmbedOption_],
    }

    _REGEX = re.compile(rf'\Aembed((?: (?:{embed.EmbedOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[embed.EmbedOption_] = None):
        """
        Initializes ``Embed``.

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

        self.options: typing.Final[types.Tuple[embed.EmbedOption_]] = options


@dataclasses.dataclass
class EmbedBuilder:
    """
    Builds ``Embed``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[embed.EmbedOption_] = None

    def build(self):
        """
        Builds ``EmbedBuilder`` into ``Embed``.

        Returns:
            ``Embed`` for ``EmbedBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, embed.EmbedOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(embed.EmbedOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Embed(
            options=options,
        )
