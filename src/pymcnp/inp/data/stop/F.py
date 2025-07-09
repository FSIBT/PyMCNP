import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class F(_option.StopOption):
    """
    Represents INP f elements.

    Attributes:
        suffix: Data card option option suffix.
        e: Tally fluctuation relative error before stop.
    """

    _KEYWORD = 'f'

    _ATTRS = {
        'suffix': types.Integer,
        'e': types.Integer,
    }

    _REGEX = re.compile(rf'\Af(\d+)( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, suffix: types.Integer, e: types.Integer):
        """
        Initializes ``F``.

        Parameters:
            suffix: Data card option option suffix.
            e: Tally fluctuation relative error before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, e)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                e,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.e: typing.Final[types.Integer] = e


@dataclasses.dataclass
class FBuilder(_option.StopOptionBuilder):
    """
    Builds ``F``.

    Attributes:
        suffix: Data card option option suffix.
        e: Tally fluctuation relative error before stop.
    """

    suffix: str | int | types.Integer
    e: str | int | types.Integer

    def build(self):
        """
        Builds ``FBuilder`` into ``F``.

        Returns:
            ``F`` for ``FBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        e = self.e
        if isinstance(self.e, types.Integer):
            e = self.e
        elif isinstance(self.e, int):
            e = types.Integer(self.e)
        elif isinstance(self.e, str):
            e = types.Integer.from_mcnp(self.e)

        return F(
            suffix=suffix,
            e=e,
        )

    @staticmethod
    def unbuild(ast: F):
        """
        Unbuilds ``F`` into ``FBuilder``

        Returns:
            ``FBuilder`` for ``F``.
        """

        return FBuilder(
            suffix=copy.deepcopy(ast.suffix),
            e=copy.deepcopy(ast.e),
        )
