import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Fq(DataOption):
    """
    Represents INP fq elements.

    Attributes:
        suffix: Data card option suffix.
        a1: Letters representing tally bin types.
        a2: Letters representing tally bin types.
        a3: Letters representing tally bin types.
        a4: Letters representing tally bin types.
        a5: Letters representing tally bin types.
        a6: Letters representing tally bin types.
        a7: Letters representing tally bin types.
        a8: Letters representing tally bin types.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'a1': types.String,
        'a2': types.String,
        'a3': types.String,
        'a4': types.String,
        'a5': types.String,
        'a6': types.String,
        'a7': types.String,
        'a8': types.String,
    }

    _REGEX = re.compile(
        rf'\Afq(\d+)( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        a1: types.String,
        a2: types.String,
        a3: types.String,
        a4: types.String,
        a5: types.String,
        a6: types.String,
        a7: types.String,
        a8: types.String,
    ):
        """
        Initializes ``Fq``.

        Parameters:
            suffix: Data card option suffix.
            a1: Letters representing tally bin types.
            a2: Letters representing tally bin types.
            a3: Letters representing tally bin types.
            a4: Letters representing tally bin types.
            a5: Letters representing tally bin types.
            a6: Letters representing tally bin types.
            a7: Letters representing tally bin types.
            a8: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if a1 is None or a1 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a1)
        if a2 is None or a2 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a2)
        if a3 is None or a3 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a3)
        if a4 is None or a4 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a4)
        if a5 is None or a5 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a5)
        if a6 is None or a6 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a6)
        if a7 is None or a7 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a7)
        if a8 is None or a8 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a8)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.a1: typing.Final[types.String] = a1
        self.a2: typing.Final[types.String] = a2
        self.a3: typing.Final[types.String] = a3
        self.a4: typing.Final[types.String] = a4
        self.a5: typing.Final[types.String] = a5
        self.a6: typing.Final[types.String] = a6
        self.a7: typing.Final[types.String] = a7
        self.a8: typing.Final[types.String] = a8


@dataclasses.dataclass
class FqBuilder:
    """
    Builds ``Fq``.

    Attributes:
        suffix: Data card option suffix.
        a1: Letters representing tally bin types.
        a2: Letters representing tally bin types.
        a3: Letters representing tally bin types.
        a4: Letters representing tally bin types.
        a5: Letters representing tally bin types.
        a6: Letters representing tally bin types.
        a7: Letters representing tally bin types.
        a8: Letters representing tally bin types.
    """

    suffix: str | int | types.Integer
    a1: str | types.String
    a2: str | types.String
    a3: str | types.String
    a4: str | types.String
    a5: str | types.String
    a6: str | types.String
    a7: str | types.String
    a8: str | types.String

    def build(self):
        """
        Builds ``FqBuilder`` into ``Fq``.

        Returns:
            ``Fq`` for ``FqBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.a1, types.String):
            a1 = self.a1
        elif isinstance(self.a1, str):
            a1 = types.String.from_mcnp(self.a1)

        if isinstance(self.a2, types.String):
            a2 = self.a2
        elif isinstance(self.a2, str):
            a2 = types.String.from_mcnp(self.a2)

        if isinstance(self.a3, types.String):
            a3 = self.a3
        elif isinstance(self.a3, str):
            a3 = types.String.from_mcnp(self.a3)

        if isinstance(self.a4, types.String):
            a4 = self.a4
        elif isinstance(self.a4, str):
            a4 = types.String.from_mcnp(self.a4)

        if isinstance(self.a5, types.String):
            a5 = self.a5
        elif isinstance(self.a5, str):
            a5 = types.String.from_mcnp(self.a5)

        if isinstance(self.a6, types.String):
            a6 = self.a6
        elif isinstance(self.a6, str):
            a6 = types.String.from_mcnp(self.a6)

        if isinstance(self.a7, types.String):
            a7 = self.a7
        elif isinstance(self.a7, str):
            a7 = types.String.from_mcnp(self.a7)

        if isinstance(self.a8, types.String):
            a8 = self.a8
        elif isinstance(self.a8, str):
            a8 = types.String.from_mcnp(self.a8)

        return Fq(
            suffix=suffix,
            a1=a1,
            a2=a2,
            a3=a3,
            a4=a4,
            a5=a5,
            a6=a6,
            a7=a7,
            a8=a8,
        )
