"""
Contains functions to streamline PyMCNP workflows.
"""

import inspect


def modify(modificand, modifications: dict[str, any]):
    """
    Updates immutable PyMCNP objects.

    ``modify`` copies of PyMCNP objects and makes the given modifications.

    Parameters:
        modificand: PyMCNP object to copy and modify.
        modifications: Dictionary of attributes and modifiers.
    """

    new_attributes = {}

    # Copying
    parameters = inspect.signature(modificand.__class__.__init__).parameters
    for parameter in parameters:
        if parameter == 'self':
            continue

        new_attributes[parameter] = modificand.__dict__[parameter]

    # Substituting
    for attribute, modifier in modifications.items():
        subattributes = attribute.split('.')

        try:
            eval(f'modificand.{subattributes[0]}')
        except AttributeError:
            raise ValueError

        if '.' in attribute:
            submodifications = {}
            submodifications['.'.join(subattributes[1:])] = modifier
            modifier = modify(eval(f'modificand.{subattributes[0]}'), submodifications)

        if '[' in attribute:
            name, index = subattributes[0].split('[', maxsplit=1)
            collection = list(new_attributes[name])
            exec(f'collection[{index} = modifier')
            modifier = tuple(collection)
            subattributes[0] = name

        new_attributes[subattributes[0]] = modifier

    return modificand.__class__(*new_attributes.values())
