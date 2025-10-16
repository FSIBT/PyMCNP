import re
import typing

from .. import errors


def Union(*elements: typing.Type) -> object:
    """
    Curries unions and inner type.

    Parametres:
        elements: Inner types.

    Returns:
        `_Union` with inner type.
    """

    class _Union(*elements):
        """
        Represents generic MCNP collections.

        Attributes:
            value: Union value.
        """

        REGEX = re.compile(rf'\A{r"|".join(map(lambda element: f"(?:{element._REGEX.pattern[2:-2]})", elements))}\Z', re.IGNORECASE)

        @classmethod
        def from_mcnp(cls, source: str):
            """
            Generates `Union` from MCNP.

            Parameters:
                source: MCNP with ambiguity.
                T: Inner type.

            Returns:
                `Union`.

            Raises:
                TypesError: SYNTAX_TYPE.
            """

            for element in elements:
                try:
                    return element.from_mcnp(source)
                except errors.Error:
                    pass
            else:
                raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

    return _Union
