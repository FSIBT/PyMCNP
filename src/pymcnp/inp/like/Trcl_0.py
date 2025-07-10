import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Trcl_0(_option.LikeOption):
    """
    Represents INP trcl variation #0 elements.

    Attributes:
        prefix: Star prefix.
        transformation: Like transformation number.
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'prefix': types.String,
        'transformation': types.Integer,
    }

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: types.Integer, prefix: types.String = None):
        """
        Initializes ``Trcl_0``.

        Parameters:
            prefix: Star prefix.
            transformation: Like transformation number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if transformation is None or not (transformation >= 0 and transformation <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformation,
            ]
        )

        self.prefix: typing.Final[types.String] = prefix
        self.transformation: typing.Final[types.Integer] = transformation


@dataclasses.dataclass
class TrclBuilder_0(_option.LikeOptionBuilder):
    """
    Builds ``Trcl_0``.

    Attributes:
        prefix: Star prefix.
        transformation: Like transformation number.
    """

    transformation: str | int | types.Integer
    prefix: str | types.String = None

    def build(self):
        """
        Builds ``TrclBuilder_0`` into ``Trcl_0``.

        Returns:
            ``Trcl_0`` for ``TrclBuilder_0``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

        transformation = self.transformation
        if isinstance(self.transformation, types.Integer):
            transformation = self.transformation
        elif isinstance(self.transformation, int):
            transformation = types.Integer(self.transformation)
        elif isinstance(self.transformation, str):
            transformation = types.Integer.from_mcnp(self.transformation)

        return Trcl_0(
            prefix=prefix,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_0):
        """
        Unbuilds ``Trcl_0`` into ``TrclBuilder_0``

        Returns:
            ``TrclBuilder_0`` for ``Trcl_0``.
        """

        return TrclBuilder_0(
            prefix=copy.deepcopy(ast.prefix),
            transformation=copy.deepcopy(ast.transformation),
        )
