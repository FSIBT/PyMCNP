import re
import copy
import typing
import dataclasses


from . import embed
from ._option import DataOption
from ...utils import types
from ...utils import errors


class Embed(DataOption):
    """
    Represents INP embed elements.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    _KEYWORD = 'embed'

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[embed.EmbedOption],
    }

    _REGEX = re.compile(rf'\Aembed(\d+)?((?: (?:{embed.EmbedOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[embed.EmbedOption] = None):
        """
        Initializes ``Embed``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[types.Tuple[embed.EmbedOption]] = options


@dataclasses.dataclass
class EmbedBuilder:
    """
    Builds ``Embed``.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    options: list[str] | list[embed.EmbedOption] = None

    def build(self):
        """
        Builds ``EmbedBuilder`` into ``Embed``.

        Returns:
            ``Embed`` for ``EmbedBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

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
            suffix=suffix,
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
            suffix=copy.deepcopy(ast.suffix),
            options=copy.deepcopy(ast.options),
        )
