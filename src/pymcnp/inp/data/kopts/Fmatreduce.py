import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Fmatreduce(_option.KoptsOption):
    """
    Represents INP fmatreduce elements.

    Attributes:
        setting: fmatreduce.
    """

    _KEYWORD = 'fmatreduce'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Afmatreduce( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Fmatreduce``.

        Parameters:
            setting: fmatreduce.

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
class FmatreduceBuilder(_option.KoptsOptionBuilder):
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

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Fmatreduce(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Fmatreduce):
        """
        Unbuilds ``Fmatreduce`` into ``FmatreduceBuilder``

        Returns:
            ``FmatreduceBuilder`` for ``Fmatreduce``.
        """

        return FmatreduceBuilder(
            setting=copy.deepcopy(ast.setting),
        )
