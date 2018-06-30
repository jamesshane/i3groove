#!/bin/env python3

#   Author  :   James Shane

import sys
sys.path.append("..")
import json
#import collections
import load_json as lj

if __name__=="__main__":

    data = lj.load_json("pal3.json")
    #data["pal"].update(done)
    data["pal"]["D"]=str(2)
    print(data)
    jfile=json.dumps(data, indent=4)
    with open('pal4.json', 'w') as outfile:
        #json.dump(jfile, outfile)
        outfile.write(jfile)
    exit(0)
