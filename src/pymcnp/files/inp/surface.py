"""
Contains classes representing INP surface cards.
"""

from . import _card
from ..utils import _parser


class Surface(_card.Card):
    """
    Represents INP data cards.

    ``Surface`` extends the ``_card.Card`` abstract class.

    Attributes:
        ident: Card identifier.
        line_number: Card line number.
        comment: Card inline comment.
        number: Surface card number.
        mnemonic: Surface card type identifier.
        transform: Surface card transformation number.
        periodic: Surface card periodic number.
        parameters: Surface parameter list.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Surface``.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Surface``.
        """

        number_str = self.number.to_mcnp()
        transform_str = self.transform.to_mcnp() if self.transform is not None else ' '
        parameter_str = ' '.join(
            str(parameter.value) if hasattr(parameter, 'to_mcnp') else str(parameter)
            for parameter in self.parameters
        )

        source = f'{number_str} {transform_str} {self.mnemonic.to_mcnp()} {parameter_str}'

        return _parser.Postprocessor.add_continuation_lines(source)

    def to_pyvista(self):
        raise NotImplementedError
