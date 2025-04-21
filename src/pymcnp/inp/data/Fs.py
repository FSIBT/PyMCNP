import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Fs(DataOption, keyword='fs'):
    """
    Represents INP fs elements.

    Attributes:
        suffix: Data card option suffix.
        numbers: Signed problem number of a segmenting surface..
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple[types.IntegerOrJump],
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(
        rf'\Afs(\d+)((?: {types.IntegerOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        numbers: types.Tuple[types.IntegerOrJump],
        t: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``Fs``.

        Parameters:
            suffix: Data card option suffix.
            numbers: Signed problem number of a segmenting surface..
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if numbers is None or not (
            filter(lambda entry: not (-99_999_999 <= numbers <= 99_999_999), numbers)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)
        if t is not None and t not in {'t'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t)
        if c is not None and c not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, c)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
                t,
                c,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers
        self.t: typing.Final[types.String] = t
        self.c: typing.Final[types.String] = c


@dataclasses.dataclass
class FsBuilder:
    """
    Builds ``Fs``.

    Attributes:
        suffix: Data card option suffix.
        numbers: Signed problem number of a segmenting surface..
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
    """

    suffix: str | int | types.Integer
    numbers: list[str] | list[int] | list[types.IntegerOrJump]
    t: str | types.String = None
    c: str | types.String = None

    def build(self):
        """
        Builds ``FsBuilder`` into ``Fs``.

        Returns:
            ``Fs`` for ``FsBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        numbers = []
        for item in self.numbers:
            if isinstance(item, types.IntegerOrJump):
                numbers.append(item)
            elif isinstance(item, int):
                numbers.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                numbers.append(types.IntegerOrJump.from_mcnp(item))
        numbers = types.Tuple(numbers)

        t = None
        if isinstance(self.t, types.String):
            t = self.t
        elif isinstance(self.t, str):
            t = types.String.from_mcnp(self.t)

        c = None
        if isinstance(self.c, types.String):
            c = self.c
        elif isinstance(self.c, str):
            c = types.String.from_mcnp(self.c)

        return Fs(
            suffix=suffix,
            numbers=numbers,
            t=t,
            c=c,
        )
