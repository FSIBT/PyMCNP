"""
``_parser`` contains preprocessor, parser, and postprocessor classes.

PyMCNP relies on these classes to prepare MCNP for parsing and printing by
collapsing whitespace and processing continuation lines. ``_parser`` employs
regular expressions and the deque data structure.
"""


import re
import collections


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


class Preprocessor:
    """
    ``Preprocessor`` encapsulates methods for MCNP source preprocessing.

    ``Preprocessor`` provides static method for transforming MCNP strings.
    The class processes case, tabs, contiutation lines, and whitespace, and it
    combines these operations into dedicated method for processing INP and
    PTRAC strings.
    """

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

        string = re.sub(r"\t", "    ", string)

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

        string = re.sub(r"( &\n)|(\n     )", r" ", string)

        return string

    @staticmethod
    def _process_whitespace(string: str) -> str:
        """
        ``_process_whitespace`` removes extra whitespace from strings.

        Parameters:
            string: String to preprocess.

        Returns:
            MCNP string without extra whitespace.
        """

        string = re.sub(r"( \n)|(\n )", "\n", string)
        string = re.sub(r" +", " ", string)

        return string

    @staticmethod
    def process_inp(string: str) -> str:
        """
        ``process_inp`` preprocesses INP strings.

        ``process_inp`` removes extra whitespace, upper case letters, and
        processes continuation lines.

        Parameter:
            string: String to preprocess.

        Returns:
            Preprocessed INP.
        """

        string = Preprocessor._process_case(string)
        string = Preprocessor._process_continuation(string)
        string = Preprocessor._process_whitespace(string)
        string = string.strip(" ")

        return string

    @staticmethod
    def process_ptrac(string: str) -> str:
        """
        ``process_ptrac`` preprocesses PTRAC strings.

        ``process_ptrac`` removes extra whitespace and upper case letters.

        Parameter:
            string: String to preprocess.

        Returns:
            Preprocessed PTRAC.
        """

        string = Preprocessor._process_case(string)
        string = Preprocessor._process_whitespace(string)

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

        Parameter:
            string: String to postprocessed as needed.

        Returns:
            String with continuation lines as needed.
        """

        out = ""
        line_length = 0
        words = string.split(" ")

        for word in words:
            if len(word) + line_length > 80 or len(word) + line_length > 78 and words:
                out += " &\n     "
                line_length = 5

            out += word + " "
            line_length += len(word) + 1

        return out
