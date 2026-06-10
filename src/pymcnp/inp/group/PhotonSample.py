import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class PhotonSample(Group):
    """
    Represents photonsample groups.

    Attributes:
        mt: photonsample group `mt` parameter.
        pmt: photonsample group `pmt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    mt: literal.Integer | int | str
    pmt: literal.Real | int | float | decimal.Decimal | str
