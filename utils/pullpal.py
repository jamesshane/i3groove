import colorific
import glob

html = open("index.html", "w")

for filename in glob.glob('../src/wallpapers/*'):
    html.write("<div>")
    html.write("<img width=\"150px\" src=\"" + filename + "\">")
    print (filename)
    palette = colorific.extract_colors(filename)
    print (palette)
    for color in palette.colors:
        print (color)
        hex_value = colorific.rgb_to_hex(color.value)
        html.write("""
            <div style="background: {color}; width: 500px; height: 50px; color: white;">
            {prominence} {color}
            </div>
        """.format(color=hex_value, prominence=color.prominence))
        html.write("</div>")

    if palette.bgcolor != None:
        hex_value = colorific.rgb_to_hex(palette.bgcolor.value)
        html.write("""
            <div style="background: {color}; width: 500px; height: 50px; color: white;">
            {prominence} {color}
            </div>
        """.format(color=hex_value, prominence=palette.bgcolor.prominence))
        html.write("</div>")
