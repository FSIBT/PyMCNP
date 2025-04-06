import re


""" Preprocessing Functions """


def _preprocess_horizontal(string: str):
    """ """

    tokens = re.split(r'( \d+j)', string)

    string = ''
    for i, token in enumerate(tokens):
        if (match := re.match(r'( \d+)j', token)):
            string += int(match[1]) * ' j'
        else:
            string += token

    return string


def _preprocess_case(string: str):
    """ """

    string = string.lower()

    return string


def _preprocess_whitespace(string: str):
    """ """

    string = re.sub(r' +', ' ', string)
    string = re.sub(r'\n \n', '\n\n', string)
    string = re.sub(r' = | =|= |=', ' ', string)
    string = re.sub(r'\t', '    ', string)

    return string.strip()


def _preprocess_continuation(string: str):
    """ """

    string = string.strip()
    string = re.sub(r'\n +|& *\n *', ' ', string)

    return string


def _preprocess_comments(string: str):
    """ """

    lines = []
    comments = []

    for line in string.split('\n'):
        split = line.split('$', maxsplit=1)

        if len(split) == 2:
            lines.append(split[0])
            comments.append(split[1])
        else:
            lines.append(line)

    return '\n'.join(lines), comments


def preprocess_inp(string: str):
    """ """

    string, comments = _preprocess_comments(string)
    string = _preprocess_case(string)
    string = _preprocess_whitespace(string)
    string = _preprocess_continuation(string)
    string = _preprocess_whitespace(string)
    string = _preprocess_horizontal(string)

    return string, comments


def preprocess_ptrac(string: str):
    """ """

    string = _preprocess_case(string)

    return string


""" Postprocessing Functions """


def postprocess_continuation_line(string: str):
    """ """

    lines = []
    length = 0

    for word in string.split(' '):
        if len(word) + length > 78:
            lines.append('&\n     ')
            length = 5

        lines.append(word)
        length += len(word) + 1

    return ' '.join(lines)
