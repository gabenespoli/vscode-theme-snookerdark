"""
Replace color codes with their hexes in the file

Searches for instances of a color string (e.g., @blue), and replace it will the
color hex, without the leading '#' (e.g., FFFFFF).

Filenames are hard-coded, so this can be called from the command line like so:
    `python addcolor.py`
"""

import re

def main():
    """Replace color codes with their hexes in the file"""
    filein = open('SnookerDark_template.tmTheme', 'r')
    fileout = open('SnookerDark.tmTheme', 'w')
    fileout.write(replace_colors(filein.read()))
    fileout.close()
    filein.close()

def replace_colors(string):
    """Replace color srings with color hexes"""
    colors = get_colors()
    for color, code in colors.items():
        color = '@' + color
        string = re.sub(color, code, string)
    return string

def get_colors():
    """
    Get dict of colors and hexes
    - make sure, for e.g., 'bg' comes after 'bg_light', so that '@bg_light'
    doesn't become '000000_light'
    """
    colors = {
        'bg_light':     '243730',
        'bg_sel':       '284737',
        'bg':           '212524',
        'fg_com':       '5F785C',
        'fg_dark':      '9BAD9B',
        'fg_light':     'CDC08B',
        'fg_bright':    'FCEDAB',
        'fg':           'ADAD9B',
        'red':          'E52E1A',
        'orange':       'B98036',
        'yellow':       'F5C52E',
        'green':        '1FC022',
        'cyan':         '21C296',
        'blue':         '0094CF',
        'purple':       'DF7376',
        'pink':         'C87F7F',
        'cursor':       'FFFFFF',
    }
    return colors

main()
