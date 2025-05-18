import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Unc(DataOption):
    """
    Represents INP unc elements.

    Attributes:
        settings: Tuple of uncollided secondary settings.
    """

    _ATTRS = {
        'settings': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Aunc((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, settings: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Unc``.

        Parameters:
            settings: Tuple of uncollided secondary settings.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if settings is None or not (filter(lambda entry: entry.value not in {0, 1}, settings)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, settings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.settings: typing.Final[types.Tuple[types.IntegerOrJump]] = settings


@dataclasses.dataclass
class UncBuilder:
    """
    Builds ``Unc``.

    Attributes:
        settings: Tuple of uncollided secondary settings.
    """

    settings: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``UncBuilder`` into ``Unc``.

        Returns:
            ``Unc`` for ``UncBuilder``.
        """

        if self.settings:
            settings = []
            for item in self.settings:
                if isinstance(item, types.IntegerOrJump):
                    settings.append(item)
                elif isinstance(item, int):
                    settings.append(types.IntegerOrJump(item))
                elif isinstance(item, str):
                    settings.append(types.IntegerOrJump.from_mcnp(item))
            settings = types.Tuple(settings)
        else:
            settings = None

        return Unc(
            settings=settings,
        )
