import re
import copy
import inspect
import pathlib


class McnpElement_:
    """
    Represents generic MCNP syntax elements.
    """

    _REGEX: re.Pattern

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self):
        raise NotImplementedError

    def __str__(self):
        return self.to_mcnp()

    def __eq__(a, b):
        return (a.__dict__ if a else None) == (b.__dict__ if b else None)

    def modify(self, **modifications):
        """
        Updates immutable MCNP objects.

        Parameters:
            modifications: Dictionary of attributes and modifiers.
        """

        attributes = {}

        parameters = inspect.signature(self.__class__.__init__).parameters
        for parameter in filter(lambda p: p != 'self', parameters):
            if isinstance(self.__dict__[parameter], dict):
                attributes[parameter] = tuple(self.__dict__[parameter].values())
            else:
                attributes[parameter] = self.__dict__[parameter]

        for attribute, modifier in modifications.items():
            subattributes = attribute.split('.')

            for i, _ in enumerate(subattributes[1:]):
                modifier = eval(f'self.{".".join(subattributes[:-1-i])}').modify(
                    **{subattributes[-1 - i]: modifier}
                )

            if match := re.match(r'(\S+)\[(\S+)\]', subattributes[0]):
                subattributes[0] = match[1]
                temp = copy.deepcopy(eval(f'self.{subattributes[0]}'))
                temp[eval(match[2])] = modifier

                if isinstance(temp, dict):
                    modifier = tuple(temp.values())
                else:
                    modifier = temp

            attributes[subattributes[0]] = modifier

        return self.__class__(*attributes.values())

    def append(self, **additions):
        """
        Appends to immutable MCNP collections.

        Parameters:
            additions: Dictionary of attributes and addends.
        """

        attributes = {}

        parameters = inspect.signature(self.__class__.__init__).parameters
        for parameter in filter(lambda p: p != 'self', parameters):
            if isinstance(self.__dict__[parameter], dict):
                attributes[parameter] = tuple(self.__dict__[parameter].values())
            else:
                attributes[parameter] = self.__dict__[parameter]

        for attribute, addend in additions.items():
            subattributes = attribute.split('.')

            for i, _ in enumerate(subattributes[1:]):
                addend = eval(f'self.{".".join(subattributes[:-1-i])}').append(
                    **{subattributes[-1 - i]: addend}
                )

            if match := re.match(r'(\S+)\[(\S+)\]', subattributes[0]):
                subattributes[0] = match[1]
                temp = copy.deepcopy(eval(f'self.{subattributes[0]}'))
                temp[eval(match[2])] = addend

                if isinstance(temp, dict):
                    addend = tuple(temp.values())
                else:
                    addend = temp

            temp = copy.deepcopy(eval(f'self.{subattributes[0]}'))
            if isinstance(temp, dict):
                attributes[subattributes[0]] = (*temp.values(), addend)
            elif isinstance(temp, tuple):
                attributes[subattributes[0]] = (*temp, addend)
            else:
                raise Exception

        return self.__class__(*attributes.values())


class McnpRegistry_(McnpElement_):
    """
    Represents generic MCNP syntax elements with subclass registries.
    """

    _SUBCLASSES: dict[str, list[McnpElement_]]


class McnpFile_(McnpElement_):
    """
    Represents generic MCNP files.
    """

    @staticmethod
    def from_mcnp_file(filename: pathlib.Path | str):
        raise NotImplementedError

    def to_mcnp_file(self, filename: str | pathlib.Path):
        """
        Generates MCNP files from ``McnpFile_``.

        Parameters:
            filename: new MCNP file path.
        """

        filename = pathlib.Path(filename)

        if not filename.is_file():
            raise Exception

        filename.write_text(self.to_mcnp())
