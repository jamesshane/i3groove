#!/bin/env python3

#   Author  :   James Shane

import sys
sys.path.append("..")
import json
import collections

if __name__=="__main__":

    data = {}
    JArray2 = collections.OrderedDict()
    JArray2["name"]= str('Scott')
    data["pal"]={}.append(JArray2)
    jfile=json.dumps(data, indent=4)
    with open('pal2.json', 'w') as outfile:
        #json.dump(jfile, outfile)
        outfile.write(jfile)
    exit(0)
