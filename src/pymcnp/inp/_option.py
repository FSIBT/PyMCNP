import types

from ..utils import errors
from ..utils import _object
from ..utils import _parser


class Option(_object.McnpNonterminal):
    """
    Represents generic INP options.
    """

    _ATTRS: tuple
    _KEYWORD: str

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates ``Option`` from INP.

        Parameters:
            source: ``Option`` for INP.

        Returns:
            ``Option``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)

        subclasses = cls.__subclasses__() or [cls]

        for subclass in subclasses:
            try:
                if (tokens := subclass._REGEX.match(source)) and tokens[0] == source:
                    break
                else:
                    continue
            except errors.InpError:
                continue
        else:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        attrs = {}
        for i, (name, attr) in enumerate(subclass._ATTRS.items()):
            if isinstance(attr, types.GenericAlias):
                attrs[name] = (
                    attr.from_mcnp(tokens[i + 1].strip(), attr.__args__[0])
                    if tokens[i + 1]
                    else None
                )
            else:
                attrs[name] = attr.from_mcnp(tokens[i + 1].strip()) if tokens[i + 1] else None

        return subclass(**attrs)

    def to_mcnp(self):
        """
        Generates INP from ``Option``.

        Returns:
            INP for ``Option``.
        """

        return f"{self._KEYWORD}{self.suffix if hasattr(self, 'suffix') else ''}{f':{self.designator}' if hasattr(self, 'designator') else ''} {self.value}"
