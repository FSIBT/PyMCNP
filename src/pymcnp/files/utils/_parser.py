"""
Contains classes for preprocessing, postprocessing, and parsing INP & PTRAC.
"""

import re
import collections
import itertools


class Parser:
    """
    ``Parser`` implements a deque with PyMCNP error handling.

    ``Parser`` wraps the ``collections.deque`` structure from the Python
    standard library with error handling consitent with PyMCNP. This class
    provides methods to peek, push, and pop strings, aiding in parsing.
    """

    def __init__(self, iterable, err: Exception):
        """
        ``__init__`` initializes ``Parser``

        Parameters:
            iterable: Initial iterable.
            err: Empty deque error.
        """

        self.deque = collections.deque(iterable)
        self.err = err

    def pushl(self, item: any) -> None:
        """
        ``pushl`` pushes items unto the front of deques.

        Parameters:
            item: Item to push.
        """

        self.deque.appendleft(item)

    def pushr(self, item: any) -> None:
        """
        ``pushr`` pushes items unto the back of deques.

        Parameters:
            item: Item to push.
        """

        self.deque.append(item)

    def popl(self) -> any:
        """
        ``popl`` pops items from unto the front of deques.

        Returns:
            Item from the front of the deque.

        Raises:
            self.err
        """

        if not bool(self):
            raise self.err

        return self.deque.popleft()

    def popr(self) -> str:
        """
        ``popr`` pop items from the back of deques.

        Returns:
            Item from the back of the deque.

        Raises:
            self.err
        """

        if not bool(self):
            raise self.err

        return self.deque.pop()

    def peekl(self) -> str:
        """
        ``peekl`` peeks at the item at the front of deques.

        Returns:
            Reference to item at the front of the deque.

        Raises:
            self.err
        """

        if not bool(self):
            raise self.err

        return self.deque[0]

    def peekr(self) -> str:
        """
        ``peekr`` peeks at the item at the back of deques.

        Returns:
            Reference to item at the back of the deque.

        Raises:
            self.err
        """

        if not bool(self):
            raise self.err

        return self.deque[-1]

    def __len__(self):
        """
        ``__len__`` calculates the length of deques.

        Returns:
            Deque length.
        """

        return len(self.deque)

    def __bool__(self):
        """
        ``__bool__`` calculautes the boolean value of deques.

        ``__bool__`` returns False if the list is empty and True otherwise.

        Returns:
            Deque boolean value.
        """

        return len(self.deque) != 0

    def __str__(self):
        """
        ``__str__`` stringifies deques.
        """

        return str(list(self.deque))

    @classmethod
    def from_fortran(cls, specifiers: list[int], string: str, err: Exception):
        """
        ``from_fortran`` generates ``Parser`` objects from strings and lengths.

        Parameters:
            specifiers: Fortran specifier lengths.
            string: String to read.
            err: Empty deque error.

        Returns:
            ``Parser`` based on string split.

        Raises:
            err
        """

        if len(string) != sum(specifiers):
            raise err

        specifiers = [0] + specifiers
        indicies = list(itertools.accumulate(specifiers))
        tokens = [string[i:j] for i, j in zip(indicies, indicies[1:])]

        return cls(tokens, err)


