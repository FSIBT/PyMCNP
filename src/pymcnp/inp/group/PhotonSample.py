import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class PhotonSample(Group):
    """
    Represents photon sample groups.

    Attributes:
        mt: photon sample group `mt` parameter.
        pmt: photon sample group `pmt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    mt: literal.Integer | int | str
    pmt: literal.Real | int | float | decimal.Decimal | str
