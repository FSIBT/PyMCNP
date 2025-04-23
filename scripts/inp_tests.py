import re
import pathlib
import itertools

import inp_data


def CAMEL(name: str) -> str:
    name = re.sub('/', '_', name)
    if name:
        return name[0].upper() + name[1:]
    else:
        return ''


def SNAKE(name: str) -> str:
    name = re.sub('/', '_', name)
    return name.lower()


def TEST(element, mod, parent_name):
    return f"""
class Test_{CAMEL(parent_name)}{CAMEL(element.name)}:

    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.{f"{mod}." if mod else ""}{CAMEL(element.name)}
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []
"""[1:]


path = pathlib.Path(__file__).parent / '..' / 'tests'


def get_tests(element, mod, parent_name):
    if element.options:
        return [TEST(element, mod, parent_name)] + list(
            itertools.chain(
                *(
                    get_tests(
                        option, mod + ('.' if mod else '') + SNAKE(element.name), element.name
                    )
                    for option in element.options
                )
            )
        )
    else:
        return [TEST(element, mod, parent_name)]


for card in inp_data.cards.options:
    tests = get_tests(card, '', '')

    res = f"""
import pymcnp
import _utils


{'\n\n'.join(tests)}
"""[1:]

    path_file = pathlib.Path(__file__).parent.parent / 'tests' / f'test_{card.name}.py'
    with path_file.open('w') as file:
        file.write(res)
