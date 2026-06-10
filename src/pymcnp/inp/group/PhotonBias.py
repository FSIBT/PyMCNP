import typing
import dataclasses

import collections
from ... import abc
from .. import literal
from ..Group import Group
from .PhotonSample import PhotonSample


class PhotonBias(Group):
    """
    Represents photonbias groups.

    Attributes:
        target_identifier: photonbias group `target_identifier` parameter.
        ipik: photonbias group `ipik` parameter.
        mt_pmt: photonbias group `mt_pmt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    target_identifier: literal.Zaid | str
    ipik: literal.Integer | int | str
    mt_pmt: typing.Annotated[abc.Array, PhotonSample, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[PhotonSample | str] | str = abc.Terminal[r'']('')
