import re
import pathlib

import inp_data


def CAMEL(name: str, more: str = '') -> str:
    if more:
        if '_' in name:
            name = CAMEL(name)
            return name.split('_')[0] + more + '_' + name.split('_')[1]
        else:
            return CAMEL(name) + more
    else:
        name = re.sub('/', '_', name)

        if name:
            return name[0].upper() + name[1:]
        else:
            return ''


def SNAKE(name: str) -> str:
    name = re.sub('/', '_', name)
    return name.lower()


def TEST(element, mod):
    valid = [{}, {}, {}]
    extra = {}

    for attribute in element.attributes:
        if attribute.type == 'types.Repeat':
            valid[0][attribute.name] = '_utils.string.type.REPEAT'
            valid[1][attribute.name] = '_utils.string.type.REPEAT'
            valid[2][attribute.name] = '_utils.ast.type.REPEAT'
        elif attribute.type == 'types.Insert':
            valid[0][attribute.name] = '_utils.string.type.INSERT'
            valid[1][attribute.name] = '_utils.string.type.INSERT'
            valid[2][attribute.name] = '_utils.ast.type.INSERT'
        elif attribute.type == 'types.Multiply':
            valid[0][attribute.name] = '_utils.string.type.MULTIPLY'
            valid[1][attribute.name] = '_utils.string.type.MULTIPLY'
            valid[2][attribute.name] = '_utils.ast.type.MULTIPLY'
        elif attribute.type == 'types.Jump':
            valid[0][attribute.name] = '_utils.string.type.JUMP'
            valid[1][attribute.name] = '_utils.string.type.JUMP'
            valid[2][attribute.name] = '_utils.ast.type.JUMP'
        elif attribute.type == 'types.Log':
            valid[0][attribute.name] = '_utils.string.type.LOG'
            valid[1][attribute.name] = '_utils.string.type.LOG'
            valid[2][attribute.name] = '_utils.ast.type.LOG'
        elif attribute.type == 'types.Integer':
            if (element.name, attribute.name) in [('ic', 'function'), ('blocksize', 'ncy'), ('dbcn', 'x6')]:
                valid[0][attribute.name] = '"99"'
                valid[1][attribute.name] = '99'
                valid[2][attribute.name] = 'pymcnp.utils.types.Integer(99)'
                extra[attribute.name] = '"1"'
            elif (element.name, attribute.name) in [
                ('phys_2', 'i_mcs_model'),
                ('phys_3', 'i_els_model'),
                ('phys_4', 'i_els_model'),
            ]:
                valid[0][attribute.name] = '"-1"'
                valid[1][attribute.name] = '-1'
                valid[2][attribute.name] = 'pymcnp.utils.types.Integer(-1)'
                extra[attribute.name] = '"1"'
            elif (element.name, attribute.name) in [
                ('f_1', 'suffix'),
                ('f_2', 'suffix'),
                ('fic', 'suffix'),
                ('fip', 'suffix'),
                ('fir', 'suffix'),
            ]:
                valid[0][attribute.name] = '"5"'
                valid[1][attribute.name] = '5'
                valid[2][attribute.name] = 'pymcnp.utils.types.Integer(5)'
                extra[attribute.name] = '"1"'
            elif (element.name, attribute.name) in [
                ('sp_1', 'function'),
                ('sb_1', 'function'),
            ]:
                valid[0][attribute.name] = '"-2"'
                valid[1][attribute.name] = '-2'
                valid[2][attribute.name] = 'pymcnp.utils.types.Integer(-2)'
                extra[attribute.name] = '"1"'
            elif (element.name, attribute.name) in [
                ('f_3', 'suffix'),
            ]:
                valid[0][attribute.name] = '"8"'
                valid[1][attribute.name] = '8'
                valid[2][attribute.name] = 'pymcnp.utils.types.Integer(8)'
                extra[attribute.name] = '"1"'
            else:
                valid[0][attribute.name] = '_utils.string.type.INTEGER'
                valid[1][attribute.name] = '1'
                valid[2][attribute.name] = '_utils.ast.type.INTEGER'
                if attribute.restriction and attribute.optional:
                    if (element.name, attribute.name) in [
                        ('tr_0', 'system'),
                        ('tr_1', 'system'),
                        ('tr_2', 'system'),
                        ('tr_3', 'system'),
                        ('tr_4', 'system'),
                        ('mgopt', 'iplt'),
                        ('mgopt', 'iab'),
                        ('phys_0', 'iunr'),
                        ('phys_0', 'ngam'),
                        ('phys_0', 'i_int_model'),
                        ('phys_0', 'i_els_model'),
                        ('phys_1', 'ides'),
                        ('phys_1', 'nocoh'),
                        ('phys_1', 'ispn'),
                        ('phys_1', 'nodop'),
                        ('phys_2', 'ides'),
                        ('phys_2', 'iphot'),
                        ('phys_2', 'ibad'),
                        ('phys_2', 'istrg'),
                        ('phys_3', 'istrg'),
                        ('phys_3', 'i_mcs_model'),
                        ('phys_3', 'i_int_model'),
                        ('phys_4', 'istrg'),
                        ('phys_4', 'xmunum'),
                        ('phys_4', 'i_mcs_model'),
                        ('phys_4', 'i_int_model'),
                        ('lca', 'ielas'),
                        ('lca', 'ipreg'),
                        ('lca', 'iexisa'),
                        ('lca', 'jcoul'),
                        ('lca', 'nexite'),
                        ('lca', 'npidk'),
                        ('lca', 'noact'),
                        ('lca', 'icem'),
                        ('lca', 'ilaq'),
                        ('lcc', 'npaulincl'),
                        ('lcc', 'nosurfincl'),
                        ('lea', 'ipht'),
                        ('lea', 'icc'),
                        ('lea', 'nobalc'),
                        ('lea', 'nobale'),
                        ('lea', 'ifbrk'),
                        ('lea', 'ilvden'),
                        ('lea', 'ievap'),
                        ('lea', 'nofis'),
                        ('kcode', 'knrm'),
                        ('kcode', 'kc8'),
                        ('wwp', 'mwhere'),
                        ('wwp', 'etsplt'),
                        ('phys_2', 'rnok'),
                        ('phys_2', 'enum'),
                        ('phys_2', 'numb'),
                        ('kcode', 'nsrck'),
                        ('kcode', 'kct'),
                        ('kcode', 'mrkp'),
                        ('nps', 'npsmg'),
                        ('dbcn', 'x1'),
                        ('fill_6', 'transformation'),
                    ]:
                        extra[attribute.name] = '-9999'
                    elif (element.name, attribute.name) in [
                        ('kcode', 'msrk'),
                        ('fq', 'suffix'),
                    ]:
                        extra[attribute.name] = '100000000'
                    else:
                        print((element.name, attribute.name), attribute.type, attribute.restriction)
        elif attribute.type == 'types.Real':
            if (element.name, attribute.name) in [
                ('dxc', 'probability'),
                ('fcl', 'control'),
                ('pd', 'probability'),
                ('thresh', 'fraction'),
                ('xlims', 'lower'),
                ('ylims', 'lower'),
                ('bcw', 'zb'),
                ('phys_2', 'efac'),
                ('phys_3', 'recl'),
                ('phys_4', 'efac'),
                ('phys_3', 'efac'),
                ('phys_2', 'ckvnum'),
                ('phys_3', 'ckvnum'),
                ('phys_4', 'ckvnum'),
            ]:
                valid[0][attribute.name] = '"0.8"'
                valid[1][attribute.name] = '0.8'
                valid[2][attribute.name] = 'pymcnp.utils.types.Real(0.8)'
                extra[attribute.name] = '"3.1"'
            elif (element.name, attribute.name) in [('fic', 'f1'), ('fir', 'f1'), ('fic', 'f3'), ('fir', 'f3')]:
                valid[0][attribute.name] = '"-1"'
                valid[1][attribute.name] = '-1'
                valid[2][attribute.name] = 'pymcnp.utils.types.Real(-1)'
                extra[attribute.name] = '"3.1"'
            elif (element.name, attribute.name) in [('fic', 'ro'), ('fip', 'ro'), ('fir', 'ro')]:
                valid[0][attribute.name] = '"0"'
                valid[1][attribute.name] = '0'
                valid[2][attribute.name] = 'pymcnp.utils.types.Real(0)'
                extra[attribute.name] = '"3.1"'
            else:
                valid[0][attribute.name] = '_utils.string.type.REAL'
                valid[1][attribute.name] = '3.1'
                valid[2][attribute.name] = '_utils.ast.type.REAL'
                if attribute.restriction and attribute.optional:
                    if (element.name, attribute.name) in [
                        ('phys_2', 'xnum'),
                        ('phys_3', 'tabl'),
                        ('phys_3', 'drp'),
                        ('phys_4', 'drp'),
                        ('leb', 'yzere'),
                        ('leb', 'bzere'),
                        ('leb', 'yzero'),
                        ('leb', 'bzero'),
                        ('wwp', 'wupn'),
                        ('xlims', 'nsteps'),
                        ('ylims', 'nsteps'),
                        ('wwp', 'wsurvn'),
                        ('wwp', 'mxspln'),
                    ]:
                        extra[attribute.name] = '-3.1'
                    else:
                        print((element.name, attribute.name), attribute.type, attribute.restriction)
        elif attribute.type == 'types.String':
            if (element.name, attribute.name) in [('ds_0', 'option')]:
                valid[0][attribute.name] = '"h"'
                valid[1][attribute.name] = '"h"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("h")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('mgopt', 'mcal')]:
                valid[0][attribute.name] = '"a"'
                valid[1][attribute.name] = '"a"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("a")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('de', 'method'), ('df_0', 'method')]:
                valid[0][attribute.name] = '"log"'
                valid[1][attribute.name] = '"log"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("log")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('bfld', 'kind')]:
                valid[0][attribute.name] = '"const"'
                valid[1][attribute.name] = '"const"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("const")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('file', 'setting')]:
                valid[0][attribute.name] = '"asc"'
                valid[1][attribute.name] = '"asc"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("asc")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('xs_2', 'm')]:
                valid[0][attribute.name] = '"?"'
                valid[1][attribute.name] = '"?"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("?")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('conic', 'setting')]:
                valid[0][attribute.name] = '"col"'
                valid[1][attribute.name] = '"col"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("col")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('write', 'setting'), ('reset', 'aa'), ('file', 'aa')]:
                valid[0][attribute.name] = '"all"'
                valid[1][attribute.name] = '"all"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("all")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('f_1', 'nd'), ('f_2', 'nd')]:
                valid[0][attribute.name] = '"nd"'
                valid[1][attribute.name] = '"nd"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("nd")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('fu', 'nt')]:
                valid[0][attribute.name] = '"nt"'
                valid[1][attribute.name] = '"nt"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("nt")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('fu', 'c'), ('fs', 'c')]:
                valid[0][attribute.name] = '"c"'
                valid[1][attribute.name] = '"c"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("c")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [
                ('fs', 't'),
                ('fq', 'a1'),
                ('fq', 'a2'),
                ('fq', 'a3'),
                ('fq', 'a4'),
                ('fq', 'a5'),
                ('fq', 'a6'),
                ('fq', 'a7'),
                ('fq', 'a8'),
                ('f_0', 't'),
                ('fixed', 'q'),
                ('free', 'x'),
                ('free', 'y'),
            ]:
                valid[0][attribute.name] = '"t"'
                valid[1][attribute.name] = '"t"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("t")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [
                ('factor', 'a'),
                ('f_2', 'a'),
            ]:
                valid[0][attribute.name] = '"x"'
                valid[1][attribute.name] = '"x"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("x")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('ksental', 'fileopt')]:
                valid[0][attribute.name] = '"mctal"'
                valid[1][attribute.name] = '"mctal"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("mctal")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('geom', 'geometry')]:
                valid[0][attribute.name] = '"xyz"'
                valid[1][attribute.name] = '"xyz"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("xyz")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('mtype', 'kind'), ('type', 'setting')]:
                valid[0][attribute.name] = '"flux"'
                valid[1][attribute.name] = '"flux"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("flux")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('meshgeo', 'form')]:
                valid[0][attribute.name] = '"lnk3dnt"'
                valid[1][attribute.name] = '"lnk3dnt"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("lnk3dnt")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('filetype', 'kind')]:
                valid[0][attribute.name] = '"ascii"'
                valid[1][attribute.name] = '"ascii"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("ascii")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('debug', 'parameter')]:
                valid[0][attribute.name] = '"echomesh"'
                valid[1][attribute.name] = '"echomesh"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("echomesh")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('trcor', 'setting')]:
                valid[0][attribute.name] = '"diag"'
                valid[1][attribute.name] = '"diag"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("diag")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('sp_0', 'option'), ('sb_0', 'option')]:
                valid[0][attribute.name] = '"d"'
                valid[1][attribute.name] = '"d"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("d")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [
                ('srcacc', 'setting'),
                ('calcvols', 'setting'),
                ('atom', 'setting'),
                ('kinestics', 'setting'),
                ('fmatreduce', 'setting'),
                ('fmataccel', 'setting'),
                ('fmat', 'setting'),
                ('tnorm', 'trace'),
                ('enorm', 'setting'),
                ('tnorm', 'setting'),
                ('kinetics', 'setting'),
                ('precursor', 'setting'),
                ('linear', 'setting'),
                ('constrain', 'setting'),
                ('gas', 'setting'),
                ('totnu', 'no'),
                ('vol', 'no'),
            ]:
                valid[0][attribute.name] = '"no"'
                valid[1][attribute.name] = '"no"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("no")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [
                ('wash', 'aa'),
                ('mcscat', 'setting'),
                ('nescat', 'setting'),
                ('nreact', 'setting'),
                ('rr', 'setting'),
                ('eloss', 'setting'),
                ('mphys', 'setting'),
            ]:
                valid[0][attribute.name] = '"off"'
                valid[1][attribute.name] = '"off"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("off")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('sample', 'setting')]:
                valid[0][attribute.name] = '"correlate"'
                valid[1][attribute.name] = '"correlate"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("correlate")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('dn', 'source')]:
                valid[0][attribute.name] = '"model"'
                valid[1][attribute.name] = '"model"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("model")'
                extra[attribute.name] = '"hello"'
            elif attribute.name == 'prefix':
                valid[0][attribute.name] = '"*"'
                valid[1][attribute.name] = '"*"'
                valid[2][attribute.name] = 'pymcnp.utils.types.String("*")'
                extra[attribute.name] = '"hello"'
            else:
                valid[0][attribute.name] = '_utils.string.type.STRING'
                valid[1][attribute.name] = '_utils.string.type.STRING'
                valid[2][attribute.name] = '_utils.ast.type.STRING'
                if attribute.restriction and attribute.optional:
                    if (element.name, attribute.name) in []:
                        pass
                    else:
                        print((element.name, attribute.name), attribute.type, attribute.restriction)
        elif attribute.type == 'types.DistributionNumber':
            valid[0][attribute.name] = '_utils.string.type.DISTRIBUTIONNUMBER'
            valid[1][attribute.name] = '_utils.string.type.DISTRIBUTIONNUMBER'
            valid[2][attribute.name] = '_utils.ast.type.DISTRIBUTIONNUMBER'
        elif attribute.type == 'types.EmbeddedDistributionNumber':
            valid[0][attribute.name] = '_utils.string.type.EMBEDDEDDISTRIBUTIONNUMBER'
            valid[1][attribute.name] = '_utils.string.type.EMBEDDEDDISTRIBUTIONNUMBER'
            valid[2][attribute.name] = '_utils.ast.type.EMBEDDEDDISTRIBUTIONNUMBER'
        elif attribute.type == 'types.Zaid':
            valid[0][attribute.name] = '_utils.string.type.ZAID'
            valid[1][attribute.name] = '_utils.string.type.ZAID'
            valid[2][attribute.name] = '_utils.ast.type.ZAID'
        elif attribute.type == 'types.Designator':
            valid[0][attribute.name] = '_utils.string.type.DESIGNATOR'
            valid[1][attribute.name] = '_utils.string.type.DESIGNATOR'
            valid[2][attribute.name] = '_utils.ast.type.DESIGNATOR'
        elif attribute.type == 'types.Geometry':
            valid[0][attribute.name] = '_utils.string.type.GEOMETRY'
            valid[1][attribute.name] = '_utils.string.type.GEOMETRY'
            valid[2][attribute.name] = '_utils.ast.type.GEOMETRY'
        elif attribute.type == 'types.Substance':
            valid[0][attribute.name] = '_utils.string.type.SUBSTANCE'
            valid[1][attribute.name] = '_utils.string.type.SUBSTANCE'
            valid[2][attribute.name] = '_utils.ast.type.SUBSTANCE'
        elif attribute.type == 'types.Bias':
            valid[0][attribute.name] = '_utils.string.type.BIAS'
            valid[1][attribute.name] = '_utils.string.type.BIAS'
            valid[2][attribute.name] = '_utils.ast.type.BIAS'
        elif attribute.type == 'types.Transformation_0':
            valid[0][attribute.name] = '_utils.string.type.TRANSFORMATION_0'
            valid[1][attribute.name] = '_utils.string.type.TRANSFORMATION_0'
            valid[2][attribute.name] = '_utils.ast.type.TRANSFORMATION_0'
        elif attribute.type == 'types.Transformation_1':
            valid[0][attribute.name] = '_utils.string.type.TRANSFORMATION_1'
            valid[1][attribute.name] = '_utils.string.type.TRANSFORMATION_1'
            valid[2][attribute.name] = '_utils.ast.type.TRANSFORMATION_1'
        elif attribute.type == 'types.Transformation_2':
            valid[0][attribute.name] = '_utils.string.type.TRANSFORMATION_2'
            valid[1][attribute.name] = '_utils.string.type.TRANSFORMATION_2'
            valid[2][attribute.name] = '_utils.ast.type.TRANSFORMATION_2'
        elif attribute.type == 'types.Transformation_3':
            valid[0][attribute.name] = '_utils.string.type.TRANSFORMATION_3'
            valid[1][attribute.name] = '_utils.string.type.TRANSFORMATION_3'
            valid[2][attribute.name] = '_utils.ast.type.TRANSFORMATION_3'
        elif attribute.type == 'types.Transformation_4':
            valid[0][attribute.name] = '_utils.string.type.TRANSFORMATION_4'
            valid[1][attribute.name] = '_utils.string.type.TRANSFORMATION_4'
            valid[2][attribute.name] = '_utils.ast.type.TRANSFORMATION_4'
        elif attribute.type == 'types.Stochastic':
            valid[0][attribute.name] = '_utils.string.type.STOCHASTIC'
            valid[1][attribute.name] = '_utils.string.type.STOCHASTIC'
            valid[2][attribute.name] = '_utils.ast.type.STOCHASTIC'
        elif attribute.type == 'types.IndependentDependent':
            valid[0][attribute.name] = '_utils.string.type.INDEPENDENTDEPENDENT'
            valid[1][attribute.name] = '_utils.string.type.INDEPENDENTDEPENDENT'
            valid[2][attribute.name] = '_utils.ast.type.INDEPENDENTDEPENDENT'
        elif attribute.type == 'types.Location':
            valid[0][attribute.name] = '_utils.string.type.LOCATION'
            valid[1][attribute.name] = '_utils.string.type.LOCATION'
            valid[2][attribute.name] = '_utils.ast.type.LOCATION'
        elif attribute.type == 'types.File':
            valid[0][attribute.name] = '_utils.string.type.FILE'
            valid[1][attribute.name] = '_utils.string.type.FILE'
            valid[2][attribute.name] = '_utils.ast.type.FILE'
        elif attribute.type == 'types.Diagnostic':
            valid[0][attribute.name] = '_utils.string.type.DIAGNOSTIC'
            valid[1][attribute.name] = '_utils.string.type.DIAGNOSTIC'
            valid[2][attribute.name] = '_utils.ast.type.DIAGNOSTIC'
        elif attribute.type == 'types.Ring':
            valid[0][attribute.name] = '_utils.string.type.RING'
            valid[1][attribute.name] = '_utils.string.type.RING'
            valid[2][attribute.name] = '_utils.ast.type.RING'
        elif attribute.type == 'types.Sphere':
            valid[0][attribute.name] = '_utils.string.type.SPHERE'
            valid[1][attribute.name] = '_utils.string.type.SPHERE'
            valid[2][attribute.name] = '_utils.ast.type.SPHERE'
        elif attribute.type == 'types.Shell':
            valid[0][attribute.name] = '_utils.string.type.SHELL'
            valid[1][attribute.name] = '_utils.string.type.SHELL'
            valid[2][attribute.name] = '_utils.ast.type.SHELL'
        elif attribute.type == 'types.Reaction':
            valid[0][attribute.name] = '_utils.string.type.REACTION'
            valid[1][attribute.name] = '_utils.string.type.REACTION'
            valid[2][attribute.name] = '_utils.ast.type.REACTION'
        elif attribute.type == 'types.PtracFilter':
            valid[0][attribute.name] = '_utils.string.type.PTRACFILTER'
            valid[1][attribute.name] = '_utils.string.type.PTRACFILTER'
            valid[2][attribute.name] = '_utils.ast.type.PTRACFILTER'
        elif attribute.type == 'types.PhotonBias':
            valid[0][attribute.name] = '_utils.string.type.PHOTONBIAS'
            valid[1][attribute.name] = '_utils.string.type.PHOTONBIAS'
            valid[2][attribute.name] = '_utils.ast.type.PHOTONBIAS'
        elif attribute.type == 'types.Index':
            valid[0][attribute.name] = '_utils.string.type.INDEX'
            valid[1][attribute.name] = '_utils.string.type.INDEX'
            valid[2][attribute.name] = '_utils.ast.type.INDEX'
        elif attribute.type == 'types.Matcell':
            valid[0][attribute.name] = '_utils.string.type.MATCELL'
            valid[1][attribute.name] = '_utils.string.type.MATCELL'
            valid[2][attribute.name] = '_utils.ast.type.MATCELL'
        elif attribute.type == 'types.Tuple[types.Repeat]':
            valid[0][attribute.name] = '[_utils.string.type.REPEAT]'
            valid[1][attribute.name] = '[_utils.string.type.REPEAT]'
            valid[2][attribute.name] = '[_utils.ast.type.REPEAT]'
        elif attribute.type == 'types.Tuple[types.Insert]':
            valid[0][attribute.name] = '[_utils.string.type.INSERT]'
            valid[1][attribute.name] = '[_utils.string.type.INSERT]'
            valid[2][attribute.name] = '[_utils.ast.type.INSERT]'
        elif attribute.type == 'types.Tuple[types.Multiply]':
            valid[0][attribute.name] = '[_utils.string.type.MULTIPLY]'
            valid[1][attribute.name] = '[_utils.string.type.MULTIPLY]'
            valid[2][attribute.name] = '[_utils.ast.type.MULTIPLY]'
        elif attribute.type == 'types.Tuple[types.Jump]':
            valid[0][attribute.name] = '[_utils.string.type.JUMP]'
            valid[1][attribute.name] = '[_utils.string.type.JUMP]'
            valid[2][attribute.name] = '[_utils.ast.type.JUMP]'
        elif attribute.type == 'types.Tuple[types.Log]':
            valid[0][attribute.name] = '[_utils.string.type.LOG]'
            valid[1][attribute.name] = '[_utils.string.type.LOG]'
            valid[2][attribute.name] = '[_utils.ast.type.LOG]'
        elif attribute.type == 'types.Tuple[types.Integer]':
            valid[0][attribute.name] = '[_utils.string.type.INTEGER]'
            valid[1][attribute.name] = '[1]'
            valid[2][attribute.name] = '[_utils.ast.type.INTEGER]'
        elif attribute.type == 'types.Tuple[types.Real]':
            valid[0][attribute.name] = '[_utils.string.type.REAL]'
            valid[1][attribute.name] = '[3.1]'
            valid[2][attribute.name] = '[_utils.ast.type.REAL]'
        elif attribute.type == 'types.Tuple[types.String]':
            valid[0][attribute.name] = '[_utils.string.type.STRING]'
            valid[1][attribute.name] = '[_utils.string.type.STRING]'
            valid[2][attribute.name] = '[_utils.ast.type.STRING]'
        elif attribute.type == 'types.Tuple[types.DistributionNumber]':
            valid[0][attribute.name] = '[_utils.string.type.DISTRIBUTIONNUMBER]'
            valid[1][attribute.name] = '[_utils.string.type.DISTRIBUTIONNUMBER]'
            valid[2][attribute.name] = '[_utils.ast.type.DISTRIBUTIONNUMBER]'
        elif attribute.type == 'types.Tuple[types.EmbeddedDistributionNumber]':
            valid[0][attribute.name] = '[_utils.string.type.EMBEDDEDDISTRIBUTIONNUMBER]'
            valid[1][attribute.name] = '[_utils.string.type.EMBEDDEDDISTRIBUTIONNUMBER]'
            valid[2][attribute.name] = '[_utils.ast.type.EMBEDDEDDISTRIBUTIONNUMBER]'
        elif attribute.type == 'types.Tuple[types.Zaid]':
            valid[0][attribute.name] = '[_utils.string.type.ZAID]'
            valid[1][attribute.name] = '[_utils.string.type.ZAID]'
            valid[2][attribute.name] = '[_utils.ast.type.ZAID]'
        elif attribute.type == 'types.Tuple[types.Designator]':
            valid[0][attribute.name] = '[_utils.string.type.DESIGNATOR]'
            valid[1][attribute.name] = '[_utils.string.type.DESIGNATOR]'
            valid[2][attribute.name] = '[_utils.ast.type.DESIGNATOR]'
        elif attribute.type == 'types.Tuple[types.Geometry]':
            valid[0][attribute.name] = '[_utils.string.type.GEOMETRY]'
            valid[1][attribute.name] = '[_utils.string.type.GEOMETRY]'
            valid[2][attribute.name] = '[_utils.ast.type.GEOMETRY]'
        elif attribute.type == 'types.Tuple[types.Substance]':
            valid[0][attribute.name] = '[_utils.string.type.SUBSTANCE]'
            valid[1][attribute.name] = '[_utils.string.type.SUBSTANCE]'
            valid[2][attribute.name] = '[_utils.ast.type.SUBSTANCE]'
        elif attribute.type == 'types.Tuple[types.Bias]':
            valid[0][attribute.name] = '[_utils.string.type.BIAS]'
            valid[1][attribute.name] = '[_utils.string.type.BIAS]'
            valid[2][attribute.name] = '[_utils.ast.type.BIAS]'
        elif attribute.type == 'types.Tuple[types.Transformation_0]':
            valid[0][attribute.name] = '[_utils.string.type.TRANSFORMATION_0]'
            valid[1][attribute.name] = '[_utils.string.type.TRANSFORMATION_0]'
            valid[2][attribute.name] = '[_utils.ast.type.TRANSFORMATION_0]'
        elif attribute.type == 'types.Tuple[types.Transformation_1]':
            valid[0][attribute.name] = '[_utils.string.type.TRANSFORMATION_1]'
            valid[1][attribute.name] = '[_utils.string.type.TRANSFORMATION_1]'
            valid[2][attribute.name] = '[_utils.ast.type.TRANSFORMATION_1]'
        elif attribute.type == 'types.Tuple[types.Transformation_2]':
            valid[0][attribute.name] = '[_utils.string.type.TRANSFORMATION_2]'
            valid[1][attribute.name] = '[_utils.string.type.TRANSFORMATION_2]'
            valid[2][attribute.name] = '[_utils.ast.type.TRANSFORMATION_2]'
        elif attribute.type == 'types.Tuple[types.Transformation_3]':
            valid[0][attribute.name] = '[_utils.string.type.TRANSFORMATION_3]'
            valid[1][attribute.name] = '[_utils.string.type.TRANSFORMATION_3]'
            valid[2][attribute.name] = '[_utils.ast.type.TRANSFORMATION_3]'
        elif attribute.type == 'types.Tuple[types.Transformation_4]':
            valid[0][attribute.name] = '[_utils.string.type.TRANSFORMATION_4]'
            valid[1][attribute.name] = '[_utils.string.type.TRANSFORMATION_4]'
            valid[2][attribute.name] = '[_utils.ast.type.TRANSFORMATION_4]'
        elif attribute.type == 'types.Tuple[types.Stochastic]':
            valid[0][attribute.name] = '[_utils.string.type.STOCHASTIC]'
            valid[1][attribute.name] = '[_utils.string.type.STOCHASTIC]'
            valid[2][attribute.name] = '[_utils.ast.type.STOCHASTIC]'
        elif attribute.type == 'types.Tuple[types.IndependentDependent]':
            valid[0][attribute.name] = '[_utils.string.type.INDEPENDENTDEPENDENT]'
            valid[1][attribute.name] = '[_utils.string.type.INDEPENDENTDEPENDENT]'
            valid[2][attribute.name] = '[_utils.ast.type.INDEPENDENTDEPENDENT]'
        elif attribute.type == 'types.Tuple[types.Location]':
            valid[0][attribute.name] = '[_utils.string.type.LOCATION]'
            valid[1][attribute.name] = '[_utils.string.type.LOCATION]'
            valid[2][attribute.name] = '[_utils.ast.type.LOCATION]'
        elif attribute.type == 'types.Tuple[types.File]':
            valid[0][attribute.name] = '[_utils.string.type.FILE]'
            valid[1][attribute.name] = '[_utils.string.type.FILE]'
            valid[2][attribute.name] = '[_utils.ast.type.FILE]'
        elif attribute.type == 'types.Tuple[types.Diagnostic]':
            valid[0][attribute.name] = '[_utils.string.type.DIAGNOSTIC]'
            valid[1][attribute.name] = '[_utils.string.type.DIAGNOSTIC]'
            valid[2][attribute.name] = '[_utils.ast.type.DIAGNOSTIC]'
        elif attribute.type == 'types.Tuple[types.Ring]':
            valid[0][attribute.name] = '[_utils.string.type.RING]'
            valid[1][attribute.name] = '[_utils.string.type.RING]'
            valid[2][attribute.name] = '[_utils.ast.type.RING]'
        elif attribute.type == 'types.Tuple[types.Sphere]':
            valid[0][attribute.name] = '[_utils.string.type.SPHERE]'
            valid[1][attribute.name] = '[_utils.string.type.SPHERE]'
            valid[2][attribute.name] = '[_utils.ast.type.SPHERE]'
        elif attribute.type == 'types.Tuple[types.Shell]':
            valid[0][attribute.name] = '[_utils.string.type.SHELL]'
            valid[1][attribute.name] = '[_utils.string.type.SHELL]'
            valid[2][attribute.name] = '[_utils.ast.type.SHELL]'
        elif attribute.type == 'types.Tuple[types.Reaction]':
            valid[0][attribute.name] = '[_utils.string.type.REACTION]'
            valid[1][attribute.name] = '[_utils.string.type.REACTION]'
            valid[2][attribute.name] = '[_utils.ast.type.REACTION]'
        elif attribute.type == 'types.Tuple[types.PtracFilter]':
            valid[0][attribute.name] = '[_utils.string.type.PTRACFILTER]'
            valid[1][attribute.name] = '[_utils.string.type.PTRACFILTER]'
            valid[2][attribute.name] = '[_utils.ast.type.PTRACFILTER]'
        elif attribute.type == 'types.Tuple[types.PhotonBias]':
            valid[0][attribute.name] = '[_utils.string.type.PHOTONBIAS]'
            valid[1][attribute.name] = '[_utils.string.type.PHOTONBIAS]'
            valid[2][attribute.name] = '[_utils.ast.type.PHOTONBIAS]'
        elif attribute.type == 'types.Tuple[types.Index]':
            valid[0][attribute.name] = '[_utils.string.type.INDEX]'
            valid[1][attribute.name] = '[_utils.string.type.INDEX]'
            valid[2][attribute.name] = '[_utils.ast.type.INDEX]'
        elif attribute.type == 'types.Tuple[types.Matcell]':
            valid[0][attribute.name] = '[_utils.string.type.MATCELL]'
            valid[1][attribute.name] = '[_utils.string.type.MATCELL]'
            valid[2][attribute.name] = '[_utils.ast.type.MATCELL]'

        elif attribute.type == 'types.Tuple[dawwg.DawwgOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.dawwg.BLOCK]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.dawwg.BLOCK]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.dawwg.BLOCK]'
        elif attribute.type == 'types.Tuple[block.BlockOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.dawwg.block.AJED]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.dawwg.block.AJED]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.dawwg.block.AJED]'
        elif attribute.type == 'types.Tuple[embed.EmbedOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.embed.BACKGROUND]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.embed.BACKGROUND]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.embed.BACKGROUND]'
        elif attribute.type == 'types.Tuple[embee.EmbeeOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.embee.ATOM]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.embee.ATOM]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.embee.ATOM]'
        elif attribute.type == 'types.Tuple[m_0.MOption_0]':
            valid[0][attribute.name] = '[_utils.string.inp.data.m_0.ALIB]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.m_0.ALIB]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.m_0.ALIB]'
        elif attribute.type == 'types.Tuple[act.ActOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.act.DG]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.act.DG]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.act.DG]'
        elif attribute.type == 'types.Tuple[fmult.FmultOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.fmult.DATA]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.fmult.DATA]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.fmult.DATA]'
        elif attribute.type == 'types.Tuple[tropt.TroptOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.tropt.ELOSS]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.tropt.ELOSS]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.tropt.ELOSS]'
        elif attribute.type == 'types.Tuple[bfld.BfldOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.bfld.AXS]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.bfld.AXS]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.bfld.AXS]'
        elif attribute.type == 'types.Tuple[sdef.SdefOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.sdef.ARA]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.sdef.ARA]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.sdef.ARA]'
        elif attribute.type == 'types.Tuple[ssw.SswOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.ssw.CEL]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.ssw.CEL]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.ssw.CEL]'
        elif attribute.type == 'types.Tuple[ssr.SsrOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.ssr.AXS]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.ssr.AXS]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.ssr.AXS]'
        elif attribute.type == 'types.Tuple[kopts.KoptsOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.kopts.BLOCKSIZE]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.kopts.BLOCKSIZE]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.kopts.BLOCKSIZE]'
        elif attribute.type == 'types.Tuple[t_1.TOption_1]':
            valid[0][attribute.name] = '[_utils.string.inp.data.t_1.CBEG]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.t_1.CBEG]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.t_1.CBEG]'
        elif attribute.type == 'types.Tuple[df_1.DfOption_1]':
            valid[0][attribute.name] = '[_utils.string.inp.data.df_1.FAC]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.df_1.FAC]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.df_1.FAC]'
        elif attribute.type == 'types.Tuple[pert.PertOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.pert.CELL]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.pert.CELL]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.pert.CELL]'
        elif attribute.type == 'types.Tuple[kpert.KpertOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.kpert.CELL]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.kpert.CELL]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.kpert.CELL]'
        elif attribute.type == 'types.Tuple[ksen.KsenOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.ksen.CONSTRAIN]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.ksen.CONSTRAIN]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.ksen.CONSTRAIN]'
        elif attribute.type == 'types.Tuple[fmesh.FmeshOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.fmesh.AXS]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.fmesh.AXS]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.fmesh.AXS]'
        elif attribute.type == 'types.Tuple[var.VarOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.var.RR]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.var.RR]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.var.RR]'
        elif attribute.type == 'types.Tuple[mesh.MeshOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.mesh.AXS]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.mesh.AXS]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.mesh.AXS]'
        elif attribute.type == 'types.Tuple[stop.StopOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.stop.CTME]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.stop.CTME]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.stop.CTME]'
        elif attribute.type == 'types.Tuple[ptrac.PtracOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.ptrac.BUFFER]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.ptrac.BUFFER]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.ptrac.BUFFER]'
        elif attribute.type == 'types.Tuple[mplot.MplotOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.mplot.BAR]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.mplot.BAR]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.mplot.BAR]'
        elif attribute.type == 'free.FreeOption':
            valid[0][attribute.name] = '_utils.string.inp.data.mplot.free.ALL'
            valid[1][attribute.name] = '_utils.builder.inp.data.mplot.free.ALL'
            valid[2][attribute.name] = '_utils.ast.inp.data.mplot.free.ALL'
        elif attribute.type == 'types.Tuple[contour.ContourOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.mplot.contour.ALL]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.mplot.contour.ALL]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.mplot.contour.ALL]'
        elif attribute.type == 'types.Tuple[rand.RandOption]':
            valid[0][attribute.name] = '[_utils.string.inp.data.rand.GEN]'
            valid[1][attribute.name] = '[_utils.builder.inp.data.rand.GEN]'
            valid[2][attribute.name] = '[_utils.ast.inp.data.rand.GEN]'

        else:
            valid[0][attribute.name] = None
            valid[1][attribute.name] = None
            valid[2][attribute.name] = None

            print(attribute.type)

    invalid = [{}]
    for attribute in element.attributes:
        test = valid[0].copy()
        test[attribute.name] = None

        if not attribute.optional:
            invalid.append(test)
        else:
            valid.append(test)

    if extra:
        for name, value in extra.items():
            test = valid[0].copy()
            test[name] = value
            invalid.append(test)

    if valid[0] == valid[1]:
        valid.pop(0)

    if invalid[0] == {}:
        invalid.pop(0)

    return f"""
class Test_{CAMEL(element.name)}:

    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.{f"{mod}." if mod else ""}{CAMEL(element.name)}
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.{f"{mod}." if mod else ""}{CAMEL(element.name, 'Builder')}
        EXAMPLES_VALID = [{', '.join(f'{{{", ".join(f"'{key}':{val}" for key, val in example.items())}}}' for example in valid)}]
        EXAMPLES_INVALID = [{', '.join(f'{{{", ".join(f"'{key}':{val}" for key, val in example.items())}}}' for example in invalid)}]
"""[1:]


def helper(element, mod, path):
    path_file = path / SNAKE(f'test_{element.name}.py')

    res = f"""
import pymcnp
{f"from {'.' * (str(path).count('/') - 6)} import _utils" if str(path).count('/') > 6 else 'import _utils'}


{TEST(element, mod)}
"""[1:]

    with path_file.open('w') as file:
        file.write(res)

    if element.options:
        for option in element.options:
            path_mod = path / element.name
            path_mod.mkdir(parents=True, exist_ok=True)
            (path_mod / '__init__.py').touch()
            helper(option, f'{mod}.{SNAKE(element.name)}' if mod else SNAKE(element.name), path_mod)


path = pathlib.Path(__file__).parent.parent / 'tests' / 'inp'
for card in inp_data.cards.options:
    if card.options:
        helper(card, '', path)
