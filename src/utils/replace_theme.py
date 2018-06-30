import json

import replace_line as rl
import msgfunc as prnt

def replace_theme(json_file,back,fore,wallpaper_file):
    prnt.prnt( '-n', 'Replacing your theme configuration file')
    json_file["comment"]["back"]=back
    json_file["comment"]["fore"]=fore
    json_file['polybar']['background']=back
    json_file['polybar']['foreground']=fore
    json_file['polybar']['label-unfocused-background']=back
    json_file['polybar']['label-unfocused-foreground']=fore
    json_file['polybar']['label-mode-background']=back
    json_file['polybar']['label-visible-background']=back
    json_file['polybar']['format-background']=back
    json_file['polybar']['format-connected-background']=back
    json_file['polybar']['format-connected-foreground']=fore
    json_file['wallpaper']=wallpaper_file
    return json_file
