import re
import copy
import typing
import dataclasses


from . import t_1
from . import _option
from ...utils import types
from ...utils import errors


class T_1(_option.DataOption):
    """
    Represents INP t variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    _KEYWORD = 't'

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[t_1.TOption_1],
    }

    _REGEX = re.compile(rf'\At(\d+)((?: (?:{t_1.TOption_1._REGEX.pattern[2:-2]}))+?)\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[t_1.TOption_1]):
        """
        Initializes ``T_1``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if options is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, options)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[types.Tuple[t_1.TOption_1]] = options


@dataclasses.dataclass
class TBuilder_1(_option.DataOptionBuilder):
    """
    Builds ``T_1``.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    options: list[str] | list[t_1.TOption_1]

    def build(self):
        """
        Builds ``TBuilder_1`` into ``T_1``.

        Returns:
            ``T_1`` for ``TBuilder_1``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, t_1.TOption_1):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(t_1.TOption_1.from_mcnp(item))
                elif isinstance(item, t_1.TOptionBuilder_1):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return T_1(
            suffix=suffix,
            options=options,
        )

    @staticmethod
    def unbuild(ast: T_1):
        """
        Unbuilds ``T_1`` into ``TBuilder_1``

        Returns:
            ``TBuilder_1`` for ``T_1``.
        """

        return TBuilder_1(
            suffix=copy.deepcopy(ast.suffix),
            options=copy.deepcopy(ast.options),
        )
