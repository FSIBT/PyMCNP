"""
Contains functions to streamline PyMCNP workflows.
"""

import inspect
from . import files


def modify(modificand, **modifications):
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

        # Type Coercion
        if not isinstance(modifier, type(new_attributes[subattributes[0]])):
            if isinstance(
                new_attributes[subattributes[0]], files.utils.types.McnpInteger
            ) and isinstance(modifier, int):
                modifier = files.utils.types.McnpInteger(modifier)
            if isinstance(
                new_attributes[subattributes[0]], files.utils.types.McnpReal
            ) and isinstance(modifier, float):
                modifier = files.utils.types.McnpReal(modifier)

        new_attributes[subattributes[0]] = modifier

    new = modificand.__class__(*new_attributes.values())
    modificand.__dict__ = new.__dict__
    new.__class__ = new.__class__
