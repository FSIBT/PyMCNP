import re
import typing
import dataclasses


from .option_ import StopOption_
from ....utils import types
from ....utils import errors


class Fk(StopOption_, keyword='fk'):
    """
    Represents INP fk elements.

    Attributes:
        e: Tally fluctuation relative error before stop.
        suffix: Data card option option suffix.
    """

    _ATTRS = {
        'e': types.IntegerOrJump,
        'suffix': types.Integer,
    }

    _REGEX = re.compile(rf'\Afk(\d+)( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, e: types.IntegerOrJump, suffix: types.Integer):
        """
        Initializes ``Fk``.

        Parameters:
            e: Tally fluctuation relative error before stop.
            suffix: Data card option option suffix.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, e)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                e,
            ]
        )

        self.e: typing.Final[types.IntegerOrJump] = e
        self.suffix: typing.Final[types.Integer] = suffix


@dataclasses.dataclass
class FkBuilder:
    """
    Builds ``Fk``.

    Attributes:
        e: Tally fluctuation relative error before stop.
        suffix: Data card option option suffix.
    """

    e: str | int | types.IntegerOrJump
    suffix: str | int | types.Integer

    def build(self):
        """
        Builds ``FkBuilder`` into ``Fk``.

        Returns:
            ``Fk`` for ``FkBuilder``.
        """

        if isinstance(self.e, types.Integer):
            e = self.e
        elif isinstance(self.e, int):
            e = types.IntegerOrJump(self.e)
        elif isinstance(self.e, str):
            e = types.IntegerOrJump.from_mcnp(self.e)

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
