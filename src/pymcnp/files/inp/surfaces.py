"""
'surfaces' contains classes representing INP surface card blocks.

'surfaces' packages the 'Surfaces' class, providing an importable
interface for INP surface card blocks.
"""


from typing import Self

from .block import Block
from .surface import Surface
from .._utils import parser


class Surfaces(Block):
    """
    'Surfaces' represents MNCP INP surface card blocks.

    'Surfaces' abstracts the INP cell card syntax element and it
    encapsulates all functionallity for parsing cell card blocks.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Surfaces'.
        """

        super().__init__()

    @classmethod
    def from_mcnp(cls, source: str) -> Self:
        """
        'from_mcnp' generates surface block objects from INP.

        'from_mcnp' constructs instances of 'Surfaces' from
        INP strings, so it functions as a class constructor.

        Parameters:
            source: INP to parse.

        Returns:
            Surface block object.
        """

        block = cls()

        lines = parser.Preprocessor.process_inp(source).split("\n")
        for line in lines:
            if line == "":
                break

            block.append(Surface.from_mcnp(line))

        return block

    def to_mcnp(self) -> str:
        """
        'to_mcnp' generates INP from surface block objects.

        'to_mcnp' provides an MCNP endpoints for writing
        INP source strings.

        Returns:
            INP for surface block object.
        """

        return "\n".join([surface.to_mcnp() for surface in self._cards.values()] + [""])

    def to_arguments(self) -> list:
        """
        'to_arguments' generates lists of surface card objects.

        'to_arguments' creates dictionaries whose keys are
        attribute names, and whose values are attribute value.

        Returns:
            arugments: List of surface blocks object.
        """

        return [card.to_arguments() for card in self._cards.values()]

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        'to_cadquery' generates cadquery from surface block objects.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            Cadquery for surface block object.
        """

        cadquery = "import cadquery as cq\n\n" if hasHeader else ""
        surfaces_line = "\nsurfaces = cq.Workplane()"

        for surface in self.cards.values():
            if hasattr(surface, "to_cadquery"):
                new_cadquery = surface.to_cadquery(hasHeader)
                surfaces_line += f".add({new_cadquery.split(maxsplit=1)[0]})"
                cadquery += new_cadquery

        return cadquery + surfaces_line + "\n\n"

    def to_cadquery_file(self, filename: str, hasHeader: bool = True) -> None:
        """
        'to_cadquery_file' generates cadquery files from surface block objects.

        Parameters:
            filename: Output filename.
            hasHeader: Boolean to include cadquery header.
        """

        with open(filename, "w") as file:
            file.write(self.to_cadquery(hasHeader))
