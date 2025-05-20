import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Nonu(DataOption):
    """
    Represents INP nonu elements.

    Attributes:
        settings: Tuple of fission settings.
    """

    _ATTRS = {
        'settings': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Anonu((?: {types.Integer._REGEX.pattern})+?)?\Z')

    def __init__(self, settings: types.Tuple[types.Integer] = None):
        """
        Initializes ``Nonu``.

        Parameters:
            settings: Tuple of fission settings.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if settings is not None and not (
            filter(
                lambda entry: not (entry.value == 0 or entry.value == 1 or entry.value == 2),
                settings,
            )
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, settings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.settings: typing.Final[types.Tuple[types.Integer]] = settings


@dataclasses.dataclass
class NonuBuilder:
    """
    Builds ``Nonu``.

    Attributes:
        settings: Tuple of fission settings.
    """

    settings: list[str] | list[int] | list[types.Integer] = None

    def build(self):
        """
        Builds ``NonuBuilder`` into ``Nonu``.

        Returns:
            ``Nonu`` for ``NonuBuilder``.
        """

        if self.settings:
            settings = []
            for item in self.settings:
                if isinstance(item, types.Integer):
                    settings.append(item)
                elif isinstance(item, int):
                    settings.append(types.Integer(item))
                elif isinstance(item, str):
                    settings.append(types.Integer.from_mcnp(item))
            settings = types.Tuple(settings)
        else:
            settings = None

        return Nonu(
            settings=settings,
        )
