import re
import copy
import typing
import dataclasses


from . import embee
from ._option import DataOption
from ...utils import types
from ...utils import errors


class Embee(DataOption):
    """
    Represents INP embee elements.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    _KEYWORD = 'embee'

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[embee.EmbeeOption],
    }

    _REGEX = re.compile(rf'\Aembee(\d+)((?: (?:{embee.EmbeeOption._REGEX.pattern}))+?)?\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[embee.EmbeeOption] = None):
        """
        Initializes ``Embee``.

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
        self.options: typing.Final[types.Tuple[embee.EmbeeOption]] = options


@dataclasses.dataclass
class EmbeeBuilder:
    """
    Builds ``Embee``.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    options: list[str] | list[embee.EmbeeOption] = None

    def build(self):
        """
        Builds ``EmbeeBuilder`` into ``Embee``.

        Returns:
            ``Embee`` for ``EmbeeBuilder``.
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
                if isinstance(item, embee.EmbeeOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(embee.EmbeeOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Embee(
            suffix=suffix,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Embee):
        """
        Unbuilds ``Embee`` into ``EmbeeBuilder``

        Returns:
            ``EmbeeBuilder`` for ``Embee``.
        """

        return Embee(
            suffix=copy.deepcopy(ast.suffix),
            options=copy.deepcopy(ast.options),
        )
