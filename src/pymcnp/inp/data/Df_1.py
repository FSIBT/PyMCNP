import re
import typing
import dataclasses


from . import df_1
from ._option import DataOption
from ...utils import types
from ...utils import errors


class Df_1(DataOption):
    """
    Represents INP df variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[df_1.DfOption_1],
    }

    _REGEX = re.compile(rf'\Adf(\d+)((?: (?:{df_1.DfOption_1._REGEX.pattern}))+?)\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[df_1.DfOption_1]):
        """
        Initializes ``Df_1``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if options is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, options)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[types.Tuple[df_1.DfOption_1]] = options


@dataclasses.dataclass
class DfBuilder_1:
    """
    Builds ``Df_1``.

    Attributes:
        suffix: Data card option suffix.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    options: list[str] | list[df_1.DfOption_1]

    def build(self):
        """
        Builds ``DfBuilder_1`` into ``Df_1``.

        Returns:
            ``Df_1`` for ``DfBuilder_1``.
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
                if isinstance(item, df_1.DfOption_1):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(df_1.DfOption_1.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Df_1(
            suffix=suffix,
            options=options,
        )
