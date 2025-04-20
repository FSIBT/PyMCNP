import re
import typing
import dataclasses


from . import t_1
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class T_1(DataOption_, keyword='t'):
    """
    Represents INP t variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        options: Data card options.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[t_1.T_1Option_],
    }

    _REGEX = re.compile(rf'\At(\d+)((?: (?:{t_1.T_1Option_._REGEX.pattern}))+?)\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[t_1.T_1Option_]):
        """
        Initializes ``T_1``.

        Parameters:
            suffix: Data card option suffix.
            options: Data card options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if options is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, options)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[types.Tuple[t_1.T_1Option_]] = options


@dataclasses.dataclass
class TBuilder_1:
    """
    Builds ``T_1``.

    Attributes:
        suffix: Data card option suffix.
        options: Data card options.
    """

    suffix: str | int | types.Integer
    options: list[str] | list[t_1.T_1Option_]

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
            if isinstance(item, t_1.T_1Option_):
                options.append(item)
            elif isinstance(item, str):
                options.append(t_1.T_1Option_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return T_1(
            suffix=suffix,
            options=options,
        )
