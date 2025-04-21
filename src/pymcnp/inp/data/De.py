import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class De(DataOption, keyword='de'):
    """
    Represents INP de elements.

    Attributes:
        suffix: Data card option suffix.
        method: Interpolation method for energy table.
        values: Energy values.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'method': types.String,
        'values': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Ade(\d+)( (?:log|lin))?((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(
        self,
        suffix: types.Integer,
        values: types.Tuple[types.RealOrJump],
        method: types.String = None,
    ):
        """
        Initializes ``De``.

        Parameters:
            suffix: Data card option suffix.
            method: Interpolation method for energy table.
            values: Energy values.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if method is not None and method not in {'log', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, method)
        if values is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, values)

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
class DeBuilder:
    """
    Builds ``De``.

    Attributes:
        suffix: Data card option suffix.
        method: Interpolation method for energy table.
        values: Energy values.
    """

    suffix: str | int | types.Integer
    values: list[str] | list[float] | list[types.RealOrJump]
    method: str | types.String = None

    def build(self):
        """
        Builds ``DeBuilder`` into ``De``.

        Returns:
            ``De`` for ``DeBuilder``.
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

        return De(
            suffix=suffix,
            method=method,
            values=values,
        )
