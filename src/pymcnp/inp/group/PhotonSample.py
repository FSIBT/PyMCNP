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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    mt: literal.Integer | int | str = dataclasses.field(kw_only=True)
    pmt: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
