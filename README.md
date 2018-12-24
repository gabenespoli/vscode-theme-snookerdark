# SnookerDark Colorscheme for VSCode

Merry Christmas Dane! This is a clone of my vim colorscheme based on the colors
of a snooker table for Visual Studio Code.

## Installation

1. If you have already installed VSCode, you probably already have a
   `~/.vscode/extensions` folder. If you don't, create it. 

```bash
mkdir ~/.vscode/extensions
```

2. Then clone this repository there.

```bash
cd ~/.vscode/extensions
git clone https://github.com/gabenespoli/vscode-theme-snookerdark
```

3. Restart VSCode.

4. The 'SnookerDark' colorscheme should appear in the list of available
   colorschemes.

## Editing and rebuilding the theme

Open the `SnookerDark_template.tmTheme` file. It's an xml file that contains
syntax highlight groups and color hexes for those groups. Replace the color
hexes with color codes like so (for example): `#ADAD9B` becomes `#@fg`.

Color codes are in the style of
[base16](https://github.com/chriskempson/base16) colorschemes. See my
[iterm-color-palettes](https://github.com/gabenespoli/iterm-color-palettes) for
some info on how each color code is used in the scheme. Available color codes
and their corresponding color hexes for the SnookerDark theme are as follows.

| Color Code  | Hex     |
| ----------- | ------- |
| #@bg_light  | #243730 |
| #@bg_sel    | #284737 |
| #@bg        | #212524 |
| #@fg_com    | #5F785C |
| #@fg_dark   | #9BAD9B |
| #@fg_light  | #CDC08B |
| #@fg_bright | #FCEDAB |
| #@fg        | #ADAD9B |
| #@red       | #E52E1A |
| #@orange    | #B98036 |
| #@yellow    | #F5C52E |
| #@green     | #1FC022 |
| #@cyan      | #21C296 |
| #@blue      | #0094CF |
| #@purple    | #DF7376 |
| #@pink      | #C87F7F |
| #@cursor    | #FFFFFF |

Then use the included `addcolor.py` from the command line to replace the colors
in the template with the hexes, and save the file as the non-template.

```bash
cd ~/.vscode/extensions/vscode-theme-snookerdark/themes
python addcolor.py
```
