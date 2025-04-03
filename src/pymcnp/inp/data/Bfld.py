import re
import typing


from . import bfld
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Bfld(DataOption_, keyword='bfld'):
    """
    Represents INP bfld elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'kind': types.String,
        'options': types.Tuple[bfld.BfldOption_],
    }

    _REGEX = re.compile(
        rf'\Abfld(\d+)( {types.String._REGEX.pattern})((?: (?:{bfld.BfldOption_._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        kind: types.String,
        options: types.Tuple[bfld.BfldOption_] = None,
    ):
        """
        Initializes ``Bfld``.

        Parameters:
            suffix: Data card option suffix.
            kind: Magnetic field type.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if kind is None or type not in {'const', 'quad', 'quadff'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.kind: typing.Final[types.String] = kind
        self.options: typing.Final[types.Tuple[bfld.BfldOption_]] = options
