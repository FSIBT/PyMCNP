import re
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Atom(EmbeeOption):
    """
    Represents INP atom elements.

    Attributes:
        setting: Flag to multiply by atom density.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aatom( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Atom``.

        Parameters:
            setting: Flag to multiply by atom density.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class AtomBuilder:
    """
    Builds ``Atom``.

    Attributes:
        setting: Flag to multiply by atom density.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``AtomBuilder`` into ``Atom``.

        Returns:
            ``Atom`` for ``AtomBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Atom(
            setting=setting,
        )
