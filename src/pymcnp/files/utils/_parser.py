"""
'parser'
"""


import re
import collections


class Parser:
    """
    'Parser'
    """

    def __init__(self, iterable, err: Exception):
        """
        '__init__'
        """

        self.deque = collections.deque(iterable)
        self.err = err

    def pushl(self, item: any) -> None:
        """
        'pushl'
        """

        self.deque.appendleft(item)

    def pushr(self, item: any) -> None:
        """
        'pushr'
        """

        self.deque.append(item)

    def popl(self) -> any:
        """
        'popl'
        """

        if not bool(self):
            raise self.err

        return self.deque.popleft()

    def peekl(self) -> str:
        """
        'peekl'
        """

        if not bool(self):
            raise self.err

        return self.deque[0]

    def popr(self) -> str:
        """
        'popr'
        """

        if not bool(self):
            raise self.err

        return self.deque.pop()

    def peekr(self) -> str:
        """
        'peekr'
        """

        if not bool(self):
            raise self.err

        return self.deque[-1]

    def __len__(self):
        """
        '__len__'
        """

        return len(self.deque)

    def __bool__(self):
        """
        '__bool__'
        """

        return len(self.deque) != 0

    def __str__(self):
        """
        '__str__'
        """

        return str(list(self.deque))


class Preprocessor:
    """
    'Preprocessor'
    """

    @staticmethod
    def _process_case(string: str) -> str:
        """
        '_process_case'
        """

        string = string.lower()

        return string

    @staticmethod
    def _process_tabs(string: str) -> str:
        """
        '_process_whitespace'
        """

        string = re.sub(r"\t", "    ", string)

        return string

    @staticmethod
    def _process_continuation(string: str) -> str:
        """
        '_process_continuation'
        """

        string = re.sub(r"( &\n)|(\n     )", r" ", string)

        return string

    @staticmethod
    def _process_whitespace(string: str) -> str:
        """
        '_process_whitespace'
        """

        string = re.sub(r"( \n)|(\n )", "\n", string)
        string = re.sub(r" +", " ", string)

        return string

    @staticmethod
    def process_inp(string: str) -> str:
        """
        'process_inp'
        """

        string = Preprocessor._process_case(string)
        string = Preprocessor._process_continuation(string)
        string = Preprocessor._process_whitespace(string)
        string = string.strip(" ")

        return string

    @staticmethod
    def process_ptrac(string: str) -> str:
        """
        'process_ptrac'
        """

        string = Preprocessor._process_case(string)
        string = Preprocessor._process_whitespace(string)

        return string


class Postprocessor:
    """
    'Postprocessor'
    """

    @staticmethod
    def add_continuation_lines(string: str) -> str:
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
