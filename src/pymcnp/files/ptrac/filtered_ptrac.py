"""
Contains classes representing fitlered PTRAC file.
"""

from . import ptrac
from . import header
from . import filters
from . import filtered_history


class FilteredPtrac(ptrac.Ptrac):
    @staticmethod
    def from_mcnp(source: str, filters: filters.Filters):
        """
        ``from_mcnp`` generates ``Ptrac`` objects from PTRAC.

        ``from_mcnp`` constructs instances of ``FilterPtrac`` from PTRAC source
        strings, so it operates as a class constructor method and PTRAC parser.
        It filters ``Event`` objects using filters.

        Parameters:
            source: PTRAC source string.
            filters: PyMCNP PTRAC filters.


        Returns:
            ``FilteredPtrac`` object.
        """

        # Processing Header
        head, lines = header.Header.from_mcnp(source)

        # Processing History
        def histories(lines):
            while lines:
                history, lines = filtered_history.FilteredHistory.from_mcnp(lines, head, filters)
                yield history

        return FilteredPtrac(head, histories(lines))

    @staticmethod
    def from_mcnp_file(filename: str, filters: filters.Filters):
        """
        ``from_mcnp_file`` generates ``Ptrac`` objects from PTRAC files.

        ``from_mcnp_file`` constructs instances of ``FilteredPtrac`` from PTRAC files,
        so it operates as a class constructor method and PTRAC parser.
        It filters ``Event`` objects using filters.

        Parameters:
            filename: Name of file to parse.

        Returns:
            ``FilteredPtrac`` object.
        """

        with open(filename) as file:
            source = ''.join(file.readlines())

        return FilteredPtrac.from_mcnp(source, filters)
