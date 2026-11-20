import typing

from ... import abc
from .. import literal
from ..Group import Group
from .PhotonSample import PhotonSample


class PhotonBias(Group):
    """
    Represents photon bias groups.

    Attributes:
        target_identifier: photon bias group ``target_identifier`` parameter.
        ipik: photon bias group ``ipik`` parameter.
        mt_pmt: photon bias group ``mt_pmt`` parameter.
    """

    target_identifier: literal.Zaid
    ipik: literal.Integer
    mt_pmt: typing.Annotated[abc.Array, PhotonSample, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
