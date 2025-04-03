import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fq(DataOption_, keyword='fq'):
    """
    Represents INP fq elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if a1 is None or a1 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a1)
        if a2 is None or a2 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a2)
        if a3 is None or a3 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a3)
        if a4 is None or a4 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a4)
        if a5 is None or a5 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a5)
        if a6 is None or a6 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a6)
        if a7 is None or a7 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a7)
        if a8 is None or a8 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a8)

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

        self.suffix: typing.Final[types.IntegerOrJump] = suffix
        self.a1: typing.Final[types.String] = a1
        self.a2: typing.Final[types.String] = a2
        self.a3: typing.Final[types.String] = a3
        self.a4: typing.Final[types.String] = a4
        self.a5: typing.Final[types.String] = a5
        self.a6: typing.Final[types.String] = a6
        self.a7: typing.Final[types.String] = a7
        self.a8: typing.Final[types.String] = a8
