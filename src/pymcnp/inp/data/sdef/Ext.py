import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ext(_option.SdefOption):
    """
    Represents INP ext elements.

    Attributes:
        distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'distance_cosine': types.Real,
    }

    _REGEX = re.compile(rf'\Aext( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, distance_cosine: types.Real):
        """
        Initializes ``Ext``.

        Parameters:
            distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if distance_cosine is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, distance_cosine)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                distance_cosine,
            ]
        )

        self.distance_cosine: typing.Final[types.Real] = distance_cosine


@dataclasses.dataclass
class ExtBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Ext``.

    Attributes:
        distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.
    """

    distance_cosine: str | float | types.Real

    def build(self):
        """
        Builds ``ExtBuilder`` into ``Ext``.

        Returns:
            ``Ext`` for ``ExtBuilder``.
        """

        distance_cosine = self.distance_cosine
        if isinstance(self.distance_cosine, types.Real):
            distance_cosine = self.distance_cosine
        elif isinstance(self.distance_cosine, float) or isinstance(self.distance_cosine, int):
            distance_cosine = types.Real(self.distance_cosine)
        elif isinstance(self.distance_cosine, str):
            distance_cosine = types.Real.from_mcnp(self.distance_cosine)

        return Ext(
            distance_cosine=distance_cosine,
        )

    @staticmethod
    def unbuild(ast: Ext):
        """
        Unbuilds ``Ext`` into ``ExtBuilder``

        Returns:
            ``ExtBuilder`` for ``Ext``.
        """

        return ExtBuilder(
            distance_cosine=copy.deepcopy(ast.distance_cosine),
        )
