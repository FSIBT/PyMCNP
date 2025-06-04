import re
import copy
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Sample(ActOption):
    """
    Represents INP sample elements.

    Attributes:
        setting: Flag for correlated or uncorrelated.
    """

    _KEYWORD = 'sample'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Asample( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Sample``.

        Parameters:
            setting: Flag for correlated or uncorrelated.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'correlate', 'nonfiss_cor'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class SampleBuilder:
    """
    Builds ``Sample``.

    Attributes:
        setting: Flag for correlated or uncorrelated.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``SampleBuilder`` into ``Sample``.

        Returns:
            ``Sample`` for ``SampleBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Sample(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Sample):
        """
        Unbuilds ``Sample`` into ``SampleBuilder``

        Returns:
            ``SampleBuilder`` for ``Sample``.
        """

        return Sample(
            setting=copy.deepcopy(ast.setting),
        )
