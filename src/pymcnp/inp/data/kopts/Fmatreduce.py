import re
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmatreduce(KoptsOption, keyword='fmatreduce'):
    """
    Represents INP fmatreduce elements.

    Attributes:
        setting: fmatreduce.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Afmatreduce( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Fmatreduce``.

        Parameters:
            setting: fmatreduce.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class FmatreduceBuilder:
    """
    Builds ``Fmatreduce``.

    Attributes:
        setting: fmatreduce.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``FmatreduceBuilder`` into ``Fmatreduce``.

        Returns:
            ``Fmatreduce`` for ``FmatreduceBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Fmatreduce(
            setting=setting,
        )
