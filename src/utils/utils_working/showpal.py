#!/bin/env python3

#   Author  :   James Shane

import sys
sys.path.append("..")
import load_json as lj

if __name__=="__main__":

    html = open("pal.html", "w")
    jfile = lj.load_json("defpal.json")
    for l in jfile['pal']:
        hex_value=jfile['pal'][l]
        print (hex_value)
        html.write("""
            <div style="background: {color}; width: 500px; height: 50px; color: white;">
            {color}
            </div>
        """.format(color=hex_value))
        html.write("</div>")
    exit(0)
