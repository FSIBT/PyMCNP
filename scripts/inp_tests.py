import re
import pathlib
import itertools

import inp_data


def CAMEL(name: str, more: str = '') -> str:
    if more:
        if '_' in name:
            name = CAMEL(name)
            return name.split('_')[0] + more + '_' + name.split('_')[1]
        else:
            return CAMEL(name) + more
    else:
        name = re.sub('/', '_', name)

        if name:
            return name[0].upper() + name[1:]
        else:
            return ''


def SNAKE(name: str) -> str:
    name = re.sub('/', '_', name)
    return name.lower()


def TEST(element, mod, parent_name):
    valid = [{}, {}, {}]
    for attribute in element.attributes:
        if attribute.type == 'types.String':
            valid[0][attribute.name] = "'a'"
            valid[1][attribute.name] = "'a'"
            valid[2][attribute.name] = '_utils.STRING'
        elif attribute.type == 'types.Integer' or attribute.type == 'types.Integer':
            valid[0][attribute.name] = "'1'"
            valid[1][attribute.name] = '1'
            valid[2][attribute.name] = '_utils.INTEGER'
        elif attribute.type == 'types.Real' or attribute.type == 'types.Real':
            valid[0][attribute.name] = "'1.0'"
            valid[1][attribute.name] = '1.0'
            valid[2][attribute.name] = '_utils.REAL'
        elif attribute.type == 'types.Designator':
            valid[0][attribute.name] = "'n'"
            valid[1][attribute.name] = "'n'"
            valid[2][attribute.name] = '_utils.DESIGNATOR'
        elif (
            attribute.type == 'types.Tuple[types.Integer]'
            or attribute.type == 'types.Tuple[types.Integer]'
        ):
            valid[0][attribute.name] = "['1']"
            valid[1][attribute.name] = '[1]'
            valid[2][attribute.name] = '[_utils.INTEGER]'
        elif (
            attribute.type == 'types.Tuple[types.Real]'
            or attribute.type == 'types.Tuple[types.Real]'
        ):
            valid[0][attribute.name] = "['1.0']"
            valid[1][attribute.name] = '[1.0]'
            valid[2][attribute.name] = '[_utils.REAL]'
        elif attribute.type == 'types.Jump':
            valid[0][attribute.name] = "'J'"
            valid[1][attribute.name] = "'J'"
            valid[2][attribute.name] = '_utils.JUMP'
        else:
            if parent_name not in {'cell', 'surface'}:
                print(attribute.type)
            valid[0][attribute.name] = None
            valid[1][attribute.name] = None
            valid[2][attribute.name] = None

    invalid = []
    for _ in range(len(element.attributes)):
        invalid.append(valid[0].copy())

    for i, example in enumerate(invalid):
        example[list(example.keys())[i]] = None

    return f"""
class Test_{CAMEL(parent_name)}{CAMEL(element.name)}:

    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.{f"{mod}." if mod else ""}{CAMEL(element.name)}
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.{f"{mod}." if mod else ""}{CAMEL(element.name, 'Builder')}
        EXAMPLES_VALID = [{', '.join(f'{{{", ".join(f"'{key}':{val}" for key, val in example.items())}}}' for example in valid)}]
        EXAMPLES_INVALID = [{', '.join(f'{{{", ".join(f"'{key}':{val}" for key, val in example.items())}}}' for example in invalid)}]
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
