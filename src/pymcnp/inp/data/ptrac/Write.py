import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Write(PtracOption):
    """
    Represents INP write elements.

    Attributes:
        setting: Controls what particle parameters are written.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'\Awrite(?: (pos|all))\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Write``.

        Parameters:
            setting: Controls what particle parameters are written.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'pos', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class WriteBuilder:
    """
    Builds ``Write``.

    Attributes:
        setting: Controls what particle parameters are written.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``WriteBuilder`` into ``Write``.

        Returns:
            ``Write`` for ``WriteBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Write(
            setting=setting,
        )
