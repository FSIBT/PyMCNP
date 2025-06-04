import re
import copy
import typing
import dataclasses


from . import kpert
from ._option import DataOption
from ...utils import types
from ...utils import errors


class Kpert(DataOption):
    """
    Represents INP kpert elements.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    _KEYWORD = 'kpert'

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[kpert.KpertOption],
    }

    _REGEX = re.compile(rf'\Akpert(\d+)((?: (?:{kpert.KpertOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[kpert.KpertOption] = None):
        """
        Initializes ``Kpert``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (0 < suffix.value <= 10_000):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[types.Tuple[kpert.KpertOption]] = options


@dataclasses.dataclass
class KpertBuilder:
    """
    Builds ``Kpert``.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    options: list[str] | list[kpert.KpertOption] = None

    def build(self):
        """
        Builds ``KpertBuilder`` into ``Kpert``.

        Returns:
            ``Kpert`` for ``KpertBuilder``.
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
                if isinstance(item, kpert.KpertOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(kpert.KpertOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Kpert(
            suffix=suffix,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Kpert):
        """
        Unbuilds ``Kpert`` into ``KpertBuilder``

        Returns:
            ``KpertBuilder`` for ``Kpert``.
        """

        return Kpert(
            suffix=copy.deepcopy(ast.suffix),
            options=copy.deepcopy(ast.options),
        )
