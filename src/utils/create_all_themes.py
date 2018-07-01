#!/bin/env python3

#   Author  :   James Shane

import colorific
import glob
import json
from os import remove,system

#html = open("index.html", "w")

for filename in glob.glob('../wallpapers/*'):
    a,b,c=filename.split('/')
    html = open(c+".html", "w")
    data = {"pal": {}}
    done = {}
    cnt = 1
    html.write("<div>")
    html.write("<img width=\"150px\" src=\"" + filename + "\">")
    print (filename)
    palette = colorific.extract_colors(filename)
    print (palette)
    for color in palette.colors:
        print (color)
        hex_value = colorific.rgb_to_hex(color.value)
        done[str(cnt)]=hex_value
        html.write("""
            <div style="background: {color}; width: 500px; height: 50px; color: white;">
            {prominence} {color}
            </div>
        """.format(color=hex_value, prominence=color.prominence))
        #.1html.write("</div>")
        cnt+=1

    if palette.bgcolor != None:
        hex_value = colorific.rgb_to_hex(palette.bgcolor.value)
        done[str(cnt)]=hex_value
        html.write("""
            <div style="background: {color}; width: 500px; height: 50px; color: white;">
            <span>BG:</span>{prominence} {color}
            </div>
        """.format(color=hex_value, prominence=palette.bgcolor.prominence))
        cnt+=1
    html.write("</div>")
    html.close()
    remove(c+'.html')
    data["pal"].update(done)
    print(data)
    jfile=json.dumps(data, indent=4)
    with open(c+'.json', 'w') as outfile:
        #json.dump(jfile, outfile)
        outfile.write(jfile)
    outfile.close()
    e,f=c.split('.')
    system("./create_theme.py -c config.yaml -t "+e)
    remove(c+'.json')
