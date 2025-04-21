import re
import typing
import dataclasses


from . import t_1
from ._option import DataOption
from ...utils import types
from ...utils import errors


class T_1(DataOption, keyword='t'):
    """
    Represents INP t variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        options: Data card options.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[t_1.T_1Option],
    }

    _REGEX = re.compile(rf'\At(\d+)((?: (?:{t_1.T_1Option._REGEX.pattern}))+?)\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[t_1.T_1Option]):
        """
        Initializes ``T_1``.

        Parameters:
            suffix: Data card option suffix.
            options: Data card options.

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
        self.options: typing.Final[types.Tuple[t_1.T_1Option]] = options


@dataclasses.dataclass
class TBuilder_1:
    """
    Builds ``T_1``.

    Attributes:
        suffix: Data card option suffix.
        options: Data card options.
    """

    suffix: str | int | types.Integer
    options: list[str] | list[t_1.T_1Option]

    def build(self):
        """
        Builds ``TBuilder_1`` into ``T_1``.

        Returns:
            ``T_1`` for ``TBuilder_1``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        options = []
        for item in self.options:
            if isinstance(item, t_1.T_1Option):
                options.append(item)
            elif isinstance(item, str):
                options.append(t_1.T_1Option.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return T_1(
            suffix=suffix,
            options=options,
        )
