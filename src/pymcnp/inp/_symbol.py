import re

from .. import _symbol


class InpNonterminal(_symbol.Nonterminal):
    """
    Represents generic MCNP nonterminal symbols.
    """

    @staticmethod
    def _preprocess(source: str) -> str:
        """
        Preprocess INP for `from_mcnp`.

        Parameters:
            source: INP to preprocess.

        Returns:
            Preprocess INP.
        """

        source = re.sub(r'\n +|& *\n *', ' ', source)
        source = re.sub(r' +', ' ', source)
        source = re.sub(r'[(] ', '(', source)
        source = re.sub(r' [)]', ')', source)
        source = re.sub(r'\n \n', '\n\n', source)
        source = re.sub(r' = | =|= |=', ' ', source)
        source = re.sub(r'\t', '    ', source)
        source = source.strip()

        source = re.sub(r'((?: [jJ]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}j' + match[2], source)
        source = re.sub(r'((?: [rR]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}r' + match[2], source)
        source = re.sub(r'((?: [iI]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}i' + match[2], source)
        source = re.sub(r'((?: [lL][oO][gG]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}log' + match[2], source)
        source = re.sub(r'((?: [iI][lL][oO][gG]){2,})(\s|\Z|\n)', lambda match: f' {len(match[1].strip().split())}ilog' + match[2], source)
        source = re.sub(r' (\d+)[jJ](\s|\Z|\n)', lambda match: int(match[1]) * ' j' + match[2], source)
        source = re.sub(r' (\d+)[rR](\s|\Z|\n)', lambda match: int(match[1]) * ' r' + match[2], source)
        source = re.sub(r' (\d+)[iI](\s|\Z|\n)', lambda match: int(match[1]) * ' i' + match[2], source)
        source = re.sub(r' (\d+)[jJ](\s|\Z|\n)', lambda match: int(match[1]) * ' j' + match[2], source)
        source = re.sub(r' (\d+)[lL][oO][gG](\s|\Z|\n)', lambda match: int(match[1]) * ' log' + match[2], source)
        source = re.sub(r' (\d+)[iI][lL][oO][gG](\s|\Z|\n)', lambda match: int(match[1]) * ' ilog' + match[2], source)

        return source