class Preprocessor:
    """
    ``Preprocessor`` encapsulates methods for MCNP source preprocessing.

    ``Preprocessor`` provides static method for transforming MCNP strings.
    The class processes case, tabs, contiutation lines, and whitespace, and it
    combines these operations into dedicated method for processing INP and
    PTRAC strings.
    """

    @staticmethod
    def _process_jump(string: str) -> str:
        for match in re.finditer(r'(\s)(\d+)j(\s)', string):
            string = (
                string[: match.start(0)]
                + match[1]
                + ' j' * int(match[2])
                + match[3]
                + string[match.end(0) :]
            )

        return string

    @staticmethod
    def _process_repeat(string: str) -> str:
        for match in re.finditer(r'\s(\S+)\s(\d*)r(\s)', string):
            string = (
                string[: match.start(0)]
                + f' {match[1]}' * (int(match[2] if match[2] else 1) + 1)
                + match[3]
                + string[match.end(0) :]
            )

        return string

    @staticmethod
    def _process_case(string: str) -> str:
        """
        ``_process_case`` replaces upper case with lower case from strings.

        Parameters:
            string: String to preprocess.

        Returns:
            Lower case string.
        """

        string = string.lower()

        return string

    @staticmethod
    def _process_tabs(string: str) -> str:
        """
        ``_process_whitespace`` replaces tabs with whitespaces from strings.

        Parameters:
           string: String to preprocess.

        Returns:
            String without tabs.
        """

        string = re.sub(r'\t', '    ', string)

        return string

    @staticmethod
    def _process_continuation(string: str) -> str:
        """
        ``_process_continuation`` processes MCNP continuation lines.

        ``_process_continuation`` replaces continuation lines with single
        spaces, removing them and adding their content to the inital lines.

        Parameters:
            string: String to preprocess.

        Returns:
            MCNP string without continuation lines.
        """

        string = re.sub(r'\n *\n', '\n\n', string)

        # Processing comments, storing and subsituting
        comments = re.findall(r'[$].*?(?=\n|\Z)', string)
        char = '*'
        while char in string:
            char += '*' if char[-1] == '&' else '&'
        string = re.sub(r'[$].*?(?=\n|\Z)', char, string)

        # Processing continuation lines
        string = re.sub(r'\n +|& *\n +', ' ', string)

        # Processing inline comments
        lines = []
        for line in string.split('\n'):
            if char in line:
                count = line.count(char)
                content = ' '.join(segment.strip() for segment in line.split(char))
                comment = ' '.join(comments.pop(0) for _ in range(count))
                lines.append(content + ' ' + comment)
            else:
                lines.append(line)

        return '\n'.join(lines)

    @staticmethod
    def _process_whitespace(string: str) -> str:
        """
        ``_process_whitespace`` removes extra whitespace from strings.

        Parameters:
            string: String to preprocess.

        Returns:
            MCNP string without extra whitespace.
        """

        string = re.sub(r' +', ' ', string)
        string = re.sub(r'( \n)|(\n )', '\n', string)

        return string

    @staticmethod
    def _process_equals(string: str) -> str:
        """
        ``_process_equals`` removes extra whitespace around equal signs from strings.

        Parameters:
            string: String to preprocess.

        Returns:
            MCNP string without extra whitespace around equal signs.
        """

        string = re.sub(r' = | =|= ', '=', string)

        return string

    @staticmethod
    def _process_comments(string: str) -> str:
        """
        ``_process_equals`` removes inline comments from strings.

        Parameters:
            string: String to preprocess.

        Returns:
            MCNP string without inline comments.
        """

        string = re.sub(r'[$].+(\n|\Z)', '\n', string)

        return string

    @staticmethod
    def _process_verticalformat(string: str) -> str:
        table = []
        output = ''
        for line in string.split('\n'):
            if line.startswith('#', 0, 5):
                output += '\n'.join(table)
                table = line.split(' ')[1:]
            elif table != [] and not re.match(
                r'(vol|area|tr|[*]tr|u|lat|fill|[*]fill|uran|dm|dawwg|embed|embee|embeb|embem|embtb \
                |embtm|embde|embdf|m|mt|mx|otfdb|totnu|nonu|awtab|xs|void|mgopt|drxs|mode|phys|act  \
                |cut|elpt|tmp|thtme|mphys|lca|lcb|lcc|lea|leb|fmult|tropt|unc|cosyp|cosy|bfld|bflcl \
                |field|sdef|si|sp|sb|ds|sc|ssw|ssr|kcode|ksrc|kopts|hsrc|burn|source|srdx|f|[*]f    \
                |fip|fir|fic|fc|e|t|c|[*]c|fq|em|de|df|em|tm|cm|cf|sf|fs|sd|fu|tallyx|ft|tf|notrn   \
                |pert|kpert|ksen|tmesh|fmesh|spdtl|imp|var|wwe|wwt|wwn|wwp|wwg|wwge|wwgt|mesh|esplt \
                |tsplt|ext|vect|fcl|dxt|dd|pd|dxc|bbrem|pikmt|spabi|pwt|nps|ctme|stop|print|talnp   \
                |prdmp|ptrac|mplot|histp|rand|dbcn|lost|idum|rdum|za|zb|zc|zd|file).+',
                line,
            ):
                for i, token in enumerate(line.split(' ')):
                    table[i] += f' {token}'
            else:
                output += '\n'.join(table + [line]) + '\n'
                table = []

        output += '\n'.join(table)

        return output

    @staticmethod
    def process_inp_comments(string: str) -> tuple:
        """
        ``process_inp_comments`` preprocess INP inline comments.

        ``process_inp_comments`` isolates INP inlines comments from the rest of
        the source code.

        Parameters:
            string: String to preprocess.

        Returns:
            Tuple of string and inline comments.
        """

        string = Preprocessor._process_continuation(string)
        string, *comments = string.split('$')

        string = string.strip()
        comments = [comment.strip() for comment in comments]

        return string, comments

    @staticmethod
    def process_inp(string: str, hasColumnarData=True) -> str:
        """
        ``process_inp`` preprocesses INP strings.

        ``process_inp`` removes extra whitespace, upper case letters, and
        processes continuation lines.

        Parameters:
            string: String to preprocess.
            hasComments: Process vertical data format flag.

        Returns:
            Preprocessed INP.
        """

        string = Preprocessor._process_case(string)
        string = Preprocessor._process_tabs(string)
        string = Preprocessor._process_jump(string)
        string = Preprocessor._process_repeat(string)
        string = Preprocessor._process_continuation(string)

        if hasColumnarData:
            string = Preprocessor._process_whitespace(string)
            string = Preprocessor._process_verticalformat(string)

        string = Preprocessor._process_whitespace(string)
        string = Preprocessor._process_equals(string)
        string = string.strip(' ')
        string = string.strip('\n')

        return string

    @staticmethod
    def process_ptrac(string: str) -> str:
        """
        ``process_ptrac`` preprocesses PTRAC strings.

        ``process_ptrac`` removes extra whitespace and upper case letters.

        Parameters:
            string: String to preprocess.

        Returns:
            Preprocessed PTRAC.
        """

        string = Preprocessor._process_case(string)

        return string


class Postprocessor:
    """
    ``Postprocessor`` encapsulates methods for MCNP source postprocesing.

    ``Preprocessor`` provides static method for transforming MCNP strings.
    The class undoes preprocessing by adding continuation lines as needed.
    """

    @staticmethod
    def add_continuation_lines(string: str) -> str:
        """
        ``add_continuation_lines`` adds INP continuation lines.

        Parameters:
            string: String to postprocessed as needed.

        Returns:
            String with continuation lines as needed.
        """

        out = []
        line_length = 0

        for word in string.split(' '):
            if len(word) + line_length > 80 or len(word) + line_length > 78:
                out += ' &\n     '
                line_length = 5

            out.append(word)
            line_length += len(word) + 1

        return ' '.join(out)
