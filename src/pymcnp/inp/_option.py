from . import _symbol
from .. import errors
from .. import types

_TRANSFORMATIONS = (types.Transformation_0, types.Transformation_1, types.Transformation_2, types.Transformation_3, types.Transformation_4)


class Option(_symbol.InpNonterminal):
    """
    Represents generic INP options.
    """

    _ATTRS: dict
    _CODE = errors.InpCode.SEMANTICS_OPTION
    _KEYWORD: str

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates `Option` from INP.

        Parameters:
            source: `Option` for INP.

        Returns:
            `Option`.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source = Option._preprocess(source)
        subclasses = cls.__subclasses__() or [cls]

        for subclass in subclasses:
            if (tokens := subclass._REGEX.match(source)) and tokens[0] == source:
                break
            else:
                continue
        else:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        groups = _symbol._top_groups(subclass._REGEX)
        attrs = {}
        for i, (name, attr) in enumerate(subclass._ATTRS.items()):
            attrs[name] = attr.from_mcnp(tokens[groups[i]].strip()) if tokens[groups[i]] else None

        return subclass(**attrs)

    def to_mcnp(self):
        """
        Generates INP from `Option`.

        Returns:
            INP for `Option`.
        """

        value = []
        for name in filter(lambda name: name.lower() not in {'prefix', 'suffix', 'designator'}, self._ATTRS.keys()):
            if (attribute := getattr(type(self), name).__get__(self)) is not None:
                value.append(f'({str(attribute).strip()})' if isinstance(attribute, _TRANSFORMATIONS) else attribute)
        value = ' '.join(map(str, value))

        source = f'{self.prefix if hasattr(self, "prefix") and self.prefix is not None else ""}{self._KEYWORD}{self.suffix if hasattr(self, "suffix") and self.suffix is not None else ""}{(f":{self.designator}" if self.designator else "") if hasattr(self, "designator") else ""} {value}'

        return source
