import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Trcl_1(_option.LikeOption):
    """
    Represents INP trcl variation #1 elements.

    Attributes:
        prefix: Star prefix.
        transformation: Like transformation..
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'prefix': types.String,
        'transformation': types.Transformation_0,
    }

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Transformation_0._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: types.Transformation_0, prefix: types.String = None):
        """
        Initializes ``Trcl_1``.

        Parameters:
            prefix: Star prefix.
            transformation: Like transformation..

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if transformation is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformation,
            ]
        )

        self.prefix: typing.Final[types.String] = prefix
        self.transformation: typing.Final[types.Transformation_0] = transformation


@dataclasses.dataclass
class TrclBuilder_1(_option.LikeOptionBuilder):
    """
    Builds ``Trcl_1``.

    Attributes:
        prefix: Star prefix.
        transformation: Like transformation..
    """

    transformation: str | types.Transformation_0
    prefix: str | types.String = None

    def build(self):
        """
        Builds ``TrclBuilder_1`` into ``Trcl_1``.

        Returns:
            ``Trcl_1`` for ``TrclBuilder_1``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

        transformation = self.transformation
        if isinstance(self.transformation, types.Transformation_0):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_0.from_mcnp(self.transformation)

        return Trcl_1(
            prefix=prefix,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_1):
        """
        Unbuilds ``Trcl_1`` into ``TrclBuilder_1``

        Returns:
            ``TrclBuilder_1`` for ``Trcl_1``.
        """

        return TrclBuilder_1(
            prefix=copy.deepcopy(ast.prefix),
            transformation=copy.deepcopy(ast.transformation),
        )
