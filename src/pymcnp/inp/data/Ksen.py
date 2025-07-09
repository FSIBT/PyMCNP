import re
import copy
import typing
import dataclasses


from . import ksen
from . import _option
from ...utils import types
from ...utils import errors


class Ksen(_option.DataOption):
    """
    Represents INP ksen elements.

    Attributes:
        suffix: Data card option suffix.
        sen: Type of sensitivity.
        options: Dictionary of options.
    """

    _KEYWORD = 'ksen'

    _ATTRS = {
        'suffix': types.Integer,
        'sen': types.String,
        'options': types.Tuple[ksen.KsenOption],
    }

    _REGEX = re.compile(rf'\Aksen(\d+)( {types.String._REGEX.pattern[2:-2]})((?: (?:{ksen.KsenOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, suffix: types.Integer, sen: types.String, options: types.Tuple[ksen.KsenOption] = None):
        """
        Initializes ``Ksen``.

        Parameters:
            suffix: Data card option suffix.
            sen: Type of sensitivity.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix > 0 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if sen is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, sen)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                sen,
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.sen: typing.Final[types.String] = sen
        self.options: typing.Final[types.Tuple[ksen.KsenOption]] = options


@dataclasses.dataclass
class KsenBuilder(_option.DataOptionBuilder):
    """
    Builds ``Ksen``.

    Attributes:
        suffix: Data card option suffix.
        sen: Type of sensitivity.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    sen: str | types.String
    options: list[str] | list[ksen.KsenOption] = None

    def build(self):
        """
        Builds ``KsenBuilder`` into ``Ksen``.

        Returns:
            ``Ksen`` for ``KsenBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        sen = self.sen
        if isinstance(self.sen, types.String):
            sen = self.sen
        elif isinstance(self.sen, str):
            sen = types.String.from_mcnp(self.sen)

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, ksen.KsenOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(ksen.KsenOption.from_mcnp(item))
                elif isinstance(item, ksen.KsenOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Ksen(
            suffix=suffix,
            sen=sen,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Ksen):
        """
        Unbuilds ``Ksen`` into ``KsenBuilder``

        Returns:
            ``KsenBuilder`` for ``Ksen``.
        """

        return KsenBuilder(
            suffix=copy.deepcopy(ast.suffix),
            sen=copy.deepcopy(ast.sen),
            options=copy.deepcopy(ast.options),
        )
