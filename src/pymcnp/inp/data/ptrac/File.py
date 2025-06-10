import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class File(_option.PtracOption):
    """
    Represents INP file elements.

    Attributes:
        setting: PTRAC file type.
    """

    _KEYWORD = 'file'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'\Afile(?: (asc|bin|aov|bov))\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``File``.

        Parameters:
            setting: PTRAC file type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'asc', 'bin', 'aov', 'bov'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class FileBuilder(_option.PtracOptionBuilder):
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

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return File(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: File):
        """
        Unbuilds ``File`` into ``FileBuilder``

        Returns:
            ``FileBuilder`` for ``File``.
        """

        return FileBuilder(
            setting=copy.deepcopy(ast.setting),
        )
