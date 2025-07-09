import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fs(_option.DataOption):
    """
    Represents INP fs elements.

    Attributes:
        suffix: Data card option suffix.
        numbers: Signed problem number of a segmenting surface..
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
    """

    _KEYWORD = 'fs'

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple[types.Integer],
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(rf'\Afs(\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)( t)?( c)?\Z')

    def __init__(self, suffix: types.Integer, numbers: types.Tuple[types.Integer], t: types.String = None, c: types.String = None):
        """
        Initializes ``Fs``.

        Parameters:
            suffix: Data card option suffix.
            numbers: Signed problem number of a segmenting surface..
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)
        if t is not None and t not in {'t'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t)
        if c is not None and c not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
                t,
                c,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers
        self.t: typing.Final[types.String] = t
        self.c: typing.Final[types.String] = c


@dataclasses.dataclass
class FsBuilder(_option.DataOptionBuilder):
    """
    Builds ``Fs``.

    Attributes:
        suffix: Data card option suffix.
        numbers: Signed problem number of a segmenting surface..
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
    """

    suffix: str | int | types.Integer
    numbers: list[str] | list[int] | list[types.Integer]
    t: str | types.String = None
    c: str | types.String = None

    def build(self):
        """
        Builds ``FsBuilder`` into ``Fs``.

        Returns:
            ``Fs`` for ``FsBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.numbers:
            numbers = []
            for item in self.numbers:
                if isinstance(item, types.Integer):
                    numbers.append(item)
                elif isinstance(item, int):
                    numbers.append(types.Integer(item))
                elif isinstance(item, str):
                    numbers.append(types.Integer.from_mcnp(item))
            numbers = types.Tuple(numbers)
        else:
            numbers = None

        t = self.t
        if isinstance(self.t, types.String):
            t = self.t
        elif isinstance(self.t, str):
            t = types.String.from_mcnp(self.t)

        c = self.c
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

    @staticmethod
    def unbuild(ast: Fs):
        """
        Unbuilds ``Fs`` into ``FsBuilder``

        Returns:
            ``FsBuilder`` for ``Fs``.
        """

        return FsBuilder(
            suffix=copy.deepcopy(ast.suffix),
            numbers=copy.deepcopy(ast.numbers),
            t=copy.deepcopy(ast.t),
            c=copy.deepcopy(ast.c),
        )
