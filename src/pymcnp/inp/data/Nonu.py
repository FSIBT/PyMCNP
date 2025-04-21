import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Nonu(DataOption, keyword='nonu'):
    """
    Represents INP nonu elements.

    Attributes:
        settings: Tuple of fission settings.
    """

    _ATTRS = {
        'settings': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Anonu((?: {types.IntegerOrJump._REGEX.pattern})+?)?\Z')

    def __init__(self, settings: types.Tuple[types.IntegerOrJump] = None):
        """
        Initializes ``Nonu``.

        Parameters:
            settings: Tuple of fission settings.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if settings is not None and not (
            filter(lambda entry: not (entry == 0 or entry == 1 or entry == 2), settings)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, settings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.settings: typing.Final[types.Tuple[types.IntegerOrJump]] = settings


@dataclasses.dataclass
class NonuBuilder:
    """
    Builds ``Nonu``.

    Attributes:
        settings: Tuple of fission settings.
    """

    settings: list[str] | list[int] | list[types.IntegerOrJump] = None

    def build(self):
        """
        Builds ``NonuBuilder`` into ``Nonu``.

        Returns:
            ``Nonu`` for ``NonuBuilder``.
        """

        settings = []
        for item in self.settings:
            if isinstance(item, types.IntegerOrJump):
                settings.append(item)
            elif isinstance(item, int):
                settings.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                settings.append(types.IntegerOrJump.from_mcnp(item))
        settings = types.Tuple(settings)

        return Nonu(
            settings=settings,
        )
