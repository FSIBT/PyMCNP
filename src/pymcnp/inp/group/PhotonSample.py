from .. import literal
from ..Group import Group


class PhotonSample(Group):
    """
    Represents photon sample groups.

    Attributes:
        mt: photon sample group ``mt`` parameter.
        pmt: photon sample group ``pmt`` parameter.
    """

    mt: literal.Integer
    pmt: literal.Real
