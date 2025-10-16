from .. import _option


class SdefOption(_option.Option):
    """
    Represents generic INP sdef options.
    """

    # (?:(?:ara|ccc|cel|eff|erg|ext|nrm|rad|sur|tme|wgt|tr|tr|x|y|z) (?:j|log|ilog|\d*m|i|r|[-+0-9.eE]+))|(?:(?:ara|axs|bap|bem|ccc|cel|dat|dir|eff|erg|ext|loc|nrm|par|pos|rad|sur|tme|vec|wgt|tr|x|y|z) f(?:cel|sur|erg|tme|dir|vec|nrm|pos|rad|ext|axs|ccc|ara|wgt|eff|par|dat|loc|bem|bap|tr|x|y|z) [dD]\d+)|(?:(?:axs|bap|bem|dat|loc|vec) (?:j|log|ilog|\d*m|i|r|[-+0-9.eE]+) (?:j|log|ilog|\d*m|i|r|[-+0-9.eE]+) (?:j|log|ilog|\d*m|i|r|[-+0-9.eE]+))|(?:pos(?: (?:j|log|ilog|\d*m|i|r|[-+0-9.eE]+))+?)|(?:dir (?:j|log|ilog|\d*m|i|r|[-+0-9.eE]+)?)|(?:tme [dD]\d+(?: ?< ?[dD]\d+)*)|(?:par \S+)|(?:(?:erg|dir|rad|cel|x|y|z|tr|pos) [dD]\d+)

    pass
