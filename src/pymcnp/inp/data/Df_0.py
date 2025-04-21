import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Df_0(DataOption, keyword='df'):
    """
    Represents INP df variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        method: Interpolation method for dose function table.
        values: Dose function values.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'method': types.String,
        'values': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Adf(\d+)( (?:log|lin))?((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(
        self,
        suffix: types.Integer,
        values: types.Tuple[types.RealOrJump],
        method: types.String = None,
    ):
        """
        Initializes ``Df_0``.

        Parameters:
            suffix: Data card option suffix.
            method: Interpolation method for dose function table.
            values: Dose function values.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if method is not None and method not in {'log', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, method)
        if values is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, values)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                method,
                values,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.method: typing.Final[types.String] = method
        self.values: typing.Final[types.Tuple[types.RealOrJump]] = values


@dataclasses.dataclass
class DfBuilder_0:
    """
    Builds ``Df_0``.

    Attributes:
        suffix: Data card option suffix.
        method: Interpolation method for dose function table.
        values: Dose function values.
    """

    suffix: str | int | types.Integer
    values: list[str] | list[float] | list[types.RealOrJump]
    method: str | types.String = None

    def build(self):
        """
        Builds ``DfBuilder_0`` into ``Df_0``.

        Returns:
            ``Df_0`` for ``DfBuilder_0``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        method = None
        if isinstance(self.method, types.String):
            method = self.method
        elif isinstance(self.method, str):
            method = types.String.from_mcnp(self.method)

        values = []
        for item in self.values:
            if isinstance(item, types.RealOrJump):
                values.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                values.append(types.RealOrJump(item))
            elif isinstance(item, str):
                values.append(types.RealOrJump.from_mcnp(item))
        values = types.Tuple(values)

        return Df_0(
            suffix=suffix,
            method=method,
            values=values,
        )
