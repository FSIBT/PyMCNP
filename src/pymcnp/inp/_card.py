from . import _symbol
from .. import errors


class Card(_symbol.InpNonterminal):
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

        source, comments = cls._preprocess(source)
        tokens = cls._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        attrs = {}
        for i, (name, attr) in enumerate(cls._ATTRS.items()):
            attrs[name] = attr.from_mcnp(tokens[i + 1]) if tokens[i + 1] else None

        card = cls(**attrs)
        card.comments = comments
        return card

    @staticmethod
    def _preprocess(source: str) -> tuple[str, tuple[str]]:
        """
        Preprocess INP for ``from_mcnp``.

        Parameters:
            source: INP to preprocess.

        Returns:
            Preprocess INP.
        """

        lines = []
        comments = []

        for line in source.split('\n'):
            split = line.split('$', maxsplit=1)

            if len(split) == 2:
                lines.append(split[0])
                comments.append(split[1])
            else:
                lines.append(line)

        source = '\n'.join(lines)
        source = _symbol.InpNonterminal._preprocess(source)

        return source, comments

    @staticmethod
    def _postprocess(source: str) -> str:
        """
        Postprocesses INP for ``to_mcnp``.

        Parameters:
            source: INP to postprocess.

        Returns:
            Postprocessed INP.
        """

        lines = []
        length = 0

        for word in source.split(' '):
            if len(word) + length > 78:
                lines.append('&\n     ')
                length = 5

            lines.append(word)
            length += len(word) + 1

        return ' '.join(lines)
