# -*- coding: utf-8 -*-

import yaml
import jinja2
import pprint

def pp(data):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)


lecionoj = []

for i in range(1,2):
    leciono = {
      'teksto': None,
      'gramatiko': None,
      'ekzercoj': None,
    }
    i_padded = str(i).zfill(2)

    filename = 'lecionoj/netradukenda/tekstoj/' + i_padded + '.yml'
    leciono['teksto'] = yaml.load(file(filename, 'r'))

    filename = 'lecionoj/tradukenda/de/gramatiko/' + i_padded + '.yml'
    leciono['gramatiko'] = yaml.load(file(filename, 'r'))

    filename = 'lecionoj/tradukenda/de/ekzercoj/' + i_padded + '.yml'
    ekzercoj1 = yaml.load(file(filename, 'r'))

    filename = 'lecionoj/netradukenda/ekzercoj/' + i_padded + '.yml'
    ekzercoj2 = yaml.load(file(filename, 'r'))

    # Merge ekzercoj.
    ekzercoj = ekzercoj1.copy()
    ekzercoj.update(ekzercoj2)

    # Covert from dict to list.
    leciono['ekzercoj'] = []
    for key in sorted(ekzercoj.keys()):
        leciono['ekzercoj'].append(ekzercoj[key])

    lecionoj.append(leciono)


#pp(lecionoj)

print jinja2.Environment(trim_blocks=True,loader=jinja2.FileSystemLoader('html/templates/')).get_template('index.html').render(lecionoj=lecionoj)