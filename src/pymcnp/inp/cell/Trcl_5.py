import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Trcl_5(_option.CellOption):
    """
    Represents INP trcl variation #5 elements.

    Attributes:
        prefix: Star prefix.
        transformation: Cell transformation..
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'prefix': types.String,
        'transformation': types.Transformation_4,
    }

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Transformation_4._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: types.Transformation_4, prefix: types.String = None):
        """
        Initializes ``Trcl_5``.

        Parameters:
            prefix: Star prefix.
            transformation: Cell transformation..

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
        self.transformation: typing.Final[types.Transformation_4] = transformation


@dataclasses.dataclass
class TrclBuilder_5(_option.CellOptionBuilder):
    """
    Builds ``Trcl_5``.

    Attributes:
        prefix: Star prefix.
        transformation: Cell transformation..
    """

    transformation: str | types.Transformation_4
    prefix: str | types.String = None

    def build(self):
        """
        Builds ``TrclBuilder_5`` into ``Trcl_5``.

        Returns:
            ``Trcl_5`` for ``TrclBuilder_5``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

        transformation = self.transformation
        if isinstance(self.transformation, types.Transformation_4):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_4.from_mcnp(self.transformation)

        return Trcl_5(
            prefix=prefix,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_5):
        """
        Unbuilds ``Trcl_5`` into ``TrclBuilder_5``

        Returns:
            ``TrclBuilder_5`` for ``Trcl_5``.
        """

        return TrclBuilder_5(
            prefix=copy.deepcopy(ast.prefix),
            transformation=copy.deepcopy(ast.transformation),
        )
