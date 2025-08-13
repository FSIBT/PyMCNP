import re

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
        Generates `Card` from INP.

        Parameters:
            source: `Card` for INP.

        Returns:
            `Card`.

        Raises:
            InpError: SYNTAX_CARD.
        """

        source, comments = Card._preprocess(source)
        tokens = cls._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_CARD, source)

        attrs = {}
        for i, (name, attr) in enumerate(cls._ATTRS.items()):
            attrs[name] = attr.from_mcnp(tokens[i + 1].strip()) if tokens[i + 1] else None

        card = cls(**attrs)
        card.comments = comments
        return card

    def to_mcnp(self):
        """
        Generates INP from `Option`.

        Returns:
            INP for `Option`.
        """

        value = []
        for name in filter(lambda name: name.lower() not in {'prefix', 'suffix', 'designator'}, self._ATTRS.keys()):
            if (attribute := getattr(type(self), name).__get__(self)) is not None:
                value.append(attribute)
        value = ' '.join(map(str, value))

        source = f'{self.prefix if hasattr(self, "prefix") and self.prefix is not None else ""}{self._KEYWORD}{self.suffix if hasattr(self, "suffix") and self.suffix is not None else ""}{(f":{self.designator}" if self.designator else "") if hasattr(self, "designator") else ""} {value}'
        source = Card._postprocess(source.strip())

        return source

    @staticmethod
    def _preprocess(source: str) -> tuple[str, tuple[str]]:
        """
        Preprocess INP for `from_mcnp`.

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
        Postprocesses INP for `to_mcnp`.

        Parameters:
            source: INP to postprocess.

        Returns:
            Postprocessed INP.
        """

        source = re.sub(r'((?: [jJ]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}j' + match[2], source)
        source = re.sub(r'((?: [rR]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}r' + match[2], source)
        source = re.sub(r'((?: [iI]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}i' + match[2], source)
        source = re.sub(r'((?: [lL][oO][gG]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}log' + match[2], source)
        source = re.sub(r'((?: [iI][lL][oO][gG]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}ilog' + match[2], source)

        lines = []
        length = 0

        for word in source.split(' '):
            if len(word) + length > 78:
                lines.append('&\n     ')
                length = 5

            lines.append(word)
            length += len(word) + 1

        return ' '.join(lines)
