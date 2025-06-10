import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Df_0(_option.DataOption):
    """
    Represents INP df variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        method: Interpolation method for dose function table.
        values: Dose function values.
    """

    _KEYWORD = 'df'

    _ATTRS = {
        'suffix': types.Integer,
        'method': types.String,
        'values': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Adf(\d+)( (?:log|lin))?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, values: types.Tuple[types.Real], method: types.String = None):
        """
        Initializes ``Df_0``.

        Parameters:
            suffix: Data card option suffix.
            method: Interpolation method for dose function table.
            values: Dose function values.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999):
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
        self.values: typing.Final[types.Tuple[types.Real]] = values


@dataclasses.dataclass
class DfBuilder_0(_option.DataOptionBuilder):
    """
    Builds ``Df_0``.

    Attributes:
        suffix: Data card option suffix.
        method: Interpolation method for dose function table.
        values: Dose function values.
    """

    suffix: str | int | types.Integer
    values: list[str] | list[float] | list[types.Real]
    method: str | types.String = None

    def build(self):
        """
        Builds ``DfBuilder_0`` into ``Df_0``.

        Returns:
            ``Df_0`` for ``DfBuilder_0``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        method = self.method
        if isinstance(self.method, types.String):
            method = self.method
        elif isinstance(self.method, str):
            method = types.String.from_mcnp(self.method)

        if self.values:
            values = []
            for item in self.values:
                if isinstance(item, types.Real):
                    values.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    values.append(types.Real(item))
                elif isinstance(item, str):
                    values.append(types.Real.from_mcnp(item))
            values = types.Tuple(values)
        else:
            values = None

        return Df_0(
            suffix=suffix,
            method=method,
            values=values,
        )

    @staticmethod
    def unbuild(ast: Df_0):
        """
        Unbuilds ``Df_0`` into ``DfBuilder_0``

        Returns:
            ``DfBuilder_0`` for ``Df_0``.
        """

        return DfBuilder_0(
            suffix=copy.deepcopy(ast.suffix),
            method=copy.deepcopy(ast.method),
            values=copy.deepcopy(ast.values),
        )
