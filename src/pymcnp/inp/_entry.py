from . import _symbol
from .. import errors


class Entry(_symbol.InpNonterminal):
    """
    Represents generic INP entries.
    """

    _ATTRS: tuple
    _KEYWORD: str

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates `Entry` from INP.

        Parameters:
            source: `Entry` for INP.

        Returns:
            `Entry`.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source = cls._preprocess(source)
        subclasses = cls.__subclasses__() or [cls]

        for subclass in subclasses:
            if (tokens := subclass._REGEX.match(source)) and tokens[0] == source:
                break
            else:
                continue
        else:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        attrs = {}
        for i, (name, attr) in enumerate(subclass._ATTRS.items()):
            attrs[name] = attr.from_mcnp(tokens[i + 1].strip()) if tokens[i + 1] else None

        return subclass(**attrs)

    def to_mcnp(self):
        """
        Generates INP from `Entry`.

        Returns:
            INP for `Entry`.
        """

        value = []
        for name in self._ATTRS.keys():
            if (attribute := getattr(type(self), name).__get__(self)) is not None:
                value.append(attribute)
        value = ' '.join(map(str, value))

        return value
