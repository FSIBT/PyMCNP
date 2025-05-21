import re
import copy
import typing
import dataclasses


from ._option import StopOption
from ....utils import types
from ....utils import errors


class Fk(StopOption):
    """
    Represents INP fk elements.

    Attributes:
        e: Tally fluctuation relative error before stop.
        suffix: Data card option option suffix.
    """

    _KEYWORD = 'fk'

    _ATTRS = {
        'e': types.Integer,
        'suffix': types.Integer,
    }

    _REGEX = re.compile(rf'\Afk(\d+)( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, e: types.Integer, suffix: types.Integer):
        """
        Initializes ``Fk``.

        Parameters:
            e: Tally fluctuation relative error before stop.
            suffix: Data card option option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, e)
        if suffix is None or not (suffix.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                e,
            ]
        )

        self.e: typing.Final[types.Integer] = e
        self.suffix: typing.Final[types.Integer] = suffix


@dataclasses.dataclass
class FkBuilder:
    """
    Builds ``Fk``.

    Attributes:
        e: Tally fluctuation relative error before stop.
        suffix: Data card option option suffix.
    """

    e: str | int | types.Integer
    suffix: str | int | types.Integer

    def build(self):
        """
        Builds ``FkBuilder`` into ``Fk``.

        Returns:
            ``Fk`` for ``FkBuilder``.
        """

        e = self.e
        if isinstance(self.e, types.Integer):
            e = self.e
        elif isinstance(self.e, int):
            e = types.Integer(self.e)
        elif isinstance(self.e, str):
            e = types.Integer.from_mcnp(self.e)

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        return Fk(
            e=e,
            suffix=suffix,
        )

    @staticmethod
    def unbuild(ast: Fk):
        """
        Unbuilds ``Fk`` into ``FkBuilder``

        Returns:
            ``FkBuilder`` for ``Fk``.
        """

        return Fk(
            e=copy.deepcopy(ast.e),
            suffix=copy.deepcopy(ast.suffix),
        )
