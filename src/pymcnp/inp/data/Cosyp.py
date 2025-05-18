import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Cosyp(DataOption):
    """
    Represents INP cosyp elements.

    Attributes:
        prefix: Prefix number of the COSY map files.
        axsh: Horiztonal axis orientation.
        axsv: Vertical axis orientation.
        emaps: Tuple of operating beam energies.
    """

    _ATTRS = {
        'prefix': types.IntegerOrJump,
        'axsh': types.IntegerOrJump,
        'axsv': types.IntegerOrJump,
        'emaps': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(
        rf'\Acosyp( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})((?: {types.RealOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        prefix: types.IntegerOrJump,
        axsh: types.IntegerOrJump,
        axsv: types.IntegerOrJump,
        emaps: types.Tuple[types.RealOrJump],
    ):
        """
        Initializes ``Cosyp``.

        Parameters:
            prefix: Prefix number of the COSY map files.
            axsh: Horiztonal axis orientation.
            axsv: Vertical axis orientation.
            emaps: Tuple of operating beam energies.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if axsh is None or axsh.value not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, axsh)
        if axsv is None or axsv.value not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, axsv)
        if emaps is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, emaps)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                prefix,
                axsh,
                axsv,
                emaps,
            ]
        )

        self.prefix: typing.Final[types.IntegerOrJump] = prefix
        self.axsh: typing.Final[types.IntegerOrJump] = axsh
        self.axsv: typing.Final[types.IntegerOrJump] = axsv
        self.emaps: typing.Final[types.Tuple[types.RealOrJump]] = emaps


@dataclasses.dataclass
class CosypBuilder:
    """
    Builds ``Cosyp``.

    Attributes:
        prefix: Prefix number of the COSY map files.
        axsh: Horiztonal axis orientation.
        axsv: Vertical axis orientation.
        emaps: Tuple of operating beam energies.
    """

    prefix: str | int | types.IntegerOrJump
    axsh: str | int | types.IntegerOrJump
    axsv: str | int | types.IntegerOrJump
    emaps: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``CosypBuilder`` into ``Cosyp``.

        Returns:
            ``Cosyp`` for ``CosypBuilder``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.Integer):
            prefix = self.prefix
        elif isinstance(self.prefix, int):
            prefix = types.IntegerOrJump(self.prefix)
        elif isinstance(self.prefix, str):
            prefix = types.IntegerOrJump.from_mcnp(self.prefix)

        axsh = self.axsh
        if isinstance(self.axsh, types.Integer):
            axsh = self.axsh
        elif isinstance(self.axsh, int):
            axsh = types.IntegerOrJump(self.axsh)
        elif isinstance(self.axsh, str):
            axsh = types.IntegerOrJump.from_mcnp(self.axsh)

        axsv = self.axsv
        if isinstance(self.axsv, types.Integer):
            axsv = self.axsv
        elif isinstance(self.axsv, int):
            axsv = types.IntegerOrJump(self.axsv)
        elif isinstance(self.axsv, str):
            axsv = types.IntegerOrJump.from_mcnp(self.axsv)

        if self.emaps:
            emaps = []
            for item in self.emaps:
                if isinstance(item, types.RealOrJump):
                    emaps.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    emaps.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    emaps.append(types.RealOrJump.from_mcnp(item))
            emaps = types.Tuple(emaps)
        else:
            emaps = None

        return Cosyp(
            prefix=prefix,
            axsh=axsh,
            axsv=axsv,
            emaps=emaps,
        )
