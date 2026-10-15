import functools
import re
import re._constants as _constants
import re._parser as _parser

from .. import _symbol


@functools.cache
def _top_groups(regex: re.Pattern) -> tuple[int, ...]:
    """
    Finds the capture groups of a pattern that are not nested in another capture group.

    Embedded sub-patterns bring their own capture groups, which shift the group numbers.
    """

    found = []

    def walk(items):
        for op, arg in items:
            if op is _constants.SUBPATTERN:
                group, _, _, body = arg
                if group:
                    found.append(group)
                else:
                    walk(body)
            elif op in (_constants.MAX_REPEAT, _constants.MIN_REPEAT):
                walk(arg[2])
            elif op is _constants.BRANCH:
                for branch in arg[1]:
                    walk(branch)

    walk(_parser.parse(regex.pattern, regex.flags))
    return tuple(found)


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
