import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Cosyp(_option.DataOption):
    """
    Represents INP cosyp elements.

    Attributes:
        pre: Prefix number of the COSY map files.
        axsh: Horiztonal axis orientation.
        axsv: Vertical axis orientation.
        emaps: Tuple of operating beam energies.
    """

    _KEYWORD = 'cosyp'

    _ATTRS = {
        'pre': types.Integer,
        'axsh': types.Integer,
        'axsv': types.Integer,
        'emaps': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Acosyp( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, pre: types.Integer, axsh: types.Integer, axsv: types.Integer, emaps: types.Tuple[types.Real]):
        """
        Initializes ``Cosyp``.

        Parameters:
            pre: Prefix number of the COSY map files.
            axsh: Horiztonal axis orientation.
            axsv: Vertical axis orientation.
            emaps: Tuple of operating beam energies.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if pre is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, pre)
        if axsh is None or axsh not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, axsh)
        if axsv is None or axsv not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, axsv)
        if emaps is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, emaps)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                pre,
                axsh,
                axsv,
                emaps,
            ]
        )

        self.pre: typing.Final[types.Integer] = pre
        self.axsh: typing.Final[types.Integer] = axsh
        self.axsv: typing.Final[types.Integer] = axsv
        self.emaps: typing.Final[types.Tuple[types.Real]] = emaps


@dataclasses.dataclass
class CosypBuilder(_option.DataOptionBuilder):
    """
    Builds ``Cosyp``.

    Attributes:
        pre: Prefix number of the COSY map files.
        axsh: Horiztonal axis orientation.
        axsv: Vertical axis orientation.
        emaps: Tuple of operating beam energies.
    """

    pre: str | int | types.Integer
    axsh: str | int | types.Integer
    axsv: str | int | types.Integer
    emaps: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``CosypBuilder`` into ``Cosyp``.

        Returns:
            ``Cosyp`` for ``CosypBuilder``.
        """

        pre = self.pre
        if isinstance(self.pre, types.Integer):
            pre = self.pre
        elif isinstance(self.pre, int):
            pre = types.Integer(self.pre)
        elif isinstance(self.pre, str):
            pre = types.Integer.from_mcnp(self.pre)

        axsh = self.axsh
        if isinstance(self.axsh, types.Integer):
            axsh = self.axsh
        elif isinstance(self.axsh, int):
            axsh = types.Integer(self.axsh)
        elif isinstance(self.axsh, str):
            axsh = types.Integer.from_mcnp(self.axsh)

        axsv = self.axsv
        if isinstance(self.axsv, types.Integer):
            axsv = self.axsv
        elif isinstance(self.axsv, int):
            axsv = types.Integer(self.axsv)
        elif isinstance(self.axsv, str):
            axsv = types.Integer.from_mcnp(self.axsv)

        if self.emaps:
            emaps = []
            for item in self.emaps:
                if isinstance(item, types.Real):
                    emaps.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    emaps.append(types.Real(item))
                elif isinstance(item, str):
                    emaps.append(types.Real.from_mcnp(item))
            emaps = types.Tuple(emaps)
        else:
            emaps = None

        return Cosyp(
            pre=pre,
            axsh=axsh,
            axsv=axsv,
            emaps=emaps,
        )

    @staticmethod
    def unbuild(ast: Cosyp):
        """
        Unbuilds ``Cosyp`` into ``CosypBuilder``

        Returns:
            ``CosypBuilder`` for ``Cosyp``.
        """

        return CosypBuilder(
            pre=copy.deepcopy(ast.pre),
            axsh=copy.deepcopy(ast.axsh),
            axsv=copy.deepcopy(ast.axsv),
            emaps=copy.deepcopy(ast.emaps),
        )
