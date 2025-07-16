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


def UPPER(name: str) -> str:
    name = re.sub('/', '_', name)
    return name.upper()


def TEST(element, mod):
    valid_init = [{}]
    valid_build = [{}, {}, {}]
    extra = {}

    for attribute in element.attributes:
        if attribute.type == 'types.Repeat':
            valid_build[0][attribute.name] = 'consts.string.types.REPEAT'
            valid_build[1][attribute.name] = 'consts.string.types.REPEAT'
            valid_build[2][attribute.name] = 'consts.ast.types.REPEAT'
            valid_init[0][attribute.name] = 'consts.ast.types.REPEAT'
        elif attribute.type == 'types.Insert':
            valid_build[0][attribute.name] = 'consts.string.types.INSERT'
            valid_build[1][attribute.name] = 'consts.string.types.INSERT'
            valid_build[2][attribute.name] = 'consts.ast.types.INSERT'
            valid_init[0][attribute.name] = 'consts.ast.types.INSERT'
        elif attribute.type == 'types.Multiply':
            valid_build[0][attribute.name] = 'consts.string.types.MULTIPLY'
            valid_build[1][attribute.name] = 'consts.string.types.MULTIPLY'
            valid_build[2][attribute.name] = 'consts.ast.types.MULTIPLY'
            valid_init[0][attribute.name] = 'consts.ast.types.MULTIPLY'
        elif attribute.type == 'types.Jump':
            valid_build[0][attribute.name] = 'consts.string.types.JUMP'
            valid_build[1][attribute.name] = 'consts.string.types.JUMP'
            valid_build[2][attribute.name] = 'consts.ast.types.JUMP'
            valid_init[0][attribute.name] = 'consts.ast.types.JUMP'
        elif attribute.type == 'types.Log':
            valid_build[0][attribute.name] = 'consts.string.types.LOG'
            valid_build[1][attribute.name] = 'consts.string.types.LOG'
            valid_build[2][attribute.name] = 'consts.ast.types.LOG'
            valid_init[0][attribute.name] = 'consts.ast.types.LOG'
        elif attribute.type == 'types.Integer':
            if (element.name, attribute.name) in [('ic', 'function'), ('blocksize', 'ncy'), ('dbcn', 'x6')]:
                valid_build[0][attribute.name] = '"99"'
                valid_build[1][attribute.name] = '99'
                valid_build[2][attribute.name] = 'pymcnp.types.Integer(99)'
                valid_init[0][attribute.name] = 'pymcnp.types.Integer(99)'
                extra[attribute.name] = '"1"'
            elif (element.name, attribute.name) in [
                ('phys_2', 'i_mcs_model'),
                ('phys_3', 'i_els_model'),
                ('phys_4', 'i_els_model'),
            ]:
                valid_build[0][attribute.name] = '"-1"'
                valid_build[1][attribute.name] = '-1'
                valid_build[2][attribute.name] = 'pymcnp.types.Integer(-1)'
                valid_init[0][attribute.name] = 'pymcnp.types.Integer(-1)'
                extra[attribute.name] = '"1"'
            elif (element.name, attribute.name) in [
                ('f_1', 'suffix'),
                ('f_2', 'suffix'),
                ('fic', 'suffix'),
                ('fip', 'suffix'),
                ('fir', 'suffix'),
            ]:
                valid_build[0][attribute.name] = '"5"'
                valid_build[1][attribute.name] = '5'
                valid_build[2][attribute.name] = 'pymcnp.types.Integer(5)'
                valid_init[0][attribute.name] = 'pymcnp.types.Integer(5)'
                extra[attribute.name] = '"1"'
            elif (element.name, attribute.name) in [
                ('sp_1', 'function'),
                ('sb_1', 'function'),
            ]:
                valid_build[0][attribute.name] = '"-2"'
                valid_build[1][attribute.name] = '-2'
                valid_build[2][attribute.name] = 'pymcnp.types.Integer(-2)'
                valid_init[0][attribute.name] = 'pymcnp.types.Integer(-2)'
                extra[attribute.name] = '"1"'
            elif (element.name, attribute.name) in [
                ('f_3', 'suffix'),
            ]:
                valid_build[0][attribute.name] = '"8"'
                valid_build[1][attribute.name] = '8'
                valid_build[2][attribute.name] = 'pymcnp.types.Integer(8)'
                valid_init[0][attribute.name] = 'pymcnp.types.Integer(8)'
                extra[attribute.name] = '"1"'
            else:
                valid_build[0][attribute.name] = 'consts.string.types.INTEGER'
                valid_build[1][attribute.name] = '1'
                valid_build[2][attribute.name] = 'consts.ast.types.INTEGER'
                valid_init[0][attribute.name] = 'consts.ast.types.INTEGER'
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
                valid_build[0][attribute.name] = '"0.8"'
                valid_build[1][attribute.name] = '0.8'
                valid_build[2][attribute.name] = 'pymcnp.types.Real(0.8)'
                valid_init[0][attribute.name] = 'pymcnp.types.Real(0.8)'
                extra[attribute.name] = '"3.1"'
            elif (element.name, attribute.name) in [('fic', 'f1'), ('fir', 'f1'), ('fic', 'f3'), ('fir', 'f3')]:
                valid_build[0][attribute.name] = '"-1"'
                valid_build[1][attribute.name] = '-1'
                valid_build[2][attribute.name] = 'pymcnp.types.Real(-1)'
                valid_init[0][attribute.name] = 'pymcnp.types.Real(-1)'
                extra[attribute.name] = '"3.1"'
            elif (element.name, attribute.name) in [('fic', 'ro'), ('fip', 'ro'), ('fir', 'ro')]:
                valid_build[0][attribute.name] = '"0"'
                valid_build[1][attribute.name] = '0'
                valid_build[2][attribute.name] = 'pymcnp.types.Real(0)'
                valid_init[0][attribute.name] = 'pymcnp.types.Real(0)'
                extra[attribute.name] = '"3.1"'
            else:
                valid_build[0][attribute.name] = 'consts.string.types.REAL'
                valid_build[1][attribute.name] = '3.1'
                valid_build[2][attribute.name] = 'consts.ast.types.REAL'
                valid_init[0][attribute.name] = 'consts.ast.types.REAL'
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
                valid_build[0][attribute.name] = '"h"'
                valid_build[1][attribute.name] = '"h"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("h")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("h")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('mgopt', 'mcal')]:
                valid_build[0][attribute.name] = '"a"'
                valid_build[1][attribute.name] = '"a"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("a")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("a")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('de', 'method'), ('df_0', 'method')]:
                valid_build[0][attribute.name] = '"log"'
                valid_build[1][attribute.name] = '"log"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("log")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("log")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('bfld', 'kind')]:
                valid_build[0][attribute.name] = '"const"'
                valid_build[1][attribute.name] = '"const"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("const")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("const")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('file', 'setting')]:
                valid_build[0][attribute.name] = '"asc"'
                valid_build[1][attribute.name] = '"asc"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("asc")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("asc")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('xs_2', 'm')]:
                valid_build[0][attribute.name] = '"?"'
                valid_build[1][attribute.name] = '"?"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("?")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("?")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('conic', 'setting')]:
                valid_build[0][attribute.name] = '"col"'
                valid_build[1][attribute.name] = '"col"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("col")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("col")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('write', 'setting'), ('reset', 'aa'), ('file', 'aa')]:
                valid_build[0][attribute.name] = '"all"'
                valid_build[1][attribute.name] = '"all"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("all")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("all")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('f_1', 'nd'), ('f_2', 'nd')]:
                valid_build[0][attribute.name] = '"nd"'
                valid_build[1][attribute.name] = '"nd"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("nd")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("nd")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('fu', 'nt')]:
                valid_build[0][attribute.name] = '"nt"'
                valid_build[1][attribute.name] = '"nt"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("nt")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("nt")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('fu', 'c'), ('fs', 'c')]:
                valid_build[0][attribute.name] = '"c"'
                valid_build[1][attribute.name] = '"c"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("c")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("c")'
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
                valid_build[0][attribute.name] = '"t"'
                valid_build[1][attribute.name] = '"t"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("t")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("t")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [
                ('factor', 'a'),
                ('f_2', 'a'),
            ]:
                valid_build[0][attribute.name] = '"x"'
                valid_build[1][attribute.name] = '"x"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("x")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("x")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('ksental', 'fileopt')]:
                valid_build[0][attribute.name] = '"mctal"'
                valid_build[1][attribute.name] = '"mctal"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("mctal")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("mctal")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('geom', 'geometry')]:
                valid_build[0][attribute.name] = '"xyz"'
                valid_build[1][attribute.name] = '"xyz"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("xyz")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("xyz")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('mtype', 'kind'), ('type', 'setting')]:
                valid_build[0][attribute.name] = '"flux"'
                valid_build[1][attribute.name] = '"flux"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("flux")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("flux")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('meshgeo', 'form')]:
                valid_build[0][attribute.name] = '"lnk3dnt"'
                valid_build[1][attribute.name] = '"lnk3dnt"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("lnk3dnt")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("lnk3dnt")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('filetype', 'kind')]:
                valid_build[0][attribute.name] = '"ascii"'
                valid_build[1][attribute.name] = '"ascii"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("ascii")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("ascii")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('debug', 'parameter')]:
                valid_build[0][attribute.name] = '"echomesh"'
                valid_build[1][attribute.name] = '"echomesh"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("echomesh")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("echomesh")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('trcor', 'setting')]:
                valid_build[0][attribute.name] = '"diag"'
                valid_build[1][attribute.name] = '"diag"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("diag")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("diag")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('sp_0', 'option'), ('sb_0', 'option')]:
                valid_build[0][attribute.name] = '"d"'
                valid_build[1][attribute.name] = '"d"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("d")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("d")'
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
                valid_build[0][attribute.name] = '"no"'
                valid_build[1][attribute.name] = '"no"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("no")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("no")'
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
                valid_build[0][attribute.name] = '"off"'
                valid_build[1][attribute.name] = '"off"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("off")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("off")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('sample', 'setting')]:
                valid_build[0][attribute.name] = '"correlate"'
                valid_build[1][attribute.name] = '"correlate"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("correlate")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("correlate")'
                extra[attribute.name] = '"hello"'
            elif (element.name, attribute.name) in [('dn', 'source')]:
                valid_build[0][attribute.name] = '"model"'
                valid_build[1][attribute.name] = '"model"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("model")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("model")'
                extra[attribute.name] = '"hello"'
            elif attribute.name == 'prefix':
                valid_build[0][attribute.name] = '"*"'
                valid_build[1][attribute.name] = '"*"'
                valid_build[2][attribute.name] = 'pymcnp.types.String("*")'
                valid_init[0][attribute.name] = 'pymcnp.types.String("*")'
                extra[attribute.name] = '"hello"'
            else:
                valid_build[0][attribute.name] = 'consts.string.types.STRING'
                valid_build[1][attribute.name] = 'consts.string.types.STRING'
                valid_build[2][attribute.name] = 'consts.ast.types.STRING'
                valid_init[0][attribute.name] = 'consts.ast.types.STRING'
                if attribute.restriction and attribute.optional:
                    if (element.name, attribute.name) in []:
                        pass
                    else:
                        print((element.name, attribute.name), attribute.type, attribute.restriction)
        elif attribute.type == 'types.Distribution':
            valid_build[0][attribute.name] = 'consts.string.types.DISTRIBUTION'
            valid_build[1][attribute.name] = 'consts.string.types.DISTRIBUTION'
            valid_build[2][attribute.name] = 'consts.ast.types.DISTRIBUTION'
            valid_init[0][attribute.name] = 'consts.ast.types.DISTRIBUTION'
        elif attribute.type == 'types.EmbeddedDistribution':
            valid_build[0][attribute.name] = 'consts.string.types.EMBEDDEDDISTRIBUTION'
            valid_build[1][attribute.name] = 'consts.string.types.EMBEDDEDDISTRIBUTION'
            valid_build[2][attribute.name] = 'consts.ast.types.EMBEDDEDDISTRIBUTION'
            valid_init[0][attribute.name] = 'consts.ast.types.EMBEDDEDDISTRIBUTION'
        elif attribute.type == 'types.Zaid':
            valid_build[0][attribute.name] = 'consts.string.types.ZAID'
            valid_build[1][attribute.name] = 'consts.string.types.ZAID'
            valid_build[2][attribute.name] = 'consts.ast.types.ZAID'
            valid_init[0][attribute.name] = 'consts.ast.types.ZAID'
        elif attribute.type == 'types.Designator':
            valid_build[0][attribute.name] = 'consts.string.types.DESIGNATOR'
            valid_build[1][attribute.name] = 'consts.string.types.DESIGNATOR'
            valid_build[2][attribute.name] = 'consts.ast.types.DESIGNATOR'
            valid_init[0][attribute.name] = 'consts.ast.types.DESIGNATOR'
        elif attribute.type == 'cell.Geometry':
            valid_build[0][attribute.name] = 'consts.string.inp.cell.GEOMETRY'
            valid_build[1][attribute.name] = 'consts.string.inp.cell.GEOMETRY'
            valid_build[2][attribute.name] = 'consts.ast.inp.cell.GEOMETRY'
            valid_init[0][attribute.name] = 'consts.ast.inp.cell.GEOMETRY'
        elif attribute.type == 'types.Substance':
            valid_build[0][attribute.name] = 'consts.string.types.SUBSTANCE'
            valid_build[1][attribute.name] = 'consts.string.types.SUBSTANCE'
            valid_build[2][attribute.name] = 'consts.ast.types.SUBSTANCE'
            valid_init[0][attribute.name] = 'consts.ast.types.SUBSTANCE'
        elif attribute.type == 'types.Bias':
            valid_build[0][attribute.name] = 'consts.string.types.BIAS'
            valid_build[1][attribute.name] = 'consts.string.types.BIAS'
            valid_build[2][attribute.name] = 'consts.ast.types.BIAS'
            valid_init[0][attribute.name] = 'consts.ast.types.BIAS'
        elif attribute.type == 'types.Transformation_0':
            valid_build[0][attribute.name] = 'consts.string.types.TRANSFORMATION_0'
            valid_build[1][attribute.name] = 'consts.string.types.TRANSFORMATION_0'
            valid_build[2][attribute.name] = 'consts.ast.types.TRANSFORMATION_0'
            valid_init[0][attribute.name] = 'consts.ast.types.TRANSFORMATION_0'
        elif attribute.type == 'types.Transformation_1':
            valid_build[0][attribute.name] = 'consts.string.types.TRANSFORMATION_1'
            valid_build[1][attribute.name] = 'consts.string.types.TRANSFORMATION_1'
            valid_build[2][attribute.name] = 'consts.ast.types.TRANSFORMATION_1'
            valid_init[0][attribute.name] = 'consts.ast.types.TRANSFORMATION_1'
        elif attribute.type == 'types.Transformation_2':
            valid_build[0][attribute.name] = 'consts.string.types.TRANSFORMATION_2'
            valid_build[1][attribute.name] = 'consts.string.types.TRANSFORMATION_2'
            valid_build[2][attribute.name] = 'consts.ast.types.TRANSFORMATION_2'
            valid_init[0][attribute.name] = 'consts.ast.types.TRANSFORMATION_2'
        elif attribute.type == 'types.Transformation_3':
            valid_build[0][attribute.name] = 'consts.string.types.TRANSFORMATION_3'
            valid_build[1][attribute.name] = 'consts.string.types.TRANSFORMATION_3'
            valid_build[2][attribute.name] = 'consts.ast.types.TRANSFORMATION_3'
            valid_init[0][attribute.name] = 'consts.ast.types.TRANSFORMATION_3'
        elif attribute.type == 'types.Transformation_4':
            valid_build[0][attribute.name] = 'consts.string.types.TRANSFORMATION_4'
            valid_build[1][attribute.name] = 'consts.string.types.TRANSFORMATION_4'
            valid_build[2][attribute.name] = 'consts.ast.types.TRANSFORMATION_4'
            valid_init[0][attribute.name] = 'consts.ast.types.TRANSFORMATION_4'
        elif attribute.type == 'types.Stochastic':
            valid_build[0][attribute.name] = 'consts.string.types.STOCHASTIC'
            valid_build[1][attribute.name] = 'consts.string.types.STOCHASTIC'
            valid_build[2][attribute.name] = 'consts.ast.types.STOCHASTIC'
            valid_init[0][attribute.name] = 'consts.ast.types.STOCHASTIC'
        elif attribute.type == 'types.IndependentDependent':
            valid_build[0][attribute.name] = 'consts.string.types.INDEPENDENTDEPENDENT'
            valid_build[1][attribute.name] = 'consts.string.types.INDEPENDENTDEPENDENT'
            valid_build[2][attribute.name] = 'consts.ast.types.INDEPENDENTDEPENDENT'
            valid_init[0][attribute.name] = 'consts.ast.types.INDEPENDENTDEPENDENT'
        elif attribute.type == 'ksrc.Location':
            valid_build[0][attribute.name] = 'consts.string.types.LOCATION'
            valid_build[1][attribute.name] = 'consts.string.types.LOCATION'
            valid_build[2][attribute.name] = 'consts.ast.types.LOCATION'
            valid_init[0][attribute.name] = 'consts.ast.types.LOCATION'
        elif attribute.type == 'types.File':
            valid_build[0][attribute.name] = 'consts.string.types.FILE'
            valid_build[1][attribute.name] = 'consts.string.types.FILE'
            valid_build[2][attribute.name] = 'consts.ast.types.FILE'
            valid_init[0][attribute.name] = 'consts.ast.types.FILE'
        elif attribute.type == 'types.Diagnostic':
            valid_build[0][attribute.name] = 'consts.string.inp.data.dd.DIAGNOSTIC'
            valid_build[1][attribute.name] = 'consts.string.inp.data.dd.DIAGNOSTIC'
            valid_build[2][attribute.name] = 'consts.ast.inp.data.dd.DIAGNOSTIC'
            valid_init[0][attribute.name] = 'consts.ast.inp.data.dd.DIAGNOSTIC'
        elif attribute.type == 'types.Ring':
            valid_build[0][attribute.name] = 'consts.string.types.RING'
            valid_build[1][attribute.name] = 'consts.string.types.RING'
            valid_build[2][attribute.name] = 'consts.ast.types.RING'
            valid_init[0][attribute.name] = 'consts.ast.types.RING'
        elif attribute.type == 'types.Sphere':
            valid_build[0][attribute.name] = 'consts.string.types.SPHERE'
            valid_build[1][attribute.name] = 'consts.string.types.SPHERE'
            valid_build[2][attribute.name] = 'consts.ast.types.SPHERE'
            valid_init[0][attribute.name] = 'consts.ast.types.SPHERE'
        elif attribute.type == 'types.Shell':
            valid_build[0][attribute.name] = 'consts.string.types.SHELL'
            valid_build[1][attribute.name] = 'consts.string.types.SHELL'
            valid_build[2][attribute.name] = 'consts.ast.types.SHELL'
            valid_init[0][attribute.name] = 'consts.ast.types.SHELL'
        elif attribute.type == 'types.Reaction':
            valid_build[0][attribute.name] = 'consts.string.types.REACTION'
            valid_build[1][attribute.name] = 'consts.string.types.REACTION'
            valid_build[2][attribute.name] = 'consts.ast.types.REACTION'
            valid_init[0][attribute.name] = 'consts.ast.types.REACTION'
        elif attribute.type == 'types.PtracFilter':
            valid_build[0][attribute.name] = 'consts.string.types.PTRACFILTER'
            valid_build[1][attribute.name] = 'consts.string.types.PTRACFILTER'
            valid_build[2][attribute.name] = 'consts.ast.types.PTRACFILTER'
            valid_init[0][attribute.name] = 'consts.ast.types.PTRACFILTER'
        elif attribute.type == 'types.Photonbias':
            valid_build[0][attribute.name] = 'consts.string.types.PHOTONBIAS'
            valid_build[1][attribute.name] = 'consts.string.types.PHOTONBIAS'
            valid_build[2][attribute.name] = 'consts.ast.types.PHOTONBIAS'
            valid_init[0][attribute.name] = 'consts.ast.types.PHOTONBIAS'
        elif attribute.type == 'types.Index':
            valid_build[0][attribute.name] = 'consts.string.types.INDEX'
            valid_build[1][attribute.name] = 'consts.string.types.INDEX'
            valid_build[2][attribute.name] = 'consts.ast.types.INDEX'
            valid_init[0][attribute.name] = 'consts.ast.types.INDEX'
        elif attribute.type == 'matcell.Entry':
            valid_build[0][attribute.name] = 'consts.string.types.MATCELL'
            valid_build[1][attribute.name] = 'consts.string.types.MATCELL'
            valid_build[2][attribute.name] = 'consts.ast.types.MATCELL'
            valid_init[0][attribute.name] = 'consts.ast.types.MATCELL'
        elif attribute.type == 'types.Tuple[types.Repeat]':
            valid_build[0][attribute.name] = '[consts.string.types.REPEAT]'
            valid_build[1][attribute.name] = '[consts.string.types.REPEAT]'
            valid_build[2][attribute.name] = '[consts.ast.types.REPEAT]'
            valid_init[0][attribute.name] = '[consts.ast.types.REPEAT]'
        elif attribute.type == 'types.Tuple[types.Insert]':
            valid_build[0][attribute.name] = '[consts.string.types.INSERT]'
            valid_build[1][attribute.name] = '[consts.string.types.INSERT]'
            valid_build[2][attribute.name] = '[consts.ast.types.INSERT]'
            valid_init[0][attribute.name] = '[consts.ast.types.INSERT]'
        elif attribute.type == 'types.Tuple[types.Multiply]':
            valid_build[0][attribute.name] = '[consts.string.types.MULTIPLY]'
            valid_build[1][attribute.name] = '[consts.string.types.MULTIPLY]'
            valid_build[2][attribute.name] = '[consts.ast.types.MULTIPLY]'
            valid_init[0][attribute.name] = '[consts.ast.types.MULTIPLY]'
        elif attribute.type == 'types.Tuple[types.Jump]':
            valid_build[0][attribute.name] = '[consts.string.types.JUMP]'
            valid_build[1][attribute.name] = '[consts.string.types.JUMP]'
            valid_build[2][attribute.name] = '[consts.ast.types.JUMP]'
            valid_init[0][attribute.name] = '[consts.ast.types.JUMP]'
        elif attribute.type == 'types.Tuple[types.Log]':
            valid_build[0][attribute.name] = '[consts.string.types.LOG]'
            valid_build[1][attribute.name] = '[consts.string.types.LOG]'
            valid_build[2][attribute.name] = '[consts.ast.types.LOG]'
            valid_init[0][attribute.name] = '[consts.ast.types.LOG]'
        elif attribute.type == 'types.Tuple[types.Integer]':
            valid_build[0][attribute.name] = '[consts.string.types.INTEGER]'
            valid_build[1][attribute.name] = '[1]'
            valid_build[2][attribute.name] = '[consts.ast.types.INTEGER]'
            valid_init[0][attribute.name] = '[consts.ast.types.INTEGER]'
        elif attribute.type == 'types.Tuple[types.Real]':
            valid_build[0][attribute.name] = '[consts.string.types.REAL]'
            valid_build[1][attribute.name] = '[3.1]'
            valid_build[2][attribute.name] = '[consts.ast.types.REAL]'
            valid_init[0][attribute.name] = '[consts.ast.types.REAL]'
        elif attribute.type == 'types.Tuple[types.String]':
            valid_build[0][attribute.name] = '[consts.string.types.STRING]'
            valid_build[1][attribute.name] = '[consts.string.types.STRING]'
            valid_build[2][attribute.name] = '[consts.ast.types.STRING]'
            valid_init[0][attribute.name] = '[consts.ast.types.STRING]'
        elif attribute.type == 'types.Tuple[types.Distribution]':
            valid_build[0][attribute.name] = '[consts.string.types.DISTRIBUTION]'
            valid_build[1][attribute.name] = '[consts.string.types.DISTRIBUTION]'
            valid_build[2][attribute.name] = '[consts.ast.types.DISTRIBUTION]'
            valid_init[0][attribute.name] = '[consts.ast.types.DISTRIBUTION]'
        elif attribute.type == 'types.Tuple[types.EmbeddedDistribution]':
            valid_build[0][attribute.name] = '[consts.string.types.EMBEDDEDDISTRIBUTION]'
            valid_build[1][attribute.name] = '[consts.string.types.EMBEDDEDDISTRIBUTION]'
            valid_build[2][attribute.name] = '[consts.ast.types.EMBEDDEDDISTRIBUTION]'
            valid_init[0][attribute.name] = '[consts.ast.types.EMBEDDEDDISTRIBUTION]'
        elif attribute.type == 'types.Tuple[types.Zaid]':
            valid_build[0][attribute.name] = '[consts.string.types.ZAID]'
            valid_build[1][attribute.name] = '[consts.string.types.ZAID]'
            valid_build[2][attribute.name] = '[consts.ast.types.ZAID]'
            valid_init[0][attribute.name] = '[consts.ast.types.ZAID]'
        elif attribute.type == 'types.Tuple[types.Designator]':
            valid_build[0][attribute.name] = '[consts.string.types.DESIGNATOR]'
            valid_build[1][attribute.name] = '[consts.string.types.DESIGNATOR]'
            valid_build[2][attribute.name] = '[consts.ast.types.DESIGNATOR]'
            valid_init[0][attribute.name] = '[consts.ast.types.DESIGNATOR]'
        elif attribute.type == 'types.Tuple[cell.Geometry]':
            valid_build[0][attribute.name] = '[consts.string.inp.cell.GEOMETRY]'
            valid_build[1][attribute.name] = '[consts.string.inp.cell.GEOMETRY]'
            valid_build[2][attribute.name] = '[consts.ast.inp.cell.GEOMETRY]'
            valid_init[0][attribute.name] = '[consts.ast.inp.cell.GEOMETRY]'
        elif attribute.type == 'types.Tuple[types.Substance]':
            valid_build[0][attribute.name] = '[consts.string.types.SUBSTANCE]'
            valid_build[1][attribute.name] = '[consts.string.types.SUBSTANCE]'
            valid_build[2][attribute.name] = '[consts.ast.types.SUBSTANCE]'
            valid_init[0][attribute.name] = '[consts.ast.types.SUBSTANCE]'
        elif attribute.type == 'types.Tuple[types.Bias]':
            valid_build[0][attribute.name] = '[consts.string.types.BIAS]'
            valid_build[1][attribute.name] = '[consts.string.types.BIAS]'
            valid_build[2][attribute.name] = '[consts.ast.types.BIAS]'
            valid_init[0][attribute.name] = '[consts.ast.types.BIAS]'
        elif attribute.type == 'types.Tuple[types.Transformation_0]':
            valid_build[0][attribute.name] = '[consts.string.types.TRANSFORMATION_0]'
            valid_build[1][attribute.name] = '[consts.string.types.TRANSFORMATION_0]'
            valid_build[2][attribute.name] = '[consts.ast.types.TRANSFORMATION_0]'
            valid_init[0][attribute.name] = '[consts.ast.types.TRANSFORMATION_0]'
        elif attribute.type == 'types.Tuple[types.Transformation_1]':
            valid_build[0][attribute.name] = '[consts.string.types.TRANSFORMATION_1]'
            valid_build[1][attribute.name] = '[consts.string.types.TRANSFORMATION_1]'
            valid_build[2][attribute.name] = '[consts.ast.types.TRANSFORMATION_1]'
            valid_init[0][attribute.name] = '[consts.ast.types.TRANSFORMATION_1]'
        elif attribute.type == 'types.Tuple[types.Transformation_2]':
            valid_build[0][attribute.name] = '[consts.string.types.TRANSFORMATION_2]'
            valid_build[1][attribute.name] = '[consts.string.types.TRANSFORMATION_2]'
            valid_build[2][attribute.name] = '[consts.ast.types.TRANSFORMATION_2]'
            valid_init[0][attribute.name] = '[consts.ast.types.TRANSFORMATION_2]'
        elif attribute.type == 'types.Tuple[types.Transformation_3]':
            valid_build[0][attribute.name] = '[consts.string.types.TRANSFORMATION_3]'
            valid_build[1][attribute.name] = '[consts.string.types.TRANSFORMATION_3]'
            valid_build[2][attribute.name] = '[consts.ast.types.TRANSFORMATION_3]'
            valid_init[0][attribute.name] = '[consts.ast.types.TRANSFORMATION_3]'
        elif attribute.type == 'types.Tuple[types.Transformation_4]':
            valid_build[0][attribute.name] = '[consts.string.types.TRANSFORMATION_4]'
            valid_build[1][attribute.name] = '[consts.string.types.TRANSFORMATION_4]'
            valid_build[2][attribute.name] = '[consts.ast.types.TRANSFORMATION_4]'
            valid_init[0][attribute.name] = '[consts.ast.types.TRANSFORMATION_4]'
        elif attribute.type == 'types.Tuple[types.Stochastic]':
            valid_build[0][attribute.name] = '[consts.string.types.STOCHASTIC]'
            valid_build[1][attribute.name] = '[consts.string.types.STOCHASTIC]'
            valid_build[2][attribute.name] = '[consts.ast.types.STOCHASTIC]'
            valid_init[0][attribute.name] = '[consts.ast.types.STOCHASTIC]'
        elif attribute.type == 'types.Tuple[types.IndependentDependent]':
            valid_build[0][attribute.name] = '[consts.string.types.INDEPENDENTDEPENDENT]'
            valid_build[1][attribute.name] = '[consts.string.types.INDEPENDENTDEPENDENT]'
            valid_build[2][attribute.name] = '[consts.ast.types.INDEPENDENTDEPENDENT]'
            valid_init[0][attribute.name] = '[consts.ast.types.INDEPENDENTDEPENDENT]'
        elif attribute.type == 'types.Tuple[ksrc.Location]':
            valid_build[0][attribute.name] = '[consts.string.types.LOCATION]'
            valid_build[1][attribute.name] = '[consts.string.types.LOCATION]'
            valid_build[2][attribute.name] = '[consts.ast.types.LOCATION]'
            valid_init[0][attribute.name] = '[consts.ast.types.LOCATION]'
        elif attribute.type == 'types.Tuple[types.File]':
            valid_build[0][attribute.name] = '[consts.string.types.FILE]'
            valid_build[1][attribute.name] = '[consts.string.types.FILE]'
            valid_build[2][attribute.name] = '[consts.ast.types.FILE]'
            valid_init[0][attribute.name] = '[consts.ast.types.FILE]'
        elif attribute.type == 'types.Tuple[types.Diagnostic]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.dd.DIAGNOSTIC]'
            valid_build[1][attribute.name] = '[consts.string.inp.data.dd.DIAGNOSTIC]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.dd.DIAGNOSTIC]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.dd.DIAGNOSTIC]'
        elif attribute.type == 'types.Tuple[types.Ring]':
            valid_build[0][attribute.name] = '[consts.string.types.RING]'
            valid_build[1][attribute.name] = '[consts.string.types.RING]'
            valid_build[2][attribute.name] = '[consts.ast.types.RING]'
            valid_init[0][attribute.name] = '[consts.ast.types.RING]'
        elif attribute.type == 'types.Tuple[types.Sphere]':
            valid_build[0][attribute.name] = '[consts.string.types.SPHERE]'
            valid_build[1][attribute.name] = '[consts.string.types.SPHERE]'
            valid_build[2][attribute.name] = '[consts.ast.types.SPHERE]'
            valid_init[0][attribute.name] = '[consts.ast.types.SPHERE]'
        elif attribute.type == 'types.Tuple[types.Shell]':
            valid_build[0][attribute.name] = '[consts.string.types.SHELL]'
            valid_build[1][attribute.name] = '[consts.string.types.SHELL]'
            valid_build[2][attribute.name] = '[consts.ast.types.SHELL]'
            valid_init[0][attribute.name] = '[consts.ast.types.SHELL]'
        elif attribute.type == 'types.Tuple[types.Reaction]':
            valid_build[0][attribute.name] = '[consts.string.types.REACTION]'
            valid_build[1][attribute.name] = '[consts.string.types.REACTION]'
            valid_build[2][attribute.name] = '[consts.ast.types.REACTION]'
            valid_init[0][attribute.name] = '[consts.ast.types.REACTION]'
        elif attribute.type == 'types.Tuple[types.PtracFilter]':
            valid_build[0][attribute.name] = '[consts.string.types.PTRACFILTER]'
            valid_build[1][attribute.name] = '[consts.string.types.PTRACFILTER]'
            valid_build[2][attribute.name] = '[consts.ast.types.PTRACFILTER]'
            valid_init[0][attribute.name] = '[consts.ast.types.PTRACFILTER]'
        elif attribute.type == 'types.Tuple[types.Photonbias]':
            valid_build[0][attribute.name] = '[consts.string.types.PHOTONBIAS]'
            valid_build[1][attribute.name] = '[consts.string.types.PHOTONBIAS]'
            valid_build[2][attribute.name] = '[consts.ast.types.PHOTONBIAS]'
            valid_init[0][attribute.name] = '[consts.ast.types.PHOTONBIAS]'
        elif attribute.type == 'types.Tuple[types.Index]':
            valid_build[0][attribute.name] = '[consts.string.types.INDEX]'
            valid_build[1][attribute.name] = '[consts.string.types.INDEX]'
            valid_build[2][attribute.name] = '[consts.ast.types.INDEX]'
            valid_init[0][attribute.name] = '[consts.ast.types.INDEX]'
        elif attribute.type == 'types.Tuple[matcell.Entry]':
            valid_build[0][attribute.name] = '[consts.string.types.MATCELL]'
            valid_build[1][attribute.name] = '[consts.string.types.MATCELL]'
            valid_build[2][attribute.name] = '[consts.ast.types.MATCELL]'
            valid_init[0][attribute.name] = '[consts.ast.types.MATCELL]'

        elif attribute.type == 'types.Tuple[dawwg.DawwgOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.dawwg.BLOCK]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.dawwg.BLOCK]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.dawwg.BLOCK]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.dawwg.BLOCK]'
        elif attribute.type == 'types.Tuple[block.BlockOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.dawwg.block.AJED]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.dawwg.block.AJED]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.dawwg.block.AJED]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.dawwg.block.AJED]'
        elif attribute.type == 'types.Tuple[embed.EmbedOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.embed.BACKGROUND]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.embed.BACKGROUND]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.embed.BACKGROUND]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.embed.BACKGROUND]'
        elif attribute.type == 'types.Tuple[embee.EmbeeOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.embee.ATOM]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.embee.ATOM]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.embee.ATOM]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.embee.ATOM]'
        elif attribute.type == 'types.Tuple[m_0.MOption_0]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.m_0.ALIB]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.m_0.ALIB]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.m_0.ALIB]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.m_0.ALIB]'
        elif attribute.type == 'types.Tuple[act.ActOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.act.DG]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.act.DG]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.act.DG]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.act.DG]'
        elif attribute.type == 'types.Tuple[fmult.FmultOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.fmult.DATA]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.fmult.DATA]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.fmult.DATA]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.fmult.DATA]'
        elif attribute.type == 'types.Tuple[tropt.TroptOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.tropt.ELOSS]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.tropt.ELOSS]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.tropt.ELOSS]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.tropt.ELOSS]'
        elif attribute.type == 'types.Tuple[bfld.BfldOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.bfld.AXS]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.bfld.AXS]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.bfld.AXS]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.bfld.AXS]'
        elif attribute.type == 'types.Tuple[sdef.SdefOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.sdef.ARA]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.sdef.ARA]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.sdef.ARA]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.sdef.ARA]'
        elif attribute.type == 'types.Tuple[ssw.SswOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.ssw.CEL]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.ssw.CEL]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.ssw.CEL]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.ssw.CEL]'
        elif attribute.type == 'types.Tuple[ssr.SsrOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.ssr.AXS]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.ssr.AXS]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.ssr.AXS]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.ssr.AXS]'
        elif attribute.type == 'types.Tuple[kopts.KoptsOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.kopts.BLOCKSIZE]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.kopts.BLOCKSIZE]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.kopts.BLOCKSIZE]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.kopts.BLOCKSIZE]'
        elif attribute.type == 'types.Tuple[t_1.TOption_1]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.t_1.CBEG]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.t_1.CBEG]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.t_1.CBEG]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.t_1.CBEG]'
        elif attribute.type == 'types.Tuple[df_1.DfOption_1]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.df_1.FAC]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.df_1.FAC]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.df_1.FAC]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.df_1.FAC]'
        elif attribute.type == 'types.Tuple[pert.PertOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.pert.CELL]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.pert.CELL]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.pert.CELL]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.pert.CELL]'
        elif attribute.type == 'types.Tuple[kpert.KpertOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.kpert.CELL]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.kpert.CELL]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.kpert.CELL]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.kpert.CELL]'
        elif attribute.type == 'types.Tuple[ksen.KsenOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.ksen.CONSTRAIN]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.ksen.CONSTRAIN]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.ksen.CONSTRAIN]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.ksen.CONSTRAIN]'
        elif attribute.type == 'types.Tuple[fmesh.FmeshOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.fmesh.AXS]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.fmesh.AXS]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.fmesh.AXS]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.fmesh.AXS]'
        elif attribute.type == 'types.Tuple[var.VarOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.var.RR]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.var.RR]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.var.RR]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.var.RR]'
        elif attribute.type == 'types.Tuple[mesh.MeshOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.mesh.AXS]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.mesh.AXS]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.mesh.AXS]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.mesh.AXS]'
        elif attribute.type == 'types.Tuple[stop.StopOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.stop.CTME]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.stop.CTME]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.stop.CTME]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.stop.CTME]'
        elif attribute.type == 'types.Tuple[ptrac.PtracOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.ptrac.BUFFER]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.ptrac.BUFFER]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.ptrac.BUFFER]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.ptrac.BUFFER]'
        elif attribute.type == 'types.Tuple[mplot.MplotOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.mplot.BAR]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.mplot.BAR]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.mplot.BAR]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.mplot.BAR]'
        elif attribute.type == 'free.FreeOption':
            valid_build[0][attribute.name] = 'consts.string.inp.data.mplot.free.ALL'
            valid_build[1][attribute.name] = 'consts.ast.inp.data.mplot.free.ALL'
            valid_build[2][attribute.name] = 'consts.ast.inp.data.mplot.free.ALL'
            valid_init[0][attribute.name] = 'consts.ast.inp.data.mplot.free.ALL'
        elif attribute.type == 'types.Tuple[contour.ContourOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.mplot.contour.ALL]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.mplot.contour.ALL]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.mplot.contour.ALL]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.mplot.contour.ALL]'
        elif attribute.type == 'types.Tuple[rand.RandOption]':
            valid_build[0][attribute.name] = '[consts.string.inp.data.rand.GEN]'
            valid_build[1][attribute.name] = '[consts.ast.inp.data.rand.GEN]'
            valid_build[2][attribute.name] = '[consts.ast.inp.data.rand.GEN]'
            valid_init[0][attribute.name] = '[consts.ast.inp.data.rand.GEN]'

        else:
            valid_build[0][attribute.name] = None
            valid_build[1][attribute.name] = None
            valid_build[2][attribute.name] = None
            valid_init[0][attribute.name] = None

            print(attribute.type)

    invalid_build = [{}]
    for attribute in element.attributes:
        test = valid_build[0].copy()
        test[attribute.name] = None

        if not attribute.optional:
            invalid_build.append(test)
        else:
            valid_build.append(test)

    if extra:
        for name, value in extra.items():
            test = valid_build[0].copy()
            test[name] = value
            invalid_build.append(test)

    if valid_build[0] == valid_build[1]:
        valid_build.pop(0)

    if invalid_build[0] == {}:
        invalid_build.pop(0)

    invalid_init = []
    for attribute in element.attributes:
        test = valid_init[0].copy()
        test[attribute.name] = None

        if not attribute.optional:
            invalid_init.append(test)
        else:
            valid_init.append(test)

    return f"""
class Test_{CAMEL(element.name)}:

    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.{f"{mod}." if mod else ""}{CAMEL(element.name)}
        EXAMPLES_VALID = [{', '.join(f'{{{", ".join(f"'{key}':{val}" for key, val in example.items())}}}' for example in valid_build)}]
        EXAMPLES_INVALID = [{', '.join(f'{{{", ".join(f"'{key}':{val}" for key, val in example.items())}}}' for example in invalid_build)}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.{f"{mod}." if mod else ""}{CAMEL(element.name)}
        EXAMPLES_VALID = [consts.string.inp.{f"{mod}." if mod else ""}{UPPER(element.name)}]
        EXAMPLES_INVALID = ['hello']

{f'''
    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.{f"{mod}." if mod else ""}{CAMEL(element.name)}
        EXAMPLES = [consts.string.inp.{f"{mod}." if mod else ""}{UPPER(element.name)}]
''' if "def draw" in element.extra else ""}
"""[1:]


def helper(element, mod, path):
    path_file = path / f'test_{CAMEL(element.name)}.py'

    res = f"""
import pymcnp
{f"from {'.' * (str(path).count('/') - 6)} import consts" if str(path).count('/') > 6 else 'import consts'}
{f"from {'.' * (str(path).count('/') - 6)} import classes" if str(path).count('/') > 6 else 'import classes'}


{TEST(element, mod)}
"""[1:]

    with path_file.open('w') as file:
        file.write(res)

    if element.options:
        for option in element.options:
            path_mod = path / f'test_{element.name}'
            path_mod.mkdir(parents=True, exist_ok=True)
            (path_mod / '__init__.py').touch()
            helper(option, f'{mod}.{SNAKE(element.name)}' if mod else SNAKE(element.name), path_mod)


path = pathlib.Path(__file__).parent.parent / 'tests' / 'test_pymcnp' / 'test_inp'
for card in inp_data.cards.options:
    if card.options:
        helper(card, '', path)
