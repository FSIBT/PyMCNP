import re
import copy
import typing
import dataclasses


from . import block
from . import _option
from ....utils import types
from ....utils import errors


class Block(_option.DawwgOption):
    """
    Represents INP block elements.

    Attributes:
        setting: Destination of key-value pairs.
        options: Dictionary of options.
    """

    _KEYWORD = 'block'

    _ATTRS = {
        'setting': types.Integer,
        'options': types.Tuple[block.BlockOption],
    }

    _REGEX = re.compile(rf'\Ablock( {types.Integer._REGEX.pattern[2:-2]})((?: (?:{block.BlockOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, setting: types.Integer, options: types.Tuple[block.BlockOption] = None):
        """
        Initializes ``Block``.

        Parameters:
            setting: Destination of key-value pairs.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {1, 3, 5, 6}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
                options,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting
        self.options: typing.Final[types.Tuple[block.BlockOption]] = options


@dataclasses.dataclass
class BlockBuilder(_option.DawwgOptionBuilder):
    """
    Builds ``Block``.

    Attributes:
        setting: Destination of key-value pairs.
        options: Dictionary of options.
    """

    setting: str | int | types.Integer
    options: list[str] | list[block.BlockOption] = None

    def build(self):
        """
        Builds ``BlockBuilder`` into ``Block``.

        Returns:
            ``Block`` for ``BlockBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, block.BlockOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(block.BlockOption.from_mcnp(item))
                elif isinstance(item, block.BlockOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Block(
            setting=setting,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Block):
        """
        Unbuilds ``Block`` into ``BlockBuilder``

        Returns:
            ``BlockBuilder`` for ``Block``.
        """

        return BlockBuilder(
            setting=copy.deepcopy(ast.setting),
            options=copy.deepcopy(ast.options),
        )
