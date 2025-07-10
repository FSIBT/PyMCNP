import re
import copy
import dataclasses


from . import like
from ._card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Like(Card):
    """
    Represents INP cell cards.

    Attributes:
        number: cell number.
        original: cell similar.
        options: cell options.
    """

    _ATTRS = {
        'number': types.Integer,
        'original': types.Integer,
        'options': types.Tuple[like.LikeOption],
    }

    _REGEX = re.compile(rf'\A(\S+) like (\S+) but((?: (?:{like.LikeOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(
        self,
        number: types.Integer,
        original: types.Integer,
        options: types.Tuple[like.LikeOption] = None,
    ):
        """
        Initializes ``Like``.

        Parameters:
            number: cell number.
            original: cell similar.
            options: cell options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)
        if original is None or not (1 <= original <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, original)

        self.number: types.Integer = number
        self.original: types.Integer = original
        self.options: types.Tuple[like.LikeOption] = options

    def to_mcnp(self):
        """
        Generates INP from ``Like``.

        Returns:
            INP cell card.
        """

        source = f'{self.number} like {self.original} but {self.options or ""}'
        source, comments = _parser.preprocess_inp(source)
        source = _parser.postprocess_inp(source)

        return source


@dataclasses.dataclass
class LikeBuilder:
    """
    Builds ``Like``.

    Attributes:
        number: cell number.
        original: cell similar.
        options: cell options.
    """

    number: str | int | types.Integer
    original: str | int | types.Integer
    options: list[str] | list[like.LikeOption] | list[like.LikeOptionBuilder] = None

    def build(self):
        """
        Builds ``LikeBuilder`` into ``Like``.

        Returns:
            ``Like`` for ``LikeBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        original = self.original
        if isinstance(self.original, types.Integer):
            original = self.original
        elif isinstance(self.original, int):
            original = types.Integer(self.original)
        elif isinstance(self.original, str):
            original = types.Integer.from_mcnp(self.original)

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, like.LikeOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(like.LikeOption.from_mcnp(item))
                elif isinstance(item, like.LikeOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Like(
            number=number,
            original=original,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Like):
        """
        Unbuilds ``Like`` into ``LikeBuilder``

        Returns:
            ``LikeBuilder`` for ``Like``.
        """

        return LikeBuilder(
            number=copy.deepcopy(ast.number),
            original=copy.deepcopy(ast.original),
            options=copy.deepcopy(ast.options),
        )
