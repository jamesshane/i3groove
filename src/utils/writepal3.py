#!/bin/env python3

#   Author  :   James Shane

import sys
sys.path.append("..")
import json
import collections

if __name__=="__main__":

    data = {"pal": {}}
    done = {}
    done['D'] = "0"
    data["pal"].update(done)
    print(data)
    jfile=json.dumps(data, indent=4)
    with open('pal3.json', 'w') as outfile:
        #json.dump(jfile, outfile)
        outfile.write(jfile)
    exit(0)
