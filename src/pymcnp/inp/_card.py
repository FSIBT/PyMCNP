from .. import errors
from .. import _symbol
from ..utils import _parser


class Card(_symbol.Nonterminal):
    """
    Represents generic INP cards.
    """

    _ATTRS: tuple

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates ``Card`` from INP.

        Parameters:
            source: ``Card`` for INP.

        Returns:
            ``Card``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = cls._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        attrs = {}
        for i, (name, attr) in enumerate(cls._ATTRS.items()):
            attrs[name] = attr.from_mcnp(tokens[i + 1]) if tokens[i + 1] else None

        card = cls(**attrs)
        card.comments = comments
        return card
