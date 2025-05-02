import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class File(PtracOption):
    """
    Represents INP file elements.

    Attributes:
        setting: PTRAC file type.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Afile(?: (asc|bin|aov|bov))\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``File``.

        Parameters:
            setting: PTRAC file type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'asc', 'bin', 'aov', 'bov'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class FileBuilder:
    """
    Builds ``File``.

    Attributes:
        setting: PTRAC file type.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``FileBuilder`` into ``File``.

        Returns:
            ``File`` for ``FileBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return File(
            setting=setting,
        )
