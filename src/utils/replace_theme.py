import json

import replace_line as rl
import msgfunc as prnt

def replace_theme(json_file,back,fore):
    prnt.prnt( '-n', 'Replacing your theme configuration file')

    rl.replace_line( json_file, 'background =', 'background = '+back)
    rl.replace_line( json_file, 'foreground =', 'foreground = '+fore)
    rl.replace_line( json_file, 'label-unfocused-background', 'label-unfocused-background = '+back)
    rl.replace_line( json_file, 'label-unfocused-foreground', 'label-unfocused-foreground = '+fore)
    rl.replace_line( json_file, 'label-mode-background', 'label-mode-background = '+back)
    rl.replace_line( json_file, 'label-visible-background', 'label-visible-background = '+back)
    rl.replace_line( json_file, 'format-background', 'format-background = '+back)
    rl.replace_line( json_file, 'format-connected-background', 'format-connected-background = '+back)
    rl.replace_line( json_file, 'format-connected-foreground', 'format-connected-foreground = '+fore)
