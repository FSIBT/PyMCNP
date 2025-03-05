import types

from ..utils import errors
from ..utils import _object
from ..utils import _parser


class Option_(_object.McnpElement_):
    """
    Represents generic INP cards.
    """

    _ATTRS: tuple
    _KEYWORD: str

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates ``Option_`` from INP.

        Parameters:
            source: ``Option_`` for INP.

        Returns:
            ``Option_``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)

        for subcls in sorted(
            sum(cls._SUBCLASSES.values(), []), reverse=True, key=lambda val: len(val._KEYWORD)
        ):
            try:
                if subcls._REGEX.match(source):
                    break
                else:
                    continue
            except errors.InpError:
                continue

        if not (tokens := subcls._REGEX.match(source)):
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        attrs = {}
        for i, (name, attr) in enumerate(subcls._ATTRS.items()):
            if isinstance(attr, types.GenericAlias):
                attrs[name] = (
                    attr.from_mcnp(tokens[i + 1], attr.__args__[0]) if tokens[i + 1] else None
                )
            else:
                attrs[name] = attr.from_mcnp(tokens[i + 1]) if tokens[i + 1] else None

        return subcls(**attrs)

    def to_mcnp(self):
        """
        Generates INP from ``Option_``.

        Returns:
            INP for ``Option_``.
        """

        return f"{self._KEYWORD}{self.suffix if hasattr(self, 'suffix') else ''}{f':{self.designator}' if hasattr(self, 'designator') else ''} {self.value}"
