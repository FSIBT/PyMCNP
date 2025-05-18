import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Libname(BlockOption):
    """
    Represents INP libname elements.

    Attributes:
        setting: Cross-section file name.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Alibname( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Libname``.

        Parameters:
            setting: Cross-section file name.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class LibnameBuilder:
    """
    Builds ``Libname``.

    Attributes:
        setting: Cross-section file name.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``LibnameBuilder`` into ``Libname``.

        Returns:
            ``Libname`` for ``LibnameBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Libname(
            setting=setting,
        )
