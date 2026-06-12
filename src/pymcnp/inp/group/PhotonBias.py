import typing
import dataclasses

import collections
from ... import abc
from .. import literal
from ..Group import Group
from .PhotonSample import PhotonSample


class PhotonBias(Group):
    """
    Represents photon bias groups.

    Attributes:
        target_identifier: photon bias group `target_identifier` parameter.
        ipik: photon bias group `ipik` parameter.
        mt_pmt: photon bias group `mt_pmt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    target_identifier: literal.Zaid | str
    ipik: literal.Integer | int | str
    mt_pmt: typing.Annotated[abc.Array, PhotonSample, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[PhotonSample | str] | str = abc.Terminal[r'']('')
