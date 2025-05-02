import re
import typing
import dataclasses


from . import bfld
from ._option import DataOption
from ...utils import types
from ...utils import errors


class Bfld(DataOption):
    """
    Represents INP bfld elements.

    Attributes:
        suffix: Data card option suffix.
        kind: Magnetic field type.
        options: Dictionary of options.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'kind': types.String,
        'options': types.Tuple[bfld.BfldOption],
    }

    _REGEX = re.compile(
        rf'\Abfld(\d+)( {types.String._REGEX.pattern})((?: (?:{bfld.BfldOption._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        kind: types.String,
        options: types.Tuple[bfld.BfldOption] = None,
    ):
        """
        Initializes ``Bfld``.

        Parameters:
            suffix: Data card option suffix.
            kind: Magnetic field type.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if kind is None or type not in {'const', 'quad', 'quadff'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.kind: typing.Final[types.String] = kind
        self.options: typing.Final[types.Tuple[bfld.BfldOption]] = options


@dataclasses.dataclass
class BfldBuilder:
    """
    Builds ``Bfld``.

    Attributes:
        suffix: Data card option suffix.
        kind: Magnetic field type.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    kind: str | types.String
    options: list[str] | list[bfld.BfldOption] = None

    def build(self):
        """
        Builds ``BfldBuilder`` into ``Bfld``.

        Returns:
            ``Bfld`` for ``BfldBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        options = []
        for item in self.options:
            if isinstance(item, bfld.BfldOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(bfld.BfldOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Bfld(
            suffix=suffix,
            kind=kind,
            options=options,
        )
