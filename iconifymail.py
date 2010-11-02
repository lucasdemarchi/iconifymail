#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Lucas De Marchi <lucas.de.marchi@gmail.com>
Copyright (C) 2010 ProFUSION embedded systems

This file is part of iconifymail.

iconifymail is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

iconifymail is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
iconifymail. If not, see http://www.gnu.org/licenses/.
"""

import sys, os

usage = "iconifymail domain_image name_address"
if len(sys.argv) != 3:
    print(usage)
    sys.exit(1)

imgstr = sys.argv[1]
addrstr = sys.argv[2]

FONT = 'EurostileLTStd-Demi.otf'
FONT_DIRS = ['~/.fonts/', '/usr/share/fonts/']
FONTPXSIZE = 14
COLOR_BACKGROUND= '#ffffff'
COLOR_TEXT = '#3C465F'
COLOR_BORDER = '#bebec7'
IMG_OUTPUT = 'mail_' + addrstr + '.png'

import Image, ImageFont, ImageDraw, ImageOps

def load_font(FONT, FONT_DIRS, FONTPXSIZE):
    font = None
    for d in FONT_DIRS:
        d = os.path.expanduser(d)
        for dirpath, dirnames, filenames in os.walk(d):
            for f in filenames:
                if f == FONT:
                    font = '/'.join([dirpath, f])
                    break
    if font:
        return ImageFont.truetype(font, FONTPXSIZE)

    return None

f = load_font(FONT, FONT_DIRS, FONTPXSIZE)
if not f:
    raise Exception('Unable to find font %s' % (FONT))

img_domain = Image.open(imgstr)
w, h = img_domain.size

wtxt, htxt = f.getsize(addrstr)

# + 2 for the border line
wtxt += 2

# ideally domain's height should be the biggest, but if it's not
# at least we don't fail
if htxt > h:
    h = htxt
w = w + wtxt

img = Image.new('RGBA', (w, h), COLOR_BACKGROUND)
img.paste(img_domain, (wtxt, 0))

draw = ImageDraw.Draw(img)
draw.text((2, h - htxt + 1 ), addrstr, COLOR_TEXT,f)
draw.rectangle([(0 ,0), (w - 1, h - 1)], outline=COLOR_BORDER)


img.save(IMG_OUTPUT)
