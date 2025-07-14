import re
import decimal


""" Preprocessing Functions """


def _preprocess_vertical(string: str):
    """ """

    tokens = re.split(r'\n(#(?: \S+)+\n(?: *\d\S*(?: +\S+)+\n)+)', string)

    string = ''
    for token in tokens:
        if match := re.match(r'#((?: \S+)+)\n((?: *\d\S*(?: +\S+)+\n)+)', token):
            cards = re.split(r'\s+', match[1])[1:]
            rows = [[card] for card in cards]

            lines = match[2].split('\n')[:-1]
            for line in lines:
                parameters = re.split(r'\s+', line)
                for parameter, row in zip(parameters, rows):
                    row.append(parameter)

            string += '\n' + '\n'.join([' '.join(row) for row in rows]) + '\n'
        else:
            string += token

    return string


def _preprocess_horizontal(string: str):
    """ """

    tokens = re.split(r'( \d+j)', string)

    string = ''
    for token in tokens:
        if match := re.match(r'( \d+)j', token):
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
    string = re.sub(r'[(] ', '(', string)
    string = re.sub(r' [)]', ')', string)
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

    string = _preprocess_vertical(string)
    string, comments = _preprocess_comments(string)
    string = _preprocess_case(string)
    string = _preprocess_whitespace(string)
    string = _preprocess_continuation(string)
    string = _preprocess_whitespace(string)
    string = _preprocess_horizontal(string)

    return string, comments


""" Postprocessing Functions """


def _postprocess_continuation_line(string: str):
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


def postprocess_exponenet(number: decimal.Decimal, percision: int, offset: int = 1):
    """ """

    e = number.adjusted() + offset

    s, d, _ = number.as_tuple()
    s = '-' if s else ' '
    d = ''.join(map(str, d[: percision - offset + 1]))

    if d == '0':
        return f'{s}0.{'0' * (percision - 1)}E+00'
    else:
        d = offset * '0' + d

        a = d[:1]
        b = d[1:]

        return f'{s}{a}.{b}E{e:+03}'


def postprocess_inp(string: str):
    """ """

    string = _postprocess_continuation_line(string)

    return string
