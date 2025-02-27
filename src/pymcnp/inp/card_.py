import types

from ..utils import errors
from ..utils import _object
from ..utils import _parser


class Card_(_object.McnpElement_):
    """
    Represents generic INP cards.
    """

    _ATTRS: tuple

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates ``Card_`` from INP.

        Parameters:
                source: ``Card_`` for INP.

        Returns:
                ``Card_``.

        Raises:
                InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = cls._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        attrs = {}
        for i, (name, attr) in enumerate(cls._ATTRS.items()):
            if isinstance(attr, types.GenericAlias):
                attrs[name] = (
                    attr.from_mcnp(tokens[i + 1], attr.__args__[0]) if tokens[i + 1] else None
                )
            else:
                attrs[name] = attr.from_mcnp(tokens[i + 1]) if tokens[i + 1] else None

        card = cls(**attrs)
        card.comments = comments
        return card
