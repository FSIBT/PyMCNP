import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Trcl_2(_option.LikeOption):
    """
    Represents INP trcl variation #2 elements.

    Attributes:
        prefix: Star prefix.
        transformation: Like transformation..
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'prefix': types.String,
        'transformation': types.Transformation_1,
    }

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Transformation_1._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: types.Transformation_1, prefix: types.String = None):
        """
        Initializes ``Trcl_2``.

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
        self.transformation: typing.Final[types.Transformation_1] = transformation


@dataclasses.dataclass
class TrclBuilder_2(_option.LikeOptionBuilder):
    """
    Builds ``Trcl_2``.

    Attributes:
        prefix: Star prefix.
        transformation: Like transformation..
    """

    transformation: str | types.Transformation_1
    prefix: str | types.String = None

    def build(self):
        """
        Builds ``TrclBuilder_2`` into ``Trcl_2``.

        Returns:
            ``Trcl_2`` for ``TrclBuilder_2``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

        transformation = self.transformation
        if isinstance(self.transformation, types.Transformation_1):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_1.from_mcnp(self.transformation)

        return Trcl_2(
            prefix=prefix,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_2):
        """
        Unbuilds ``Trcl_2`` into ``TrclBuilder_2``

        Returns:
            ``TrclBuilder_2`` for ``Trcl_2``.
        """

        return TrclBuilder_2(
            prefix=copy.deepcopy(ast.prefix),
            transformation=copy.deepcopy(ast.transformation),
        )
